# customer_portal

[All resources](../methods.md)

## get_customer_portal_profile

Retrieve the signed-in customer

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```rust
pub async fn get_customer_portal_profile(
        &self,
    ) -> Result<SdkGetCustomerPortalProfileResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `SdkGetCustomerPortalProfileResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let result = client.customer_portal().get_customer_portal_profile().await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update_customer_portal_profile

Update the signed-in customer

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn update_customer_portal_profile(
        &self,
        params: UpdateCustomerPortalProfileParams,
    ) -> Result<SdkUpdateCustomerPortalProfileResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateCustomerPortalProfileParams` | Yes |

Returns: `SdkUpdateCustomerPortalProfileResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::UpdateCustomerPortalProfileParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = UpdateCustomerPortalProfileParams::new(serde_json::from_str("{\"locale\":\"en-US\"}")?);
    let result = client.customer_portal().update_customer_portal_profile(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_customer_portal_orders

List customer orders

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```rust
pub async fn list_customer_portal_orders(
        &self,
    ) -> Result<SdkListCustomerPortalOrdersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `SdkListCustomerPortalOrdersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let result = client.customer_portal().list_customer_portal_orders().await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_customer_portal_order

Retrieve a customer order

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```rust
pub async fn get_customer_portal_order(
        &self,
        order: &str,
    ) -> Result<SdkGetCustomerPortalOrderResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |

Returns: `SdkGetCustomerPortalOrderResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let result = client.customer_portal().get_customer_portal_order("9001").await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_customer_portal_subscriptions

List customer subscriptions

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```rust
pub async fn list_customer_portal_subscriptions(
        &self,
    ) -> Result<SdkListCustomerPortalSubscriptionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `SdkListCustomerPortalSubscriptionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let result = client.customer_portal().list_customer_portal_subscriptions().await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_customer_portal_subscription

Retrieve a customer subscription

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```rust
pub async fn get_customer_portal_subscription(
        &self,
        subscription: &str,
    ) -> Result<SdkGetCustomerPortalSubscriptionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| subscription | `&str` | Yes |

Returns: `SdkGetCustomerPortalSubscriptionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let result = client.customer_portal().get_customer_portal_subscription("991").await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_customer_portal_subscription_capabilities

Retrieve subscription capabilities

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```rust
pub async fn get_customer_portal_subscription_capabilities(
        &self,
        subscription: &str,
    ) -> Result<SdkGetCustomerPortalSubscriptionCapabilitiesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| subscription | `&str` | Yes |

Returns: `SdkGetCustomerPortalSubscriptionCapabilitiesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let result = client.customer_portal().get_customer_portal_subscription_capabilities("42").await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_customer_portal_entitlements

List customer entitlements

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```rust
pub async fn list_customer_portal_entitlements(
        &self,
    ) -> Result<SdkListCustomerPortalEntitlementsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `SdkListCustomerPortalEntitlementsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let result = client.customer_portal().list_customer_portal_entitlements().await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## cancel_customer_subscription_at_period_end

Cancel at period end

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn cancel_customer_subscription_at_period_end(
        &self,
        product_subscription: &str,
        params: CancelCustomerSubscriptionAtPeriodEndParams,
    ) -> Result<SdkCancelCustomerSubscriptionAtPeriodEndResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `CancelCustomerSubscriptionAtPeriodEndParams` | Yes |

Returns: `SdkCancelCustomerSubscriptionAtPeriodEndResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::CancelCustomerSubscriptionAtPeriodEndParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = CancelCustomerSubscriptionAtPeriodEndParams::new(serde_json::from_str("{\"reason\":\"Customer requested this change\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().cancel_customer_subscription_at_period_end_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## cancel_customer_subscription_immediately

Cancel immediately

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn cancel_customer_subscription_immediately(
        &self,
        product_subscription: &str,
        params: CancelCustomerSubscriptionImmediatelyParams,
    ) -> Result<SdkCancelCustomerSubscriptionImmediatelyResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `CancelCustomerSubscriptionImmediatelyParams` | Yes |

Returns: `SdkCancelCustomerSubscriptionImmediatelyResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::CancelCustomerSubscriptionImmediatelyParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = CancelCustomerSubscriptionImmediatelyParams::new(serde_json::from_str("{\"reason\":\"Customer requested this change\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().cancel_customer_subscription_immediately_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## pause_customer_subscription

Pause a subscription

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn pause_customer_subscription(
        &self,
        product_subscription: &str,
        params: PauseCustomerSubscriptionParams,
    ) -> Result<SdkPauseCustomerSubscriptionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `PauseCustomerSubscriptionParams` | Yes |

Returns: `SdkPauseCustomerSubscriptionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::PauseCustomerSubscriptionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = PauseCustomerSubscriptionParams::new(serde_json::from_str("{\"reason\":\"Customer requested this change\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().pause_customer_subscription_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## resume_customer_subscription

Resume a subscription

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn resume_customer_subscription(
        &self,
        product_subscription: &str,
        params: ResumeCustomerSubscriptionParams,
    ) -> Result<SdkResumeCustomerSubscriptionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `ResumeCustomerSubscriptionParams` | Yes |

Returns: `SdkResumeCustomerSubscriptionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::ResumeCustomerSubscriptionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = ResumeCustomerSubscriptionParams::new(serde_json::from_str("{\"reason\":\"Customer requested this change\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().resume_customer_subscription_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update_customer_subscription_payment_method

Update payment method

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn update_customer_subscription_payment_method(
        &self,
        product_subscription: &str,
        params: UpdateCustomerSubscriptionPaymentMethodParams,
    ) -> Result<SdkUpdateCustomerSubscriptionPaymentMethodResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `UpdateCustomerSubscriptionPaymentMethodParams` | Yes |

Returns: `SdkUpdateCustomerSubscriptionPaymentMethodResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::UpdateCustomerSubscriptionPaymentMethodParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = UpdateCustomerSubscriptionPaymentMethodParams::new(serde_json::from_str("{\"reason\":\"Customer requested this change\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().update_customer_subscription_payment_method_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## preview_customer_subscription_plan_change

Preview a plan change

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn preview_customer_subscription_plan_change(
        &self,
        product_subscription: &str,
        params: PreviewCustomerSubscriptionPlanChangeParams,
    ) -> Result<SdkPreviewCustomerSubscriptionPlanChangeResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `PreviewCustomerSubscriptionPlanChangeParams` | Yes |

Returns: `SdkPreviewCustomerSubscriptionPlanChangeResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::PreviewCustomerSubscriptionPlanChangeParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = PreviewCustomerSubscriptionPlanChangeParams::new(serde_json::from_str("{\"product_variant_id\":84}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().preview_customer_subscription_plan_change_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## confirm_customer_subscription_plan_change

Confirm a plan change

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn confirm_customer_subscription_plan_change(
        &self,
        product_subscription: &str,
        params: ConfirmCustomerSubscriptionPlanChangeParams,
    ) -> Result<SdkConfirmCustomerSubscriptionPlanChangeResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `ConfirmCustomerSubscriptionPlanChangeParams` | Yes |

Returns: `SdkConfirmCustomerSubscriptionPlanChangeResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::ConfirmCustomerSubscriptionPlanChangeParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = ConfirmCustomerSubscriptionPlanChangeParams::new(serde_json::from_str("{\"preview_id\":\"preview_01K4\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().confirm_customer_subscription_plan_change_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## preview_customer_subscription_renewal_date_change

Preview a renewal-date change

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn preview_customer_subscription_renewal_date_change(
        &self,
        product_subscription: &str,
        params: PreviewCustomerSubscriptionRenewalDateChangeParams,
    ) -> Result<SdkPreviewCustomerSubscriptionRenewalDateChangeResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `PreviewCustomerSubscriptionRenewalDateChangeParams` | Yes |

Returns: `SdkPreviewCustomerSubscriptionRenewalDateChangeResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::PreviewCustomerSubscriptionRenewalDateChangeParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = PreviewCustomerSubscriptionRenewalDateChangeParams::new(serde_json::from_str("{\"renewal_date\":\"2026-10-15\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().preview_customer_subscription_renewal_date_change_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## confirm_customer_subscription_renewal_date_change

Confirm a renewal-date change

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```rust
pub async fn confirm_customer_subscription_renewal_date_change(
        &self,
        product_subscription: &str,
        params: ConfirmCustomerSubscriptionRenewalDateChangeParams,
    ) -> Result<SdkConfirmCustomerSubscriptionRenewalDateChangeResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `ConfirmCustomerSubscriptionRenewalDateChangeParams` | Yes |

Returns: `SdkConfirmCustomerSubscriptionRenewalDateChangeResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_portal::ConfirmCustomerSubscriptionRenewalDateChangeParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_customer_session(std::env::var("SELLAPP_CUSTOMER_SESSION")?);
    let mut params = ConfirmCustomerSubscriptionRenewalDateChangeParams::new(serde_json::from_str("{\"preview_id\":\"preview_01K4\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.customer_portal().confirm_customer_subscription_renewal_date_change_with_options("42", params, Some(&request_options)).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

