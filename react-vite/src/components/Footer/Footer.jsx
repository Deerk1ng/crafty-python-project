import { NavLink } from 'react-router-dom';
import './Footer.css'

const Footer = () => {
    return (
        <footer className='footer'>
            <div className='left-ftr'>
                <NavLink to={'/'} ><img className='img-ftr' src='/logofornow.svg' alt='Crafty Logo'></img></NavLink>

            </div>

        </footer>
    )
}


export default Footer;
