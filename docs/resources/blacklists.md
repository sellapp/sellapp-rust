# blacklists

[All resources](../methods.md)

## list

List all blacklist rules

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn list(&self, params: ListParams) -> Result<BlacklistListResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `BlacklistListResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.blacklists().list(params).await?;
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

## create

Create a blacklist rule

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn create(&self, params: CreateParams) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"type\":\"ASN\",\"data\":\"@blocked.example\",\"description\":\"Retired after the growth experiment ended.\"}")?);
    let result = client.blacklists().create(params).await?;
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

Documented HTTP responses: 201, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a blacklist rule

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn get(&self, blacklist: &str) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `&str` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.blacklists().get("1").await?;
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

## update

Update a blacklist rule

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        blacklist: &str,
        params: UpdateParams,
    ) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{}")?);
    let result = client.blacklists().update("1", params).await?;
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

## delete

Delete a blacklist rule

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn delete(&self, blacklist: &str) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `&str` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.blacklists().delete("1").await?;
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

## v_2_list_blacklists

List blacklist rules

[API reference](https://sell.app/docs/api/blacklists/list-blacklists) · Effect: **read**

```rust
pub async fn v_2_list_blacklists(
        &self,
        params: V2ListBlacklistsParams,
    ) -> Result<BlacklistListResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2ListBlacklistsParams` | Yes |

Returns: `BlacklistListResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::V2ListBlacklistsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ListBlacklistsParams::default();
    let result = client.blacklists().v_2_list_blacklists(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_create_blacklist

Create a blacklist rule

[API reference](https://sell.app/docs/api/blacklists/create-blacklist) · Effect: **consequential**

```rust
pub async fn v_2_create_blacklist(
        &self,
        params: V2CreateBlacklistParams,
    ) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2CreateBlacklistParams` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::V2CreateBlacklistParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2CreateBlacklistParams::new(serde_json::from_str("{\"type\":\"EMAIL\",\"data\":\"blocked@example.com\",\"description\":\"Blocked after a verified fraud report.\"}")?);
    let result = client.blacklists().v_2_create_blacklist(params).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_get_blacklist

Retrieve a blacklist rule

[API reference](https://sell.app/docs/api/blacklists/retrieve-blacklist) · Effect: **read**

```rust
pub async fn v_2_get_blacklist(
        &self,
        blacklist: &str,
        params: V2GetBlacklistParams,
    ) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `&str` | Yes |
| params | `V2GetBlacklistParams` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::V2GetBlacklistParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2GetBlacklistParams::default();
    let result = client.blacklists().v_2_get_blacklist("42", params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_replace_blacklist

Replace a blacklist rule

[API reference](https://sell.app/docs/api/blacklists) · Effect: **consequential**

```rust
pub async fn v_2_replace_blacklist(
        &self,
        blacklist: &str,
        params: V2ReplaceBlacklistParams,
    ) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `&str` | Yes |
| params | `V2ReplaceBlacklistParams` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::V2ReplaceBlacklistParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplaceBlacklistParams::new(serde_json::from_str("{\"description\":\"Blocked after a verified fraud report.\"}")?);
    let result = client.blacklists().v_2_replace_blacklist("42", params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_update_blacklist

Update a blacklist rule

[API reference](https://sell.app/docs/api/blacklists/update-blacklist) · Effect: **consequential**

```rust
pub async fn v_2_update_blacklist(
        &self,
        blacklist: &str,
        params: V2UpdateBlacklistParams,
    ) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `&str` | Yes |
| params | `V2UpdateBlacklistParams` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::V2UpdateBlacklistParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2UpdateBlacklistParams::new(serde_json::from_str("{\"description\":\"Blocked after a verified fraud report.\"}")?);
    let result = client.blacklists().v_2_update_blacklist("42", params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_delete_blacklist

Delete a blacklist rule

[API reference](https://sell.app/docs/api/blacklists/delete-blacklist) · Effect: **consequential**

```rust
pub async fn v_2_delete_blacklist(
        &self,
        blacklist: &str,
        params: V2DeleteBlacklistParams,
    ) -> Result<BlacklistResponse, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `&str` | Yes |
| params | `V2DeleteBlacklistParams` | Yes |

Returns: `BlacklistResponse`.

```rs
use sellapp::Client;
use sellapp::resources::blacklists::V2DeleteBlacklistParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2DeleteBlacklistParams::default();
    let result = client.blacklists().v_2_delete_blacklist("42", params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

