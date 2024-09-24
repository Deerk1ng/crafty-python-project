import "./ProductDetails.css"
import { getReviews } from "../../redux/reviews"
import { useDispatch, useSelector } from "react-redux"
import { useEffect, useState } from "react"
import { IoMdStar, IoMdHeart, IoMdPerson } from "react-icons/io";
import { useParams } from 'react-router-dom';
import Footer from "../Footer"
import { getOneProduct } from "../../redux/products";

const ProductDetailsPage = () => {
    const {product_id} = useParams()
    const product = useSelector(state => state.productsReducer.currProduct)
    const review = useSelector((state) => state.reviewsReducer.ReviewsForCurrentProduct)
    const [isLoaded, setIsLoaded] = useState(false)
    const dispatch = useDispatch()

    const getStarRating = (rating) => {
        if (rating >= 5) return 5;
        if (rating >= 4) return 4;
        if (rating >= 3) return 3;
        if (rating >= 2) return 2;
        return 1;
    };

    const reviewLoop = (reviews) => {
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        const rLength = Object.keys(reviews).length
        const revArr = []

        for (let i = 1; i < rLength + 1; i++) {
            console.log(reviews[i])
            const dateFormatted = new Date(reviews[i]?.created_at)
            const date = months[dateFormatted.getMonth()] + " " + dateFormatted.getFullYear()
            revArr.push((
                <div className={`review-${i}`}>
                    <p>{Array.from({ length: getStarRating(reviews[i]?.itemRating) }, (_, index) => ( <IoMdStar key={index} className="stars" /> ))}</p>
                    <div className="prod-description" key={i}>{reviews[i]?.description}</div>
                    <div className="prod-item">purchased item: {product.name}</div>
                    {reviews[i]?.image.length ? ( <img src={reviews[i]?.image.url} alt="image uploaded by user of the product received" className="review-img"/> ) : (<></>)}
                    <div><IoMdPerson/> {reviews[i]?.user.name} {date}</div>
                </div>
             ))
        }
        return revArr
    }

    useEffect(() => {
        dispatch(getOneProduct(product_id))
        .then(dispatch(getReviews(product_id)))
        .then(setIsLoaded(true))
        console.log("at dispatch", review)
    }, [product_id])


    return (
        <>
        { isLoaded ? (
            <>
            <div className="prod-shopping">
                <div className="photos"></div>
                <div className="buy-container">
                    <h2 className="prod-price">{product?.price}</h2>
                    <div className="prod-title">{product?.name}</div>
                    <div className="user-reviews">Shop Seller: {product?.avgRating}</div>
                    <button className="buy-button">Buy it Now</button>
                    <button className="cart-button">Add to Cart</button>
                    <button className="favorites-button"> <IoMdHeart /> Add to Favorites</button>
                </div>
            </div>
            <div className="prod-review">
                <div>{product?.reviews?.length} Reviews</div>
                <p>{Array.from({ length: getStarRating(product.avgRating) }, (_, index) => ( <IoMdStar key={index} className="stars" /> ))}<span style={{marginLeft: '6px', fontWeight: '100'}}>({product.avgRating})</span></p>
                <div className="review-container">
                    {Object.keys(review).length ? reviewLoop(review) : <></>}
                </div>
            </div>
            <div className="prod-details">
                <h3>Item Details</h3>
                <div className="item-details">{product?.description}</div>
                <div className="prod-owner">Sold by: {product?.owner?.first_name}</div>
            </div>
            <Footer />
        </>
        ) : <></>}
        </>
    )
}

export default ProductDetailsPage
