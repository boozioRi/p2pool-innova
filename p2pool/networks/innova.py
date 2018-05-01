from p2pool.dash import networks

PARENT = networks.nets['innova']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '1C018E126E58B46D'.decode('hex')
PREFIX = '1C018E101A4CD06E'.decode('hex')
COINBASEEXT = '2f7032706f6f6c2d696e6e6f76612f'.decode('hex')
P2P_PORT = 2961
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 2962
BOOTSTRAP_ADDRS = 'p2p-spb.xyz '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-inn'
VERSION_CHECK = lambda v: v >= 120100
