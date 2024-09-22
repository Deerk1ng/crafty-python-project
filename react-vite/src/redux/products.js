import { csrfFetch } from "./csrf";

// Action types
const ALL_PRODUCTS = 'session/allProducts';

// Action creator for loading all products
const loadProducts = (products) => ({
    type: ALL_PRODUCTS,
    products
});

// Thunk to fetch all products
export const getProducts = () => async (dispatch) => {
    const res = await csrfFetch('/api/products');

    if (res.ok) {
        const data = await res.json();
        dispatch(loadProducts(data));
        return data;
    }
    return res;
};

// Initial state
const initialState = { allProducts: {} };

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
