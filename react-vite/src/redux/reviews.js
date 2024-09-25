import { csrfFetch } from "./csrf";

// Action types
const REVIEWS_BY_ID = 'reviews/allReviewsByProductId';
const ADD_REVIEW = 'reviews/createNewReview'
const DELETE_REVIEW = 'reviews/DeleteReview'

// Action creator for loading all products

const loadReviews = (reviews) => ({
    type: REVIEWS_BY_ID,
    reviews
});

const makeReview = (review) => ({
    type: ADD_REVIEW,
    review
})

const removeReview = (review_id) => ({
    type: DELETE_REVIEW,
    review_id
})

// Thunk to fetch all products
export const getReviews = (product_id) => async (dispatch) => {

    const res = await csrfFetch(`/api/products/${product_id}/reviews`);

    if (res.ok) {
        const data = await res.json();
        dispatch(loadReviews(data.reviews));
        return data;
    }
    return res.errors;
};

export const createReview = (el) => async (dispatch) => {
    const {item_rating, shipping_rating, description, product_id} = el

    const res = await csrfFetch(`/api/products/${product_id}/reviews`, {
        method: 'POST',
        body: JSON.stringify({
            item_rating,
            shipping_rating,
            description
        })
    })

    const data = await res.json()
    if(res.ok){
        const newRev = { ...data }
        dispatch(makeReview(newRev.created_review))
        return newRev
    }
    return data.errors
}

export const deleteReview = (review_id) => async (dispatch) => {
    const res = await csrfFetch(`/api/reviews/${review_id}`, {
        method: 'DELETE'
    })

    if(res.ok){
        dispatch(removeReview(review_id))
        return res
    }
}
// Initial state
const initialState = { ReviewsForCurrentProduct: {} };

// Reducer
function reviewsReducer(state = initialState, action) {
    switch (action.type) {
        case REVIEWS_BY_ID: {
            const ReviewsForCurrentProduct = {};
            action.reviews.forEach((review) => {
                ReviewsForCurrentProduct[review.id] = review;
            });
            return {
                ...state,
                ReviewsForCurrentProduct,
            };
        }
        case ADD_REVIEW: {
            const new_state = { ...state }
            new_state['ReviewsForCurrentProduct'][action.review.id] = action.review
            return new_state
        }
        case DELETE_REVIEW: {
            const new_state = {...state}
            delete new_state['ReviewsForCurrentProduct'][action.review_id]
            return new_state
        }
        default:
            return state;
    }
}

export default reviewsReducer;
