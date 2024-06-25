
import os
from contextlib import contextmanager

default_lock_file_path='.\lock'

@contextmanager
def global_lock(lock_file_path= default_lock_file_path):
    name_locked= os.path.join(lock_file_path,'locked')
    name_unlock= os.path.join(lock_file_path,'unlock')
    os.rename(name_unlock,name_locked)
    yield
    os.rename(name_locked,name_unlock)


def init_lock(lock_file_path= default_lock_file_path):
    os.makedirs(lock_file_path, exist_ok=True)
    name_locked= os.path.join(lock_file_path,'locked')
    name_unlock= os.path.join(lock_file_path,'unlock')
    if os.path.exists(name_locked): os.remove(name_locked)
    open(name_unlock,'w').close()
