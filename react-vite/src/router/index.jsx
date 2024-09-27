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
        element: <h1>Coming Soon</h1>
      },
      {
        path: '/shopping-cart/current',
        element: <h1>Coming Soon</h1>
      },
      {
        path: 'products',
        children: [
          {
            path: ':product_id',
            element: <ProductDetailsPage />
          }
        ]
      }
    ],
  },
  {
    path: '/products/current',
    element: <UserListings  />
  },
  {
    path: '/products/new',
    element: <CreateProduct />
  },
  {
    path: '/products/:product_id/edit',
    element: <EditProduct />
  }
]);
