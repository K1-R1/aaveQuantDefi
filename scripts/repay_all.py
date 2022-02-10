from .approve_erc20 import aprrove_erc20
from web3 import Web3
from brownie import config, network


def repay_all(amount, lending_pool, account):
    aprrove_erc20(lending_pool.address, Web3.toWei(amount, 'ether'), config['networks'][network.show_active()]['dai_address'], account)
    repay_tx = lending_pool.repay(config['networks'][network.show_active()]['dai_address'], Web3.toWei(amount, 'ether'), 1, account.address, {'from': account})
    repay_tx.wait(1)
    print('Debt repaid ... \n')