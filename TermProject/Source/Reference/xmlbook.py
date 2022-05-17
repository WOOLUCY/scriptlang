# -*- coding: utf-8 -*-
from xml.dom.minidom import parse
from xml.etree import ElementTree

##### global
BooksDoc = None

#### Menu  implementation

#### xml function implementation
def LoadXMLFromFile():
    global BooksDoc
    fileName = input ("please input file name to load :") 
 
    try:
        with open(fileName, encoding='utf-8') as xmlFD:
            try:
                dom = parse(xmlFD)
            except Exception:
                print ("loading fail!!!")
            else:
                print ("XML Document loading complete")
                BooksDoc = dom  #####
                return dom
    except IOError:
        print ("invalid file name or path")
        return None
    return None

def BooksFree():
    if checkDocument():
        BooksDoc.unlink()
     


def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc.toprettyxml(newl=''))

def PrintBookTitle(tags):
    global BooksDoc
    if not checkDocument():
        return None
        
    booklists = BooksDoc.childNodes
    books = booklists[0].childNodes
    for book in books:
        if book.nodeName == "book":
            subitems = book.childNodes
            for item in subitems:
                if item.nodeName in tags:
                    print("title=",item.firstChild.nodeValue)

def AddBook(bookdata):
    global BooksDoc
    if not checkDocument() :
        return None
     
    newBook = BooksDoc.createElement('book')
    newBook.setAttribute('ISBN',bookdata['ISBN'])
    titleEle = BooksDoc.createElement('title')
    titleNode = BooksDoc.createTextNode(bookdata['title'])
    try:
        titleEle.appendChild(titleNode)
        newBook.appendChild(titleEle)
        booklist = BooksDoc.firstChild
    except Exception:
        print ("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if booklist != None:
            booklist.appendChild(newBook)   
            cnt = int(booklist.getAttribute('cnt')) + 1
            booklist.setAttribute('cnt',str(cnt))

def SearchBookTitle(keyword):
    global BooksDoc
    retlist = []
    if not checkDocument():
        return None
    #print(repr(BooksDoc.toprettyxml())) #################
        
    try:
        tree = ElementTree.fromstring(BooksDoc.toxml())
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
        
    bookElements = tree.iter("book") 
    for book in bookElements:
        title = book.find("title")
        if title.text.find(keyword) >=0:
            retlist.append((book.attrib["ISBN"], title.text))
    
    return retlist

# 둘다 markup언어이지만 : xml은 구조를 정의, html은 내용을 정의
def MakeHtmlDoc(BookList):
    from xml.dom.minidom import getDOMImplementation
    impl = getDOMImplementation()
    
    newdoc = impl.createDocument(None, "html", None)
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    body = newdoc.createElement('body')

    for bookitem in BookList:
        b = newdoc.createElement('b')
        ibsnText = newdoc.createTextNode("ISBN:" + bookitem[0])
        b.appendChild(ibsnText)
        body.appendChild(b)
    
        p = newdoc.createElement('p')
        titleText= newdoc.createTextNode("Title:" + bookitem[1])
        p.appendChild(titleText)
        body.appendChild(p)

        br = newdoc.createElement('br')
        body.appendChild(br)
         
    top_element.appendChild(body)
    
    return newdoc.toprettyxml()
    
def printBookList(blist):
    for res in blist:
        print (res)    
    
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True