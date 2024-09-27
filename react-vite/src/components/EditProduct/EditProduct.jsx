import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { createProduct, updateProductDetails } from "../../redux/products";
import { thunkAuthenticate, thunkLogout } from "../../redux/session";
import { NavLink, useNavigate } from "react-router-dom";
import { IoMdHome } from "react-icons/io";
import { IoSettings } from "react-icons/io5";
import { TfiAnnouncement, TfiHelpAlt } from "react-icons/tfi";
import { FaMoneyBillTrendUp } from "react-icons/fa6";
import { MdFavoriteBorder, MdReviews, MdQueryStats } from "react-icons/md";
import { useParams } from "react-router-dom";
import { getOneProduct } from "../../redux/products";


const EditProduct = () => {
    const { product_id } = useParams();

    const [isLoaded, setIsLoaded] = useState(false);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const productById = useSelector(state => state.productsReducer.currProduct);
    console.log('product BY id      ',productById)

    const [name, setName] = useState('');
    const [price, setPrice] = useState('');
    const [description, setDescription] = useState('');
    const [category, setCategory] = useState('');

    const [errors, setErrors] = useState({});


    useEffect(() => {

        if (productById) {
            setName(productById.name || '');
            setPrice(productById.price || '');
            setDescription(productById.description || '');

            if (typeof productById.category === 'string') {
                setCategory(productById.category.toLowerCase());
            }
        }
    }, [productById]);

    const handleSubmit = async (e) => {
        e.preventDefault();


        const serverResponse = await dispatch(
            updateProductDetails({
                name,
                price: parseFloat(price).toFixed(2),
                description,
                category: category.toLowerCase(),
            }, product_id)
        );

        if (serverResponse.errors) {
            setErrors(serverResponse.errors);
        } else {
            dispatch(updateProductDetails(serverResponse, product_id))
            navigate(`/products/${product_id}`);
        }
    };

    const logout = (e) => {
        e.preventDefault();
        dispatch(thunkLogout()).then(() => {
            navigate('/');
        });
    };

    const handleGoBack = () => {
        navigate('/products/current');
    };

    const handleCategoryChange = (e) => {
        setCategory(e.target.value);
    };

    useEffect(() => {
        dispatch(getOneProduct(product_id))
            .then(() => dispatch(thunkAuthenticate()))
            .then(() => setIsLoaded(true));
    }, [product_id, dispatch]);

    return (
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
            <div className="create-listing-top">
                <button onClick={handleGoBack}>Back to Listings</button>
                <h2>Edit Listing</h2>
                <ul>
                    <li>About</li>
                    <li>Price</li>
                    <li>Details</li>
                </ul>
            </div>
            <div>
                <form onSubmit={handleSubmit}>
                    <section>
                        <h2>About</h2>
                        <p>Tell the world about your item and why they will love it.</p>
                    </section>
                    <section>
                        <h2>Title<span className="required">*</span></h2>
                        <p>Include keywords that buyers would use to search for this item.</p>
                        <input
                            type="name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                        {errors.name && <p>{errors.name}</p>}
                    </section>
                    <section>
                        <h2>Description<span className="required">*</span></h2>
                        <p>What makes your product special? Buyers will only be able to see the first few lines unless they view the product.</p>
                        <textarea
                            type="text"
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                            required
                        />
                        {errors.name && <p>{errors.name}</p>}
                    </section>
                    <section>
                        <h2>Price<span className="required">*</span></h2>
                        <p>Set a price for your item.</p>
                        $<input
                            className="price-input"
                            type="text"
                            value={price}
                            onChange={(e) => setPrice(e.target.value)}
                            required
                        />
                    </section>
                    <section>
                        <h2>Details</h2>
                        <p>Share with us the category that your product falls in.</p>
                    </section>
                    <section>
                        <h2>Category<span className="required">*</span></h2>
                        <select id="category" name="category" value={category} onChange={handleCategoryChange} >
                            <option value="">--Please choose an option--</option>
                            <option value="mens">Mens</option>
                            <option value="womens">Womens</option>
                            <option value="melee">Melee</option>
                            <option value="long-range">Long-range</option>
                            <option value="accessories">Accessories</option>
                        </select>
                    </section>
                    <section>
                        <button onClick={handleGoBack}>Cancel</button>
                        <button type="submit" className="submit-product">Publish</button>
                    </section>
                </form>
            </div>
        </div>
    );
};

export default EditProduct;
