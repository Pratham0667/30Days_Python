# Day 28 - API & HTTP

# 🎯 Topics Covered

- Introduction to APIs
- Web APIs
- RESTful APIs
- API Endpoints
- Building APIs
- HTTP
- Client-Server Model
- HTTP Request and Response
- HTTP Message Structure
- Request Line
- Response Status Line
- HTTP Headers
- HTTP Message Body
- HTTP Request Methods
- GET
- POST
- PUT
- DELETE
- CRUD Operations
- API and Database Communication

---

# 📚 Introduction

**API** stands for **Application Programming Interface**.

An API provides a defined way for different software applications to communicate with each other.

In web development, a **Web API** provides an interface through which applications can request and exchange data using HTTP.

API responses are commonly returned in formats such as:

- JSON
- XML

Modern web APIs commonly use **REST (Representational State Transfer)** principles.

---

# 1. What is an API?

An API acts as a communication interface between different applications.

For example:

```text
Client Application
       │
       │ API Request
       ▼
     Web API
       │
       │
       ▼
     Server
       │
       ▼
     Database
       │
       │ API Response
       ▼
Client Application
```

Instead of directly accessing another application's internal system, a client communicates through the API provided by the application.

---

# 2. Web APIs

A **Web API** is an API that communicates over the web using HTTP.

Web APIs allow applications and services to exchange:

- Data
- Resources
- Information
- Commands

For example, an application can request information from a server through an API endpoint and receive the result as JSON.

---

# 3. API Endpoint

An **API endpoint** is a URL through which a client can access a particular resource or service.

Example:

```text
https://example.com/api/students
```

The endpoint identifies the resource that the client wants to interact with.

---

# 4. RESTful API

A **RESTful API** is an API that follows REST principles and uses HTTP methods to perform operations on resources.

The major HTTP methods used for CRUD operations are:

| HTTP Method | CRUD Operation | Purpose |
|-------------|-----------------|---------|
| GET | Read | Retrieve data |
| POST | Create | Create new data |
| PUT | Update | Update existing data |
| DELETE | Delete | Remove data |

---

# 5. API and CRUD

APIs are commonly used to perform **CRUD** operations.

CRUD stands for:

```text
C → Create
R → Read
U → Update
D → Delete
```

These operations can be mapped to HTTP methods:

```text
CREATE → POST
READ   → GET
UPDATE → PUT
DELETE → DELETE
```

---

# 6. Building an API

A RESTful API can be built using technologies such as:

```text
Python
   │
   ▼
Flask
   │
   ▼
REST API
   │
   ▼
MongoDB
```

The previous lessons introduced:

- Python
- Flask
- MongoDB

These technologies can be combined to build a RESTful API that performs CRUD operations on database data.

---

# 7. HTTP

**HTTP** stands for:

**Hypertext Transfer Protocol**

HTTP is a communication protocol used between clients and servers.

A web browser acts as an HTTP client.

The server receives the request and sends an HTTP response.

---

# 8. Client-Server Model

HTTP follows the **client-server model**.

```text
Client
  │
  │ HTTP Request
  ▼
Server
  │
  │ HTTP Response
  ▼
Client
```

### Client

The client is usually an application such as:

- Web browser
- Mobile application
- Desktop application
- API client

### Server

The server processes the request and returns the requested resource or result.

---

# 9. HTTP Request-Response Cycle

The basic HTTP communication process is:

```text
1. Client sends request
          │
          ▼
2. Server receives request
          │
          ▼
3. Server processes request
          │
          ▼
4. Server sends response
          │
          ▼
5. Client receives response
```

This is known as the **HTTP request-response cycle**.

---

# 10. Structure of HTTP Messages

HTTP requests and responses have a similar structure.

They contain:

```text
Initial Line
     │
     ▼
Header Fields
     │
     ▼
Blank Line
     │
     ▼
Optional Message Body
```

The main components are:

- Initial line
- Header fields
- Blank line
- Optional message body

---

# 11. HTTP Request

An HTTP request is sent from the client to the server.

Example:

