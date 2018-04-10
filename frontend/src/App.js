import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    todos: []
  };
  
  // asynchronously fetch the todo items from the backend endpoint
  // set state of todos using setstate api
  // catch any exceptions 
  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/todos/');
      const todos = await res.json();
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }
  // display the title of the todo as a heading and the description
  render() {  
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
    );
  }

  
}

export default App;
