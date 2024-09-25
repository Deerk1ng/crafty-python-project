import './ShoppingCart.css'
import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { getCartThunk } from '../../redux/cart';
import { getItemsThunk } from '../../redux/cart';

const ShoppingCart = () => {

    const user = useSelector((state) => state.session.user)
    const dispatch = useDispatch();

    let cartEmpty = true

    useEffect(() => {
        dispatch(getCartThunk())
    })



    return (
    <div>
        { user ?
            cartEmpty ?
            <div className='cart-empty'>
                <h2>Your cart is empty</h2>
                    <div>Discover items to fill up your cart</div>
                    <NavLink to={'/favorites/current'} className="to-favorites">View your favorites</NavLink>
            </div>
            :
            <div> Not Empty </div>
         :
            <h2 className='please-sign-in'>Please sign in to use Shopping Cart</h2>
         }
    </div>
    )

}


export default ShoppingCart;
