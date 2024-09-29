import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { createProduct } from "../../redux/products";
import { thunkAuthenticate, thunkLogout } from "../../redux/session";
import { NavLink, useNavigate } from "react-router-dom";
import { IoMdHome } from "react-icons/io";
import { IoSettings } from "react-icons/io5";
import { TfiAnnouncement, TfiHelpAlt } from "react-icons/tfi";
import { FaMoneyBillTrendUp } from "react-icons/fa6";
import { MdFavoriteBorder, MdReviews, MdQueryStats } from "react-icons/md";
import './CreateProduct.css'

const fileArr = ['.png', '.jpg', '.jpeg'];

const CreateProduct = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const [name, setName] = useState("");
    const [price, setPrice] = useState(0);
    const [description, setDescription] = useState("");
    const [category, setCategory] = useState('');
    const [images, setImages] = useState([]);

    const [errors, setErrors] = useState({});

    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
    }, [dispatch]);

    const user = useSelector((state) => state.session.user);

    const validateData = () => {
        const fileArr = ['.png', '.jpg', 'jpeg']
        const error = {};

        if (name.length < 5) error['name'] = "Product name must be longer than 5 characters";
        if (name.length > 30) error['name'] = "Product name must be shorter than 30 characters";

        if ( isNaN(price) || price <= 0) error['price'] = "Price must be a valid number greater than 0";

        if (description.length < 10) error['description'] = "Description must be longer than 10 characters";
        if (description.length > 300) error['description'] = "Description must be shorter than 300 characters";

        if (!category) error['category'] = "Please select a category for your product";

        images.forEach((url, index) => {
            if (!fileArr.includes(url.slice(-4))) {
                error[`image${index}`] = 'Image URL must end in .png, .jpg, or .jpeg';
            }
        });

        setErrors(error);
        return Object.keys(error).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (validateData()) {
            const serverResponse = await dispatch(
                createProduct({
                    owner_id: user.id,
                    name,
                    price: parseFloat(price).toFixed(2),
                    description,
                    category: category.toLowerCase(),
                    images
                })
            );

            if (serverResponse.errors) {
                setErrors((error) => ({ ...error, ...serverResponse.errors }));
            } else {
                navigate(`/products/${serverResponse.id}`);
            }
        }
    };

    const handleImageChange = (index, value) => {
        const updatedImages = [...images];
        updatedImages[index] = value;
        setImages(updatedImages);
    };

    const addImageInput = () => {
        if (images.length < 5) {
            setImages([...images, ""]);
        } else {
            setErrors((prev) => ({ ...prev, image: "You can only upload up to 5 images." }));
        }
    };

    const removeImageInput = (index) => {
        const updatedImages = images.filter((_, i) => i !== index);
        setImages(updatedImages);
    };

    const handleCategoryChange = (e) => {
        setCategory(e.target.value);
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

    return (
        <div>
            <div className='side-nav'>
                <ul>
                    <li style={{ fontWeight: '800' }}>Shop Manager</li>
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
                <h2>New Listing</h2>
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
                            type="text"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            required
                        />
                        {errors.name && <p className='errors-msgs'>{errors.name}</p>}
                    </section>

                    <section>
                        <h2>
                            Photos <span className="required">*</span>
                        </h2>
                        <p>Add up to 5 photos</p>
                        {images.map((image, index) => (
                            <div key={index} style={{ marginBottom: "10px" }}>
                                <input
                                    type="text"
                                    placeholder={`Image URL ${index + 1}`}
                                    value={image}
                                    onChange={(e) => handleImageChange(index, e.target.value)}
                                    required
                                />
                                {images.length > 1 && (
                                    <button type="button" onClick={() => removeImageInput(index)}>
                                        Remove
                                    </button>
                                )}
                                {errors[`image${index}`] && (
                                    <p className="errors-msgs">{errors[`image${index}`]}</p>
                                )}
                            </div>
                        ))}
                        {images.length < 5 && (
                            <button type="button" onClick={addImageInput}>
                                Add photo
                            </button>
                        )}
                        {errors.image && <p className='errors-msgs'>{errors.image}</p>}
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
                        {errors.description && <p className='errors-msgs'>{errors.description}</p>}
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
                        {errors.price && <p className='errors-msgs'>{errors.price}</p>}
                    </section>

                    <section>
                        <h2>Details</h2>
                        <p>Share with us the category that your product falls in.</p>
                    </section>

                    <section>
                        <h2>Category<span className="required">*</span></h2>
                        <select id="category" name="category" value={category} onChange={handleCategoryChange}>
                            <option value="">--Please choose an option--</option>
                            <option value="Mens">Mens</option>
                            <option value="Womens">Womens</option>
                            <option value="Melee">Melee</option>
                            <option value="long-range">Long-range</option>
                            <option value="accessories">Accessories</option>
                        </select>
                        {errors.category && <p className='errors-msgs'>{errors.category}</p>}
                    </section>

                    <section>
                        <button onClick={handleGoBack}>cancel</button>
                        <button type="submit" className="submit-product">Publish</button>
                    </section>
                </form>
            </div>
        </div>
    );
};

export default CreateProduct;
