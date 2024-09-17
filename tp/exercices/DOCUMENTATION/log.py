import logging

logging.basicConfig(level=logging.DEBUG, # faire afficher les erreur selon les niveaux
                    format= '%(asctime)s - %(levelname)s - %(message)s',
                    filename = "app.log",
                    filemode = "a"
                    )

logging.debug("debug permet juste de voir si une fonction est excecuter. comme un print. voir le retour de notre script")
logging.info("permet d'avoir un message generique lu par un utilisateur")
logging.warning("avertissement")
logging.error("une erreur s'estpridiuit")
logging.critical("erreur critique, le script s'arrete")
