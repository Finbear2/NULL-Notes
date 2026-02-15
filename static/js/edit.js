const height = (window.innerHeight - 164) + "px";
let autosaveTimeout;

const easyMDE = new EasyMDE({
    element: document.getElementById("text"),
    toolbar: [
        {
            name: "bold",
            action: EasyMDE.toggleBold,
            className: "fa-solid fa-bold",
            title: "Bold"
        },
        {
            name: "italic",
            action: EasyMDE.toggleItalic,
            className: "fa-solid fa-italic",
            title: "Italic"
        },
        {
            name: "heading",
            action: EasyMDE.toggleHeadingSmaller,
            className: "fa-solid fa-heading",
            title: "Heading"
        },
        "code",
        "quote",
        "unordered-list",
        "ordered-list"
    ],
    renderingConfig: {
        singleLineBreaks: false,
        codeSyntaxHighlighting: true
    },
    autofocus: true,
    tabSize: 4,
    toolbarTips: true,
    status: ["lines", "words", "cursor"],
    autoDownloadFontAwesome: false, 
    indentWithTabs: true,
    placeholder: "NULL",
    spellChecker: false,            
    lineWrapping: true,  
    inputStyle: "contenteditable",           
    forceSync: true,
    maxHeight: height                
});

function autosave() {
    
    clearTimeout(autosaveTimeout);
    
    autosaveTimeout = setTimeout(() => {
        const content = easyMDE.value();
        const url = window.location.pathname;

        fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ autosave: true, text: content })
        })
        .then(res => res.json())
        .then(data => console.log("Autosaved at", new Date().toLocaleTimeString()))
        .catch(err => console.error("Autosave failed", err));

    }, 500);
}

easyMDE.codemirror.on("change", autosave);