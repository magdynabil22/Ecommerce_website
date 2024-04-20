import "./App.css";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Login from "./Login/Login";
import RegisterPage from "./Pages/RegisterPage";
import HomePage from "./Pages/HomePage";
import ProfilePage from "./Pages/ProfilePage";
import ShopPage from "./Pages/ShopPage";
import RegisterationType from "./Pages/RegisterationType";
import SellerRegisteration from "./Pages/SellerRegisteration";
import OrderHistory from "./Pages/OrderHistory";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<HomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/registerationtype" element={<RegisterationType/>}/>
        <Route path="/signupbuyer" element={<RegisterPage />} />
        <Route path="/signup" element={<RegisterPage />} />   
        <Route path="/signupseller" element={<SellerRegisteration />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="*" element={<Login />} />
        <Route path="/account" element={<ProfilePage />} />{" "}
        {/*should be account+id and should be if logged in*/}
        <Route path="/shop" element={<ShopPage />} />
        <Route path="/orderhistory" element={<OrderHistory/>}/> {/*should be orderhistory+accountid*/}
       
      </Routes>
    </BrowserRouter>
  );
}

export default App;
