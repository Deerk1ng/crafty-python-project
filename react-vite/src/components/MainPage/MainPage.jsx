import './MainPage.css'
import { getProducts } from '../../redux/products';
import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';

const MainPage = () => {

    const products = useSelector(state => state.productsReducer.allProducts)
    console.log(products)
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProducts());
    }, [dispatch]);

    return (
        <div className='main-div'>
            <h3>Take a peek on some trending items on Crafty</h3>

        </div>
    )
}


export default MainPage;
