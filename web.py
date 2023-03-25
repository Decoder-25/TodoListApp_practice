import streamlit  as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title('To-Do App')
st.subheader('This to-do app will increase your productivity')

unique_value = 0
for todo in todos:
    unique_value += 1
    st.checkbox(todo, key=f"todo{unique_value}")

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

