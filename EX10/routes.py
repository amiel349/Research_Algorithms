from flask import Flask, redirect, render_template, request, url_for, session
from EX10.flask_example.gspread_utils import read_and_write_gspread
from EX10.input import GoogleSheetsForm, RandomGraphForm
import networkx as nx
from flask_example.algo import maximum_weight_fractional_matching
import os


SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
global my_dict
global url
global flag


@app.route('/', methods=('GET', 'POST'))
def index():
    global my_dict, flag, url
    flag = False
    sheets = GoogleSheetsForm()
    form = RandomGraphForm()
    if form.validate_on_submit():
        my_dict = {'nodes': form.nodes.data, 'p': form.p.data}
        return redirect(url_for('random_graph'))
    if sheets.validate_on_submit():
        url = sheets.data['url']
        return redirect(url_for('google_sheets_graph'))
    return render_template('home.html', form=form, sheets=sheets)


@app.route('/random-input', methods=('GET', 'POST'))
def random_graph():
    global my_dict, flag, url
    if flag:
        flag = False
        form = RandomGraphForm()
        sheets = GoogleSheetsForm()
        if 'url' in sheets.data and sheets.data['url']:
            url = sheets.data['url']
            return redirect(url_for('google_sheets_graph'))
        my_dict = {'nodes': form.nodes.data, 'p': form.p.data}
        return redirect(url_for('random_graph'))
    p = my_dict['p']
    nodes = my_dict['nodes']
    G = nx.gnp_random_graph(nodes, p)
    res = maximum_weight_fractional_matching(G)
    edges = len(G.edges)
    form = RandomGraphForm()
    sheets = GoogleSheetsForm()
    flag = True
    return render_template('random-input.html', sheets=sheets, form=form, nodes=nodes, edges=edges, p=p, res=res)


@app.route('/result', methods=('GET', 'POST'))
def google_sheets_graph():
    global my_dict, flag, url
    form = RandomGraphForm()
    sheets = GoogleSheetsForm()
    if request.method == 'POST':
        nodes, edges, res = read_and_write_gspread(str(url))
        return render_template('google-result.html', form=form, sheets=sheets, nodes=nodes, edges=edges, res=res, url=url)
    return render_template('result.html', form=form, sheets=sheets, url=url)


@app.route('/networkx-documentation')
def networkx_documentation():
    return redirect('https://networkx.org/')


@app.route('/git-ola')
def git_ola():
    return redirect('https://github.com/OLAnetworkx/networkx/blob'\
                    '/max-weight-frac-match/networkx/algorithms'\
                    '/maximum_weight_fractional_matching.py')


# if __name__ == '__main__':
#     app.run(debug=True)
