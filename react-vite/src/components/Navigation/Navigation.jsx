import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import './Navigation.css'
import OpenModalMenuItem from "./OpenModalMenuItem";
import Categories from "../CategoriesModalPage";
import { useEffect, useState, ulRef } from "react";
import { RiMenu4Line } from "react-icons/ri";
import { MdFavoriteBorder } from "react-icons/md";
import { BsCart2 } from "react-icons/bs";
import { FaChevronRight } from "react-icons/fa";



function Navigation() {
  const [showMenu, setShowMenu] = useState(false);

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

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

  return (
    <ul className="Nav-bar">

      <li>
        <NavLink to="/"><img id='logo-img' src="/logofornow.svg" alt="Crafty Logo"></img></NavLink>
      </li>

      <li>
        <button className='categories-btn' onClick={toggleMenu}><RiMenu4Line /> Categories</button>
      </li>
        {showMenu && (
          <ul className={"categories-dropdown"} ref={ulRef}>
            <NavLink to={'comingsoon'}>Category1 </NavLink>
            <NavLink to={'comingsoon'}>Category2 </NavLink>
            <NavLink to={'comingsoon'}>Category3 </NavLink>
            <NavLink to={'comingsoon'}>Category4 </NavLink>
            <NavLink to={'comingsoon'}>Category5 </NavLink>
          </ul>
        )}

      <li>
        <input
        text="Text"
        placeholder="Search..."
        className="search-bar"
        ></input>
      </li>

      <li>
        <NavLink to={'/api/favorites/current'}><MdFavoriteBorder className='heart'/></NavLink>
      </li>

      <li>
        <ProfileButton />
      </li>
      <li>
        <NavLink to={'/api/shopping-cart/current'}><BsCart2 className="cart"/> </NavLink>
      </li>
    </ul>
  );
}

export default Navigation;
