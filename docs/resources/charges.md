# charges

[All resources](../methods.md)

## list

List all charges

[API reference](https://sell.app/docs/api/charges/list-all-charges) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListChargesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListChargesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::charges::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.charges().list(params).await?;
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

Create a charge

[API reference](https://sell.app/docs/api/charges/create-a-charge) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateChargeResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateChargeResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::charges::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"email\":\"sofia.rivera@example.com\",\"return_url\":\"https://example.com/launch-complete\",\"currency\":\"USD\",\"total\":10000,\"payment_method\":\"PAYPAL\",\"reference\":\"One more thing launch\"}")?);
    let result = client.charges().create(params).await?;
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

Retrieve a charge

[API reference](https://sell.app/docs/api/charges/retrieve-a-charge) · Effect: **read**

```rust
pub async fn get(
        &self,
        charge: &str,
        params: GetParams,
    ) -> Result<SdkGetChargeResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetChargeResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::charges::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.charges().get("1", params).await?;
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

## mark_completed

Mark pending charge completed

[API reference](https://sell.app/docs/api/charges/mark-pending-charge-completed) · Effect: **consequential**

```rust
pub async fn mark_completed(
        &self,
        charge_id: &str,
        params: MarkCompletedParams,
    ) -> Result<SdkMarkPendingChargeCompletedResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge_id | `&str` | Yes |
| params | `MarkCompletedParams` | Yes |

Returns: `SdkMarkPendingChargeCompletedResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::charges::MarkCompletedParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = MarkCompletedParams::default();
    let result = client.charges().mark_completed("1", params).await?;
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

## mark_voided

Mark pending charge voided

[API reference](https://sell.app/docs/api/charges/mark-pending-charge-voided) · Effect: **consequential**

```rust
pub async fn mark_voided(
        &self,
        charge_id: &str,
        params: MarkVoidedParams,
    ) -> Result<SdkMarkPendingChargeVoidedResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge_id | `&str` | Yes |
| params | `MarkVoidedParams` | Yes |

Returns: `SdkMarkPendingChargeVoidedResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::charges::MarkVoidedParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = MarkVoidedParams::default();
    let result = client.charges().mark_voided("1", params).await?;
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

