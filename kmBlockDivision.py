# -*- coding: utf-8 -*-

import cv2

def kmBlockDivision(frame, bSize):
    newx = frame.shape[1] / bSize
    newy = frame.shape[0] / bSize
    blockImg = cv2.resize(frame, (newx, newy), interpolation=cv2.INTER_AREA)
    
    return blockImg