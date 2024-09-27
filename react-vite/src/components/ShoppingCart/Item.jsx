import './Item.css'
import { useNavigate } from 'react-router-dom'
import { removeItemThunk, addQuantThunk, subQuantThunk} from '../../redux/cart';
import { useDispatch } from 'react-redux';

const ItemCard = ({ id, shopName, name, price, preview, quantity}) => {

    const navigate = useNavigate();
    const dispatch = useDispatch();
    price = price.toFixed(2) //adds two decimal places
    let quant = 1

    //calculates total price of card
    let priceTimesQuant = price * quantity
    priceTimesQuant = priceTimesQuant.toFixed(2)

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
        dispatch(subQuantThunk(id, quant))
    }

  return (
    <div className='card'>
        <div className='preview-box' onClick={(e)=> goToSpotDetails(e, id)}>
            <img src={preview} alt={name} />
        </div>
        <div className='location-box'>
            <span>
                {shopName}, {name}, {quantity}
            </span>
        </div>
        <div className='price-box'>
            <span>${priceTimesQuant}</span>
        </div>
        <button
            id='remove-button'
            onClick={(e) => RemoveClick(e, id)}
            >
            Remove
        </button>
        <button onClick={(e) => AddClick(e, id, quant)}>
            +
        </button>
        <span>
            {quantity}
        </span>
        <button onClick={(e) => SubClick(e, id, quant)}>
            -
        </button>
    </div>
  );
}

export default ItemCard;
