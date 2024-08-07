import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Job started")
    for i in range(1000):
        logging.info(f"Processing item {i}")
        time.sleep(1)  # Simulate work by sleeping for 1 second
    logging.info("Job completed")

if __name__ == "__main__":
    main()
