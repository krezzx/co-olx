from forms import RegistrationForm,LoginForm
from flask import render_template,flash,redirect,url_for,request
from app import db,bcrypt,app,User,Product
from flask_login import current_user,login_required,logout_user,login_user
import os
from werkzeug.utils import secure_filename
import random





@app.route('/category_cycle')
def cyclecat():

    P=Product.query.with_entities(Product.id).filter(Product.cat.like('cycle')).all()
    P.reverse()
    p=dict()
    for i in P:
        post=Product.query.filter_by(id=i[0]).first()
        if(post.rm==0):
            a=[]
            a.append(post.title)
            a.append(post.desc)
            a.append(post.price)
            pi=post.pic
            picname='uploads/'+pi
            p[picname]=a
    return render_template('category.html',prod=p,cat_passed='Cycle')


@app.route('/category_book')
def bookcat():
    P=Product.query.with_entities(Product.id).filter(Product.cat.like('books')).all()
    P.reverse()
    p=dict()
    for i in P:
        post=Product.query.filter_by(id=i[0]).first()
        if(post.rm==0):
            a=[]
            a.append(post.title)
            a.append(post.desc)
            a.append(post.price)
            pi=post.pic
            picname='uploads/'+pi
            p[picname]=a
    return render_template('category.html',prod=p,cat_passed='Books')


@app.route('/category_appliances')
def appcat():
    P=Product.query.with_entities(Product.id).filter(Product.cat.like('appliances')).all()
    P.reverse()
    p=dict()
    for i in P:
        post=Product.query.filter_by(id=i[0]).first()
        if(post.rm==0):
            a=[]
            a.append(post.title)
            a.append(post.desc)
            a.append(post.price)
            pi=post.pic
            picname='uploads/'+pi
            p[picname]=a
    return render_template('category.html',prod=p,cat_passed='appliances')
@app.route('/category_elect')
def eleccat():
    P=Product.query.with_entities(Product.id).filter(Product.cat.like('electronics')).all()
    P.reverse()
    p=dict()
    for i in P:
        post=Product.query.filter_by(id=i[0]).first()
        if(post.rm==0):
            a=[]
            a.append(post.title)
            a.append(post.desc)
            a.append(post.price)
            pi=post.pic
            picname='uploads/'+pi
            p[picname]=a
    return render_template('category.html',prod=p,cat_passed='electronics')
@app.route('/category_lab')
def labcat():
    P=Product.query.with_entities(Product.id).filter(Product.cat.like('lab')).all()
    P.reverse()
    p=dict()
    for i in P:
        post=Product.query.filter_by(id=i[0]).first()
        if(post.rm==0):
            a=[]
            a.append(post.title)
            a.append(post.desc)
            a.append(post.price)
            pi=post.pic
            picname='uploads/'+pi
            p[picname]=a
    return render_template('category.html',prod=p,cat_passed='Lab Equip')


@app.route('/category_sports')
def sportcat():
    P=Product.query.with_entities(Product.id).filter(Product.cat.like('sports')).all()
    P.reverse()
    p=dict()
    for i in P:
        post=Product.query.filter_by(id=i[0]).first()
        if(post.rm==0):
            a=[]
            a.append(post.title)
            a.append(post.desc)
            a.append(post.price)
            pi=post.pic
            picname='uploads/'+pi
            p[picname]=a
    return render_template('category.html',prod=p,cat_passed='SPORTS')


@app.route('/category_other')
def othercat():
    P=Product.query.with_entities(Product.id).filter(Product.cat.like('other')).all()
    P.reverse()
    p=dict()
    for i in P:
        post=Product.query.filter_by(id=i[0]).first()
        if(post.rm==0):
            a=[]
            a.append(post.title)
            a.append(post.desc)
            a.append(post.price)
            pi=post.pic
            picname='uploads/'+pi
            p[picname]=a
    return render_template('category.html',prod=p,cat_passed='Others')