import requests
from tkinter import *

window = Tk()
window.geometry('700x700')

frame = Frame(window)
frame.pack(fill=BOTH,expand=1)

canvas = Canvas(frame)
canvas.pack(side=LEFT,fill=BOTH,expand=1)

scroll1 = Scrollbar(frame, orient=VERTICAL,command=canvas.yview)
scroll1.pack(side=RIGHT,fill=Y)

scroll2 = Scrollbar(frame, orient=HORIZONTAL,command=canvas.xview)
scroll2.pack(side=BOTTOM,fill=X)

canvas.config(yscrollcommand=scroll1.set)
canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

canvas.config(xscrollcommand=scroll2.set)
canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

frame2 = Frame(canvas)

canvas.create_window((0,0),window=frame2,anchor='nw')

api_key = "RGAPI-b969d97b-b4a3-45d5-a7ab-f55ac4a84c7c"

api_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4755286728'
api_url = api_url + '?api_key=' + api_key

puuid = 'GqNVujBeugkp9-pov5TudRh5oe8myFF9iMDfy_909m5kY7uVoytCEK-r5N-eVTZOaVzIeiDlwTgaWA'
resp = requests.get(api_url)
match_data = resp.json()
part_index = match_data['metadata']['participants'].index(puuid)
row = 0
stats = match_data['info']['participants'][part_index]
for i in stats:
    if i == 'challenges':
        Label(frame2, text=f'{i}:').grid(row=row, column=0, pady=10, padx=10)
        i = ''
        Label(frame2, text='').grid(row=row, column=1, pady=10)
    elif i == 'perks':
        Label(frame2, text=f'{i}:').grid(row=row, column=0, pady=10, padx=10)
        i = ''
        Label(frame2, text='').grid(row=row, column=1, pady=10)
    else:
        Label(frame2, text=f'{i}:').grid(row=row,column=0,pady=10,padx=10)
        Label(frame2, text=stats.get(i)).grid(row=row, column=1, pady=10)
    row += 1

window.mainloop()