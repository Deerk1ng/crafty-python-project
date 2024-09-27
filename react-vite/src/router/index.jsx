import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import MainPage from '../components/MainPage';
import ShoppingCart from '../components/ShoppingCart';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <MainPage />,
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
        element: <ShoppingCart />,
      }
    ],
  },
  // different nav
  {
    path: '/products/current',
    element: <h1>Coming Soon</h1>
  },
]);
