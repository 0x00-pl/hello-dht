from global_lock import global_lock

config_file='.\config.cfg'


if __name__=='__main__':
    with global_lock():
        print('ok')
        input()
        
