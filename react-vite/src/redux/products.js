import { csrfFetch } from "./csrf";

// Action types
const ALL_PRODUCTS = 'products/allProducts';
const ONE_PRODUCT = "products/oneProduct"
const ADD_PRODUCT = 'session/ADDPRODUCT';
const ALL_USER_PRODUCTS = 'session/allUserProducts';


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
        console.log(data);  // Check what the response looks like in the console
        dispatch(loadUserProducts(data));  // Dispatch user-specific products action
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
    console.log('wwwwwwww',created_product)

    // If product.images is an array, handle multiple images

        for (const imageUrl of product.images) {
            let image = {
                url: imageUrl,
                preview: true,
                product_id: created_product.id
            };
            console.log("image    ",image)
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


    // dispatch(addProduct(created_product));
    return created_product;
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
                allGroups: {
                    ...state.allProducts,
                    [newProduct.id]: newProduct
                }
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
                allGroups: {
                    ...state.allProducts,
                    [newProduct.id]: newProduct
                }
            };
        }
        default:
            return state;
    }
}

export default productsReducer;
