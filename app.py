from flask import Flask, render_template, request, redirect, url_for, jsonify
from userManager import *
from indexer import *
from parser import *
from models import User

# usernames is a set so you can only use in
users, userNames = createUsers()

app = Flask(__name__)

@app.route("/<user>/words/", methods=["GET", "POST"])
def wordsPage(user):
    
    if user not in userNames:
        return "User not found", 404
    else:
        return render_template("words.html", words = users[user].words, user=users[user])   

@app.route("/<user>/notes/", methods=["GET", "POST"])
def notesPage(user):
    
    if user not in userNames:
        return "User not found", 404
    else:
        return render_template("notes.html", notes = users[user].notes, user=users[user])

@app.route("/<user>/create/", methods=["GET", "POST"])
def create(user):
    global users
    
    if request.method == "POST":
        
        noteName = request.form.get("name", "")
        noteName = noteName.replace(" ", "_")
        
        if not noteName.endswith(".md"):
            noteName = f"{noteName}.md"
        
        if noteName in users[user].notes:
            return "A note with this name already exists!", 400
        else:
            with open(f"Notes/{user}/{noteName}", "w", encoding="utf-8") as file:
                file.write("")
        
        users[user].notes, users[user].words = indexSingular(notes, words, noteName, users[user])
        
        return redirect(url_for("edit", noteName=noteName, user=users[user]))
    
    return render_template("create.html")

@app.route("/<user>/preview/<noteName>/", methods=["GET", "POST"])
def preview(user, noteName):
    
    global users
    
    if user in userNames:
    
        if noteName not in users[user].notes:
            return "This note is NULL (Not Found)", 404
        else:
            note = users[user].notes[noteName]
            
            htmlText = highlightHtml(note.text)
    
            return render_template("preview.html", noteText=htmlText, user=users[user] )       
    else:
        
        return "profile does not exist", 404
    
    

@app.route("/<user>/edit/<noteName>/", methods=["GET", "POST"])
def edit(user, noteName):
    
    global users
    
    if request.method == "POST" and request.is_json:
        
        data = request.get_json()
        
        if data.get("autosave"):
            
            newText = data.get("text", "")
            newText = newText.replace("\r\n", "\n")
            
            with open(f"Notes/{users[user].name}/{noteName}", "w", encoding="utf-8") as file:
                file.write(newText)
                
            notes, words = indexSingular(users[user].notes, users[user].words, noteName, users[user])
                
            return jsonify({"status": "ok"})
        
        
    if user in userNames:
        
        if noteName not in users[user].notes:
            return "This note is NULL (Not Found)", 404
        else:
            note = users[user].notes[noteName]
            return render_template("edit.html", note=note, user=users[user])    
    
        
    
        
if __name__ == "__main__":
    app.run(debug=True)