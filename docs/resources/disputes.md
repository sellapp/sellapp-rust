# disputes

[All resources](../methods.md)

## list_disputes

List disputes

[API reference](https://sell.app/docs/api/disputes) · Effect: **read**

```rust
pub async fn list_disputes(
        &self,
        params: ListDisputesParams,
    ) -> Result<SdkListDisputesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListDisputesParams` | Yes |

Returns: `SdkListDisputesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::disputes::ListDisputesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListDisputesParams::default();
    let result = client.disputes().list_disputes(params).await?;
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

## get_dispute

Retrieve a dispute

[API reference](https://sell.app/docs/api/disputes) · Effect: **read**

```rust
pub async fn get_dispute(
        &self,
        dispute: &str,
        params: GetDisputeParams,
    ) -> Result<SdkGetDisputeResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| dispute | `&str` | Yes |
| params | `GetDisputeParams` | Yes |

Returns: `SdkGetDisputeResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::disputes::GetDisputeParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetDisputeParams::default();
    let result = client.disputes().get_dispute("01992b10-a7d2-7b91-9822-32e8d7454e7c", params).await?;
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

