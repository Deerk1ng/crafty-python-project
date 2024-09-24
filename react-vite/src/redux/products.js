import { csrfFetch } from "./csrf";

// Action types
const ALL_PRODUCTS = 'products/allProducts';
const ONE_PRODUCT = "products/oneProduct"

// Action creator for loading all products
const loadProducts = (products) => ({
    type: ALL_PRODUCTS,
    products
});

const loadOneProduct = (product) => ({
    type: ONE_PRODUCT,
    product
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

export const getOneProduct = (product_id) => async (dispatch) => {
    const res = await csrfFetch(`/api/products/${product_id}`);

    if (res.ok) {
        const data = await res.json();
        dispatch(loadOneProduct(data.product));
        return data;
    }
    return res;
};

// Initial state
const initialState = { allProducts: {}, currProduct: {} };

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
        } case ONE_PRODUCT: {
            const currProduct = action.product
            return {
                ...state,
                currProduct,
            };
        }
        default:
            return state;
    }
}

export default productsReducer;
