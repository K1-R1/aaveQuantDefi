from brownie import interface, config, network


def get_aave_lending_pool():
    #get address from LendingPoolAddressesProvider
    lending_pool_address_provider = interface.ILendingPoolAddressesProvider(
        config['networks'][network.show_active()]['aave_lending_pool_addresses_provider']
    )
    lending_pool_address = lending_pool_address_provider.getLendingPool()
    #get lending pool
    lending_pool = interface.ILendingPool(lending_pool_address)
    print('Lending pool contract acquired ...\n')
    return lending_pool


def main():
    get_aave_lending_pool()