```http
GET / HTTP/1.1
Host: example.com
```

The request contains information about:

- HTTP method
- Requested resource
- HTTP version
- Headers
- Optional body

---

# 12. Request Line

The initial line of an HTTP request is called the **request line**.

It contains three main parts:

```text
METHOD PATH HTTP-VERSION
```

Example:

```http
GET / HTTP/1.1
```

Here:

```text
GET       → Request method
/         → Requested path
HTTP/1.1  → HTTP version
```

---

# 13. HTTP Response

After receiving a request, the server sends an HTTP response.

Example:

```http
HTTP/1.1 200 OK
```

The response contains:

- HTTP version
- Status code
- Reason phrase
- Headers
- Optional message body

---

# 14. Response Status Line

The first line of an HTTP response is called the **status line**.

Example:

```http
HTTP/1.1 200 OK
```

It contains:

```text
HTTP Version
     │
     ▼
Status Code
     │
     ▼
Reason Phrase
```

---

# 15. HTTP Status Codes

HTTP status codes indicate the result of a request.

### 200 OK

```text
200 OK
```

The request was successful.

---

### 404 Not Found

```text
404 Not Found
```

The requested resource could not be found.

For example, accessing a URL for which the server has no defined resource or route can result in a 404 response.

---

### 500 Server Error

```text
500 Internal Server Error
```

The server encountered an unexpected problem while processing the request.

---

# 16. HTTP Headers

Headers provide additional information about an HTTP request or response.

Example:

```http
GET / HTTP/1.1
Host: example.com
Connection: keep-alive
Cache-Control: no-cache
User-Agent: Mozilla/5.0
```

Common headers include:

| Header | Purpose |
|--------|---------|
| `Host` | Specifies the server being requested |
| `User-Agent` | Identifies the client software |
| `Content-Type` | Describes the type of data |
| `Content-Length` | Specifies the size of the message body |
| `Cache-Control` | Controls caching behavior |
| `Accept` | Specifies acceptable response formats |

---

# 17. HTTP Message Body

An HTTP message may contain a **message body**.

The body can contain:

- HTML
- JSON
- Text
- Images
- Uploaded files
- Query data
- Other resources

For example, an API may return JSON in the response body:

```json
{
    "name": "Anvesha",
    "country": "India",
    "city": "Mangalore"
}
```

---

# 18. Content-Type

The `Content-Type` header describes the type of data contained in the message body.

Examples:

```text
text/html
```

HTML content.

```text
application/json
```

JSON data.

```text
text/plain
```

Plain text.

```text
image/gif
```

GIF image data.

---

# 19. GET Method

The **GET** method is used to retrieve data from a server.

Example:

```http
GET /students HTTP/1.1
```

Typical use:

```text
GET → Read data
```

For example:

```text
GET /students
```

could retrieve a list of students.

---

# 20. POST Method

The **POST** method is used to send data to a server and create a new resource.

Example:

```http
POST /students
```

The request body could contain:

```json
{
    "name": "Anvesha",
    "age": 20
}
```

Typical use:

```text
POST → Create data
```

---

# 21. PUT Method

The **PUT** method is used to update or replace an existing resource.

Example:

```http
PUT /students/1
```

Typical use:

```text
PUT → Update data
```

---

# 22. DELETE Method

The **DELETE** method is used to remove data from a server.

Example:

```http
DELETE /students/1
```

Typical use:

```text
DELETE → Remove data
```

---

# 23. HTTP Methods and CRUD

The relationship between HTTP methods and CRUD operations can be summarized as:

```text
             CRUD
              │
     ┌────────┼────────┐
     │        │        │
   CREATE    READ    UPDATE    DELETE
     │        │        │        │
    POST     GET      PUT     DELETE
```

| Operation | HTTP Method | Example |
|-----------|-------------|---------|
| Create | POST | `/students` |
| Read | GET | `/students` |
| Update | PUT | `/students/1` |
| Delete | DELETE | `/students/1` |

---

# 📊 API Request-Response Workflow

