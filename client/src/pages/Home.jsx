import React, { useEffect } from 'react'
import useAuth from '../hooks/useAuth'
import useUser from '../hooks/useUser';
import useEthBalance from '../hooks/useEthBalance';

export default function Home() {
    const { user } = useAuth();
    const getUser = useUser()
    const ethBalance = useEthBalance()
    useEffect(() => {
        getUser()
    }, [])

    return (
        <div className='container mt-3'>
            <h2>
                <div className='row'>
                    <div className="mb-12">
                        {user?.email !== undefined ? 'List user Ethereum balance' : 'Please login first'}
                        {ethBalance !== undefined && (
                            <div>
                                <br />
                                <h4>{ethBalance} ETH</h4>
                            </div>
                        )}
                    </div>
                </div>
            </h2>
        </div>
    )
}
