# API with Python and Flask

## CRUD Books

### Objective

Create an API that provides a CRUD (Create, Read, Update, Delete) functionality for books.

### Requirements

- Python 3.12
- Flask

### Usage

1. Run the application:
   ```sh
   python app.py
   ```

## Endpoints

### GET /books

- Description: Retrieve a list of all books.
- Example Response:

```json
  {
    "id": 1,
    "title": "Lord of the Ring: The Fellowship of the Ring",
    "author": "J.R.R. Tolkien"
  },
  {
    "id": 2,
    "title": "Lord of the Ring: The Two Towers",
    "author": "J.R.R. Tolkien"
  },
  {
    "id": 3,
    "title": "Lord of the Ring: The Return of the King",
    "author": "J.R.R. Tolkien"
  },
```

### GET /books/id

- Description: Retrieve a book by its ID.
- Example response:

```json
{
  "id": 1,
  "title": "Lord of the Ring: The Fellowship of the Ring",
  "author": "J.R.R. Tolkien"
}
```

### POST /books

- Description: Add a new book.
- Example request body:

```json
{
  "id": 5,
  "title": "Estas estórias",
  "author": "João Guimarães Rosa"
}
```

- Example response:

```json
{
    "id": 1,
    "title": "Lord of the Ring: The Fellowship of the Ring",
    "author": "J.R.R. Tolkien"
  },
  ...
  {
    "id": 5,
    "title": "Estas estórias",
    "author": "João Guimarães Rosa"
  }
```

### PUT /books

- Update a book by its ID
- Example request body:

```json
{
  "title": "The Fellowship of the Ring",
  "author": "J.R.R. Tolkien"
}
```

- Example response:

```json
{
  "id": 1,
  "title": "The Fellowship of the Ring",
  "author": "J.R.R. Tolkien"
}
```
### DELETE /books/
- Delete a book by its ID
- Example response:
```json
[
  {
    "id": 1,
    "title": "Lord of the Ring: The Fellowship of the Ring",
    "author": "J.R.R. Tolkien"
  },
  ...
]
```
## 🤝 Colaborador

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Teuuzim" title="Github do Matheus Henrique Vaz">
        <img src="https://avatars.githubusercontent.com/u/106777198?v=4" width="100px;" alt="Foto do Matheus Henrique Vaz no Github"/><br>
        <sub>
          <b>Matheus Henrique Vaz marques</b>
        </sub>
      </a>
    </td>
  </tr>
</table>