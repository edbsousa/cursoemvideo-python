# Exercício 21 – Tocando um MP3
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


import pygame


pygame.mixer.init()
pygame.init()

file = 'JohnBartmann_EarningHappiness.mp3'

pygame.mixer.music.load(file)
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()



