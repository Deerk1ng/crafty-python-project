import { useEffect, useRef, useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import "./LoginForm.css";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import SignupFormModal from "../SignupFormModal";
import { useModal } from "../../context/Modal";



function LogInFormModal() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const { closeModal } = useModal()


  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);


  if (sessionUser) return <Navigate to="/" replace={true} />;

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal()
      navigate("/");
    }
  };

  const DemoSignIn = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({ email: "demo@aa.io", password: "password" }))

      if (serverResponse) {
        setErrors(serverResponse);
      } else {
        closeModal()
        navigate("/");
      }
  }

  return (
    <div className="main-login">
    <div className="login-top">
      <h1>Sign In</h1>
      <button className="span-signup"><OpenModalMenuItem
        itemText="Sign Up"
        onItemClick={closeMenu}
        modalComponent={<SignupFormModal />}/></button>
    </div>
      {/* {errors.length > 0 &&
        errors.map((message) => <p key={message} className="errors">{message}</p>)} */}
      <form className='form-login' onSubmit={handleSubmit}>
        <div>
          Email
        </div>
        {errors.email && <span className="errors-msgs">{errors.email}</span>}
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        <div>
          Password
         </div>
         {errors.password && <span className="errors-msgs">{errors.password}</span>}
        <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

        <button type="submit" className="login-button">Log In</button>
        <button onClick={DemoSignIn} className="demo-button">Log in as Demo User</button>
      </form>
    </div>
  );
}

export default LogInFormModal;
