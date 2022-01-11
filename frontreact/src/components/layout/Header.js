import { Container } from "react-bootstrap";
import styles from "./Header.module.css";
export default function Header() {
  return (
    <>
      <header className={styles.header + " bg-dark"}>
        <Container>
          <nav className="navbar navbar-expand-lg navbar-dark">
            <collapse className="navbar-collapse" id="collapse">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <a href="" className="nav-link">
                    Home
                  </a>
                </li>
              </ul>
            </collapse>
          </nav>
        </Container>
      </header>
    </>
  );
}
