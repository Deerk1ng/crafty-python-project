import { csrfFetch } from "./csrf";

// Action types
const ALL_PRODUCTS = 'products/allProducts';
const ONE_PRODUCT = "products/oneProduct"
const ADD_PRODUCT = 'session/ADDPRODUCT';
const ALL_USER_PRODUCTS = 'session/allUserProducts';

const UPDATE_PRODUCT = 'session/updateProduct'



// Action creator for loading all products
const loadProducts = (products) => ({
    type: ALL_PRODUCTS,
    products
});

const loadOneProduct = (product) => ({
    type: ONE_PRODUCT,
    product
});

// load current Users listings
const loadUserProducts = (products) => ({
    type: ALL_USER_PRODUCTS,
    products
});

// add a product action creator
const addProduct = (payload) => ({
    type: ADD_PRODUCT,
    payload
});


const updateAProduct = (product) => ({
    type: UPDATE_PRODUCT,
    product,
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

export const getUserProducts = () => async (dispatch) => {
    const res = await csrfFetch('/api/products/current');

    if (res.ok) {
        const data = await res.json();
        console.log(data);
        dispatch(loadUserProducts(data));
        return data;
    }
    return res;
};

// create product thunk
export const createProduct = (product) => async (dispatch) => {
    let res;
    let newProduct = {
        owner_id: product.owner_id,
        name: product.name,
        price: product.price,
        description: product.description,
        category: product.category
    }

    try {
        res = await csrfFetch('/api/products', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(newProduct)
        });
    } catch (error) {
        return error.json();
    }

    const data = await res.json();

    const {created_product} = data;




        for (const imageUrl of product.images) {
            let image = {
                url: imageUrl,
                preview: true,
                product_id: created_product.id
            };

            try {
                await csrfFetch(`/api/products/${created_product.id}/images`, {
                    method: 'POST',
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(image)
                });
            } catch (error) {
                return await error.json();
            }
        }


    dispatch(addProduct(created_product));
    return created_product;
};

// edit product details
export const updateProductDetails = (product, product_id) => async (dispatch) => {
    let res;
    console.log(product.category)

    let updateProduct = {
        name: product.name,
        price: product.price,
        description: product.description,
        category: product.category
    };

    try {
        console.log(product_id)
        res = await csrfFetch(`/api/products/${product_id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updateProduct)
        });
    } catch (error) {
        return await error.json();
    }

    if (res.ok) {
        const updatedProduct = await res.json();
        dispatch(updateAProduct(updatedProduct));
        return updatedProduct;
    } else {
        return res
    }
};




// Initial state
const initialState = { allProducts: {}, currProduct: {}, userProducts: {} };

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
        case ADD_PRODUCT: {
            const newProduct = action.payload;
            return {
                ...state,
                allProducts: {
                    ...state.allProducts,
                    [newProduct.id]: newProduct
                }
            };
        }
        case UPDATE_PRODUCT: {
            const updatedProduct = action.product;
            return {
                ...state,
                allProducts: {
                    ...state.allProducts,
                    [updatedProduct.id]: updatedProduct
                },
                currProduct: updatedProduct,  // Update current product if necessary
            };
        }
        default:
            return state;
    }
}

export default productsReducer;
