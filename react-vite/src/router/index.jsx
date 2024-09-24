import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import MainPage from '../components/MainPage';
import ProductDetailsPage from '../components/ProductDetailsPage';

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
        element: <h1>Comming Soon</h1>
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
  // different nav
  {
    path: '/products/current',
    element: <h1>Coming Soon</h1>
  },
]);
