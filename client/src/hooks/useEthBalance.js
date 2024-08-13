import { useEffect, useState } from "react"
import useAxiosPrivate from "./usePrivate"
import useAuth from "./useAuth"

export default function useEthBalance() {
    const [ethBalance, setEthBalance] = useState(undefined)
    const { isLoggedIn } = useAuth()
    const axiosPrivateInstance = useAxiosPrivate()

    useEffect(() => {
        async function getEthBalance() {
            try {
                const { data } = await axiosPrivateInstance.get('auth/eth-balance')
                setEthBalance(data.eth_balance)
            } catch (error) {
                console.log("===", error.response)
            }
        }

        getEthBalance()
    }, [isLoggedIn, axiosPrivateInstance])

    return ethBalance
}