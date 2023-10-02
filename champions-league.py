
import random

# this are UEFA teams from 2021 champions league 
teams = [
    {"name": "Bayern Munich", "league": "Bundesliga", "coefficient": 154.000},
    {"name": "Real Madrid", "league": "La Liga", "coefficient": 134.000},
    {"name": "Manchester City", "league": "Premier League", "coefficient": 131.000},
    {"name": "Liverpool", "league": "Premier League", "coefficient": 125.000},
    {"name": "Chelsea", "league": "Premier League", "coefficient": 124.000},
    {"name": "Atletico Madrid", "league": "La Liga", "coefficient": 120.000},
    {"name": "Barcelona", "league": "La Liga", "coefficient": 118.000},
    {"name": "Manchester United", "league": "Premier League", "coefficient": 103.000},
    {"name": "Juventus", "league": "Serie A", "coefficient": 100.000},
    {"name": "Paris Saint-Germain", "league": "Ligue 1", "coefficient": 96.000},
    {"name": "Sevilla", "league": "La Liga", "coefficient": 95.000},
    {"name": "Dortmund", "league": "Bundesliga", "coefficient": 90.000},
    {"name": "Porto", "league": "Primeira Liga", "coefficient": 87.000},
    {"name": "Ajax", "league": "Eredivisie", "coefficient": 79.500},
    {"name": "RB Leipzig", "league": "Bundesliga", "coefficient": 66.000},
    {"name": "Lazio", "league": "Serie A", "coefficient": 60.000},
    {"name": "Inter Milan", "league": "Serie A", "coefficient": 53.000},
    {"name": "Atalanta", "league": "Serie A", "coefficient": 50.500},
    {"name": "Borussia Monchengladbach", "league": "Bundesliga", "coefficient": 50.000},
    {"name": "Shakhtar Donetsk", "league": "Ukrainian Premier League", "coefficient": 48.000},
    {"name": "Olympiacos", "league": "Super League Greece", "coefficient": 45.000},
    {"name": "Lokomotiv Moscow", "league": "Russian Premier League", "coefficient": 37.500},
    {"name": "Marseille", "league": "Ligue 1", "coefficient": 35.000},
    {"name": "Club Brugge", "league": "Belgian First Division A", "coefficient": 34.000},
    {"name": "Borussia Dortmund", "league": "Bundesliga", "coefficient": 30.000},
    {"name": "Ferencvaros", "league": "Nemzeti Bajnokság I", "coefficient": 30.000},
    {"name": "Rennes", "league": "Ligue 1", "coefficient": 29.500},
    {"name": "Istanbul Basaksehir", "league": "Süper Lig", "coefficient": 29.500},
    {"name": "Midtjylland", "league": "Superliga", "coefficient": 29.000},
    {"name": "Krasnodar", "league": "Russian Premier League", "coefficient": 28.000},
    {"name": "Salzburg", "league": "Austrian Bundesliga", "coefficient": 25.500},
    {"name": "Slavia Prague", "league": "Czech First League", "coefficient": 25.500},
    {"name": "Celtic", "league": "Scottish Premiership", "coefficient": 25.000},
    {"name": "Basel", "league": "Swiss Super League", "coefficient": 24.500},
    {"name": "Wolfsburg", "league": "Bundesliga", "coefficient": 24.000},
    {"name": "Young Boys", "league": "Swiss Super League", "coefficient": 23.500},
    {"name": "Genk", "league": "Belgian First Division A", "coefficient": 23.000},
    {"name": "Copenhagen", "league": "Superliga", "coefficient": 22.500},
    {"name": "Malmo", "league": "Allsvenskan", "coefficient": 22.500},
    {"name": "Ludogorets", "league": "First Professional Football League", "coefficient": 22.000},
    {"name": "Sparta Prague", "league": "Czech First League", "coefficient": 22.000},
    {"name": "Zorya Luhansk", "league": "Ukrainian Premier League", "coefficient": 21.500},
    {"name": "Red Star Belgrade", "league": "Serbian SuperLiga", "coefficient": 21.500},
    {"name": "Dinamo Zagreb", "league": "Prva HNL", "coefficient": 21.500},
    {"name": "Rapid Vienna", "league": "Austrian Bundesliga", "coefficient": 21.000},
    {"name": "Rangers", "league": "Scottish Premiership", "coefficient": 20.500},
    {"name": "Feyenoord", "league": "Eredivisie", "coefficient": 20.500},
    {"name": "AZ Alkmaar", "league": "Eredivisie", "coefficient": 20.000},
    {"name": "PAOK", "league": "Super League Greece", "coefficient": 19.500},
    {"name": "Molde", "league": "Eliteserien", "coefficient": 19.000},
    {"name": "Slovan Bratislava", "league": "Slovak Super Liga", "coefficient": 18.500},
    {"name": "Slovan Liberec", "league": "Czech First League", "coefficient": 18.500},
    {"name": "Qarabag", "league": "Azerbaijan Premier League", "coefficient": 18.000},
    {"name": "Rosenborg", "league": "Eliteserien", "coefficient": 17.500},
    {"name": "Hapoel Be'er Sheva", "league": "Israeli Premier League", "coefficient": 17.000},
    {"name": "Ferencvaros", "league": "Nemzeti Bajnokság I", "coefficient": 16.000},
    {"name": "Dinamo Tbilisi", "league": "Erovnuli Liga", "coefficient": 16.000},
    {"name": "Djurgarden", "league": "Allsvenskan", "coefficient": 15.500},
    {"name": "Sileks", "league": "Macedonian First Football League", "coefficient": 15.000},
    {"name": "Dundalk", "league": "League of Ireland Premier Division", "coefficient": 15.000},
    {"name": "CSKA Sofia", "league": "First Professional Football League", "coefficient": 15.000},
    {"name": "Mura", "league": "Slovenian PrvaLiga", "coefficient": 14.500},
    {"name": "Partizani", "league": "Kategoria Superiore", "coefficient": 14.500},
    {"name": "Riga FC", "league": "Latvian Higher League", "coefficient": 14.000},
    {"name": "Fola Esch", "league": "National Division", "coefficient": 13.500},
    {"name": "Connah's Quay Nomads", "league": "Cymru Premier", "coefficient": 13.000},
      {"name": "Maccabi Haifa", "league": "Israeli Premier League", "coefficient": 12.500},
    {"name": "Neftchi Baku", "league": "Azerbaijan Premier League", "coefficient": 12.000},
    {"name": "Dinamo Batumi", "league": "Erovnuli Liga", "coefficient": 12.000},
    {"name": "Lincoln Red Imps", "league": "Gibraltar Premier Division", "coefficient": 11.500},
    {"name": "Borac Banja Luka", "league": "Premier League of Bosnia and Herzegovina", "coefficient": 11.500},
    {"name": "Prishtina", "league": "Kategoria Superiore", "coefficient": 11.000},
    {"name": "Vllaznia", "league": "Kategoria Superiore", "coefficient": 11.000},
    {"name": "La Chaux-de-Fonds", "league": "Swiss Promotion League", "coefficient": 10.500},
    {"name": "B36 Torshavn", "league": "Betri deildin", "coefficient": 10.000},
    {"name": "HB", "league": "Betri deildin", "coefficient": 10.000},
    {"name": "Santa Coloma", "league": "Primera Divisió", "coefficient": 9.500},
    {"name": "HB", "league": "Betri deildin", "coefficient": 9.000},
    {"name": "Engordany", "league": "Primera Divisió", "coefficient": 8.000},
    {"name": "Tre Fiori", "league": "Campionato Sammarinese di Calcio", "coefficient": 7.500},
    {"name": "Glacis United", "league": "Gibraltar National League", "coefficient": 7.000},
    {"name": "St Joseph's", "league": "Gibraltar National League", "coefficient": 6.500},
    {"name": "College Europa", "league": "Gibraltar National League", "coefficient": 6.000},
    {"name": "Victoria Hotspurs", "league": "Gibraltar National League", "coefficient": 5.500},
    {"name": "Atlantas", "league": "A Lyga", "coefficient": 5.000},
    {"name": "Ararat-Armenia", "league": "Armenian Premier League", "coefficient": 4.500},
    {"name": "La Fiorita", "league": "Campionato Sammarinese di Calcio", "coefficient": 4.000},
    {"name": "Glentoran", "league": "NIFL Premiership", "coefficient": 3.500},
    {"name": "Drita", "league": "Football Superleague of Kosovo", "coefficient": 3.000},
    {"name": "HB", "league": "Betri deildin", "coefficient": 2.500},
    {"name": "Lincoln Red Imps", "league": "Gibraltar National League", "coefficient": 2.000},
    {"name": "Tre Fiori", "league": "Campionato Sammarinese di Calcio", "coefficient": 1.500},
    {"name": "Prishtina", "league": "Football Superleague of Kosovo", "coefficient": 1.000},
]
# Sort teams using the lamba fuction for sorting x "coefficient", in descending order
teams.sort(key=lambda x: -x["coefficient"])

