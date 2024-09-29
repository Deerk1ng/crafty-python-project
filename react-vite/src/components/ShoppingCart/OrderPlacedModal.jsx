import './OrderPlacedModal.css'
import { useModal } from '../../context/Modal';

function OrderPlacedModal() {
    const { closeModal } = useModal()

    return (
        <div id='order-placed-box'>
            <h1>Thank you for your order!</h1>
            <p>Your order has been recieved.</p>
            <br></br>
            <button
                onClick={closeModal}
                id='ok-button'
            >Ok</button>
        </div>

    )
}
export default OrderPlacedModal;
