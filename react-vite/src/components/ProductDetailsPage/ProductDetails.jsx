import "./ProductDetails.css"
import { getReviews } from "../../redux/reviews"
import { useDispatch, useSelector } from "react-redux"
import { useEffect, useState } from "react"
import { IoMdStar, IoMdHeart, IoMdPerson } from "react-icons/io";
import { useParams } from 'react-router-dom';
import Footer from "../Footer"
import { getOneProduct } from "../../redux/products";
import OpenModalButton from "../OpenModalButton/OpenModalButton"
import CreateReviewModal from "../CreateReviewModal/CreateReviewModal"
import DeleteReviewModal from "../DeleteReviewModal/DeleteReviewModal";

const ProductDetailsPage = () => {
    const { product_id } = useParams();
    const user = useSelector(state => state.session.user);
    const product = useSelector(state => state.productsReducer.currProduct);
    const review = useSelector((state) => state.reviewsReducer.ReviewsForCurrentProduct);
    const [isLoaded, setIsLoaded] = useState(false);
    const [revArr, setRevArr] = useState([]);
    const dispatch = useDispatch();

    const getStarRating = (rating) => {
        if (Number(rating) >= 5) return 5;
        if (Number(rating) >= 4) return 4;
        if (Number(rating) >= 3) return 3;
        if (Number(rating) >= 2) return 2;
        return 1;
    };

    useEffect(() => {
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const reviewArr = [];

        Object.keys(review).forEach((key, i) => {
            const dateFormatted = new Date(review[key]?.created_at);
            const date = `${months[dateFormatted.getMonth()]} ${dateFormatted.getDate()} ${dateFormatted.getFullYear()}`;

            reviewArr.push((
                <div className={`review-${i}`} key={i}>
                    <p>{Array.from({ length: getStarRating(review[key]?.item_rating) }, (_, index) => (<IoMdStar key={index} className="stars" />))}</p>
                    <div className="prod-description">{review[key]?.description}</div>
                    <div className="prod-item">Purchased item: {product?.name}</div>
                    {review[key]?.image?.url ? (
                        <img src={review[key]?.image.url} alt="image uploaded by user of the product received" className="review-img" />
                    ) : null}
                    <div><IoMdPerson /> {review[key]?.user?.name} {date}</div>
                    {review[key]?.user_id === user?.id ? (
                        <OpenModalButton
                            buttonText="Delete"
                            className='delete-button'
                            modalComponent={<DeleteReviewModal review_id={review[key].id} />}
                        />
                    ) : null}
                </div>
            ));
        });
        setRevArr(reviewArr);
    }, [review, product, user]);

    const imgLoop = (images) => {
        const newImgArr = [];
        for (let i = 0; i < 5; i++) {
            const currImg = images[i];
            if (currImg) {
                newImgArr.push(
                    <img key={currImg.id} src={currImg.url} alt={`image belonging to the spot ${product?.name}`} className="preview" />
                );
            }
        }
        return newImgArr;
    };

    const checkCritics = (reviews) => {
        const idLog = [];
        Object.values(reviews).forEach(review => idLog.push(review.user_id));
        return idLog.includes(user?.id);
    };

    useEffect(() => {
        dispatch(getOneProduct(product_id))
            .then(() => dispatch(getReviews(product_id)))
            .then(() => setIsLoaded(true));
    }, [product_id, dispatch]);

    return (
        <>
            {isLoaded ? (
                <>
                    <div className="prod-shopping">
                        <div className="photos">
                            {product?.images?.length ? imgLoop(product.images) : <div>No images available</div>}
                        </div>
                        <div className="buy-container">
                            <h2 className="prod-price">{product.price}</h2>
                            <div className="prod-title">{product.name}</div>
                            <div className="user-reviews">Shop Seller: {product?.avgRating}</div>
                            <button className="buy-button">Buy it Now</button>
                            <button className="cart-button">Add to Cart</button>
                            <button className="favorites-button"><IoMdHeart /> Add to Favorites</button>
                        </div>
                    </div>
                    {(user && user.id !== product?.owner_id) && !checkCritics(review) ? (
                        <OpenModalButton
                            buttonText="Post Your Review"
                            className='newSpot-button'
                            modalComponent={<CreateReviewModal product_id={product.id} />}
                        />
                    ) : null}
                    <div className="prod-review">
                        <div>{product?.reviews?.length} Reviews</div>
                        <p>{Array.from({ length: getStarRating(product?.avgRating) }, (_, index) => (
                            <IoMdStar key={index} className="stars" />
                        ))}<span style={{ marginLeft: '6px', fontWeight: '100' }}>({product?.avgRating})</span></p>
                        <div className="review-container">
                            {revArr}
                        </div>
                    </div>
                    <div className="prod-details">
                        <h3>Item Details</h3>
                        <div className="item-details">{product?.description}</div>
                        <div className="prod-owner">Sold by: {product?.owner?.first_name}</div>
                    </div>
                    <Footer />
                </>
            ) : null}
        </>
    );
}

export default ProductDetailsPage;
