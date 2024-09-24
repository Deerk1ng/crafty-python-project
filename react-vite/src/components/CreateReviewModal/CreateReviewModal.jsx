import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { FaStar } from 'react-icons/fa'

function CreateReviewModal() {
  const [stars, setStars] = useState(0)
  const [hover, setHover] = useState(null)

    return (
        <div className="modal">
            <h3>My Review</h3>
            {errors.server && <p>{errors.server}</p>}
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
                                onClick={() => setStars(currentRate)}
                            />
                            <FaStar
                                className='star'
                                size={25}
                                color={currentRate <= (hover || stars) ? '#5985E1' : '#cccccc'}
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
                        value="filler"
                        onChange={()=> x}
                        required
                     />
                </label>
                <label>
                    Add a photo (optional)
                    <input
                        type="url"
                        placeholder="url"
                        onChange={() => x}
                    />
                </label>
            </form>
        </div>
    )
}
