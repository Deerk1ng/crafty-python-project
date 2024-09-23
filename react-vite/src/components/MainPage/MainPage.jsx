import './MainPage.css'
import { getProducts } from '../../redux/products';
import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { IoMdStar } from "react-icons/io";
import { NavLink } from 'react-router-dom';
import Footer from '../Footer/footer';

const MainPage = () => {

    const products = useSelector(state => state.productsReducer.allProducts)


    const allProducts = products ? Object.values(products) : [];

        // Function to calculate the correct number of stars
        const getStarRating = (rating) => {
            if (rating >= 5) return 5;
            if (rating >= 4) return 4;
            if (rating >= 3) return 3;
            if (rating >= 2) return 2;
            return 1;
        };

    // func for random 5 products to show case
    function getRandomProducts(productsArray, numberOfProducts = 5) {
        // Shuffle the array using the Fisher-Yates shuffle algorithm
        for (let i = productsArray.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [productsArray[i], productsArray[j]] = [productsArray[j], productsArray[i]];
        }

        // Return the first 'numberOfProducts' items after shuffle
        return productsArray.slice(0, numberOfProducts);
    }
    const randomProducts = getRandomProducts(allProducts);


    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProducts());
    }, [dispatch]);

    return (
        <div className='main-div'>
            <div className='cat-bubbles'>
                <h3>Top products that are trending....</h3>
                <ul>
                    {randomProducts.map(productran => (
                        <NavLink to={`/products/${productran.id}`} className={'bubbles'}>
                            <img className='bubble-img' src={productran.images[0].url} alt='product image'></img>
                            <h3>{productran.name}</h3>
                        </NavLink>
                    ))}
                </ul>
            </div>

            <h2>Products</h2>
            <div className='products-main'>
                {allProducts.map(product => (
                    <div className='product-container'>
                        <NavLink className={'product_nav'} to={`/products/${product.id}`}>
                        <img className='main-prdct-img' src={product.images[0].url} alt={product.name}></img>
                        <h3>{product.name}</h3>
                        <p>{Array.from({ length: getStarRating(product.avgRating) }, (_, index) => ( <IoMdStar key={index} className="stars" /> ))}<span style={{marginLeft: '6px', fontWeight: '100'}}>({product.reviews.length})</span></p>
                        <p>${product.price.toFixed(2)}</p>
                        <p>{product.owner.shop_name}</p>
                        </NavLink>
                    </div>
                ))}
            </div>
            <Footer />

        </div>
    )
}


export default MainPage;
