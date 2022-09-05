import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
import Cart from './pages/Cart'
import Catalog from './pages/Catalog'
import Feed from './pages/Feed';

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/cart" element={<Cart />} />
        <Route path="/catalog" element={<Catalog />} />
        <Route path="/feed" element={<Feed />} />
      </Routes>
    </Router>
  )
}

export default AppRoutes;