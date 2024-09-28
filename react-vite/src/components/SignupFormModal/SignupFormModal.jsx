
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [shopName, setShopName] = useState("");
  const [address, setAddress] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const validateData = () => {
    const err ={}
    if(firstName.length < 2) err["first_name"] = "First name must be longer than 2 characters"
    if(firstName.length > 50) err["first_name"] = "First name must be less than 150 characters"
    if(lastName.length < 2) err["last_name"] = "Last name must be longer than 2 characters"
    if(lastName.length > 50) err["last_name"] = "Last name must be less than 150 characters"
    if(shopName.length < 2) err["shop_name"] = "Shop name must be longer than 2 characters"
    if(shopName.length > 50) err["shop_name"] = "Shop name must be less than 150 characters"
    if(address.length < 2) err["address"] = "Address must be longer than 2 characters"
    if(email.length == 0) err["email"] = "Email is required"
    if(!(email.endsWith('.com') || email.endsWith('.net') || email.endsWith('.org') || email.endsWith('.io') || email.includes('@'))) err["email"] = "must be a valid email"
    if(username.length < 5) err["username"] = "Username must be longer than 5 characters"
    if(username.length > 50) err["username"] = "Username must be less than 150 characters"
    if(password.length < 5) err["password"] = "Password must be longer than 5 characters"
    if(password.length > 50) err["password"] = "Password must be less than 150 characters"
    if(confirmPassword != password) err['confirmPassword'] = "Password and Confirm Password must match"
    setErrors(err)
    if(Object.values(err).length){
        return false
    } else return true
  }



  const handleSubmit = async (e) => {
    e.preventDefault();


    if (validateData()) {

      const serverResponse = await dispatch(
        thunkSignup({
          first_name: firstName,
          last_name: lastName,
          shop_name: shopName,
          address: address,
          email: email,
          username: username,
          password: password,
        })
      );

      if (serverResponse) {
        setErrors(...errors, ...serverResponse);
      } else {
        closeModal();
      }
    };
  }

  return (
    <>
      <h1>Sign Up</h1>
      {errors.server && <p className='error'>{errors.server}</p>}
      <form onSubmit={handleSubmit}>
        <label>
          First Name
          <input
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </label>
        {errors.first_name && <p className='error'>{errors.first_name}</p>}

        <label>
          Last Name
          <input
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </label>
        {errors.last_name && <p className='error'>{errors.last_name}</p>}

        <label>
          Shop Name
          <input
            type="text"
            value={shopName}
            onChange={(e) => setShopName(e.target.value)}
            required
          />
        </label>
        {errors.shop_name && <p className='error'>{errors.shop_name}</p>}

        <label>
          Address
          <input
            type="text"
            value={address}
            onChange={(e) => setAddress(e.target.value)}
            required
          />
        </label>
        {errors.address && <p className='error'>{errors.address}</p>}

        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p className='error'>{errors.email}</p>}

        <label>
          Username
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        {errors.username && <p className='error'>{errors.username}</p>}

        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p className='error'>{errors.password}</p>}

        <label>
          Confirm Password
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
        {errors.confirmPassword && <p className='error'>{errors.confirmPassword}</p>}

        <button type="submit">Sign Up</button>
      </form>
    </>
  );
}

export default SignupFormModal;
