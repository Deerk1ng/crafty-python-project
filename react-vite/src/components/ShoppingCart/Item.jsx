import './Item.css'
import { useNavigate } from 'react-router-dom'
import { removeItemThunk, addQuantThunk, subQuantThunk} from '../../redux/cart';
import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import {IoMdHeart, IoMdHeartEmpty} from "react-icons/io";
import { createFavorite, deleteFavorite, getFavoritesThunk } from "../../redux/favorites";
import { FaUserCircle } from 'react-icons/fa';


const ItemCard = ({ id, product_id, shopName, name, price, preview, quantity}) => {

    const navigate = useNavigate();
    const dispatch = useDispatch();
    const favorites = useSelector((state) => state.favoritesReducer.currentFavorites)
    const product = useSelector(state => state.cartState.items[id].product);
    price = price.toFixed(2) //adds two decimal places
    let quant = 1

    //calculates total price of card
    let priceTimesQuant = price * quantity
    priceTimesQuant = priceTimesQuant.toFixed(2)


    //Button handlers
    const goToSpotDetails = (e, id) => {
        e.stopPropagation();
        navigate(`/products/${id}`)
    }

    const RemoveClick = (e, id) => {
        e.preventDefault();
        dispatch(removeItemThunk(id))
    }

    const AddClick = (e, id, quant) => {
        e.preventDefault();
        dispatch(addQuantThunk(id, quant))
    }

    const SubClick = (e, id, quant) => {
        e.preventDefault();

        if(quantity > 1){
            dispatch(subQuantThunk(id, quant))
        } else {
            dispatch(removeItemThunk(id))
        }
    }
    const handleDelete = (e) => {
        e.preventDefault();

        dispatch(deleteFavorite(favorites[product.id].id,product.id))
    }

    const handleAdd = (e) => {
        e.preventDefault();
        dispatch(createFavorite(product.id))

    }

    //useEffect

    useEffect(() => {
        dispatch(getFavoritesThunk())
    }, [product_id, dispatch]);

  return (
    <div className='item-card'>
        <FaUserCircle className='shop-user-logo'/>
        <div  className='item-shop-name'>{shopName}</div>
        <div className='item-preview-box' onClick={(e)=> goToSpotDetails(e, product.id)}>
            <img src={preview} alt={name} />
        </div>
        <div className='item-price-box'>
            <span id='item-price'>${priceTimesQuant}</span>
        </div>

        {favorites[product.id] ?

        <button className="item-favorites-button" onClick={(e) => handleDelete(e)}><IoMdHeart /> Delete from Favorites</button>
        :
        <button className="item-favorites-button" onClick={(e) => handleAdd(e)}><IoMdHeartEmpty /> Add item to Favorites</button>}

        <button
            id='remove-button'
            onClick={(e) => RemoveClick(e, id)}>
            Remove
        </button>
        <div id='quant-box'>
            <div id='quant-text'>Quantity</div>
            <button onClick={(e) => SubClick(e, id, quant)}>
                -
            </button>

            <span id='item-quantity'>
                {quantity}
            </span>

            <button
                id='add-button'
                onClick={(e) => AddClick(e, id, quant)}>
                +
            </button>
        </div>

        <div id='item-name'>{name}</div>
    </div>
  );
}

export default ItemCard;
