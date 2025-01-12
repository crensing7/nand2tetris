import pygame
from cpu import cpu


def pc():
    processor = cpu(32, 24577)
    processor.reset()
    while True:
        try:
            processor.cycle()
        except IndexError:
            print('No more instructions!')
            break




















