from web3 import Web3

class Web3EthAPI:
    def __init__(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")

    
    def get_balance(self, eth_address):
        """
        Retrieves the balance of the specified Ethereum address.

        Parameters:
            eth_address (str): The Ethereum address to retrieve the balance for.

        Returns:
            int: The balance of the Ethereum address in wei.
        """
        return self.web3.eth.get_balance(eth_address)
    
    def wei_to_eth(self, wei):
        """
        Converts a given value in wei to ether.

        Parameters:
        - wei: The value in wei to be converted.

        Returns:
        - The converted value in ether.
        """
        return self.web3.from_wei(wei, 'ether')