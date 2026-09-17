# orders

[All resources](../methods.md)

## list

List orders

[API reference](https://sell.app/docs/api/orders/list-orders) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListOrdersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListOrdersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.orders().list(params).await?;
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

Create an order

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateOrderResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateOrderResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"customer_email\":\"maya@example.com\",\"payment_method\":\"STRIPE\",\"product_variants\":{\"4321\":{\"quantity\":1}}}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().create_with_options(params, Some(&request_options)).await?;
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

## search

Search orders

[API reference](https://sell.app/docs/api/orders/search-orders) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchOrdersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchOrdersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"transaction_id\",\"operator\":\"contains\",\"value\":\"pi_3Example\"},{\"field\":\"status\",\"operator\":\"in\",\"value\":[\"COMPLETED\"]}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}],\"pagination\":{\"page\":1,\"limit\":25}}")?);
    let result = client.orders().search(params).await?;
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

Retrieve an order

[API reference](https://sell.app/docs/api/orders/retrieve-an-order) · Effect: **read**

```rust
pub async fn get(
        &self,
        order: &str,
        params: GetParams,
    ) -> Result<SdkGetOrderResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetOrderResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.orders().get("1042", params).await?;
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

## update_status

Update order status

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn update_status(
        &self,
        order: &str,
        params: UpdateStatusParams,
    ) -> Result<SdkUpdateOrderStatusResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `UpdateStatusParams` | Yes |

Returns: `SdkUpdateOrderStatusResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::UpdateStatusParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateStatusParams::new(serde_json::from_str("{\"status\":\"COMPLETED\",\"expected_status\":\"PAID\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().update_status_with_options("9001", params, Some(&request_options)).await?;
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

## create_checkout

Create order checkout

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn create_checkout(
        &self,
        order: &str,
        params: CreateCheckoutParams,
    ) -> Result<SdkCreateOrderCheckoutResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `CreateCheckoutParams` | Yes |

Returns: `SdkCreateOrderCheckoutResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::CreateCheckoutParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateCheckoutParams::new(serde_json::from_str("{}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().create_checkout_with_options("9001", params, Some(&request_options)).await?;
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create_replacement

Issue replacements

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn create_replacement(
        &self,
        order: &str,
        params: CreateReplacementParams,
    ) -> Result<SdkCreateOrderReplacementResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `CreateReplacementParams` | Yes |

Returns: `SdkCreateOrderReplacementResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::CreateReplacementParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateReplacementParams::new(serde_json::from_str("{\"product_variants\":[4321]}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().create_replacement_with_options("9001", params, Some(&request_options)).await?;
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

## create_refund

Refund an order

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn create_refund(
        &self,
        order: &str,
        params: CreateRefundParams,
    ) -> Result<SdkCreateOrderRefundResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `CreateRefundParams` | Yes |

Returns: `SdkCreateOrderRefundResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::CreateRefundParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateRefundParams::new(serde_json::from_str("{\"amount\":\"5.00\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().create_refund_with_options("9001", params, Some(&request_options)).await?;
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

## retry_fulfillment

Retry fulfillment

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn retry_fulfillment(
        &self,
        order: &str,
        params: RetryFulfillmentParams,
    ) -> Result<SdkRetryOrderFulfillmentResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `RetryFulfillmentParams` | Yes |

Returns: `SdkRetryOrderFulfillmentResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::RetryFulfillmentParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RetryFulfillmentParams::new(serde_json::from_str("{\"email\":\"maya@example.com\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().retry_fulfillment_with_options("9001", params, Some(&request_options)).await?;
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

## retry_dynamic_delivery

Retry dynamic delivery

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn retry_dynamic_delivery(
        &self,
        order: &str,
        params: RetryDynamicDeliveryParams,
    ) -> Result<SdkRetryOrderDynamicDeliveryResponseValue202ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `RetryDynamicDeliveryParams` | Yes |

Returns: `SdkRetryOrderDynamicDeliveryResponseValue202ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::RetryDynamicDeliveryParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RetryDynamicDeliveryParams::new(serde_json::from_str("{\"delivered_product_id\":81}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().retry_dynamic_delivery_with_options("9001", params, Some(&request_options)).await?;
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

Documented HTTP responses: 202, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## send_fulfillment_notifications

Send fulfillment notifications

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn send_fulfillment_notifications(
        &self,
        order: &str,
        params: SendFulfillmentNotificationsParams,
    ) -> Result<SdkSendOrderFulfillmentNotificationsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `SendFulfillmentNotificationsParams` | Yes |

Returns: `SdkSendOrderFulfillmentNotificationsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::SendFulfillmentNotificationsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SendFulfillmentNotificationsParams::new(serde_json::from_str("{\"email\":\"maya@example.com\",\"product_variant_ids\":[4321]}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().send_fulfillment_notifications_with_options("9001", params, Some(&request_options)).await?;
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

## list_deliverables

List order deliverables

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **read**

```rust
pub async fn list_deliverables(
        &self,
        order: &str,
        params: ListDeliverablesParams,
    ) -> Result<SdkListOrderDeliverablesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `ListDeliverablesParams` | Yes |

Returns: `SdkListOrderDeliverablesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::ListDeliverablesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListDeliverablesParams::default();
    let result = client.orders().list_deliverables("9001", params).await?;
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

## create_from_wallet

Create and pay an order from a wallet

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn create_from_wallet(
        &self,
        params: CreateFromWalletParams,
    ) -> Result<SdkCreateWalletOrderResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateFromWalletParams` | Yes |

Returns: `SdkCreateWalletOrderResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::CreateFromWalletParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateFromWalletParams::new(serde_json::from_str("{\"customer_email\":\"maya.chen@example.com\",\"product_variants\":{\"4321\":{\"quantity\":1}},\"country\":\"US\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().create_from_wallet_with_options(params, Some(&request_options)).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## pay_from_wallet

Pay an existing order from its customer wallet

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```rust
pub async fn pay_from_wallet(
        &self,
        order: &str,
        params: PayFromWalletParams,
    ) -> Result<SdkPayOrderFromWalletResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `PayFromWalletParams` | Yes |

Returns: `SdkPayOrderFromWalletResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders::PayFromWalletParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = PayFromWalletParams::new(serde_json::from_str("{\"expected_status\":\"PENDING\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.orders().pay_from_wallet_with_options("42", params, Some(&request_options)).await?;
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

