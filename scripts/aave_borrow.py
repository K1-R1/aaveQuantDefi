from .general_scripts import get_account, config, network
from .get_weth import get_weth
from .get_aave_lending_pool import get_aave_lending_pool
from .approve_erc20 import aprrove_erc20
from .get_borrowable_data import get_borrowable_data
from .get_asset_price import get_assetETH_price
from .repay_all import repay_all
from web3 import Web3


amount = 0.1 * (10**18)


def aave_borrow():
    #Get WETH
    account = get_account()
    weth_address = config['networks'][network.show_active()]['weth_address']
    get_weth()
    #Deposit to lending pool
    aave_lending_pool = get_aave_lending_pool()
    aprrove_erc20(aave_lending_pool.address, amount, weth_address, account)
    aave_lending_pool.deposit(weth_address, amount, account.address, 0, {'from': account}).wait(1)
    print('Tokens deposited ... \n')
    #Borrow DAI
    borrowable_ETH, total_debt_ETH = get_borrowable_data(aave_lending_pool, account)
    dai_eth_price = get_assetETH_price(config['networks'][network.show_active()]['dai_eth_price_feed'])
    amount_to_borrow = (borrowable_ETH * 0.95) / dai_eth_price
    print(f"Amount of DAI to borrow: {amount_to_borrow}, at DAI/ETH price of {dai_eth_price}\n")
    dai_address = config['networks'][network.show_active()]['dai_address']
    borrow_tx = aave_lending_pool.borrow(dai_address, Web3.toWei(amount_to_borrow, 'ether'), 1, 0, account.address, {'from': account})
    borrow_tx.wait(1)
    get_borrowable_data(aave_lending_pool, account)
    #Repay
    repay_all(amount_to_borrow, aave_lending_pool, account)
    #Verify data
    get_borrowable_data(aave_lending_pool, account)

def main():
    aave_borrow()