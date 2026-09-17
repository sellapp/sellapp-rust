# tickets_messages

[All resources](../methods.md)

## list

List all ticket messages

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn list(
        &self,
        ticket: &str,
        params: ListParams,
    ) -> Result<SdkListTicketMessagesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListTicketMessagesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_messages::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.tickets_messages().list("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## reply

Reply to ticket

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn reply(
        &self,
        ticket: &str,
        params: ReplyParams,
    ) -> Result<SdkReplyToTicketResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `ReplyParams` | Yes |

Returns: `SdkReplyToTicketResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_messages::ReplyParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplyParams::new(serde_json::from_str("{\"content\":\"You can choose from the payment methods shown at checkout.\"}")?);
    let result = client.tickets_messages().reply("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 201, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve specific ticket message

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn get(
        &self,
        ticket: &str,
        message: &str,
    ) -> Result<SdkGetTicketMessageResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| message | `&str` | Yes |

Returns: `SdkGetTicketMessageResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.tickets_messages().get("1", "2").await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search ticket messages

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn search(
        &self,
        ticket: &str,
        params: SearchParams,
    ) -> Result<SdkSearchTicketMessagesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `SearchParams` | Yes |

Returns: `SdkSearchTicketMessagesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_messages::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.tickets_messages().search("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_list_ticket_messages

List all ticket messages

[API reference](https://sell.app/docs/api/tickets/list-all-ticket-messages) · Effect: **read**

```rust
pub async fn v_2_list_ticket_messages(
        &self,
        ticket: &str,
        params: V2ListTicketMessagesParams,
    ) -> Result<SdkV2ListTicketMessagesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `V2ListTicketMessagesParams` | Yes |

Returns: `SdkV2ListTicketMessagesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_messages::V2ListTicketMessagesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ListTicketMessagesParams::default();
    let result = client.tickets_messages().v_2_list_ticket_messages("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_reply_to_ticket

Reply to ticket

[API reference](https://sell.app/docs/api/tickets/reply-to-ticket) · Effect: **consequential**

```rust
pub async fn v_2_reply_to_ticket(
        &self,
        ticket: &str,
        params: V2ReplyToTicketParams,
    ) -> Result<SdkV2ReplyToTicketResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `V2ReplyToTicketParams` | Yes |

Returns: `SdkV2ReplyToTicketResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_messages::V2ReplyToTicketParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplyToTicketParams::new(serde_json::from_str("{\"content\":\"You can choose from the payment methods shown at checkout.\"}")?);
    let result = client.tickets_messages().v_2_reply_to_ticket("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_search_ticket_messages

Search ticket messages

[API reference](https://sell.app/docs/api/tickets/search-ticket-messages) · Effect: **read**

```rust
pub async fn v_2_search_ticket_messages(
        &self,
        ticket: &str,
        params: V2SearchTicketMessagesParams,
    ) -> Result<SdkV2SearchTicketMessagesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `V2SearchTicketMessagesParams` | Yes |

Returns: `SdkV2SearchTicketMessagesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_messages::V2SearchTicketMessagesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2SearchTicketMessagesParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.tickets_messages().v_2_search_ticket_messages("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_get_ticket_message

Retrieve specific ticket message

[API reference](https://sell.app/docs/api/tickets/retrieve-specific-ticket-message) · Effect: **read**

```rust
pub async fn v_2_get_ticket_message(
        &self,
        ticket: &str,
        message: &str,
        params: V2GetTicketMessageParams,
    ) -> Result<SdkV2GetTicketMessageResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| message | `&str` | Yes |
| params | `V2GetTicketMessageParams` | Yes |

Returns: `SdkV2GetTicketMessageResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_messages::V2GetTicketMessageParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2GetTicketMessageParams::default();
    let result = client.tickets_messages().v_2_get_ticket_message("1", "2", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

