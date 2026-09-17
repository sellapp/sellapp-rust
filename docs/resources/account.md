# account

[All resources](../methods.md)

## get_account

Read your profile

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```rust
pub async fn get_account(&self) -> Result<SdkGetAccountResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `SdkGetAccountResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.account().get_account().await?;
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
    ]
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_stores

List accessible stores

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```rust
pub async fn list_stores(&self) -> Result<SdkListStoresResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `SdkListStoresResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.account().list_stores().await?;
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
    ]
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create_store

Create a store

[API reference](https://sell.app/docs/api/oauth) · Effect: **write**

```rust
pub async fn create_store(
        &self,
        params: CreateStoreParams,
    ) -> Result<SdkCreateStoreResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateStoreParams` | Yes |

Returns: `SdkCreateStoreResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::account::CreateStoreParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateStoreParams::new(serde_json::from_str("{\"name\":\"Launch Lab\",\"slug\":\"launchlab\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.account().create_store_with_options(params, Some(&request_options)).await?;
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
    ]
  }
]
```

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_store

Read an accessible store

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```rust
pub async fn get_store(
        &self,
        store: &str,
    ) -> Result<SdkGetStoreResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| store | `&str` | Yes |

Returns: `SdkGetStoreResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.account().get_store("12").await?;
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
    ]
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_store_permissions

Inspect effective permissions

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```rust
pub async fn get_store_permissions(
        &self,
        params: GetStorePermissionsParams,
    ) -> Result<SdkGetStorePermissionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetStorePermissionsParams` | Yes |

Returns: `SdkGetStorePermissionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::account::GetStorePermissionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetStorePermissionsParams::new("launch-lab");
    let result = client.account().get_store_permissions(params).await?;
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

