import "./CreateReviewModal.css"
import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { FaStar } from 'react-icons/fa'
import { createReview } from "../../redux/reviews";

function CreateReviewModal({product_id, product}) {
    const [description, setDescription] = useState('')
    const [itemStars, setItemStars] = useState(0)
    const [shippingStars, setshippingStars] = useState(5)
    const [url, setUrl] = useState('')
    const [hover, setHover] = useState(null)
    const [errors, setErrors] = useState({})
    const {closeModal} = useModal()
    const dispatch = useDispatch()

    const handleSubmit = (e) => {
        e.preventDefault();

        const newReview = {
            product_id,
            item_rating: itemStars,
            shipping_rating: shippingStars,
            description,
            url
        }

        return dispatch(createReview(newReview))
        .then(closeModal)
        .catch(async (res) => {
            const data = await res
            if (data && data.errors) {
                setErrors(data.errors);
            } else setErrors(data)
        })
    }

    return (
        <div className="create-modal">
            <div className="prod-info">
                <img src={product.images[0].url} className="rev-prod-img" alt="preview image of the product"/>
                <div className="prod-name-shopname">
                    <div className="prod-name">{product.name}</div>
                    <div>{product.owner.shop_name}</div>
                </div>
            </div>
            <h3>My Review</h3>
            {errors.message && <div className='err'>{errors.message}</div>}
            <form onSubmit={handleSubmit}>
            <div className='star-container'>
                {[...Array(5)].map((star , index) => {
                    const currentRate = index + 1
                    return (
                        <label key={`star${currentRate}`}>
                            <input
                                type="radio"
                                name="rating"
                                value={currentRate}
                                onClick={() => setItemStars(currentRate)}
                            />
                            <FaStar
                                className='star'
                                size={25}
                                color={currentRate <= (hover || itemStars) ? '#5985E1' : '#cccccc'}
                                border-color={"black"}
                                onMouseEnter={() => setHover(currentRate)}
                                onMouseLeave={() => setHover(null)}
                            />
                        </label>
                    )
                })}
            </div>
            <div>
                <div className="label">Help others by sharing your feedback</div>
                <input
                    type="textarea"
                    value={description}
                    onChange={(e)=> setDescription(e.target.value)}
                    required
                    className="new-rev-desc"
                    />
            </div>
            <div>
                <div className="label">Add a photo (optional)</div>
                    <input
                        type="url"
                        placeholder="url"
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                        />
            </div>
                <button className='review-button' disabled={(description.length < 10 || !itemStars) ? true : false} >Submit Your Review</button>
            </form>
        </div>
    )
}

export default CreateReviewModal
