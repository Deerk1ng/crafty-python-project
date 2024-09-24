import { csrfFetch } from "./csrf";

// Action types
const REVIEWS_BY_ID = 'session/allReviewsByProductId';

// Action creator for loading all products
const loadReviews = (reviews) => ({
    type: REVIEWS_BY_ID,
    reviews
});

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
        default:
            return state;
    }
}

export default reviewsReducer;
