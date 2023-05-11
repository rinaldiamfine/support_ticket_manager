import "/app/globals.css";
import Navbar from "./Navbar";

export const InternalLayout = ({ children }: {children: React.ReactNode}) => {
    return (
        <div className="className">
            <Navbar></Navbar>
            { children }
            <div>Footer</div>
        </div>
    );
}