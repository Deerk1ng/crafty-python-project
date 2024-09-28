import "./ProductDetails.css"
import { addItemThunk } from "../../redux/cart"
import { getReviews } from "../../redux/reviews"
import { useDispatch, useSelector } from "react-redux"
import { useEffect, useState } from "react"
import { IoMdStar, IoMdHeart, IoMdHeartEmpty, IoMdPerson } from "react-icons/io";
import { useParams, useNavigate} from 'react-router-dom';
import { getOneProduct } from "../../redux/products";
import { createFavorite, deleteFavorite, getFavoritesThunk } from "../../redux/favorites";
import OpenModalButton from "../OpenModalButton/OpenModalButton"
import CreateReviewModal from "../CreateReviewModal/CreateReviewModal"
import DeleteReviewModal from "../DeleteReviewModal/DeleteReviewModal";
import UpdateReviewModal from "../UpdateReviewModal/UpdateReviewModal";

const ProductDetailsPage = () => {
    const { product_id } = useParams();
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const product = useSelector(state => state.productsReducer.currProduct);
    const review = useSelector((state) => state.reviewsReducer.ReviewsForCurrentProduct);
    const favorites = useSelector((state) => state.favoritesReducer.currentFavorites)
    const [isLoaded, setIsLoaded] = useState(false);
    const [bigImg, setBigImg] = useState('')
    const [imgArr, setImgArr] = useState([])
    const [revRating, setRevRating] = useState(0)
    const [reviews_list, set_reviews_list] = useState([Object.values(review).sort((a,b) => b.dateFormatted - a.dateFormatted)])


    const getStarRating = (rating) => {
        if (Number(rating) >= 5) return 5;
        if (Number(rating) >= 4) return 4;
        if (Number(rating) >= 3) return 3;
        if (Number(rating) >= 2) return 2;
        return 1;
    };
    useEffect(() => {
        set_reviews_list(Object.values(review).sort((a,b) => b.dateFormatted - a.dateFormatted))
    },[review])

    useEffect(() => {
        let ratingSum = 0
        reviews_list.forEach((rev) => {
            ratingSum += rev.item_rating

        })
        const avg = (ratingSum / reviews_list.length).toFixed(2)
        setRevRating(avg)
    }, [review, product, user, reviews_list]);


    useEffect(() => {
        if(product.images) {

            const images = product.images
            const newImgArr = [];
            for (let i = 0; i < 5; i++) {
                const currImg = images[i];
                if (currImg) {
                    newImgArr.push(
                        <img key={currImg.id} src={currImg.url} alt={`image belonging to the spot ${product?.name}`} onClick={(e) => setBigImg(e.target.src)} className="image" />
                    );
                }
            }
            setImgArr(newImgArr);
            setBigImg(images[0].url)
        }
    }, [product])

    const checkCritics = (reviews) => {
        const idLog = [];
        Object.values(reviews).forEach(review => idLog.push(review.user_id));
        return idLog.includes(user?.id);
    };

    useEffect(() => {
        dispatch(getOneProduct(product_id))
            .then(() => dispatch(getReviews(product_id)))
            .then(() => dispatch(getFavoritesThunk()))
            .then(() => setIsLoaded(true));
    }, [product_id, dispatch]);


    const AddItemClick = (e, user_id, product_id) => {
        e.preventDefault();

        dispatch(addItemThunk(user_id, product_id));
        navigate('/shopping-cart/current')
    }

    const handleDelete = (e) => {
        e.preventDefault();

        dispatch(deleteFavorite(favorites[product.id].id,product.id))
    }

    const handleAdd = (e) => {
        e.preventDefault();
        dispatch(createFavorite(product.id))

    }

    return (
        <>
            {isLoaded ? (
                <div className="prod-container">
                    <div className="prod-shopping">
                        <div className="photos">
                            {imgArr.length ? imgArr : <div>No images available</div>}
                        </div>
                        <img src={bigImg} alt={`${bigImg}`} className="big-image" />
                        <div className="buy-container">
                            <h2 className="prod-price">${product?.price?.toFixed(2)}</h2>
                            <h2 className="prod-title">{product?.name}</h2>
                            <div className="user-reviews">{product.owner.shop_name}</div>
                            {Number(revRating) ? <div className="user-rev-rating">({revRating} <IoMdStar className="stars" />)</div> : <div className="user-rev-rating">No reviews!</div> }

                            {user && user.id ?
                                <>
                                <button
                                    className="cart-button"
                                    onClick={(e) => AddItemClick(e, user.id, product.id)} >Add to Cart</button>
                                {favorites[product.id] ? <button className="favorites-button" onClick={(e) => handleDelete(e)}><IoMdHeart /> Delete from Favorites</button> : <button className="favorites-button" onClick={(e) => handleAdd(e)}><IoMdHeartEmpty /> Add to Favorites</button>}
                                </>

                            : <></>}


                        </div>
                    </div>
                    <div className="rev-container">
                        <div className="prod-review">
                            {(user && user.id !== product?.owner_id) && !checkCritics(review) ? (
                                <OpenModalButton
                                    buttonText="Post Your Review"
                                    className='newSpot-button'
                                    modalComponent={<CreateReviewModal product_id={product.id} product={product} />}
                                />
                            ) : null}
                            <div className="reviews-title-card">{reviews_list.length} Reviews {Array.from({ length: getStarRating(revRating) }, (_, index) => (
                                <IoMdStar key={index} className="stars" />
                            ))}<span style={{ marginLeft: '6px', fontWeight: '100' }}></span></div>

                            <div className="review-container">
                                {/* {revArr.length ? revArr: <></>} */}
                                {reviews_list.length ? reviews_list.map((rev) => {
                                    return (<div className={`review`} key={rev.id}>
                                        <p>{Array.from({ length: getStarRating(rev.item_rating) }, (_, index) => (<IoMdStar key={index} className="stars" />))}</p>
                                        <div className="prod-description">{rev.description}</div>
                                        <div className="prod-item">Purchased item: {product?.name}</div>
                                        {rev.image?.length ? (
                                            <img src={rev.image[0].url} alt="image uploaded by user of the product received" className="review-image" />
                                        ) : null}
                                        <div className="rev-signature"><IoMdPerson /> {rev.user?.name} {rev.date}</div>
                                        {rev.user_id === user?.id ? (
                                            <div>
                                                <OpenModalButton
                                                buttonText="Delete"
                                                className='delete-button'
                                                modalComponent={<DeleteReviewModal review_id={rev.id} />}
                                                />
                                                <OpenModalButton
                                                buttonText="Update"
                                                className='delete-button'
                                                modalComponent={<UpdateReviewModal review_id={rev.id} review={rev} product={product}/>}
                                                />
                                            </div>
                                        ) : null}
                                    </div>)}) : <div>Be the first to post your review!</div>}
                            </div>
                        </div>
                        <div className="prod-details">
                            <p className="deets">Item Details</p>
                            <div className="item-details">{product?.description}</div>
                            <p></p>
                            <div className="prod-owner">Sold by: {product?.owner?.first_name}</div>
                        </div>
                    </div>
                </div>
            ) : null}
        </>
    );
}


export default ProductDetailsPage;
