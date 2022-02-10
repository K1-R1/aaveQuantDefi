from brownie import interface, config, network
from web3 import Web3


def get_assetETH_price(price_feed_address):
    dai_eth_price_feed = interface.AggregatorV3Interface(price_feed_address)
    price = float(Web3.fromWei(dai_eth_price_feed.latestRoundData()[1], 'ether'))
    print(f"DAI/ETH price: {price}\n")
    return price


def main():
    get_assetETH_price(config['networks'][network.show_active()]['dai_eth_price_feed'])