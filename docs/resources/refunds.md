# refunds

[All resources](../methods.md)

## list_refunds

List refunds

[API reference](https://sell.app/docs/api/refunds) · Effect: **read**

```rust
pub async fn list_refunds(
        &self,
        params: ListRefundsParams,
    ) -> Result<SdkListRefundsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListRefundsParams` | Yes |

Returns: `SdkListRefundsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::refunds::ListRefundsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListRefundsParams::default();
    let result = client.refunds().list_refunds(params).await?;
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

## get_refund

Retrieve a refund

[API reference](https://sell.app/docs/api/refunds) · Effect: **read**

```rust
pub async fn get_refund(
        &self,
        refund: &str,
        params: GetRefundParams,
    ) -> Result<SdkGetRefundResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| refund | `&str` | Yes |
| params | `GetRefundParams` | Yes |

Returns: `SdkGetRefundResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::refunds::GetRefundParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetRefundParams::default();
    let result = client.refunds().get_refund("781", params).await?;
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

