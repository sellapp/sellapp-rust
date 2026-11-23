# store_sender_email

[All resources](../methods.md)

## get

Retrieve the sender email

[API reference](https://sell.app/docs/api/store-settings/sender-email) · Effect: **read**

```rust
pub async fn get(
        &self,
        params: GetParams,
    ) -> Result<SdkGetSenderEmailResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetParams` | Yes |

Returns: `SdkGetSenderEmailResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_sender_email::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.store_sender_email().get(params).await?;
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

## set

Set the sender email

[API reference](https://sell.app/docs/api/store-settings/sender-email) · Effect: **consequential**

```rust
pub async fn set(
        &self,
        params: SetParams,
    ) -> Result<SdkSetSenderEmailResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SetParams` | Yes |

Returns: `SdkSetSenderEmailResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_sender_email::SetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SetParams::new(serde_json::from_str("{\"email\":\"orders@launch-lab.example.com\"}")?);
    let result = client.store_sender_email().set(params).await?;
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

## delete

Delete the sender email

[API reference](https://sell.app/docs/api/store-settings/sender-email) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        params: DeleteParams,
    ) -> Result<SdkDeleteSenderEmailResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteSenderEmailResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_sender_email::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.store_sender_email().delete(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500, 503. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## send_verification

Send a sender email verification

[API reference](https://sell.app/docs/api/store-settings/sender-email) · Effect: **consequential**

```rust
pub async fn send_verification(
        &self,
        params: SendVerificationParams,
    ) -> Result<SdkSendSenderEmailVerificationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SendVerificationParams` | Yes |

Returns: `SdkSendSenderEmailVerificationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_sender_email::SendVerificationParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SendVerificationParams::new(serde_json::from_str("{\"email\":\"orders@launch-lab.example.com\"}")?);
    let result = client.store_sender_email().send_verification(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500, 503. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

