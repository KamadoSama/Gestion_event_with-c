import mysql.connector
import plotly.graph_objects as go

with open('./email.txt', 'r') as f:
    email = f.read()  
    f.close()  
    

cnx = mysql.connector.connect(user='zeus', password='8716taho', host='localhost', database='event')
cursor = cnx.cursor()

query1 = (f"select plat.label, count(plat.id) as nombre_commandes from reserver inner join plat on  plat.id = reserver.plat_id inner join event on event.id=eve_id inner join user on user.id=event.use_id where user.email = '{email}' GROUP BY plat.id ORDER BY nombre_commandes DESC")
cursor.execute(query1)
resultat1 = cursor.fetchall()

query2 = (f"select last_name from user where email = '{email}'")
cursor.execute(query2)
resultat2 = cursor.fetchall()


noms_plats = []
nombre_commandes = []
nom_user = []
couleurs = ['#33FFC7', '#3333FF', 'b', 'y', 'm', 'c', 'k', 'w', '#FF5733', '#6E0DD0']


for i, (nom, nombre) in enumerate(resultat1):
    noms_plats.append(nom)
    nombre_commandes.append(nombre)
    print(i, nom, nombre)

for (nom,) in  resultat2:
    nom_user.append(nom)

""" fig = go.Figure(data=[go.Pie(labels=noms_plats, values=nombre_commandes)])
fig.update_traces(marker=dict(colors=couleurs))
 """
#SELECT plat.*, count(plat.id) as nombre_commandes from plat INNER JOIN reserver ON plat.id = reserver.plat_id INNER JOIN user ON plat.eve_id = user.id WHERE user.email = '{email}' GROUP BY plat.id ORDER BY nombre_commandes DESC 

fig = go.Figure(data=[go.Pie(labels=noms_plats, values=nombre_commandes, hole=0.4)])
fig.update_traces(marker=dict(colors=couleurs, line=dict(color='#FFFFFF', width=1)))


fig.update_layout(title_text=f'Les plats préférés parmis ceux de {nom_user[0]} :', font=dict(color='#FFFFFF'))


fig.update_layout(paper_bgcolor='#212121', plot_bgcolor='#212121')


cursor.close()
cnx.close()

fig.show()