```text
        CLIENT
          │
          │ HTTP Request
          │
          ▼
       API SERVER
          │
          │ Process Request
          ▼
       DATABASE
          │
          │ Data
          ▼
       API SERVER
          │
          │ HTTP Response
          ▼
        CLIENT
```

---

# 📌 API vs HTTP

| API | HTTP |
|-----|------|
| Interface for communication | Communication protocol |
| Defines how applications interact | Defines how web requests/responses work |
| Can use HTTP in Web APIs | Used for communication over the web |
| Provides endpoints and operations | Provides methods, headers and status codes |

---

# 📌 Important Terms

| Term | Meaning |
|------|---------|
| API | Application Programming Interface |
| Web API | API accessed through the web |
| REST | Representational State Transfer |
| HTTP | Hypertext Transfer Protocol |
| Endpoint | URL through which an API resource is accessed |
| Client | Application making a request |
| Server | System processing the request |
| Request | Message sent from client to server |
| Response | Message returned by server |
| Header | Metadata about request or response |
| Body | Optional data contained in a message |
| Status Code | Indicates the result of a request |

---

# ⚠️ Common Mistakes

### 1. Confusing API with HTTP

API and HTTP are not the same thing.

```text
API → Defines an interface
HTTP → Provides a communication protocol
```

---

### 2. Using GET to Create Data

❌

```http
GET /students
```

for creating a new student.

✅

```http
POST /students
```

---

### 3. Confusing PUT and POST

A common distinction is:

```text
POST → Create a new resource
PUT  → Update/replace an existing resource
```

---

### 4. Ignoring HTTP Status Codes

Always check the response status.

For example:

```text
200 → Successful request
404 → Resource not found
500 → Server error
```

---

### 5. Forgetting the Request Body

Methods such as POST and PUT commonly send data through the request body.

Example:

```json
{
    "name": "Anvesha",
    "age": 20
}
```

---

# 🧪 Practical Observation

The HTTP request-response process was observed using browser developer tools.

The Network tab displays information such as:

- Request URL
- Request method
- Request headers
- Response headers
- Status information
- Timing information

Example request:

```text
GET /
```

The server responded with an HTTP response.

This helped visualize how a browser communicates with a web server.

---

# 📚 Day 28 Exercise

The original Day 28 exercise contains only:

> Read about API and HTTP.

No programming exercise was required for this day.

Therefore, this day was completed as a **theory and practical observation day** rather than a coding exercise.

---

# 🚀 Skills Practiced

- Understanding APIs
- Understanding Web APIs
- Understanding RESTful APIs
- Understanding HTTP
- Understanding client-server communication
- Reading HTTP requests
- Reading HTTP responses
- Understanding HTTP headers
- Understanding HTTP status codes
- Understanding API endpoints
- Understanding CRUD through HTTP
- Observing network requests using browser DevTools

---

# 📝 Key Takeaways

- API stands for **Application Programming Interface**.
- Web APIs allow applications to communicate through the web.
- RESTful APIs commonly use HTTP methods.
- HTTP is a communication protocol used between clients and servers.
- HTTP follows a request-response model.
- HTTP messages contain an initial line, headers, a blank line, and an optional body.
- `GET` is used to retrieve data.
- `POST` is commonly used to create data.
- `PUT` is used to update or replace data.
- `DELETE` is used to remove data.
- HTTP status codes communicate the result of requests.
- Headers provide additional information about requests and responses.
- API endpoints provide URLs through which resources can be accessed.
- Browser DevTools can be used to inspect real HTTP requests and responses.

---

# 💡 Reflection

Today I learned the fundamentals of **APIs and HTTP communication**. I understood how clients and servers communicate using the HTTP request-response cycle and how RESTful APIs use HTTP methods to perform CRUD operations.

I also explored HTTP requests through browser **Developer Tools**, which helped me connect the theoretical concepts of requests, responses, headers, status codes, and endpoints with what actually happens when a website communicates with a server.

Although Day 28 did not include a programming exercise, it provided an important foundation for understanding **backend development, REST APIs, Flask, databases, and full-stack applications**.
