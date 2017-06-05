# -*- coding:utf-8 -*-

from __future__ import division
from flask import Flask, request, abort, Response, redirect, url_for, flash, Blueprint, send_from_directory
from flask.templating import render_template
from flask_security.decorators import roles_required, login_required
from models import Post
import matplotlib.pyplot as plt
import io
import base64
import datetime
import numpy as np
import pandas as pd
import investor

bp_public = Blueprint('public',__name__, static_folder='../static',template_folder="../templates")

@bp_public.route('/')
def index():
    return render_template('index.html')

@bp_public.route('/Home')
def welcome():
    return render_template('index.html')


@bp_public.route('/robots.txt')
def static_from_root():
    return send_from_directory(bp_public.static_folder, request.path[1:])

@bp_public.route('/RA')
def ra_load():
        a = 1
        b = 1
        c = u"Your invest term is: "+str(a) +u", and your risk tolerance is level "+ str(b)+ u'.'
        img = io.BytesIO()
        plot_url,str1, str2 = investor.draw_plot(b,name=img)
        return render_template('ra.html', plot_url=plot_url, RES = str(c), str1 = str(str1), str2 = str(str2))

@bp_public.route('/RA', methods=['GET', 'POST'])
def ra():
    if request.method == "POST":
        a = request.form['time'] or 1
        b = request.form['risk'] or 1
        c = u"Your invest term is: "+str(a) +u", and your risk tolerance is level "+ str(b)+ u'.'
        # return render_template('ra.html', RES = str(c))
        img = io.BytesIO()
        # y = [1, 2, 3, 4, 5]
        # x = [0, 2, 1, 3, 4]
        # plt.plot(x, y)
        plot_url,str1, str2 = investor.draw_plot(b,name=img)
        #plt.savefig(img, format='png')
        # img.seek(0)
        # plot_url = base64.b64encode(img.getvalue()).decode()
        # return '<img src="data:image/png;base64,{}">'.format(plot_url)
        return render_template('ra.html', plot_url=plot_url, RES = str(c), str1 = str(str1), str2 = str(str2))
    return render_template('ra.html')

@bp_public.route('/Mojie')
def mojie_load():
        a = 1
        b = 1
        c = u"Your invest term is: "+str(a) +u", and your risk tolerance is level "+ str(b)+ u'.'
        img = io.BytesIO()
        plot_url,str1, str2 = investor.draw_plot(b,name=img)
        return render_template('mojie.html', plot_url=plot_url, RES = str(c), str1 = str(str1), str2 = str(str2))

@bp_public.route('/Mojie', methods=['GET', 'POST'])
def mojie():
    if request.method == "POST":
        invest_time = request.form['time'] or 1
        investor_risk = request.form['risk'] or 1
        result = u"Your invest term is: "+str(invest_time) +u", and your risk tolerance is level "+ str(investor_risk)+ u'.'
        img = io.BytesIO()
        plot_url,str1, str2 = investor.draw_plot(investor_risk,name=img)
        return render_template('mojie.html', plot_url=plot_url, RES = str(result), str1 = str(str1), str2 = str(str2))
    return render_template('mojie.html')

@bp_public.route('/Blog')
def blog():
    return render_template('blog.html',posts=Post.objects)


@bp_public.route('/About')
def about():
    return render_template('about.html',posts=Post.objects)