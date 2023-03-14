import os
import logging

import requests

LOGFORMAT = "%(asctime)s %(funcName)-10s [%(levelname)s] %(message)s"   # Log format

def main():
    logging.info("Starting job")
    requests.get("https://hubben-api.k8s.violaberg.nu")
    logging.info("Finishing job")

if __name__ == "__main__":
    if os.getenv("DEBUG", "false") == "true":  # Debug requested
        logging.basicConfig(level=logging.DEBUG, format=LOGFORMAT)
    logging.basicConfig(level=logging.INFO, format=LOGFORMAT)  # Default logging level

    main()
