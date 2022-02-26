"""Bibliothèque pour simplifier l'écriture de filtres AMC.

Les variables suivantes sont prêtes à l'emploi :
    - input : entrée standard textuelle (str)
    - output : sortie standard textuelle (str)
    - binary_input : entrée standard binaire (bytes)
    - binary_output : sortie standard binaire (bytes)
    - url : adresse de la page qui a invoqué le filtre
    - path : chemin d'accès contenu dans l'url
    - args : arguments contenus dans l'url
"""

import sys
import os
import urllib.parse as up
import logging


def debug(*args):
    "Ajouter un message de debug au journal"
    logging.debug(*args)


def log(*args):
    "Ajouter un message d'information au journal"
    logging.info(*args)


def oups(*args):
    "Ajouter un message d'avertissement au journal"
    logging.warning(*args)


def erreur(*args):
    "Ajouter un message d'erreur au journal"
    logging.error(*args)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)
input = sys.stdin
output = sys.stdout
binary_input = sys.stdin.buffer
binary_output = sys.stdout.buffer
url = os.environ.get("URL", None)
if url is None:
    path = None
    args = {}
else:
    x = up.urlparse(url)
    path = x.path
    args = up.parse_qs("filter=" + x.query)
    del x
