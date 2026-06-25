# API Documentation

This document outlines the REST API endpoints available in the AI API Service. 

*Note: Interactive API documentation is also automatically generated and available at the `/docs` (Swagger UI) and `/redoc` (ReDoc) routes when the application is running.*

---

## 1. Summarize Text

Summarizes a provided block of text.

- **URL:** `/api/v1/summarize`
- **Method:** `POST`
- **Content-Type:** `application/json`

### Request Body

| Field | Type | Description | Required | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `text` | string | The text to be summarized. | Yes | Min length: 10 characters |

**Example Request:**
```json
{
  "text": "Artificial intelligence is rapidly changing the landscape of software engineering. Developers are now utilizing AI assistants to write boilerplate code, debug complex errors, and optimize their workflows at an unprecedented pace."
}
```

### Response

- **Success Code:** `200 OK`

**Example Response:**
```json
{
  "original_length": 223,
  "summary_length": 86,
  "summary": "This is a mock summary of the provided text. The original text started with: 'Artificial intellige...'"
}
```

---

## 2. Translate Text

Translates text into a specified target language.

- **URL:** `/api/v1/translate`
- **Method:** `POST`
- **Content-Type:** `application/json`

### Request Body

| Field | Type | Description | Required | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `text` | string | The text to translate. | Yes | Min length: 1 character |
| `target_language` | string | The language to translate the text into. | Yes | Min length: 2 characters |

**Example Request:**
```json
{
  "text": "Hello world, how are you?",
  "target_language": "Spanish"
}
```

### Response

- **Success Code:** `200 OK`

**Example Response:**
```json
{
  "target_language": "Spanish",
  "translated_text": "[Mock Translation in Spanish]: Hello world, how are you?"
}
```

---

## 3. Generate Email

Generates an email body based on a subject, context, and tone.

- **URL:** `/api/v1/generate-email`
- **Method:** `POST`
- **Content-Type:** `application/json`

### Request Body

| Field | Type | Description | Required | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `subject` | string | The subject of the email. | Yes | Min length: 1 character |
| `context` | string | The context or main points to include. | Yes | Min length: 1 character |
| `tone` | string | The tone of the email. | No | Defaults to "professional" |

**Example Request:**
```json
{
  "subject": "Job Interview Follow-up",
  "context": "I am following up on my interview yesterday for the AI Engineer role.",
  "tone": "professional"
}
```

### Response

- **Success Code:** `200 OK`

**Example Response:**
```json
{
  "subject": "Job Interview Follow-up",
  "body": "Dear Recipient,\n\nI am writing to you regarding: Job Interview Follow-up.\n\nBased on our context: I am following up on my interview yesterday for the AI Engineer role.\n\nBest regards,\nSender (Mock generated in professional tone)"
}
```

---

## Error Handling

If a request fails validation (e.g., missing a required field or violating a length constraint), the API returns a structured error.

- **Error Code:** `422 Unprocessable Entity`

**Example Error Response:**
```json
{
  "detail": "Invalid request payload",
  "errors": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "text"
      ],
      "msg": "String should have at least 10 characters",
      "input": "Hi",
      "ctx": {
        "min_length": 10
      }
    }
  ]
}
```

If an internal server error occurs, it returns a generic `500 Internal Server Error`.
