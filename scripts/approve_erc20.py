from brownie import interface, config, network
from .general_scripts import get_account
from .get_aave_lending_pool import get_aave_lending_pool


def aprrove_erc20(spender_address, value, erc20_address, account):
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender_address, value, {'from': account})
    tx.wait(1)
    print('ERC20 approved ...\n')
    return tx

def main():
    account = get_account()
    weth_address = config['networks'][network.show_active()]['weth_address']
    amount = 0.1 * (10**18)
    aave_lending_pool = get_aave_lending_pool()
    aprrove_erc20(aave_lending_pool.address, amount, weth_address, account)