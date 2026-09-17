# payment_methods_custom

[All resources](../methods.md)

## list

List custom payment methods

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListCustomPaymentMethodsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListCustomPaymentMethodsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods_custom::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.payment_methods_custom().list(params).await?;
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

Create a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateCustomPaymentMethodResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateCustomPaymentMethodResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods_custom::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"type\":\"instructions\",\"name\":\"Manual payment\",\"instructions\":\"Contact Launch Lab before sending a payment.\",\"enabled\":false,\"modifier\":{\"percentage\":\"-2.50\",\"fixed\":\"-1.00\"}}")?);
    let result = client.payment_methods_custom().create(params).await?;
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

Retrieve a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **read**

```rust
pub async fn get(
        &self,
        custom_payment_method: &str,
        params: GetParams,
    ) -> Result<SdkGetCustomPaymentMethodResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetCustomPaymentMethodResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods_custom::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.payment_methods_custom().get("string_example", params).await?;
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

Replace a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        custom_payment_method: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceCustomPaymentMethodResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceCustomPaymentMethodResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods_custom::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"type\":\"instructions\",\"name\":\"Manual payment\",\"instructions\":\"Contact Launch Lab before sending a payment.\",\"enabled\":false}")?);
    let result = client.payment_methods_custom().replace("string_example", params).await?;
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

Update a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        custom_payment_method: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateCustomPaymentMethodResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateCustomPaymentMethodResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods_custom::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"enabled\":false,\"modifier\":null}")?);
    let result = client.payment_methods_custom().update("string_example", params).await?;
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

Delete a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        custom_payment_method: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteCustomPaymentMethodResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteCustomPaymentMethodResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods_custom::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.payment_methods_custom().delete("string_example", params).await?;
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

