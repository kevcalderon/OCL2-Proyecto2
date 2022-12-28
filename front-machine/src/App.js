// import logo from "./logo.svg";
import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import "./App.css";

function App() {
  const [input, setInput] = useState(null);
  const [algorit, setAlgorit] = useState("");

  function analizar(e) {
    e.preventDefault();

    let p = {
      inputFile: input,
      algoritmo: algorit,
    };

    let requestPost = {
      method: "POST",
      headers: { "Content-Type": "multipart/form-data" },
      body: JSON.stringify(p),
    };

    const url = "http://127.0.0.1:5000/read";

    fetch(url, requestPost)
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((err) => console.log(err));
  }

  return (
    <div>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">PROYECTO 2</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <br></br>
      <Container>
        <Row>
          <Col>
            <h1>FORMULARIO</h1>
            <Card>
              <Card.Body>
                <Form>
                  <Form.Group>
                    <Form.Label>Escoge el algoritmo</Form.Label>
                    <Form.Select
                      aria-label="Default select example"
                      onChange={(e) => setAlgorit(e.target.value)}
                    >
                      <option>Open this select menu</option>
                      <option value="1">Regresión lineal</option>
                      <option value="2">Regresión polinomial</option>
                      <option value="3">Clasificador Gaussiano</option>
                      <option value="4">Redes neuronales</option>
                    </Form.Select>
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label>Parametros a evaluar</Form.Label>
                    <Form.Control type="text" placeholder="Parametro 1" />
                    <br></br>
                    <Form.Control type="text" placeholder="Parametro 2" />
                    <br></br>
                    <Form.Control type="text" placeholder="Parametro 3" />
                    <br></br>
                    <Form.Control type="text" placeholder="Parametro 4" />
                  </Form.Group>
                  <Form.Group controlId="formFile" className="mb-3">
                    <Form.Label>Archivo a analizar</Form.Label>
                    <Form.Control
                      type="file"
                      onChange={(e) => setInput(e.target.files[0])}
                    />
                  </Form.Group>
                  <Button variant="primary" type="button" onClick={analizar}>
                    Analizar
                  </Button>
                </Form>
              </Card.Body>
            </Card>
          </Col>
          <Col>2 of 2</Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
