import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/pages/Login";
import Register from "./components/pages/Register";
import { Container } from "react-bootstrap";
import Home from "./components/pages/Home";
import Header from "./components/layout/Header";

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <Container>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/home" element={<Home />}/>
            <Route path="/register" element={<Register />} />
          </Routes>
        </Container>
      </Router>
      {/* <header className="App-header">
        <img src="" className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </div>
  );
}

export default App;
