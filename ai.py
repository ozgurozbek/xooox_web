# Get move button
# Return board
import time

def processBoard(input_button_val):
    if input_button_val == -1:
        return -1
    else:
        return runMinimax(input_button_val)

def runMinimax(input_button_val):
    """Runs Minimax with the input button, returns index from board array"""
    return input_button_val-1 if input_button_val>0 else input_button_val