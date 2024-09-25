import { csrfFetch } from "./csrf";

// Action types
const SESSION_CART = 'session/shoppingCart';
const GET_ITEMS = 'session/getItems'

// Action creator for getting cart
const getCart = (cart) => ({
    type: SESSION_CART,
    payload: cart
});

// Action creator for getting items
const getItems = (items) => ({
    type: GET_ITEMS,
    payload: items
})


// Thunk to fetch cart
export const getCartThunk = () => async (dispatch) => {
    const res = await csrfFetch('/api/shopping-cart/current');

    if (res.ok) {
        const data = await res.json();
        dispatch(getCart(data));
        return data.id; //return only the cart id
    }
    return res;
};

//Thunk to get items
export const getItemsThunk = (cart_id) => async (dispatch) => {
    const res = await csrfFetch(`/api/shopping-cart/current/${cart_id}`);

    if (res.ok) {
        const data = await res.json();
        dispatch(getItems(data));
        return data;
    }
    return res;
};

// Initial state
const initialState = { cart: {} };

// Reducer
function cartReducer(state = initialState, action) {
    let newState
    switch (action.type) {
        case SESSION_CART:
            newState = {...state}
            newState.shopping_cart = action.payload.shopping_cart
            return newState
        case GET_ITEMS:
            newState = {...state}
            newState.items = action.payload.shoppingCart.items
            return newState
        default:
            return state;
    }
}

export default cartReducer;
