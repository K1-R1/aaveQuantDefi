from .general_scripts import get_account
from brownie import interface, config, network

def get_weth():
    """
    Mints WETH by depositing ETH
    """
    account = get_account()
    weth = interface.IWeth(config['networks'][network.show_active()]['weth_address'])
    tx = weth.deposit({'from': account, 'value': 0.1 * (10**18)})
    tx.wait(1)
    print('Receieved 0.1 WETH')



def main():
    get_weth()