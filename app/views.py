"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, jsonify
from bs4 import BeautifulSoup
import requests
import urlparse

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/api/thumbnails')
def thumbnails():
    """Render website's thumbnails."""
    
    null =''
    jobject= {
        "error": null,
        "message": "Success",
        "thumbnails": [
        "https://www.walmart.com/static/img/clear.png?reqId=5f11a950-1876-11e7-96a9-93cf8aab251d&evt=product_script",
        "https://www.walmart.com/static/img/clear.png?reqId=5f11a950-1876-11e7-96a9-93cf8aab251d&evt=product_end",
        "https://ll-us-i5.wal.co/dfw/63fd9f59-579f/k2-_e1ee901c-814c-4326-ab2d-4056d02e9d5b.v11.png-b8bd30a9336f729a293f34915f0a2ba4b028b6af-crushed-70x65.png",
        "https://ll-us-i5.wal.co/dfw/63fd9f59-e2f5/k2-_7feabc9d-72da-4dda-8af2-56bba05ab4ad.v11.png-08c9161116502a45df08cb62b05bb588b43ccfb7-crushed-70x65.png",
        "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",
        "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",
        "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",
        "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",
        "https://www.walmart.com/static/img/clear.png?action=p13_start&timestamp=1490073256145&page=Product&placementId=Product-b1&bstc=undefined",
        "https://i5.walmartimages.com/asr/dd648f0a-edab-4c62-9157-051e2c73637b_1.d5bb911ec2c08224787e328e0ac7ff34.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",
        "https://i5.walmartimages.com/asr/0ac06c03-f851-4593-84ef-5e21d1460f3d_1.6fb25d21733810bd8e3439a4bb421d54.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",
        "https://i5.walmartimages.com/asr/d1127ff4-f437-459d-9503-2cbde415d7ef_1.62c03c6b7798f7e9eac2c450047221f6.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",
        "https://i5.walmartimages.com/asr/4ab87698-c642-4298-9ecb-f43bc5dce23a_1.8098f6cf872c9abdb04c31d2881698e6.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",
        "https://i5.walmartimages.com/asr/8289d1b0-b630-46bc-a33e-f0e5b347ff70_1.f06710f6452b38a99f478c87c8b87936.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",
        "https://i5.walmartimages.com/asr/93e90eef-6ff9-4ee4-b5b1-692d967450cb_1.07efa1290b82f3b4f50b95c09a9b3464.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",
        "https://i5.walmartimages.com/asr/d46e2aa0-7bc5-4e54-b9ab-1020bef0c9b5_1.4b0b4479e8e6fdf38c9b33a00f98788b.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",
        "https://i5.walmartimages.com/asr/3d62c34c-5c65-40b0-ab2d-a6555895779d_1.f34bda5c97b5d316ad4f49d79ccdd849.png?odnWidth=144&odnHeight=144&odnBg=ffffff",
        "https://www.walmart.com/static/img/clear.png?action=p13_end&timestamp=1490073256244&page=Product&placementId=Product-b1&bstc=undefined",
        "https://ll-us-i5.wal.co/dfw/63fd9f59-d0f2/k2-_c379cb69-17f1-44da-89ba-53ea082853c5.v11.png-d4b66ddbfe95500ed27934e3f401aae8c3c30f74-crushed-70x65.png",
        "https://ll-us-i5.wal.co/dfw/63fd9f59-a9e8/k2-_84280275-d251-461d-b29f-456506a3ec98.v11.png-56e11fae4af0df6777aaf267111aecad7f732698-crushed-70x65.png"
        ]
    }
    return jsonify(jobject)
    

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
