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


const CreateProduct = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const [name, setName] = useState("");
    const [price, setPrice] = useState(0);
    const [description, setDesciption] = useState("");
    const [category, setCategory] = useState('')
    const [images, setImages] = useState([])

    const [errors, setErrors] = useState({});

    const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);


    const user = useSelector((state) => state.session.user)

    const handleSubmit = async (e) => {
        e.preventDefault();

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
            setErrors(serverResponse.errors);
        } else {

            navigate(`/products/${serverResponse.id}`);
        }
    };


    const logout = (e) => {
        e.preventDefault();
        dispatch(thunkLogout()).then(() => {
            navigate('/');
        });
    };

    const handleGoBack = () => {
        navigate('/products/current')
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
          setErrors({ image: "You can only upload up to 5 images." });
        }
      };

      const removeImageInput = (index) => {
        const updatedImages = images.filter((_, i) => i !== index);
        setImages(updatedImages);
      };

      const handleCategoryChange = (e) => {
        setCategory(e.target.value);
    };

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
                        {errors.name && <p>{errors.name}</p>}
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
                            </div>
                        ))}
                        {images.length < 5 && (
                            <button type="button" onClick={addImageInput}>
                            Add photo
                            </button>
                        )}
                        {errors.image && <p>{errors.image}</p>}
                    </section>
                    <section>
                        <h2>Description<span className="required">*</span></h2>
                        <p>What makes your product special? Buyers will only be able to see the first few lines unless they view the product.</p>
                        <textarea
                            type="text"
                            value={description}
                            onChange={(e) => setDesciption(e.target.value)}
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
                            <option value="Mens">Mens</option>
                            <option value="Womens">Womens</option>
                            <option value="Melee">Melee</option>
                            <option value="long-range">Long-range</option>
                            <option value="accessories">Accessories</option>
                        </select>
                    </section>
                    <section>
                        <button onClick={handleGoBack}>cancel</button>
                        <button type="submit" className="submit-product">Publish</button>
                    </section>
                </form>
            </div>

        </div>
    )
}


export default CreateProduct;
