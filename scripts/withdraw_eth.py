from .general_scripts import get_account
from brownie import interface, config, network

def withdraw_eth():
    """
    Withdraw ETH from WETH
    """
    account = get_account()
    weth = interface.IWeth(config['networks'][network.show_active()]['weth_address'])
    tx = weth.withdraw(0.1 * (10**18), {'from': account})
    tx.wait(1)
    print('Withdrew 0.1 ETH')

def main():
    withdraw_eth()