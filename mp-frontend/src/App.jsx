import Home from './pages/Home'
import Assistant from './pages/Assistant'
import Selection from './pages/Selection'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';


function App() {

  return (
    <>
      <div>
        <Router>
          <Routes>
            <Route path = '/' element = {<Home/>} />
            <Route path = '/assistant' element = {<Assistant/>} />
            <Route path = '/assistant/:id' element = {<Selection/>} />
          </Routes>
        </Router>
      </div>
    </>
  )
}

export default App
