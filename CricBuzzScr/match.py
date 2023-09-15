import requests
from bs4 import BeautifulSoup as bs4


# This function when called will give you the popular live matches from the cricbuzz website.
def get_match():
    
    # Sending Request to the url
    url = "https://www.cricbuzz.com"
    page = requests.get(url)
    soup = bs4(page.content, 'html.parser')
    
    # Getting the links for the matches
    matches = soup.find_all("ul", "cb-col cb-col-100 videos-carousal-wrapper cb-mtch-crd-rt-itm")
    m_links = {}

    # Making a dictionary with the links
    for i in matches:
        for j in list(i.find_all("a")):
            if len(j.get_text().split()) > 2:
                m_links[j.get('title')] = str('https://www.cricbuzz.com') + j.get('href')
                
    for idx, lk in enumerate(m_links):
        print(f"{idx+1}  {lk}")
    
    # Returns the url for the match
    return m_links[list(m_links.keys())[int(input("Match Number: "))-1]]


# This function when called will give you the commentary of the match that you already selcted.
def get_commentary(url):
        
    # Sending request to the url
    page = requests.get(url)
    soup = bs4(page.content, 'html.parser')
    # Delay or anything
    delay = soup.find_all("div", "cb-col cb-col-100 cb-font-18 cb-toss-sts cb-text-delay")
    for i in list(delay):
        print(i.get_text().strip())  
    print("\n")
    
    # Score
    sc = soup.find_all("div", "cb-col cb-col-67 cb-scrs-wrp")
    for i in list(sc):
        print(i.get_text().strip())  
    print("\n")
    # Result
    rs = soup.find_all("div", "cb-col cb-col-100 cb-min-stts cb-text-complete")
    if len(rs) != 0:
        for i in list(rs):
            print(i.get_text().strip())
        print("\n")
    # POTM
    pm = soup.find_all("div", "cb-col cb-col-50 cb-mom-itm")
    if len(pm) != 0:
        for i in list(pm):
            print(i.get_text().strip())
        print("\n")
    # Batsmen and Bowlers
    bb = soup.find_all("div", "cb-col cb-col-100 cb-min-itm-rw")
    if len(bb) != 0:
        for i in range(len(bb)):
            if i == 0:
                print("Batter\tR\tB\t4s\t6s\tSR")
            elif i == len(bb)-2:
                print("\n")
                print("Bowler\tO\tM\tR\tW\tECO")
            print(bb[i].get_text().strip())
        print("\n")
    # Recent balls
    rc = soup.find_all("div", "cb-col cb-col-100 cb-font-12 cb-text-gray cb-min-rcnt")
    if len(rc) != 0:
        for i in list(rc):
            print(i.get_text())
        print("\n")
    # Key Stats
    ks = soup.find_all("div", "cb-min-itm-rw")
    if len(ks) != 0:
        for i in list(ks)[-4:]:
            print(i.get_text().strip())
        print("\n")
    # Last 12 balls commentary
    balls = soup.find_all("div", "cb-mat-mnu-wrp cb-ovr-num")
    comm = soup.find_all("p", "cb-com-ln cb-col cb-col-90")
    
    if len(balls) != 0 and len(comm) != 0:
        for i, j in zip(list(balls)[:12], list(comm)[:12]):
            if i == list(balls)[0]:
                print("Last 12 deliveries summary:\n")
            print(i.get_text().strip() + "\t" + j.get_text().strip())
        print("\n")

    return


# This function when called will give you the scorecard of the match you have selected
def get_scorecard(url):
    
    # Sending the request to the url
    page = requests.get(url)
    soup = bs4(page.content, 'html.parser')
    
    # Scraping the links for the diff tabs like commentary, scorecard, squads
    tabs = soup.find_all("a", "cb-nav-tab")

    sub_links = []

    for i in tabs:
        sub_links.append(str('https://www.cricbuzz.com') + i.get('href'))
        
    # Selecting the link for scorecard
    tab_url = sub_links[1]
    
    # Sending request to the scorecard url
    page = requests.get(tab_url)
    soup = bs4(page.content, 'html.parser')

    
    print("\t\tSCORECARD\n")

    # Full scorecard
    fs = soup.find_all("div", "cb-col cb-col-67 cb-scrd-lft-col html-refresh")


    fs_txt = ''

    for i in list(fs):
        fs_txt += i.get_text().strip()
    fs_lines = fs_txt.split("      ")

    for i in fs_lines[:-1]:
        print(i.strip())

    return