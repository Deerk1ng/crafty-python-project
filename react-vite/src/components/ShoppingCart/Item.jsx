import './Item.css'
import { useNavigate } from 'react-router-dom'

const ItemCard = ({ shopName, name, price, preview, quantity}) => {

    const navigate = useNavigate();
    price = price.toFixed(2) //adds two decimal places

    const goToSpotDetails = (e, id) => {
        e.stopPropagation();
        navigate(`/spots/${id}`)
    }
  return (
    <div className='card' onClick={(e)=> goToSpotDetails(e, id)}>
        <div className='preview-box'>
            <img src={preview} alt={name} />
        </div>
        <div className='location-box'>
            <span>
                {shopName}, {name}, {price}, {quantity}
            </span>
        </div>
        <div className='price-box'>
            <span>${price} per night</span>
        </div>
    </div>
  );
}

export default ItemCard;
