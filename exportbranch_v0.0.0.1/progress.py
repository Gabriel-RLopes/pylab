import threading
import sys


class ProgressBar:
    def __init__( self, total ):
        self.total = total
        self.current = 0
        self.lock = threading.Lock()

    def update( self ):
        with self.lock:
            self.current += 1
            percent = ( self.current/self.total ) * 100
            sys.stdout.write(f'\rProgresso: {self.current}/{self.total}({percent:.1f}%)')
            sys.stdout.flush()

    def finish( self ):
        print('\nConcluido')
