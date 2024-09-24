import { csrfFetch } from "./csrf";

// Action types
const ALL_PRODUCTS = 'session/allProducts';
// const ADD_PRODUCT = 'session/ADDPRODUCT';
const ALL_USER_PRODUCTS = 'session/allUserProducts';


// Action creator for loading all products
const loadProducts = (products) => ({
    type: ALL_PRODUCTS,
    products
});
const loadUserProducts = (products) => ({
    type: ALL_USER_PRODUCTS,
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

export const getUserProducts = () => async (dispatch) => {
    const res = await csrfFetch('/api/products/current');

    if (res.ok) {
        const data = await res.json();
        console.log(data);  // Check what the response looks like in the console
        dispatch(loadUserProducts(data));  // Dispatch user-specific products action
        return data;
    }
    return res;
};



// Initial state
const initialState = { allProducts: {}, userProducts: {} };

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
        case ALL_USER_PRODUCTS: {
            const userProducts = {};
            action.products.forEach((product) => {
                userProducts[product.id] = product;
            });
            return {
                ...state,
                userProducts,
            };
        }
        default:
            return state;
    }
}

export default productsReducer;
