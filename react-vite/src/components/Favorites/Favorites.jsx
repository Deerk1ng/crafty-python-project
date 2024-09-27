import './Favorites.css'
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import FavCard from './FavCard';


const Favorites = () => {

    const user = useSelector((state) => state.session.user)
    // const favorites = useSelector((state) => state.cartState.items)
    const [isLoaded, setIsLoaded] = useState(false);
    // const favArr = Object.values(favs)
    const [favEmpty, setFavEmpty] = useState(true)
    const dispatch = useDispatch();


    useEffect(() => {
        setIsLoaded(true)
    }, [])

    // useEffect(() => {
    //     if(items){
    //         setFavEmpty(false)
    //     }

    // }, [items])


    return isLoaded && (
    <div>
        { user ?
            favEmpty ?
            <div className='fav-empty'>
                <h2>Nothing to see here yet</h2>
                    <div>Start favoriting items to compare, shop, and keep track of things you love</div>
            </div>
            :
            <div className='items-container'>
                {/* {itemsArr.map((item) => {
                    totalCart = totalCart + (item.product.price * item.quantity)
                    return (
                        <div key={`${item.id}-${item.product_id}`} className='card-holder'>
                            <span>
                                <FavCard
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
                })} */}
            </div>
         :
            <h2 className='please-sign-in'>Please sign in to use Favorites</h2>
         }
    </div>
    )

}


export default Favorites;
