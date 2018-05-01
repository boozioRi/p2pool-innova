import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = '3c2a3ab9'.decode('hex')
P2P_PORT = 14520
ADDRESS_VERSION = 102
SCRIPT_ADDRESS_VERSION = 20
RPC_PORT = 8818
RPC_CHECK = defer.inlineCallbacks(lambda dashd: defer.returnValue(
            'innovaaddress' in (yield dashd.rpc_help()) and
            not (yield dashd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
BLOCK_PERIOD = 120 # s
SYMBOL = 'INN'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'innovacore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/innovacore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.innovacore'), 'innova.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.innovacoin.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.innovacoin.info/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.innovacoin.info/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//10000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
