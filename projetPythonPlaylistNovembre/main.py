#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from Extantion_modules.Calcules.Pourcentage import gestionPctage
from Extantion_modules.ModuleArgparse import fonctionArgparse
from Extantion_modules.Generation import Fichierm3u
from Extantion_modules.Generation import Fichierpls
from Extantion_modules.Generation import Fichierxpsf
from Extantion_modules.Basse_de_donnee.RecupDonnees import Playlist, recupererDonnees

logging.basicConfig(filename="monLog.log", level=logging.DEBUG)

logging.info("commencement du main")

args = fonctionArgparse()

'''Vérifications'''
'''Vérification d'un temps positif'''
logging.info("Utilisation de la fonction pour vérifier que le temps est un entier positif")
if args.temps<0 :
    print ("Le temps doit être positive !")
    logging.error("le temps " + str(args.temps) + " n'est pas un entier positif")
    exit(1)

logging.info("Saisies : " + str(args))

for unArg in ['genre','artiste','album', 'titre']:
    '''Si l'argument est renseigné'''
    if getattr(args, unArg) is not None:
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        gestionPctage(getattr(args, unArg))

recupererDonnees(args)
playlist = Playlist(args)

print(playlist)

if (args.formatfichier =='m3u'):
    Fichierm3u(args.nomfichier, args.formatfichier, playlist)
    print('Generation de la playliste effectuer en m3u')

if(args.formatfichier =='xspf'):
    Fichierxpsf(args.nomfichier, args.formatfichier, playlist)
    print('Generation de la playliste effectuer en xspf')

if(args.formatfichier =='pls'):
    Fichierpls(args.nomfichier, args.formatfichier, playlist)
    print('Generation de la playliste effectuer en pls')



logging.info("fin du Main")