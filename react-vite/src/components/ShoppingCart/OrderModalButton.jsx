import { useModal } from '../../context/Modal';
import { deleteCartThunk } from '../../redux/cart';
import { useDispatch } from 'react-redux';

function OrderModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed
  cart_id
}) {
const { setModalContent, setOnModalClose } = useModal();
const dispatch = useDispatch()

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (typeof onButtonClick === "function") onButtonClick();

    //delete order thunk
    dispatch(deleteCartThunk(cart_id))
  };

  return <button id='place-order-button' onClick={onClick}>{buttonText}</button>;
}

export default OrderModalButton;
