import { csrfFetch } from "./csrf";

// Action types
const ADD_FAV = 'favorites/addFavorite'
const DELETE_FAV = 'favorites/deleteFavorite'

// Action creator for adding favorites
const addFavorite = (fav) => ({
    type: ADD_FAV,
    fav
})

const delFavorite = (product_id) => ({
    type: DELETE_FAV,
    product_id
})

//thunk to add favorite
export const createFavorite = (product_id) => async (dispatch) => {
    const res = await csrfFetch(`/api/products/${product_id}/favorites`, {
        method: 'POST',
        body: JSON.stringify({
        })
    })

    if(res.ok){
        const data = await res.json()
        dispatch(addFavorite(data.fav))
        return data
    }
    return res.errors
}

export const deleteFavorite = (fav_id, product_id) => async (dispatch) => {
    const res = await csrfFetch(`/api/favorites/${fav_id}`, {
        method: 'DELETE',
    })

    if(res.ok){
        const data = await res.json()
        dispatch(delFavorite(product_id))
        return data
    }
    return res
}

//Initial state
const initialState = { currentFavorites: {} };

function favoritesReducer(state = initialState, action){
    switch(action.type) {
        case ADD_FAV: {
            const new_state = structuredClone(state)
            console.log(action.fav)
            new_state['currentFavorites'][action.fav.product_id] = action.fav
            return new_state
        }
        case DELETE_FAV: {
            const new_state = structuredClone(state)
            console.log(action.product_id, new_state['currentFavorites'][action.product_id])
            delete new_state['currentFavorites'][action.product_id]
            return new_state
        }
        default:
            return state
    }
}

export default favoritesReducer
