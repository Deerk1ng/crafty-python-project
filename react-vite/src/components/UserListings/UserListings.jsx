import './UserListings.css'
import { getUserProducts } from '../../redux/products';
import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState, ulRef } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { thunkLogout } from "../../redux/session";
import { IoMdHome, IoMdAdd } from "react-icons/io";
import { IoSettings } from "react-icons/io5";
import { TfiAnnouncement, TfiHelpAlt } from "react-icons/tfi";
import { FaMoneyBillTrendUp } from "react-icons/fa6";
import { MdFavoriteBorder, MdReviews, MdQueryStats } from "react-icons/md";
import DeleteProduct from '../DeleteProductModal/DeleteProductModal';
import OpenModalButton from '../OpenModalButton/OpenModalButton';


const UserListings = () => {
    const navigate = useNavigate();

    const [showMenu, setShowMenu] = useState(false);
    const toggleMenu = (e) => {
        e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
        setShowMenu(!showMenu);
      };

    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = (e) => {
          if (ulRef.current && !ulRef.current.contains(e.target)) {
            setShowMenu(false);
          }
        };
        document.addEventListener("click", closeMenu);

        return () => document.removeEventListener("click", closeMenu);
    }, [showMenu]);

    const closeMenu = () => setShowMenu(false);

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


    const logout = (e) => {
        e.preventDefault();
        dispatch(thunkLogout()).then(() => {
            // Redirect to home
            navigate('/');
            closeMenu();
        });
    };



    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getUserProducts());
    }, [dispatch]);

    return allProducts.length > 0 ? (
        <>
        <div>
            <div className='right-top'>
                <h3>Listings</h3>
                <NavLink className={'listing-bttn'} to={'/products/new'}><IoMdAdd />Add Listing</NavLink>
            </div>
            <div>
            <div>
    {allProducts.map(product => (
        <div key={product.id}>
            {product.images && product.images.length > 0 ? (
                <img className='user-product-img' src={product.images[0].url} alt='' />
            ) : (
                <div className='no-image'>No image available</div>
            )}
            <p>{product.name}</p>
            <p style={{ fontWeight: '700' }}>${product.price.toFixed(2)}</p>
            <p>Auto renews on {getDateTwoMonthsFromNow()}</p>
            <div className='list-btm'>
                <NavLink to={`/products/${product.id}/edit`}>Edit</NavLink>
                <OpenModalButton
                    buttonText="Remove Product"
                    className='delete-button'
                    modalComponent={<DeleteProduct product_id={product.id} />}
                />

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
            <div className='side-nav'>
                <ul>
                    <li style={{fontWeight: '800'}}>Shop Manager</li>
                    <NavLink to={'/'}><IoMdHome /> Home</NavLink>
                    <NavLink to={'/favorites/current'}><MdFavoriteBorder />Favorites</NavLink>
                    <NavLink onClick={''}><MdReviews />Shop Reviews</NavLink>
                    <NavLink onClick={''}><MdQueryStats />Stats</NavLink>
                    <NavLink onClick={''}><TfiAnnouncement />Marketing</NavLink>
                    <NavLink onClick={''}><FaMoneyBillTrendUp />Finances</NavLink>
                    <NavLink onClick={''}><TfiHelpAlt />Help</NavLink>
                    <NavLink onClick={''}><IoSettings />Settings</NavLink>
                    <button onClick={logout}>Log Out</button>

                </ul>
            </div>
            <div className='right-top-none'>
                <h3>You currently have no listings</h3>
                <NavLink className={'listing-bttn-none'} to={'/products/new'}><IoMdAdd />Add Listing</NavLink>
            </div>
        </div>
    )
}



export default UserListings;
