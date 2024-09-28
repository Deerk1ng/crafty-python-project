import './FavCard.css'
import { useNavigate } from 'react-router-dom';



const FavCard = ({id, shopName, name, price, preview}) => {

    const navigate = useNavigate();
    price = price.toFixed(2) //adds two decimal places

    const goToSpotDetails = (e, id) => {
        e.stopPropagation();
        navigate(`/products/${id}`)
    }
  return (
    <div className='favcard' onClick={(e)=> goToSpotDetails(e, id)}>
        <div className='fav-preview-box'>
            <img src={preview} alt={name} />
        </div>
        <span>
                {name}
        </span>
        <div className='location-box'>
            <span>
                {shopName}
            </span>

        </div>
        <div className='price-box'>
            <span>${price}</span>
        </div>
    </div>
  );
}

export default FavCard;
