from flask import Flask, render_template, request, redirect, url_for, jsonify
from indexer import *

notes, words = index()

app = Flask(__name__)

@app.route("/words/", methods=["GET", "POST"])
def wordsPage():
    return render_template("words.html", words = words)   

@app.route("/notes/", methods=["GET", "POST"])
def home():
    return render_template("notes.html", notes = notes)

@app.route("/edit/<noteName>/", methods=["GET", "POST"])
def edit(noteName):
    
    global notes, words
    
    if noteName not in notes:
        return "This note is NULL (Not Found)", 404
    
    note = notes[noteName]
    
    if request.method == "POST" and request.is_json:
        
        data = request.get_json()
        
        if data.get("autosave"):
            
            newText = data.get("text", "")
            newText = newText.replace("\r\n", "\n")
            
            with open(f"Notes/{noteName}", "w", encoding="utf-8") as file:
                file.write(newText)
                
            notes, words = indexSingular(notes, words, noteName)
                
            return jsonify({"status": "ok"})
        
    return render_template("edit.html", note=note)
        
if __name__ == "__main__":
    app.run(debug=True)