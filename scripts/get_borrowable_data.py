from web3 import Web3
from .get_aave_lending_pool import get_aave_lending_pool
from .general_scripts import get_account


def get_borrowable_data(lending_pool, account):
    (
        totalCollateralETH, 
        totalDebtETH, 
        availableBorrowsETH, 
        currentLiquidationThreshold, 
        ltv, 
        healthFactor
    ) = lending_pool.getUserAccountData(account.address)
    available_borrows_ETH = Web3.fromWei(availableBorrowsETH, 'ether')
    total_collateral_ETH = Web3.fromWei(totalCollateralETH, 'ether')
    total_debt_ETH = Web3.fromWei(totalDebtETH, 'ether')
    print(f"Total collatteral: {total_collateral_ETH} ETH, Total debt: {total_debt_ETH} ETH, Available borrow: {available_borrows_ETH} ETH\n")
    return float(available_borrows_ETH), float(total_debt_ETH)


def main():
    account = get_account()
    aave_lending_pool = get_aave_lending_pool()
    get_borrowable_data(aave_lending_pool, account)