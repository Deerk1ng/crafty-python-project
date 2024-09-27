import './Favorites.css'
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import FavCard from './FavCard';
import { getFavoritesThunk } from '../../redux/favorites';


const Favorites = () => {

    const user = useSelector((state) => state.session.user)
    const favorites = useSelector((state) => state.favoritesReducer.currentFavorites)
    const [isLoaded, setIsLoaded] = useState(false);
    const favArr = Object.values(favorites)
    const [favEmpty, setFavEmpty] = useState(true)
    const dispatch = useDispatch();


    useEffect(() => {
        dispatch(getFavoritesThunk())
        .then(() => setIsLoaded(true))
    }, [])

    useEffect(() => {
        if(favorites){
            setFavEmpty(false)
        }

    }, [favorites])


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
                                id={favorite.id}
                                shopName={favorite.owner.shop_name}
                                name={favorite.name}
                                price={favorite.price}
                                preview={favorite.images[0].url}
                                />
                            </span>
                            <button className="cart-button">Add to Cart</button>
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
