import visdom
import json
import numpy as np

path='losses.json' #path/to/json
name='Old losses'

f = open(path,)
  
losses = json.load(f)

X=np.stack([np.array(losses['X'])] * len(losses['legend']), 1)
Y=np.array(losses['Y'])

vis = visdom.Visdom(port='8097',env=name)

vis.line(
    Y,
    X,
    opts={
        'title': ' loss over time',
        'legend': losses['legend'],
        'xlabel': 'epoch',
        'ylabel': 'loss'},
    win=0)
