import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [first_name, setFirst_name] = useState("")
  const [last_name, setLast_name] = useState("")
  const [shop_name, setShop_name] = useState("")
  const [address, setAddress] = useState("")
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    console.log("First Nameeeeeee:", first_name);
    console.log("Last Nameeeeeeee:", last_name);
    console.log("Shop Nameeeeeeee:", shop_name);

    if (password !== confirmPassword) {
      return setErrors({
        confirmPassword:
          "Confirm Password field must be the same as the Password field",
      });
    }

    const serverResponse = await dispatch(
      thunkSignup({
        first_name,
        last_name,
        shop_name,
        address,
        email,
        username,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  return (
    <>
      <h1>Sign Up</h1>
      {errors.server && <p>{errors.server}</p>}
      <form onSubmit={handleSubmit}>
      <label>
      First Name
      <input
        type="text"
        value={first_name}
        onChange={(e) => setFirst_name(e.target.value)}
        required
      />
    </label>
    {errors.first_name && <p>{errors.first_name}</p>}

    <label>
      Last Name
      <input
        type="text"
        value={last_name}
        onChange={(e) => setLast_name(e.target.value)}
        required
      />
    </label>
    {errors.last_name && <p>{errors.last_name}</p>}

    <label>
      Shop Name
      <input
        type="text"
        value={shop_name}
        onChange={(e) => setShop_name(e.target.value)}
        required
      />
    </label>
    {errors.shop_name && <p>{errors.shop_name}</p>}

        <label>
            Address
          <input
            type="text"
            value={address}
            onChange={(e) => setAddress(e.target.value)}
            required
          />
        </label>
        {errors.address && <p>{errors.address}</p>}
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p>{errors.email}</p>}
        <label>
          Username
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        {errors.username && <p>{errors.username}</p>}
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p>{errors.password}</p>}
        <label>
          Confirm Password
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
        {errors.confirmPassword && <p>{errors.confirmPassword}</p>}
        <button type="submit">Sign Up</button>
      </form>
    </>
  );
}

export default SignupFormModal;
