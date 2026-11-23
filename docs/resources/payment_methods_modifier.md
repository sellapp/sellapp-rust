# payment_methods_modifier

[All resources](../methods.md)

## get

Retrieve a payment method modifier

[API reference](https://sell.app/docs/api/payment-methods/payment-method-modifier) · Effect: **read**

```rust
pub async fn get(
        &self,
        payment_method: &str,
        params: GetParams,
    ) -> Result<SdkGetPaymentMethodModifierResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetPaymentMethodModifierResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods_modifier::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.payment_methods_modifier().get("STRIPE", params).await?;
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

Update a payment method modifier

[API reference](https://sell.app/docs/api/payment-methods/payment-method-modifier) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        payment_method: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplacePaymentMethodModifierResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplacePaymentMethodModifierResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods_modifier::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"kind\":\"fee\",\"percentage\":\"3.00\",\"fixed_amount\":\"0.30\",\"condition\":\"below\",\"threshold\":\"20.00\"}")?);
    let result = client.payment_methods_modifier().replace("STRIPE", params).await?;
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

