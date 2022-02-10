from scripts.general_scripts import get_account, config, network
from scripts.get_aave_lending_pool import get_aave_lending_pool
from scripts.approve_erc20 import aprrove_erc20
from scripts.get_asset_price import get_assetETH_price
from brownie import config, network


def test_get_asset_price():
    # Arrange / Act
    asset_price = get_assetETH_price()
    # Assert
    assert asset_price > 0


def test_get_lending_pool():
    # Arrange / Act
    lending_pool = get_aave_lending_pool()
    # Assert
    assert lending_pool != None


def test_approve_erc20():
    # Arrange
    account = get_account()
    lending_pool = get_aave_lending_pool()
    amount = 1000000000000000000  # 1
    erc20_address = config["networks"][network.show_active()]["weth_address"]
    # Act
    approved = aprrove_erc20(amount, lending_pool.address, erc20_address, account)
    # Assert
    assert approved is True