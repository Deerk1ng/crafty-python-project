import { useEffect } from "react";
import { getfavorites } from "../../redux/favorites";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { FaHeartBroken } from "react-icons/fa";
import Footer from "../Footer";


const Favorites = () => {
    const dispatch = useDispatch()

    const favorites = useSelector(state => state.favoritesReducer.allFavorites)
    const allFavs = favorites ? Object.values(favorites) : [];

    console.log("FAVVVVVVV", allFavs)
    useEffect(() => {
        dispatch(getfavorites())
    }, [dispatch])

    return (
        <>
            {!Favorites.length > 0 ? (
                <>{allFavs.map(favorite => (
                    <div>
                        <FaHeartBroken />
                    <NavLink to={`/products/${favorite.id}`}>
                        <img className="fav-img" src={favorite.images[0]?.url} alt={favorite.name}></img>
                        <p style={{fontWeight:'800'}}>{favorite.name}</p>
                        <p >{favorite.owner.shop_name}</p>
                        <p >${favorite.price.toFixed(2)}</p>
                    </NavLink>
                        <button onClick={''}>Add to Cart</button>
                        </div>
                ))}</>
            ) : (
                <h1>world</h1>
            )}
            {/* <Footer /> */}

        </>
    )
}


export default Favorites;
