from flask import Flask, render_template, request, redirect, url_for, jsonify
from userManager import *
from indexer import *
from parser import *

# NOTES
# - ALWAYS pass through the user so the sidebar can work

# usernames is a set so you can only use in
users, userNames = createUsers()

app = Flask(__name__)

# Make word page
@app.route("/<user>/words/", methods=["GET", "POST"])
def wordsPage(user):
    user = getUser(user)
    
    if user.name not in userNames:
        return "User not found", 404
    else:
        return render_template("words.html", words = user.words, user=user)   

# Make notes page
@app.route("/<user>/notes/", methods=["GET", "POST"])
def notesPage(user):
    user = getUser(user)
    
    if user.name in userNames:
        return render_template("notes.html", notes=user.notes, user=user)
    else:
        return "User not found", 404

# Make note creation page
@app.route("/<user>/create/", methods=["GET", "POST"])
def create(user):
    global users
    user = getUser(user)
    
    if request.method == "POST":
        
        # Get the text
        noteName = request.form.get("name", "")
        # Replace the spaces with underscores so it will actually be a file name
        noteName = noteName.replace(" ", "_")
        
        if not noteName.endswith(".md"):
            noteName = f"{noteName}.md"
        
        if noteName in user.notes:
            return "A note with this name already exists!", 400
        else:
            with open(f"Notes/{user.name}/{noteName}", "w", encoding="utf-8") as file:
                file.write("EDIT ME :)")
        
        user.notes, user.words = indexSingular(user.notes, user.words, noteName, user)
        
        return redirect(url_for("edit", user=user.name, noteName=noteName))
    
    return render_template("create.html", user=user)

# Create full preview note page
@app.route("/<user>/preview/<noteName>/", methods=["GET", "POST"])
def preview(user, noteName):
    global users
    user = getUser(user)
    
    if user.name in userNames:
    
        if noteName in user.notes:
            note = user.notes[noteName]
            
            htmlText = highlightHtml(note.text)
    
            return render_template("preview.html", noteText=htmlText, user=user, noteName=noteName )    
        else:
            return "This note is NULL (Not Found)", 404       
    else:
        return "profile does not exist", 404
    
# Cretae an edit note page
@app.route("/<user>/edit/<noteName>/", methods=["GET", "POST"])
def edit(user, noteName):
    global users
    user = getUser(user)
    
    if request.method == "POST" and request.is_json:
        
        data = request.get_json()
        
        if data.get("autosave"):
            
            newText = data.get("text", "")
            newText = newText.replace("\r\n", "\n")
            
            with open(f"Notes/{user.name}/{noteName}", "w", encoding="utf-8") as file:
                file.write(newText)
                
            user.notes, user.words = indexSingular(user.notes, user.words, noteName, user)
                
            return jsonify({"status": "ok"})
        
        
    if user.name in userNames:
        
        if noteName not in user.notes:
            return "This note is NULL (Not Found)", 404
        else:
            note = user.notes[noteName]
            return render_template("edit.html", note=note, user=user, noteName=noteName)    
    
# Run app main loop        
if __name__ == "__main__":
    app.run(debug=True)