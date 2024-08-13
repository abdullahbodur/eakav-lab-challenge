from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from user.eth import Web3EthAPI

web3_api = Web3EthAPI(settings.ETH_PROVIDER_URL)

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "password", "password2", "eth_address")
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True}
        }

    def save(self):
        user = get_user_model()(
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            eth_address=self.validated_data["eth_address"]
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError(
                {"password": "Passwords do not match!"})

        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "is_staff", "first_name", "last_name", "eth_address")


class EthBalanceSerializer(serializers.Serializer):
    eth_address = serializers.CharField(max_length=42)

    def validate_eth_address(self, value):
        if not value.startswith("0x"):
            raise serializers.ValidationError("Invalid Ethereum address")
        return value
    
    
    def get_balance(self, eth_address):
        weiBalance = web3_api.get_balance(eth_address)
        ethBalance = web3_api.wei_to_eth(weiBalance)
        return ethBalance
    
    