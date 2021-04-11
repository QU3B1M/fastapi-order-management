import React, { Component, useState } from "react";
import axios from "axios";
import { API_BASE_URL, ACCESS_TOKEN_NAME } from "../../constants/apiConstants";
import { withRouter } from "react-router-dom";
import "../../styles/register.css";

class RegistrationForm extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: "",
      username: "",
      password: "",
    };
  }

  handleChange = (e) => {
    const { id, value } = e.target;
    this.setState((prevState) => ({
      ...prevState,
      [id]: value,
    }));
  };

  handleSubmitClick = (e) => {
    e.preventDefault();
    if (this.state.password === this.state.confirmPassword) {
      this.sendDetailsToServer();
    } else {
      this.props.showError("Passwords do not match");
    }
  };

  sendDetailsToServer = () => {
    if (this.state.email.length && this.state.password.length) {
      this.props.showError(null);
      const payload = {
        username: this.state.username,
        email: this.state.email,
        password: this.state.password,
      };

      axios
        .post(API_BASE_URL + "/user/register", payload)
        .then(function (response) {
          if (response.status === 200) {
            this.setState((prevState) => ({
              ...prevState,
              successMessage:
                "Registration successful. Redirecting to home page.",
            }));
            // redirectToHome();
            this.props.showError(null);
          } else {
            this.props.showError("Some error ocurred.");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    } else {
      this.props.showError("Please enter valid username and password.");
    }
  };

  render() {
    return (
      <div id="login-box" className="login-box">
        <div className="container ">
          <form>
            <h3 className="text-center text-info">Register</h3>
            <br></br>
            <div className="form-group">
              <label htmlFor="username" className="text-info">
                Username
              </label>
              <input
                type="text"
                className="form-control"
                id="username"
                placeholder="Enter username"
                value={this.state.username || ""}
                onChange={this.handleChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="exampleInputEmail1" className="text-info">
                Email
              </label>
              <input
                type="email"
                className="form-control"
                id="email"
                aria-describedby="emailHelp"
                placeholder="Enter email"
                value={this.state.email || ""}
                onChange={this.handleChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="exampleInputPassword1" className="text-info">
                Password
              </label>
              <input
                type="password"
                className="form-control"
                id="password"
                placeholder="Password"
                value={this.state.password || ""}
                onChange={this.handleChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="exampleInputPassword1" className="text-info">
                Confirm Password
              </label>
              <input
                type="password"
                className="form-control"
                id="confirmPassword"
                placeholder="Confirm Password"
                value={this.state.confirmPassword || ""}
                onChange={this.handleChange}
              />
            </div>

            <button
              type="submit"
              className="btn btn-dark btn-lg btn-block"
              onClick={this.handleSubmitClick}
            >
              Register
            </button>
            <p className="forgot-password text-right">
              Already registered <a href="#">log in?</a>
            </p>
          </form>
          <div
            className="alert alert-success mt-2"
            style={{ display: this.state.successMessage ? "block" : "none" }}
            role="alert"
          >
            {this.state.successMessage}
          </div>
        </div>
      </div>
    );
  }
}
export default withRouter(RegistrationForm);
