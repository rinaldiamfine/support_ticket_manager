import "/app/globals.css";
import Navbar from "./Navbar";
import Footer from "./Footer";

export const InternalLayout = ({ children }: {children: React.ReactNode}) => {
    return (
        <div className="className">
            <Navbar></Navbar>
            { children }
            <Footer></Footer>
        </div>
    );
}