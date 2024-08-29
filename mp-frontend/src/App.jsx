import Home from './pages/Home'
import Assistant from './pages/Assistant'
import Selection from './pages/Selection'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import VA from './pages/VA';
import Sample from './pages/Sample';
import Selection2 from './pages/VA';
import Payment from './pages/payment';


function App() {

  return (
    <>
      <div>
        <Router>
          <Routes>
            <Route path = '/' element = {<Home/>} />
            <Route path = '/assistant' element = {<Assistant/>} />
            <Route path = '/assistant/real/:id' element = {<Sample/>} />
            <Route path = '/assistant/:id' element = {<Selection2/>} />
            <Route path = '/assistant/payment' element = {<Payment/>} />


          </Routes>
        </Router>
      </div>
    </>
  )
}

export default App
