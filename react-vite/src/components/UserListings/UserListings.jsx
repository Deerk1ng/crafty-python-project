import './UserListings.css'
import { getUserProducts } from '../../redux/products';
import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState, ulRef } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { thunkLogout } from "../../redux/session";
import { IoMdAdd } from "react-icons/io";

import DeleteProduct from '../DeleteProductModal/DeleteProductModal';
import OpenModalButton from '../OpenModalButton/OpenModalButton';


const UserListings = () => {
    const navigate = useNavigate();

    const [showMenu, setShowMenu] = useState(false);



    const products = useSelector(state => state.productsReducer.userProducts)

    const allProducts = products ? Object.values(products) : [];


    function getDateTwoMonthsFromNow() {
        const now = new Date();
        // Create a new Date object to prevent modifying the current date
        const futureDate = new Date(now);

        // Set the month to 2 months ahead
        futureDate.setMonth(futureDate.getMonth() + 2);

        // Handle month overflow (e.g., going from January 31st to March 31st, will adjust to March 3rd)
        if (futureDate.getDate() < now.getDate()) {
            futureDate.setDate(0); // Set to the last day of the previous month
        }

        // Get month, day, and year
        const month = String(futureDate.getMonth() + 1).padStart(2, '0'); // Months are 0-indexed, so we add 1
        const day = String(futureDate.getDate()).padStart(2, '0');
        const year = futureDate.getFullYear();

        // Return the date in mm/dd/yyyy format
        return `${month}/${day}/${year}`;
    }





    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getUserProducts());
    }, [dispatch]);

    return allProducts.length > 0 ? (
        <>
        <div id='listings'>
            <div className='listings-top'>
                <h2>Listings</h2>
                <NavLink className={'listing-bttn'} to={'/products/new'}><IoMdAdd />Add Listing</NavLink>
            </div>
            <div>
            <div className='all-listings'>
    {allProducts.map(product => (
        <div className='user-listing' key={product.id}>
            {product.images && product.images.length > 0 ? (
                <img className='user-product-img' src={product.images[0].url} alt='' />
            ) : (
                <div className='user-product-img'>No image available</div>
            )}
            <p style={{margin: '0', padding: '0'}}>{product.name}</p>
            <p style={{ fontWeight: '600', margin: '0', padding: '0' }}>${product.price.toFixed(2)}</p>
            <p style={{fontSize: '.75rem', margin: '0', padding: '0'}}>Auto renews on {getDateTwoMonthsFromNow()}</p>
            <div className='list-btm'>
                <NavLink className='listing-navs' to={`/products/${product.id}/edit`}>Edit</NavLink>
                <NavLink className='listing-navs' to={`/products/${product.id}`}>View</NavLink>
                <div >
                <OpenModalButton
                    buttonText="Remove"
                    id='delete-button'
                    modalComponent={<DeleteProduct product_id={product.id} />}
                />
                </div>

            </div>
        </div>
    ))}
</div>

            </div>
        </div>

        </>
    ) :
    (
        <div>

            <div className='right-top-none'>
                <h3 style={{fontWeight: '700'}}>You currently have no listings</h3>
                <NavLink className={'listing-bttn'} to={'/products/new'}><IoMdAdd />Add Listing</NavLink>
            </div>
        </div>
    )
}



export default UserListings;
