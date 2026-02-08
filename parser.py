from flask import url_for
from fileLoader import loadStopwords
from markupsafe import Markup
from utils import normalizeWord
from markdown_it import MarkdownIt
from markdown_it.presets import gfm_like
from linkify_it import LinkifyIt
import mdit_py_plugins
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.tasklists import tasklists_plugin
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.field_list import fieldlist_plugin
from mdit_py_plugins.texmath import texmath_plugin
from mdit_py_plugins.subscript import sub_plugin
from mdit_py_plugins.dollarmath import dollarmath_plugin
import string
import re
   
def highlightHtml(text, user):
    
    md =( MarkdownIt("gfm-like", {"linkify": True, "breaks": True})
         .use(front_matter_plugin)
         .use(footnote_plugin)
         .use(tasklists_plugin, enabled=True, label=True)
         .use(texmath_plugin)
         .use(deflist_plugin)
         .use(fieldlist_plugin)
         .use(sub_plugin)
         .use(dollarmath_plugin)
         .enable("table")
         .enable("linkify")
         )
    
    html =  md.render(text)
    bufferWords = loadStopwords()
    
    words = []
    
    parsedText = re.findall(r'(<[^>]+>|[a-zA-Z]+|.)', html)
    
    for word in parsedText:
        
        if "<" in word or "//" in word:
            words.append(word)
            continue
        
        wordNorm = normalizeWord(word)
        
        if wordNorm is not None and wordNorm.isalpha() and wordNorm not in bufferWords:
            
            url = url_for('wordPage', user=user.name, word=word.lower())
            words.append(f'<a href="{url}" class="uniqeWord"><i><b>{word}</b></i></a>')
            
        else:
            
            words.append(word) 
    
    text = "".join(map(str, words))
    
    return Markup(text)
    
# Function to clean text
def cleanText(text, bufferWords):
    
    words = set()
    
    for word in text.split():
        
        if word.startswith("!"):
            
            words.add(word)
            
        else:
            
            word = normalizeWord(word)
            
            if word is not None:
                if word not in bufferWords:
                    words.add(word)  
                        
    return words or set()