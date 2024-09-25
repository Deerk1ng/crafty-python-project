import "./CreateReviewModal.css"
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { FaStar } from 'react-icons/fa'
import { createReview } from "../../redux/reviews";

function CreateReviewModal({product_id}) {
    const [description, setDescription] = useState('')
    const [itemStars, setItemStars] = useState(0)
    const [shippingStars, setshippingStars] = useState(5)
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
            description
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
        <div className="modal">
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
                <label>
                    Help others by sharing your feedback
                    <input
                        type="textarea"
                        value={description}
                        onChange={(e)=> setDescription(e.target.value)}
                        required
                     />
                </label>
                {/* <label>
                    Add a photo (optional)
                    <input
                        type="url"
                        placeholder="url"
                        onChange={() => x}
                    />
                </label> */}
                <button className='review-button' disabled={(description.length < 10 || !itemStars) ? true : false} >Submit Your Review</button>
            </form>
        </div>
    )
}

export default CreateReviewModal
