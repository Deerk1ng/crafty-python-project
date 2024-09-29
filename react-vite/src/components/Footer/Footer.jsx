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
                        Jan Lim
                    </li>
                    <li>
                        <Link to={'https://github.com/janblim'}>GitHub</Link>
                    </li>
                    <li>
                        <Link to={'https://www.linkedin.com/in/jan-lim-60859b32/'}>LinkedIn</Link>
                    </li>
                </ul>
                <ul>
                    <li className='footer-header'>
                        Hayden Ruiz
                    </li>
                    <li>
                        <Link to={'https://github.com/Deerk1ng'}>GitHub</Link>
                    </li>
                    <li>
                        <Link to={'https://www.linkedin.com/in/haydenr1111'}>LinkedIn</Link>
                    </li>
                </ul>
                <ul>
                    <li className='footer-header'>
                        Alex Carl
                    </li>
                    <li>
                        <Link to={'https://github.com/AlexJc23'}>GitHub</Link>
                    </li>
                    <li>
                        <Link to={'https://www.linkedin.com/in/alex-carl-bb79811b8/'}>LinkedIn</Link>
                    </li>
                    <li>
                        <Link to={'https://www.instagram.com/alx_graphix/'}>Instagram</Link>
                    </li>
                </ul>
                <ul>
                
                    <ul className='social-media'>
                        <NavLink to={'https://www.instagram.com/appacademyio/'}><FaInstagram className='social'/></NavLink>
                        <NavLink to={'https://www.facebook.com/appacademyio'}><RiFacebookBoxFill className='social'/></NavLink>
                        <NavLink to={'https://x.com/appacademyio'}><BsTwitterX className='social'/></NavLink>
                        <NavLink to={'https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran'}><FaYoutube className='social'/></NavLink>
                    </ul>
                </ul>
            </div>

        </footer>
    )
}


export default Footer;
