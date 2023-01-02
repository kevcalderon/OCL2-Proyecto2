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
import Table from "react-bootstrap/Table";
import "./App.css";

function App() {
  const [input, setInput] = useState(null);
  const [algorit, setAlgorit] = useState("");
  const [inputParam1, setInputParams1] = useState("");
  const [inputParam2, setInputParams2] = useState("");
  const [inputPredi, setInputPredi] = useState("");
  const [fine, setIsFine] = useState(false);
  const [data1, setData1] = useState();
  const [imgDraw, setImgDraw] = useState("");
  const url = "http://127.0.0.1:5000/read";
  const url2 = "http://127.0.0.1:5000/graph";

  const analizar = async (e) => {
    e.preventDefault();

    let p = {
      inputFile: input,
      algoritmo: algorit,
      param1: inputParam1,
      param2: inputParam2,
      predi: inputPredi,
    };

    let requestPost = {
      method: "POST",
      headers: { "Content-Type": "multipart/form-data" },
      body: JSON.stringify(p),
    };

    await fetch(url, requestPost)
      .then((response) => response.json())
      .then((data) => {
        setData1(data);
        console.log(data);
        if (data.graph === "true") {
          graph();
        } else {
          setImgDraw("");
        }

        setIsFine(true);
      })
      .catch((err) => setIsFine(false));
  };

  async function graph() {
    try {
      const response = await fetch(url2).catch();
      const respoData = await response.blob();
      const imageObjectUrl = URL.createObjectURL(respoData);
      setImgDraw(imageObjectUrl);
    } catch (e) {
      alert("Error al generar imagen.");
    }
  }

  function handleFileChange(e) {
    e.preventDefault();
    let readFile = e.target.files[0];
    let reader = new FileReader();
    reader.onload = function (ev) {
      setInput(ev.target.result);
    };
    reader.readAsText(readFile);
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
                      <option>Selecciona una opción</option>
                      <option value="1">Regresión lineal</option>
                      <option value="2">Regresión polinomial</option>
                      <option value="3">Clasificador Gaussiano</option>
                      <option value="4">
                        Clasificador de árboles de decisión
                      </option>
                      <option value="5">Redes neuronales</option>
                    </Form.Select>
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label>Parametros a evaluar</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="Parametro 1"
                      onChange={(e) => setInputParams1(e.target.value)}
                    />
                    <br></br>
                    <Form.Control
                      type="text"
                      placeholder="Parametro 2"
                      onChange={(e) => setInputParams2(e.target.value)}
                    />
                    <br></br>
                    <Form.Label>Parametro de predicción</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="Escribe el dato a predecir"
                      onChange={(e) => setInputPredi(e.target.value)}
                    />
                  </Form.Group>
                  <Form.Group controlId="formFile" className="mb-3">
                    <Form.Label>Archivo a analizar</Form.Label>
                    <Form.Control
                      type="file"
                      onChange={(e) => handleFileChange(e)}
                    />
                  </Form.Group>
                  <Button variant="primary" type="button" onClick={analizar}>
                    Analizar
                  </Button>
                </Form>
              </Card.Body>
            </Card>
          </Col>
          <Col>
            <h1>TABLA DE RESULTADOS</h1>
            {fine === true ? (
              <div>
                <Table striped bordered hover>
                  <thead>
                    <tr>
                      <th>Propiedad</th>
                      <th>Valor</th>
                    </tr>
                  </thead>
                  <tbody>
                    {Object.keys(data1).map((key) => {
                      return (
                        <tr key={key}>
                          <td>{key}</td>
                          <td>{data1[key]}</td>
                        </tr>
                      );
                    })}
                  </tbody>
                </Table>
                {imgDraw === "" ? (
                  <div align="center">
                    <h5>Algoritmo no aplica generación de gráfica.</h5>
                  </div>
                ) : (
                  <div align="center">
                    <img src={imgDraw} width="80%" height="80%" alt="success" />
                  </div>
                )}
              </div>
            ) : (
              <div align="center">
                <img
                  src="https://img.freepik.com/vector-gratis/trabajador-dudas_1012-193.jpg"
                  width="50%"
                  height="50%"
                  alt="start_image"
                />
              </div>
            )}
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
