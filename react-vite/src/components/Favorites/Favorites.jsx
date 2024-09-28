import './Favorites.css'
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import FavCard from './FavCard';
import { getFavoritesThunk } from '../../redux/favorites';
import { addItemThunk } from '../../redux/cart';
import { useNavigate } from 'react-router-dom';

const Favorites = () => {

    const user = useSelector((state) => state.session.user)
    const favorites = useSelector((state) => state.favoritesReducer.currentFavorites)
    const [isLoaded, setIsLoaded] = useState(false);
    const favArr = Object.values(favorites)
    const [favEmpty, setFavEmpty] = useState(true)
    const dispatch = useDispatch();
    const navigate = useNavigate();


    useEffect(() => {
        dispatch(getFavoritesThunk())
        .then(() => setIsLoaded(true))
    }, [])

    useEffect(() => {
        if(favorites){
            setFavEmpty(false)
        }

    }, [favorites])


    const AddItemClick = (e, user_id, product_id) => {
        e.preventDefault();

        dispatch(addItemThunk(user_id, product_id));
        navigate('/shopping-cart/current')
    }

    return isLoaded && (
    <div>
        { user ?
            favEmpty ?
            <div className='fav-empty'>
                <h2>Nothing to see here yet</h2>
                    <div>Start favoriting items to compare, shop, and keep track of things you love</div>
            </div>
            :
            <div className='favs-container'>
                {favArr.map((favorite) => {

                    return (
                        <div key={`${favorite.id}-${favorite.owner_id}`} className='card-holder'>

                            <span>
                                <FavCard
                                id={favorite.product_id}
                                shopName={favorite.product.owner.shop_name}
                                name={favorite.product.name}
                                price={favorite.product.price}
                                preview={favorite.product.images[0].url}
                                />
                            </span>
                            {user && user.id ?
                            (
                                <button
                                    className="cart-button"
                                    onClick={(e) => AddItemClick(e, user.id, favorite.id)}
                                >Add to Cart</button>
                            )
                                : null
                            }
                        </div>
                    )
                })}
            </div>
         :
            <h2 className='please-sign-in'>Please sign in to use Favorites</h2>
         }
    </div>
    )

}


export default Favorites;
