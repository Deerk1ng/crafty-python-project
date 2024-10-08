import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import MainPage from '../components/MainPage';
import ProductDetailsPage from '../components/ProductDetailsPage';
import UserListings from '../components/UserListings/UserListings';
import CreateProduct from '../components/CreateProduct/CreateProduct';
import EditProduct from '../components/EditProduct';
import ShoppingCart from '../components/ShoppingCart';
import Favorites from '../components/Favorites/Favorites';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <MainPage />
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: '/favorites/current',
        element: <Favorites />
      },
      {
        path: '/shopping-cart/current',
        element: <ShoppingCart />
      },
      {
        path: 'products',
        children: [
          {
            path: ':product_id',
            element: <ProductDetailsPage />
          },
          {
            path: 'current',
            element: <UserListings  />
          },
          {
            path: 'new',
            element: <CreateProduct />
          },
          {
            path: ':product_id/edit',
            element: <EditProduct />
          },
        ]
      }
    ],
  },
  {
    path: '/shopping-cart/checkout',
    element: <h1>Coming Soon</h1>
  }
]);
