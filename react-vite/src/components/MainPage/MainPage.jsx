import './MainPage.css'
import { getProducts } from '../../redux/products';
import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { IoMdStar } from "react-icons/io";
import { NavLink } from 'react-router-dom';

const MainPage = () => {
    const products = useSelector(state => state.productsReducer.allProducts)
    const allProducts = products ? Object.values(products) : [];

    const getStarRating = (rating) => {
        if (rating >= 5) return 5;
        if (rating >= 4) return 4;
        if (rating >= 3) return 3;
        if (rating >= 2) return 2;
        return 1;
    };

    const getRandomProducts = (productsArray, numberOfProducts = 5) => {
        const copyProductsArray = [...productsArray];
        for (let i = copyProductsArray.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copyProductsArray[i], copyProductsArray[j]] = [copyProductsArray[j], copyProductsArray[i]];
        }
        return copyProductsArray.slice(0, numberOfProducts);
    }

    const randomProducts = getRandomProducts(allProducts);
    const remainingProducts = allProducts.filter(product => !randomProducts.includes(product));

    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProducts());
    }, [dispatch]);

    if (!allProducts.length) return <div>Loading...</div>;

    return (
        <div className='main-div'>
            <div className='cat-bubbles'>
                <h3>Top products that are trending....</h3>
                <ul>
                    {randomProducts.map(successfulProduct => (
                        <NavLink key={successfulProduct.id} to={`/products/${successfulProduct.id}`} className={'bubbles'}>
                            {successfulProduct.images && successfulProduct.images.length > 0 ? (
                                <img className='bubble-img' src={successfulProduct.images[0].url} alt='product image'></img>
                            ) : (
                                <div className='no-image'>No image available</div>
                            )}
                            <h3>{successfulProduct.name}</h3>
                        </NavLink>
                    ))}
                </ul>
            </div>

            <h2>Products</h2>
            <div className='products-main'>
                {remainingProducts.map(product => (
                    <div className='product-container' key={product.id}>
                        <NavLink className={'product_nav'} to={`/products/${product.id}`}>
                            {product.images && product.images.length > 0 ? (
                                <img className='main-prdct-img' src={product.images[0].url} alt={product.name}></img>
                            ) : (
                                <div className='no-image'>No image available</div>
                            )}
                            <h3>{product.name}</h3>
                            <p>
                                {Array.from({ length: getStarRating(product.avgRating) }, (_, index) => (
                                    <IoMdStar key={index} className="stars" />
                                ))}
                                <span style={{ marginLeft: '6px', fontWeight: '100' }}>({product.reviews?.length || 0})</span>
                            </p>
                            <p>${product.price.toFixed(2)}</p>
                            <p>{product.owner?.shop_name || 'Anonymous'}</p>
                        </NavLink>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default MainPage;
