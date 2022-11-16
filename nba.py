import pandas as pd
import requests

def rank(url):
  r = requests.get(url, headers=header)
  dfs = pd.read_html(r.text)

  for x in dfs:
      df = pd.DataFrame(x)
  df = df[df.Player != 'Player']
  df = df.dropna(inplace=False)
  df['Score'] = [(float(x)/10)+float(y)-(float(z)/100)+(float(a)*float(b))/10+float(c) for x,y,z,a,b,c in zip(df['FG'], df['FG%'],df['TOV'],df['FT%'],df['FT'],df['eFG%'])]
  df = df.sort_values(by='Score', ascending=False)
  df = df.reset_index()
  df = df.drop(columns='index')
  df['Rk'] = [x for x in range (1,len(df)+1)]

  df = df[['Rk','Player','Pos','Age','Tm','FG','FG%','TOV','FT%','FT','eFG%','Score']]

  return df[:5]


per_game = 'https://www.basketball-reference.com/leagues/NBA_2023_per_game.html'
totals = 'https://www.basketball-reference.com/leagues/NBA_2023_totals.html'

header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}

print ('###########            PER GAME            ###########')
print (rank(per_game))
print ('###########            OVERALL            ###########')
print(rank(totals))