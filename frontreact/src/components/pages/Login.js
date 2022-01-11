import styles from "./Login.module.css";
import Input from "../layout/form/Input";
import SubmitButton from "../layout/form/SubmitButton";
import { useState } from "react";
export default function Login() {
    const [user, setUser] = useState([])
    const handleChange = (e) => {
        setUser({...user, [e.target.name]:e.target.value})
    }
    const login = (e) => {
        e.preventDefault();
        fetch("http://localhost:8000/api/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(user),
        })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.log(error));
        }
    
  return (
    <>
      <div className={styles.content}>
        <div className={styles.form}>
          <form action="" method="POST" onSubmit={login}>
            <div className={styles.padding + " row"}>
              <div className="col-4">
                  Welcome
              </div>
              <div className="col-8">
                  <h4>Login</h4>
                  <Input text="Usuário" name="username" type="text" handleOnChange={handleChange} minlenght="8" placeholder="Usuário"/>
                  <Input text="Senha" name="password" type="password" handleOnChange={handleChange} minlenght="6" placeholder="Senha"/>
                  <SubmitButton text="Entrar" className="btn btn-primary"/>
                  <a href="">Não possuo conta</a>
              </div>
            </div>
          </form>
        </div>
      </div>
    </>
  );
}
