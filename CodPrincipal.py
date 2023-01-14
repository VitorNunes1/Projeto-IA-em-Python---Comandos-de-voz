import pyautogui
import speech_recognition as sr
import time
import os
import threading
import keyboard
import requests
from tkinter import *

def listenMicrophone():
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microphone.listen(source)
        try:
            
            """img = pyautogui.locateOnScreen('PesquisaSteam.png', confidence=0.7)"""
            frase = microphone.recognize_google(audio, language='pt-BR')
            if "navegador" in frase:
                print("Você falou: " + frase)
                os.system("start Chrome.exe")
                listenMicrophone()
            if "jogo" in frase:
                print("Você falou: " + frase)
                os.system("start E:\Steam\Steam.exe")
                time.sleep(5)
                
                image = 'PesquisaSteam.png'
                local = pyautogui.locateCenterOnScreen(image, confidence=0.7)
                pyautogui.click(local)
                print(f'A posição: {local}')
                pyautogui.write('Braw')
                
                time.sleep(1.25)
                braw = 'braa.png'
                achou = pyautogui.locateCenterOnScreen(braw, confidence=0.7)
                pyautogui.click(achou)
                
                time.sleep(1.25)
                joguin = 'juegar.png'
                achoujogo = pyautogui.locateCenterOnScreen(joguin, confidence=0.7)
                pyautogui.click(achoujogo)
                listenMicrophone()
            if "jogar" in frase:
                jogarconfig = 'jogar2.png'
                jogarlog = pyautogui.locateCenterOnScreen(jogarconfig, confidence=0.7)
                print(jogarlog)
                pyautogui.click(jogarlog)
                listenMicrophone()
            if 'modo livre' in frase:
                modolivre = 'Modolivre.png'
                modol = pyautogui.locateCenterOnScreen(modolivre, confidence=0.7)
                pyautogui.click(modol)
                listenMicrophone()
            if '1 contra 1' in frase:
                v1 = '1v1.png'
                x1 = pyautogui.locateCenterOnScreen(v1, confidence=0.7)
                pyautogui.click(x1)
                listenMicrophone()
            if '2 contra 2' in frase:
                v2 = '2v2.png'
                x2 = pyautogui.locateCenterOnScreen(v2, confidence=0.7)
                pyautogui.click(x2)
                listenMicrophone()
            if '1 contra 1 experimental' in frase:
                v1ex = '1v1ex.png'
                x1ex = pyautogui.locateCenterOnScreen(v1ex, confidence=0.7)
                pyautogui.click(x1ex)
                listenMicrophone()
            if 'v' or 've' in frase:
                ve = 'letrav.png'
                vee = pyautogui.locateCenterOnScreen(ve, confidence=0.7)
                pyautogui.click(vee)
                listenMicrophone()
            if 'x' or 'fechar' in frase:
                xfecha = 'Xfechar.png'
                xfechar = pyautogui.locateCenterOnScreen(xfecha, confidence=0.7)
                pyautogui.click(xfechar)
                listenMicrophone()
            if 'mais informações' in frase:
                inf = 'MaisInformacoes.png'
                moreinf = pyautogui.locateCenterOnScreen(inf, confidence=0.7)
                pyautogui.click(moreinf)
                listenMicrophone()
                    
            print(frase)

                
        
        except sr.UnknownValueError:
            print("Não ficou nítido.")
            listenMicrophone()
                              
        return frase

def testi():
    if keyboard.is_pressed("v"):
            listenMicrophone()
def infinito():
    while True:
        testi()

janela = Tk()
janela.title("Voice of game")
janela.geometry("400x400")
texto_orientar = Label(janela, text="Clique no botão para iniciar os comandos de voz!")
texto_orientar.grid(column=0, row=0, padx=60, pady=10)
texto_orientar2 = Label(janela, text="Você falou: ")
texto_orientar2.grid(column=0, row=1, padx=10, pady=0)
botao = Button(janela, text="Press it", command=infinito)  
botao.grid(column=0, row=2, padx=30, pady=20)
janela.mainloop()

