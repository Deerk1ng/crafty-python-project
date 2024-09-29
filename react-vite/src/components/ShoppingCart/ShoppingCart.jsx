import './ShoppingCart.css'
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { getCartThunk, deleteCartThunk } from '../../redux/cart';
import ItemCard from './Item';
import OrderModalButton from './OrderModalButton';
import OrderPlacedModal from './OrderPlacedModal';

const ShoppingCart = () => {

    const user = useSelector((state) => state.session.user)
    const items = useSelector((state) => state.cartState.items)
    const cart = useSelector((state) => state.cartState.cart)
    const [isLoaded, setIsLoaded] = useState(false);
    const itemsArr = Object.values(items)
    const [cartEmpty, setCartEmpty] = useState(true)
    let totalCart = 0
    let totalItems = 0
    const dispatch = useDispatch();


    useEffect(() => {
        dispatch(getCartThunk())
        .then(() => setIsLoaded(true))
        .then(() => {if(items) {
            setCartEmpty(false)
        }})
    }, [])


    return isLoaded && (
    <div>
        { user ?
            cartEmpty ?
            <div className='cart-empty'>
                <h2>Your cart is empty</h2>
                    <div>Discover items to fill up your cart</div>
                    <NavLink to={'/favorites/current'} className="to-favorites">View your favorites</NavLink>
            </div>
            :
            <div className='cart-holder'>
                <div className='items-container'>
                    {itemsArr.map((item) => {
                        totalCart = totalCart + (item.product.price * item.quantity)
                        totalItems = totalItems + item.quantity
                        return (
                            <div key={`${item.id}-${item.product_id}`} className='card-holder'>
                                <span>
                                    <ItemCard
                                    id={item.id}
                                    product_id={item.product_id}
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

                {totalCart ?
                <div id='order-summary'>
                    <div className ='tally-row'>
                       <span>
                        Item(s) total
                        </span>
                        <span id='sales-tax'>
                            ${totalCart.toFixed(2)}
                        </span>
                    </div>
                    <hr></hr>
                    <div className ='tally-row'>
                       <span>
                        Shipping
                        </span>
                        <span id='sales-tax'>
                            ${(totalItems * 3.99).toFixed(2)}
                        </span>
                    </div>
                    <div className ='tally-row'>
                       <span>
                        Sales Tax
                        </span>
                        <span id='sales-tax'>
                            ${(totalCart * 0.06).toFixed(2)}
                        </span>
                    </div>
                    <hr></hr>
                    <div className ='tally-row'>
                       <span id='total-text'>
                        Order total {`(${totalItems} item${totalItems > 1 ? 's' : '' })`}
                        </span>
                        <span id='total-price'>
                            ${(totalCart + totalItems * 3.99 + totalCart * 0.06).toFixed(2)}
                        </span>
                    </div>

                    <OrderModalButton
                        cart_id={cart.id}
                        buttonText='Place Your Order'
                        modalComponent={<OrderPlacedModal/>}
                    />

                </div>

                        :
                    <div>
                        <div className='cart-empty'>
                        <h2>Your cart is empty</h2>
                            <div>Discover items to fill up your cart</div>
                            <NavLink to={'/favorites/current'} className="to-favorites">View your favorites</NavLink>
                        </div>
                    </div>
                }


            </div>
         :
            <h2 className='please-sign-in'>Please sign in to use Shopping Cart</h2>
         }

    </div>
    )

}


export default ShoppingCart;
