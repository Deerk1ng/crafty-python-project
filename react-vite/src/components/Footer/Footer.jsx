import { Link, NavLink } from 'react-router-dom';
import './Footer.css'
import { FaInstagram, FaPinterest, FaYoutube } from "react-icons/fa";
import { RiFacebookBoxFill } from "react-icons/ri";
import { BsTwitterX } from "react-icons/bs";

const Footer = () => {
    return (
        <footer className='footer'>
            <div className='left-ftr'>
                <Link to={'/'} ><img className='img-ftr' src='/logofornow.svg' alt='Crafty Logo'></img></Link>

            </div>
            <div className='right-ftr'>
                <ul>
                    <li className='footer-header'>
                        Shop
                    </li>
                    <li>
                        <Link to={'/'}>Gift Cards</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Crafty Registry</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Sitemap</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Crafty Blog</Link>
                    </li>
                </ul>
                <ul>
                    <li className='footer-header'>
                        Sell
                    </li>
                    <li>
                        <Link to={'/'}>Handbook</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Teams</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Forums</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Random Junk</Link>
                    </li>
                </ul>
                <ul>
                    <li className='footer-header'>
                        About
                    </li>
                    <li>
                        <Link to={'/'}>Crafty, Inc.</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Policies</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Investors</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Careers</Link>
                    </li>
                </ul>
                <ul>
                    <li className='footer-header'>
                        Help
                    </li>
                    <li>
                        <Link to={'/'}>Help Center</Link>
                    </li>
                    <li>
                        <Link to={'/'}>Privacy Settings</Link>
                    </li>
                    <ul className='social-media'>
                        <NavLink to={'https://www.instagram.com/'}><FaInstagram className='social'/></NavLink>
                        <NavLink to={'https://www.Facebook.com/'}><RiFacebookBoxFill className='social'/></NavLink>
                        <NavLink to={'https://www.pinterest.com/'}><FaPinterest className='social'/></NavLink>
                        <NavLink to={'https://www.x.com/'}><BsTwitterX className='social'/></NavLink>
                        <NavLink to={'https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran'}><FaYoutube className='social'/></NavLink>
                    </ul>
                </ul>
            </div>

        </footer>
    )
}


export default Footer;
