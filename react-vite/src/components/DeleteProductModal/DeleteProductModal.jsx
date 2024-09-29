import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { deleteProduct } from "../../redux/products";

const DeleteProduct = ({ product_id }) => {

    const { closeModal } = useModal();
    const dispatch = useDispatch();

    const handleDelete = () => {
        dispatch(deleteProduct(product_id))
            .then(() => {
                closeModal();
            });
    };

    return (
        <div className='modal'>
            <h1 className='delete-title'>Confirm Delete</h1>
            <div className='delete-desc'>Are you sure you want to delete this product?</div>
            <button className='delete-button' onClick={handleDelete}>
                Yes (Delete Product)
            </button>
            <button className='keep-button' onClick={closeModal}>
                No (Keep Product)
            </button>
        </div>
    );
};

export default DeleteProduct;
