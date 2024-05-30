translations = {
    "Navigation":{
        "en": "Navigation",
        "de": "Navigation"
    },
    "Home": {
        "en": "Home",
        "de": "Startseite"
    },
    "A few sentences about yourself.": {
        "en": "A few sentences about yourself.",
        "de": "Ein paar Sätze über dich."
    },
    "Link to CV and References": {
        "en": "Link to CV and References",
        "de": "Link zu Lebenslauf und Referenzen"
    },
    "Link to Projects": {
        "en": "Link to Projects",
        "de": "Link zu Projekten"
    },
    "Link to Blog": {
        "en": "Link to Blog",
        "de": "Link zum Blog"
    },
    "Link to ????": {
        "en": "Link to ????",
        "de": "Link zu ????"
    },
    "CV and References": {
        "en": "CV and References",
        "de": "Lebenslauf und Referenzen"
    },
    "Top general description": {
        "en": "Top general description",
        "de": "Allgemeine Beschreibung"
    },
    "Download CV and References": {
        "en": "Download CV and References",
        "de": "Lebenslauf und Referenzen herunterladen"
    },
    "University details with images": {
        "en": "University details with images",
        "de": "Universitätsdetails mit Bildern"
    },
    "Short text about University 1": {
        "en": "Short text about University 1",
        "de": "Kurzer Text über Universität 1"
    },
    "References": {
        "en": "References",
        "de": "Referenzen"
    },
    "Projects": {
        "en": "Projects",
        "de": "Projekte"
    },
    "Overview of projects": {
        "en": "Overview of projects",
        "de": "Überblick über Projekte"
    },
    "Details of Project 1": {
        "en": "Details of Project 1",
        "de": "Details des Projekts 1"
    },
    "Details of Project 2": {
        "en": "Details of Project 2",
        "de": "Details des Projekts 2"
    },
    "Header": {
        "en": "Header",
        "de": "Kopfzeile"
    },
    "Introduction": {
        "en": "Introduction",
        "de": "Einführung"
    },
    "Results": {
        "en": "Results",
        "de": "Ergebnisse"
    },
    "Acknowledgment": {
        "en": "Acknowledgment",
        "de": "Anerkennung"
    },
    "Blog": {
        "en": "Blog",
        "de": "Blog"
    },
    "Enter Password": {
        "en": "Enter Password",
        "de": "Passwort eingeben"
    },
    "Blog content here": {
        "en": "Blog content here",
        "de": "Blog-Inhalt hier"
    },
    "Please enter the correct password to access the blog.": {
        "en": "Please enter the correct password to access the blog.",
        "de": "Bitte geben Sie das richtige Passwort ein, um auf den Blog zuzugreifen."
    },
    "Legal": {
        "en": "Legal",
        "de": "Rechtliches"
    },
    "Terms": {
        "en": "Terms",
        "de": "Bedingungen"
    },
    "Privacy Policy": {
        "en": "Privacy Policy",
        "de": "Datenschutzbestimmungen"
    },
    "Terms content here": {
        "en": "Terms content here",
        "de": "Bedingungen hier"
    },
    "Privacy policy content here": {
        "en": "Privacy policy content here",
        "de": "Datenschutzbestimmungen hier"
    }
}

def translate(text, language):
    try:
        return translations.get(text, {}).get(language, translations.get(text, {}).get("en", text))
    except:
        return "en"


