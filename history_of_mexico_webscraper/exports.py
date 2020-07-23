from bs4 import BeautifulSoup
import requests

def get_citations_needed(url: str) -> int:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    references = soup.findAll("a", {"href": "/wiki/Wikipedia:Citation_needed"})
    return len(references)
    
def get_citations_needed_report(url: str) -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content)
    paragraphs = soup.findAll("p")
    filtered_paragraphs = []
    for paragraph in paragraphs:
        if len(paragraph.findAll("a", {"href": "/wiki/Wikipedia:Citation_needed"})) >= 1:
            filtered_paragraphs.append(paragraph)
    output = ""
    for paragraph in filtered_paragraphs:
        for text in paragraph.text.split("[citation needed]")[:-1]:
            output += text.strip() + "\n\n"
    return output