# the pots to be uwed for seeding
pots = {
    "Pot 1": [],
    "Pot 2": [],
    "Pot 3": [],
    "Pot 4": [],
}
# dding the teams to the pots based on their sorted coefficient
for i, team in enumerate(teams):
    if i < 8:
        pots["Pot 1"].append(team)
    elif i < 16:
        pots["Pot 2"].append(team)
    elif i < 24:
        pots["Pot 3"].append(team)
    else: #this was done just in case u have multiple teams from the same league in the top 32
        pots["Pot 4"].append(team)

# the group stages 
num_groups = 8
groups = {f"Group {i}": [] for i in range(1, num_groups + 1)}

# cheecks if two leagues are from the same team, 
def any_two_teams_same_league(group):
    leagues = [team["league"] for team in group]
    return len(set(leagues)) < len(leagues)

# randomly disperses pot one into first position in various groups
for i, pot_team in enumerate(random.sample(pots["Pot 1"], num_groups)):
    group_name = f"Group {i + 1}"
    groups[group_name].append(pot_team)
    pots["Pot 1"].remove(pot_team)

# Draw teams from Pots 2, 3, and 4 while considering the rules
for pot_name in ["Pot 2", "Pot 3", "Pot 4"]:
    random.shuffle(pots[pot_name])
    for group_name in groups:
        if len(groups[group_name]) < 4:
            team = None
            while not team:
                if not pots[pot_name]:
                    break  # Skip if the pot is empty
                selected_team = pots[pot_name].pop()
                if (
                    len(groups[group_name]) < 4
                    and not any_two_teams_same_league(groups[group_name] + [selected_team])
                ):
                    team = selected_team
            if team:
                groups[group_name].append(team)

# Ensure each group has exactly 4 teams
for group_name in groups:
    while len(groups[group_name]) < 4:
        for pot_name in ["Pot 2", "Pot 3", "Pot 4"]:
            if pots[pot_name]:
                selected_team = pots[pot_name].pop()
                groups[group_name].append(selected_team)

# Print the seeded groups
for group_name, group_teams in groups.items():
    print(f"{group_name}:")
    for team in group_teams:
        print(f"- {team['name']} (Coefficient: {team['coefficient']}, League: {team['league']})")
    print()
