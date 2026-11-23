# support_reasons

[All resources](../methods.md)

## list

List support reasons

[API reference](https://sell.app/docs/api/support-reasons/list-support-reasons) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListSupportReasonsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListSupportReasonsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reasons::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.support_reasons().list(params).await?;
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

## create

Create a support reason

[API reference](https://sell.app/docs/api/support-reasons/create-a-support-reason) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateSupportReasonResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateSupportReasonResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reasons::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"label\":\"Download link expired\",\"description\":\"The download link in the order email no longer works.\"}")?);
    let result = client.support_reasons().create(params).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a support reason

[API reference](https://sell.app/docs/api/support-reasons/retrieve-a-support-reason) · Effect: **read**

```rust
pub async fn get(
        &self,
        support_reason: &str,
        params: GetParams,
    ) -> Result<SdkGetSupportReasonResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reason | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetSupportReasonResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reasons::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.support_reasons().get("14", params).await?;
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

## replace

Update a support reason

[API reference](https://sell.app/docs/api/support-reasons/update-a-support-reason) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        support_reason: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceSupportReasonResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reason | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceSupportReasonResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reasons::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"description\":\"The download link in the order email no longer opens.\",\"expected_updated_at\":\"2026-07-03T09:10:00.000000Z\"}")?);
    let result = client.support_reasons().replace("14", params).await?;
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

Update a support reason

[API reference](https://sell.app/docs/api/support-reasons/update-a-support-reason) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        support_reason: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateSupportReasonResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reason | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateSupportReasonResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reasons::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"description\":\"The download link in the order email no longer opens.\",\"expected_updated_at\":\"2026-07-03T09:10:00.000000Z\"}")?);
    let result = client.support_reasons().update("14", params).await?;
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

## delete

Delete a support reason

[API reference](https://sell.app/docs/api/support-reasons/delete-a-support-reason) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        support_reason: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteSupportReasonResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reason | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteSupportReasonResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reasons::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.support_reasons().delete("15", params).await?;
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

## get_options

Retrieve support reason options

[API reference](https://sell.app/docs/api/support-reasons/support-reason-options) · Effect: **read**

```rust
pub async fn get_options(
        &self,
        params: GetOptionsParams,
    ) -> Result<SdkGetSupportReasonOptionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetOptionsParams` | Yes |

Returns: `SdkGetSupportReasonOptionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reasons::GetOptionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetOptionsParams::default();
    let result = client.support_reasons().get_options(params).await?;
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

