import { csrfFetch } from "./csrf";

// Action types
const SESSION_CART = 'session/shoppingCart';

// Action creator for loading all products
const getCart = (items) => ({
    type: SESSION_CART,
    payload: items
});

// Thunk to fetch cart
export const getCartThunk = () => async (dispatch) => {
    const res = await csrfFetch('/api/current');

    if (res.ok) {
        const data = await res.json();
        dispatch(loadProducts(data));
        return data;
    }
    return res;
};

// Initial state
const initialState = { cart: {} };

// Reducer
function productsReducer(state = initialState, action) {
    switch (action.type) {
        case ALL_PRODUCTS: {
            const allProducts = {};
            action.products.forEach((product) => {
                allProducts[product.id] = product;
            });
            return {
                ...state,
                allProducts,
            };
        }
        default:
            return state;
    }
}

export default productsReducer;
