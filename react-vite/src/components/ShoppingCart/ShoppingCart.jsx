import './ShoppingCart.css'
import { useEffect } from 'react';
import { NavLink } from 'react-router-dom';


const ShoppingCart = () => {

    useEffect(() => {

    })

    let cartEmpty = true

    return (
    <div>
    { cartEmpty ?
        <div className='cart-empty'>
            <h2>Your cart is empty</h2>
                <div>Discover items to fill up your cart</div>
                <NavLink to={'/favorites/current'} className="to-favorites">View your favorites</NavLink>
        </div>
        :
        <div> Not Empty </div>
    }
    </div>
    )

}


export default ShoppingCart;
