<br/>
<p align="center">
<a href="https://chain.link" target="_blank">
<img src="https://raw.githubusercontent.com/PatrickAlphaC/aave_brownie_py/main/img/aave.png" width="225" alt="Python + Aave">
<img src="https://raw.githubusercontent.com/PatrickAlphaC/aave_brownie_py/main/img/python.png" width="225" alt="Python + Aave">
</a>
</p>
<br/>

# aaveQuantDefi

Put down collateral, Borrow, and repay a loan from Aave! Use this to short assets and accrue interest. 

Upon deployment, this repo allows;

1. Approval of `ETH` to be swapped for `WETH`
2. To swap an `amount` of `ETH` for `WETH`
3. Depositing the `WETH` as collateral
4. To use that collateral to borrow `DAI`
5. Repayment of debt 


The contract is designed to be deployed and tested on multiple networks, currently those networks are:

- mainnet-fork
- Kovan test network

The contract has been tested locally on mainnet-fork, with intergration testing performed on Kovan.

## Made with
- solidity
- python
- brownie

### This repo is a project created during the course;
- smartcontractkit/full-blockchain-solidity-course-py
