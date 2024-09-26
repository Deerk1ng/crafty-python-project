import './ShoppingCart.css'
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { getCartThunk } from '../../redux/cart';
import ItemCard from './Item';


const ShoppingCart = () => {

    const user = useSelector((state) => state.session.user)
    const items = useSelector((state) => state.cartState.items)
    const itemsArr = Object.values(items)
    const [cartEmpty, setCartEmpty] = useState(true)
    const dispatch = useDispatch();


    console.log(itemsArr)

    useEffect(() => {
        dispatch(getCartThunk())
    }, [])

    useEffect(() => {
        if(items){
            setCartEmpty(false)
        }
    }, [items])


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
            <div className='items-container'>
                {itemsArr.map((item) => {
                    return (
                        <div key={`${item.id}-${item.product_id}`} className='card-holder'>
                            <span>
                                <ItemCard
                                id={item.id}
                                shopName={item.owner.shop_name}
                                name={item.product.name}
                                price={item.product.price}
                                preview={item.images[0].url}
                                quantity={item.quantity}
                                />
                            </span>

                        </div>
                    )
                })}
            </div>
         :
            <h2 className='please-sign-in'>Please sign in to use Shopping Cart</h2>
         }
    </div>
    )

}


export default ShoppingCart;
