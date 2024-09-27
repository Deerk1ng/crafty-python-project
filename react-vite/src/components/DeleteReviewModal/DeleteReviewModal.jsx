import './DeleteReviewModal.css'
import { useModal } from '../../context/Modal'
import { useDispatch } from 'react-redux';
import { deleteReview } from '../../redux/reviews'

function DeleteReviewModal({review_id}) {
    const { closeModal } = useModal()
    const dispatch = useDispatch()

    const handleDelete = () => {
        console.log(review_id)
        dispatch(deleteReview(review_id))
        .then(closeModal)
    }

    return (
        <div className='modal'>
            <h1 className='delete-title'>Confirm Delete</h1>
            <div className='delete-desc'>Are you sure you want to delete this review?</div>
            <button className='delete-button' onClick={handleDelete}>Yes (Delete Review)</button>
            <button className='keep-button' onClick={closeModal}>No (Keep Review)</button>
        </div>
    )
}

export default DeleteReviewModal
