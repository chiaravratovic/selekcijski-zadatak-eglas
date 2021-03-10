# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:06:05 2021

@author: Chiara
"""

import PySimpleGUI as sg

sg.theme('Green') 

global traffic
traffic = []

def open_error_window():
    layout = [[sg.Text('Dogodila se greška!')],
              [sg.Button('Ok', key='ok', bind_return_key=True)]]
    window = sg.Window('Greška', layout, modal=True)
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'ok'):
            break
        
    window.close()

def open_passengers_window():
    err = 0
    layout = [[sg.Text('Broj putnika koji su izašli iz tramvaja'), sg.Input(key='izasli')],
               [sg.Text('Broj putnika koji su ušli u tramvaj'), sg.Input(key='usli')],
               [sg.Button('Unesi', key='unesi', bind_return_key=True)]]
    
    window = sg.Window("Unos broja putnika", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            err = 1
            break
        
        if event == 'unesi': 
            try:
                int(values['izasli'])
            except:
                err = 1
                open_error_window()
                break
        
            try:
                int(values['usli'])
            except:
                err = 1
                open_error_window()
                break
            
            traffic.append(int(values['izasli']))
            traffic.append(int(values['usli']))
            break

    window.close()
    return err
    
def calculate_capacity():
    c = 0
    minc = 0
    i = 0
    while i < len(traffic):
        c = c - traffic[i] + traffic[i+1]
        if c > minc:
            minc = c
        i += 2
    return minc

def open_final_window(n):
    layout = [[sg.Text("Minimalni mogući kapacitet tramvaja je "+str(n)+"!")],
               [sg.Button('Ok', key = 'ok', bind_return_key=True)]]
    window = sg.Window("Kapacitet", layout, modal=True)
    while True:
        event, values = window.read()
        if event in ('ok', sg.WIN_CLOSED):
            break
        
    window.close()
    
def main():
    layout = [[sg.Text('Unesite broj stanica tramvaja:')],
               [sg.Input(key='broj_stanica')],
               [sg.Button('Ok', key = 'ok', bind_return_key=True)]]
    window = sg.Window("Unos broja stanica", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "ok":
            try:
                int(values['broj_stanica'])
            except:
                open_error_window()
                break
            for i in range(int(values['broj_stanica'])):
                err = open_passengers_window()
                if err == 1:
                    break
                
            if err == 0:
                min_capacity = calculate_capacity()
                open_final_window(min_capacity)
                break
            else:
                traffic.clear()
    window.close()
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    