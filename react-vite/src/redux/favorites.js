import { csrfFetch } from "./csrf";

const ALL_FAVORITES = 'session/allFavorites';

// Action creator to load favorites
const loadFavorites = (payload) => ({
    type: ALL_FAVORITES,
    payload
});

// Thunk to fetch all favorites
export const getfavorites = () => async (dispatch) => {
    const res = await csrfFetch('/api/favorites/current');

    if (res.ok) {
        const data = await res.json();
        dispatch(loadFavorites(data));
        console.log('Favorites data:', data);
        return data;
    }
    return res;
};

// Initial state
const initialState = { allFavorites: [] };

// Reducer to handle favorites
function favoritesReducer(state = initialState, action) {
    switch (action.type) {
        case ALL_FAVORITES: {
            const allFavorites = {};
            action.payload.forEach((favorite) => {
                allFavorites[favorite.id] = favorite;
            });
            return {
                ...state,
                allFavorites,
            };
        }
        default:
            return state;
    }
}

export default favoritesReducer;
