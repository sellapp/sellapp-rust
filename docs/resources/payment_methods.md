# payment_methods

[All resources](../methods.md)

## list

List payment methods

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListPaymentMethodsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListPaymentMethodsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.payment_methods().list(params).await?;
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

## get

Retrieve payment method status

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **read**

```rust
pub async fn get(
        &self,
        payment_method: &str,
        params: GetParams,
    ) -> Result<SdkGetPaymentMethodStatusResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetPaymentMethodStatusResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.payment_methods().get("STRIPE", params).await?;
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

## enable

Enable or disable a payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **consequential**

```rust
pub async fn enable(
        &self,
        payment_method: &str,
        params: EnableParams,
    ) -> Result<SdkEnableOrDisablePaymentMethodResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `&str` | Yes |
| params | `EnableParams` | Yes |

Returns: `SdkEnableOrDisablePaymentMethodResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods::EnableParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = EnableParams::new(serde_json::from_str("{\"enabled\":false}")?);
    let result = client.payment_methods().enable("STRIPE", params).await?;
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

## connect

Create a payment connection handoff

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **consequential**

```rust
pub async fn connect(
        &self,
        payment_method: &str,
        params: ConnectParams,
    ) -> Result<SdkCreatePaymentConnectionHandoffResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `&str` | Yes |
| params | `ConnectParams` | Yes |

Returns: `SdkCreatePaymentConnectionHandoffResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods::ConnectParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ConnectParams::default();
    let result = client.payment_methods().connect("STRIPE", params).await?;
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

## validate

Validate and save payment method configuration

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **consequential**

```rust
pub async fn validate(
        &self,
        payment_method: &str,
        params: ValidateParams,
    ) -> Result<SdkValidateAndSavePaymentMethodConfigurationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `&str` | Yes |
| params | `ValidateParams` | Yes |

Returns: `SdkValidateAndSavePaymentMethodConfigurationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::payment_methods::ValidateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ValidateParams::new(serde_json::from_str("{\"merchant_secure_key\":\"replace-with-nmi-secure-key\",\"merchant_tokenization_key\":\"replace-with-nmi-tokenization-key\",\"signing_key\":\"replace-with-nmi-signing-key\",\"currencies\":[\"USD\"]}")?);
    let result = client.payment_methods().validate("NMI", params).await?;
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

