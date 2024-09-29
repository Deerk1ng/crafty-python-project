import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { createProduct, updateProductDetails } from "../../redux/products";
import { thunkAuthenticate, thunkLogout } from "../../redux/session";
import { NavLink, useNavigate } from "react-router-dom";
import { useParams } from "react-router-dom";
import { getOneProduct } from "../../redux/products";
import { FaArrowLeftLong } from "react-icons/fa6";

const EditProduct = () => {
    const { product_id } = useParams();

    const [isLoaded, setIsLoaded] = useState(false);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const productById = useSelector(state => state.productsReducer.currProduct);

    const [name, setName] = useState('');
    const [price, setPrice] = useState('');
    const [description, setDescription] = useState('');
    const [category, setCategory] = useState('');

    const [errors, setErrors] = useState({});
    const [activeSection, setActiveSection] = useState('about');


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


    const validateData = () => {
        const fileArr = ['.png', '.jpg', 'jpeg']
        const error = {};

        if (name.length < 5) error['name'] = "Product name must be longer than 5 characters";
        if (name.length > 30) error['name'] = "Product name must be shorter than 30 characters";

        if ( isNaN(price) || price <= 0) error['price'] = "Price must be a valid number greater than 0";

        if (description.length < 10) error['description'] = "Description must be longer than 10 characters";
        if (description.length > 300) error['description'] = "Description must be shorter than 300 characters";

        if (!category) error['category'] = "Please select a category for your product";

        setErrors(error);
        return Object.keys(error).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if(validateData()) {
            const serverResponse = await dispatch(
                updateProductDetails({
                    name,
                    price: parseFloat(price).toFixed(2),
                    description,
                    category: category.toLowerCase(),
                }, product_id)
            );

            if (serverResponse.errors) {
                setErrors((error) => ({ ...error, ...serverResponse.errors }));
            } else {
                dispatch(updateProductDetails(serverResponse, product_id))
                navigate(`/products/${product_id}`);
            }
        }
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

    const scrollToSection = (id) => {
        const section = document.getElementById(id);
        if (section) {
            section.scrollIntoView({ behavior: "smooth", block: "start" });
            setActiveSection(id);
        }
    };
    const handleScroll = () => {
        const sections = ['about', 'description', 'price', 'details', 'category'];
        const scrollY = window.scrollY;

        sections.forEach(section => {
            const sectionElement = document.getElementById(section);
            if (sectionElement) {
                const { offsetTop, clientHeight } = sectionElement;
                if (scrollY >= offsetTop - 50 && scrollY < offsetTop + clientHeight) {
                    setActiveSection(section);
                }
            }
        });
    };

    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    return (
        <div id="create_prod">

            <div className="create-listing-top">
                <button onClick={handleGoBack}><FaArrowLeftLong style={{marginRight: '5px'}}/>Back to Listings</button>
                <h2 style={{margin: '13px'}}>Edit Listing</h2>
                <ul className="sections-scroll">
                    <li
                        className={`sections-form ${activeSection === 'about' ? 'active' : ''}`}
                        onClick={() => scrollToSection('about')}
                    >
                        About
                    </li>
                    <li
                        className={`sections-form ${activeSection === 'price' ? 'active' : ''}`}
                        onClick={() => scrollToSection('price')}
                    >
                        Price
                    </li>
                    <li
                        className={`sections-form ${activeSection === 'details' ? 'active' : ''}`}
                        onClick={() => scrollToSection('details')}
                    >
                        Details
                    </li>
                </ul>
            </div>
            <div id="about" className="form-prod">
                <form onSubmit={handleSubmit}>
                    <section>
                        <h2>About</h2>
                        <p>Tell the world about your item and why they will love it.</p>
                    </section>
                    <section>
                        <h2 style={{marginTop: '30px'}}>Title<span className="required">*</span></h2>
                        <p>Include keywords that buyers would use to search for this item.</p>
                        <input
                            type="name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                        {errors.name && <p className='errors-msgs'>{errors.name}</p>}
                    </section>

                    <section id='price'>
                        <h2>Description<span className="required">*</span></h2>
                        <p>What makes your product special? Buyers will only be able to see the first few lines unless they view the product.</p>
                        <textarea
                            type="text"
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                            required
                        />
                        {errors.description && <p  className='errors-msgs'>{errors.description}</p>}
                    </section>
                    <section>
                        <h2>Price<span className="required">*</span></h2>
                        <p>Set a price for your item.</p>
                        $<input
                            className="price-input"
                            id="details"
                            type="text"
                            value={price}
                            onChange={(e) => setPrice(e.target.value)}
                            required
                        />
                        {errors.price && <p className='errors-msgs'>{errors.price}</p>}
                    </section>
                    <section id="details">
                        <h2>Details</h2>
                        <p>Share with us the category that your product falls in.</p>
                    </section>
                    <section>
                        <h2 style={{marginTop: '30px'}}>Category<span className="required">*</span></h2>
                        <select id="category" name="category" value={category} onChange={handleCategoryChange} >
                            <option value="">--Please choose an option--</option>
                            <option value="mens">Mens</option>
                            <option value="womens">Womens</option>
                            <option value="melee">Melee</option>
                            <option value="long-range">Long-range</option>
                            <option value="accessories">Accessories</option>
                        </select>
                        {errors.category && <p className='errors-msgs'>{errors.category}</p>}
                    </section>
                    <section className="form-bttm">
                        <button id="cancel-btn" onClick={handleGoBack}>Cancel</button>
                        <button type="submit" className="submit-product">Publish</button>
                    </section>
                </form>
            </div>
        </div>
    );
};

export default EditProduct;
