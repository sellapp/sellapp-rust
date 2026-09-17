# tickets

[All resources](../methods.md)

## list

List all tickets

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListTicketsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListTicketsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.tickets().list(params).await?;
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

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve specific ticket

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn get(
        &self,
        ticket: &str,
    ) -> Result<SdkGetTicketResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |

Returns: `SdkGetTicketResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.tickets().get("1").await?;
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

Search tickets

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchTicketsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchTicketsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.tickets().search(params).await?;
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

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_list_tickets

List all tickets

[API reference](https://sell.app/docs/api/tickets/list-all-tickets) · Effect: **read**

```rust
pub async fn v_2_list_tickets(
        &self,
        params: V2ListTicketsParams,
    ) -> Result<SdkV2ListTicketsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2ListTicketsParams` | Yes |

Returns: `SdkV2ListTicketsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets::V2ListTicketsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ListTicketsParams::default();
    let result = client.tickets().v_2_list_tickets(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_search_tickets

Search tickets

[API reference](https://sell.app/docs/api/tickets/search-tickets) · Effect: **read**

```rust
pub async fn v_2_search_tickets(
        &self,
        params: V2SearchTicketsParams,
    ) -> Result<SdkV2SearchTicketsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2SearchTicketsParams` | Yes |

Returns: `SdkV2SearchTicketsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets::V2SearchTicketsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2SearchTicketsParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.tickets().v_2_search_tickets(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_get_ticket

Retrieve specific ticket

[API reference](https://sell.app/docs/api/tickets/retrieve-specific-ticket) · Effect: **read**

```rust
pub async fn v_2_get_ticket(
        &self,
        ticket: &str,
        params: V2GetTicketParams,
    ) -> Result<SdkV2GetTicketResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `V2GetTicketParams` | Yes |

Returns: `SdkV2GetTicketResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets::V2GetTicketParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2GetTicketParams::default();
    let result = client.tickets().v_2_get_ticket("1", params).await?;
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

## update

Close, reopen, or archive a ticket

[API reference](https://sell.app/docs/api/tickets/retrieve-specific-ticket) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        ticket: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateTicketResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateTicketResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"status\":\"CLOSED\",\"archived\":true}")?);
    let result = client.tickets().update("42", params).await?;
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

