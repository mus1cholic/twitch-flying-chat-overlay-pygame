from multiprocessing import Process, Queue

from flying_text import setup_pygame
from twitchio_client import setup_listener

def main():
    data_queue = Queue()

    twitchio_client_process = Process(target=setup_listener, args=(data_queue, ))
    twitchio_client_process.daemon = True
    twitchio_client_process.start()

    flying_text_process = Process(target=setup_pygame, args=(data_queue, ))
    flying_text_process.start()
    twitchio_client_process.join()

if __name__ == '__main__':
    main()