import { csrfFetch } from "./csrf";

// Action types
const SESSION_CART = 'session/shoppingCart'
const GET_ITEMS = 'session/getItems'
const REMOVE_ITEM = 'cart/removeItem'
const ADD_QUANT = 'cart/item/add'
const SUB_QUANT = 'cart/item/sub'
const NEW_ITEM = 'cart/newItem'
const DELETE_CART = 'cart/delete'

// ACTION CREATORS
const getCart = (cart) => ({
    type: SESSION_CART,
    payload: cart
});

const getItems = (items) => ({
    type: GET_ITEMS,
    payload: items
})

const removeItem = (id) =>({
    type: REMOVE_ITEM,
    payload: id
})

const addQuant = (data) => ({
    type: ADD_QUANT,
    payload: data
})

const subQuant = (data) => ({
    type: SUB_QUANT,
    payload: data
})

const newItem = (data) => ({
    type: NEW_ITEM,
    payload: data
})

const deleteCart = (id) => ({
    type: DELETE_CART
})

/////////////////////////

//THUNKS
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

// Thunk to remove item
export const removeItemThunk = (item_id) => async (dispatch) => {
    const res = await csrfFetch(`/api/shopping-cart/delete/${item_id}`);

    if (res.ok) {
        dispatch(removeItem(item_id))
    } else {
        throw res
    }
}

// Thunk add to quantity
export const addQuantThunk = (item_id, quantity) => async(dispatch) => {
    const res = await csrfFetch(`/api/shipping-cart/add/${item_id}/${quantity}`)

    if(res.ok){
        const data = await res.json();
        dispatch(addQuant(data))
        return data;
    }
    return res;
}

//Thunk sub from quantity
export const subQuantThunk = (item_id, quantity) => async(dispatch) => {
    const res = await csrfFetch(`/api/shipping-cart/subtract/${item_id}/${quantity}`)

    if(res.ok){
        const data = await res.json();
        dispatch(subQuant(data))
        return data;
    }
    return res;
}


// Initial state
const initialState = {
    cart: {},
    items: {}
};

// Reducer
function cartReducer(state = initialState, action) {
    let newState
    switch (action.type) {
        case SESSION_CART:
            newState = {...state}
            newState.cart = action.payload.shopping_cart
            for (let item of action.payload.shopping_cart.items){
                newState.items[item.id] = item
            }
            return newState
        case GET_ITEMS:
            newState = {...state}
            newState.items = action.payload.cart.items
            return newState
        case REMOVE_ITEM:
            newState = {...state, items: {...state.items}}
            delete newState.items[action.payload]
            return newState
        case ADD_QUANT:
            newState = {...state}
            newState.items = action.payload
            return newState
        case SUB_QUANT:
            newState = {...state}
            newState.items = action.payload
            return newState
        default:
            return state;
    }
}

export default cartReducer;
