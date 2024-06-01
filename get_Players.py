import requests
from bs4 import BeautifulSoup
import random

def scrape_basketball_reference(url):
    results = []
    title = ""
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page at {url}. Status code: {response.status_code}")
        return results, title  # Return empty list and title if the page request fails

    soup = BeautifulSoup(response.content, 'html.parser')
    tbody = soup.find('tbody')
    if not tbody:
        print(f"No 'tbody' found in table on page at {url}")
        return results, title

    if "players-who-played-for-multiple-teams-franchises" in url:
        players = tbody.find_all('th', {'data-stat': 'player'})
        if not players:
            print(f"No players found in 'tbody' on page at {url}")
            return results, title
        for player in players:
            name = player.get_text().strip()
            results.append(name)
    else:
        players = tbody.find_all('tr')
        if not players:
            print(f"No players found in 'tbody' on page at {url}")
            return results, title
        for player in players:
            name_player = player.find('td', {'data-stat': 'player'})
            if name_player:
                name = name_player.text.strip()
                results.append(name)
    
    title_tag = soup.select_one('title')
    if title_tag:
        full_title = title_tag.get_text().strip().split(" | ")[0]
        # Extract the part that starts with "NBA and ABA Players"
        start_index = full_title.find("NBA and ABA Players")
        if start_index == -1:
            title = full_title
        if start_index != -1:
            title = full_title[start_index:]
    return results, title

def choosePlayers(url):
    allPlayers, title = scrape_basketball_reference(url)
    
    if len(allPlayers) < 4:
        print(f"Not enough players found at {url}")
        return [], title
    
    return random.sample(allPlayers, 4), title

# List of Power 5 schools
power_5_schools = ["Alabama", "Arkansas", "Auburn", "Florida", "Georgia", "Kentucky", "LSU", "Mississippi", "Missouri", "South Carolina", "Tennessee", "Texas A&M", "Vanderbilt", 
                   "Illinois", "Indiana", "Iowa", "Maryland", "Michigan", "Michigan State", "Minnesota", "Nebraska", "Northwestern", "Ohio State", "Penn State", "Purdue", "Rutgers", "Wisconsin", 
                   "Arizona", "Arizona State", "California", "Colorado", "Oregon", "Oregon State", "Stanford", "UCLA", "USC", "Utah", "Washington", "Washington State",
                   "Boston College", "Clemson", "Duke", "Florida State", "Georgia Tech", "Louisville", "Miami", "North Carolina", "NC State", "Pittsburgh", "Syracuse", "Virginia", "Virginia Tech", "Wake Forest"]

# List of US States
us_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# List of NBA teams
nba_teams = ["ATL", "BOS", "BKN", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

# Function to get random URLs
def get_random_urls():
    random_year = random.randint(1970, 2003)
    random_state = random.choice(us_states)
    random_college = random.choice(power_5_schools)
    random_team1 = random.choice(nba_teams)
    random_team2 = random.choice([team for team in nba_teams if team != random_team1])

    birthplace_url = f"https://www.basketball-reference.com/friv/birthplaces.fcgi?country=US&state={random_state}"
    birthyear_url = f"https://www.basketball-reference.com/friv/birthyears.fcgi?year={random_year}"
    college_url = f"https://www.basketball-reference.com/friv/colleges.fcgi?college={random_college}"
    teams_url = f"https://www.basketball-reference.com/friv/players-who-played-for-multiple-teams-franchises.fcgi?level=franch&t1={random_team1}&t2={random_team2}&t3=--&t4=--"

    return [birthplace_url, birthyear_url, college_url, teams_url]

def ensure_unique_groups(urls):
    while True:
        player_groups = []
        titles = []
        
        for url in urls:
            players, title = choosePlayers(url)
            if len(players) < 4:
                print("Retrying due to insufficient players in one or more groups...")
                break
            player_groups.append(players)
            titles.append(title)
        else:
            # Flatten the list of groups into a single list of players
            all_players = [player for group in player_groups for player in group]
            
            # Check if all players are unique
            if len(all_players) == len(set(all_players)):
                break
    
    return player_groups, titles

def get_unique_player_groups():
    urls = get_random_urls()
    return ensure_unique_groups(urls)

if __name__ == "__main__":
    unique_player_groups, titles = get_unique_player_groups()

    # Print the groups with their descriptions
    for i, (group, title) in enumerate(zip(unique_player_groups, titles)):
        print(f"Group {i+1} ({title}): {group}")

