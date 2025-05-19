import logging
import time

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    logging.error("Not yet implemented")
    while True:
        logging.info("Doing some stuff... or not?")
        time.sleep(1)

if __name__ == "__main__":
    main()
