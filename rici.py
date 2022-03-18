import flask
from flask import Flask, request
from dicttoxml import dicttoxml
import json as simplejson
import mysql.connector
import os
import codecs

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Vivek@123", database="ricitech")
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST','GET'])
def home():

    json_data = open('F:\\RICITECH\\en_jhn_1.json').read()
    original_fn = os.path.splitext(os.path.basename('F:\\RICITECH\\en_jhn_1.json')) 
    json_dict = simplejson.loads(json_data)

    startindex = original_fn.index("_")
    sliced_orginal_fn = original_fn[startindex+1:len(original_fn)]
    sliced_startindex = sliced_orginal_fn.index("_")
    endindex = sliced_orginal_fn.index("_")
    original_fn = sliced_orginal_fn[0:endindex]
    book_name1 = original_fn
    chapters_list = json_dict["chapters"]
    
    for item in chapters_list:
        chapter_number1 = item.get("chapterNumber")
        contents_list = item.get("contents")
        for item2 in contents_list:
            verse_number1 = item2.get("verseNumber")
            verse_text1 = item2.get("verseText").replace("'", "''")
            mydb.commit()
            mycursor = mydb.cursor()
            mycursor.execute("insert into en_json(verse_number,verse_text,book_name,chapter_number)values("+verse_number1+",'"+verse_text1+"','"+book_name1+"',"+chapter_number1+")")
mydb.commit()
# mydb.close()
app.run()