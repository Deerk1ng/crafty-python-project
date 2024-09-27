import './FavCard.css'
import { FaStar } from "react-icons/fa";
import { useNavigate } from 'react-router-dom';



const FavCard = ({id, name, preview, city, state, rating, price}) => {

    const navigate = useNavigate();
    price = price.toFixed(2) //adds two decimal places
    rating ? rating = rating.toFixed(1) : rating='New'

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
                {city}, {state}
            </span>
            <span>
            <FaStar/> {rating}
            </span>
        </div>
        <div className='price-box'>
            <span>${price} per night</span>
        </div>
    </div>
  );
}

export default FavCard;
