import Input from "../layout/form/Input";
import SubmitButton from "../layout/form/SubmitButton";
import { useState } from "react";

export default function Register() {
  const [user, setUser] = useState([]);

  const handleChange = (e) => {
    setUser({ ...user, [e.target.name]: e.target.value });
  };
  const registerUser = (e) => {
    e.preventDefault();
    fetch("http://localhost:8000/users/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user),
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.log(error));
  };
  return (
    <form action="" method="POST" onSubmit={registerUser}>
      <Input
        text="Primeiro nome"
        type="text"
        name="first_name"
        placeholder="Primeiro nome"
        handleOnChange={handleChange}
      />
      <Input
        text="Último nome"
        type="text"
        name="last_name"
        placeholder="Último nome"
        handleOnChange={handleChange}
      />
      <Input
        text="E-mail"
        type="email"
        name="email"
        placeholder="E-mail"
        handleOnChange={handleChange}
      />
      <Input
        text="Usuário"
        type="text"
        name="username"
        placeholder="Usuário"
        handleOnChange={handleChange}
      />
      <Input
        text="Senha"
        type="password"
        name="password1"
        placeholder="Senha"
      />
      <Input
        text="Confirme a senha"
        name="password"
        type="password"
        placeholder="Confirme a senha"
        handleOnChange={handleChange}
      />
      <SubmitButton
        text="Registrar"
        className="btn btn-primary"
        handleOnChange={handleChange}
      />
    </form>
  );
}
