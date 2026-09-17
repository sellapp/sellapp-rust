# subscriptions

[All resources](../methods.md)

## cancel

Cancel a subscription

[API reference](https://sell.app/docs/api/subscriptions/cancel-a-subscription-immediately-with-a-refund) · Effect: **consequential**

```rust
pub async fn cancel(
        &self,
        subscription: &str,
        params: CancelParams,
    ) -> Result<SdkCancelSubscriptionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| subscription | `&str` | Yes |
| params | `CancelParams` | Yes |

Returns: `SdkCancelSubscriptionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::CancelParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CancelParams::new(serde_json::from_str("{\"cancel_at_period_end\":true,\"idempotency_key\":\"design-kit-subscription-55-cancel-v1\"}")?);
    let result = client.subscriptions().cancel("55", params).await?;
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

## get_capabilities

View subscription capabilities

[API reference](https://sell.app/docs/api/subscriptions/view-subscription-capabilities) · Effect: **read**

```rust
pub async fn get_capabilities(
        &self,
        product_subscription: &str,
        params: GetCapabilitiesParams,
    ) -> Result<SdkGetSubscriptionCapabilitiesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `GetCapabilitiesParams` | Yes |

Returns: `SdkGetSubscriptionCapabilitiesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::GetCapabilitiesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetCapabilitiesParams::default();
    let result = client.subscriptions().get_capabilities("1", params).await?;
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

## cancel_at_period_end

Cancel a subscription at period end

[API reference](https://sell.app/docs/api/subscriptions/cancel-at-period-end) · Effect: **consequential**

```rust
pub async fn cancel_at_period_end(
        &self,
        product_subscription: &str,
        params: CancelAtPeriodEndParams,
    ) -> Result<SdkCancelSubscriptionAtPeriodEndResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `CancelAtPeriodEndParams` | Yes |

Returns: `SdkCancelSubscriptionAtPeriodEndResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::CancelAtPeriodEndParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CancelAtPeriodEndParams::new(serde_json::from_str("{\"reason\":\"Customer request\"}")?);
    let result = client.subscriptions().cancel_at_period_end("55", params).await?;
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

## cancel_immediately

Cancel a subscription immediately

[API reference](https://sell.app/docs/api/subscriptions/cancel-immediately) · Effect: **consequential**

```rust
pub async fn cancel_immediately(
        &self,
        product_subscription: &str,
        params: CancelImmediatelyParams,
    ) -> Result<SdkCancelSubscriptionImmediatelyResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `CancelImmediatelyParams` | Yes |

Returns: `SdkCancelSubscriptionImmediatelyResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::CancelImmediatelyParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CancelImmediatelyParams::new(serde_json::from_str("{\"reason\":\"Customer request\"}")?);
    let result = client.subscriptions().cancel_immediately("55", params).await?;
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

## pause

Pause a subscription

[API reference](https://sell.app/docs/api/subscriptions/pause-a-subscription) · Effect: **consequential**

```rust
pub async fn pause(
        &self,
        product_subscription: &str,
        params: PauseParams,
    ) -> Result<SdkPauseSubscriptionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `PauseParams` | Yes |

Returns: `SdkPauseSubscriptionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::PauseParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = PauseParams::new(serde_json::from_str("{\"resume_at\":\"2026-10-10T12:00:00Z\",\"reason\":\"Customer request\"}")?);
    let result = client.subscriptions().pause("55", params).await?;
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

## resume

Resume a subscription

[API reference](https://sell.app/docs/api/subscriptions/resume-a-subscription) · Effect: **consequential**

```rust
pub async fn resume(
        &self,
        product_subscription: &str,
        params: ResumeParams,
    ) -> Result<SdkResumeSubscriptionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `ResumeParams` | Yes |

Returns: `SdkResumeSubscriptionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::ResumeParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ResumeParams::new(serde_json::from_str("{}")?);
    let result = client.subscriptions().resume("55", params).await?;
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

## update_payment_method

Update a subscription payment method

[API reference](https://sell.app/docs/api/subscriptions/update-payment-method) · Effect: **consequential**

```rust
pub async fn update_payment_method(
        &self,
        product_subscription: &str,
        params: UpdatePaymentMethodParams,
    ) -> Result<String, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `UpdatePaymentMethodParams` | Yes |

Returns: `String`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::UpdatePaymentMethodParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdatePaymentMethodParams::new(serde_json::from_str("{}")?);
    let result = client.subscriptions().update_payment_method("1", params).await?;
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

Documented HTTP responses: 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## preview_plan_change

Preview a subscription plan change

[API reference](https://sell.app/docs/api/subscriptions/preview-plan-change) · Effect: **consequential**

```rust
pub async fn preview_plan_change(
        &self,
        product_subscription: &str,
        params: PreviewPlanChangeParams,
    ) -> Result<String, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `PreviewPlanChangeParams` | Yes |

Returns: `String`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::PreviewPlanChangeParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = PreviewPlanChangeParams::new(serde_json::from_str("{\"target_variant_id\":4321,\"effective_timing\":\"immediate\",\"proration_behavior\":\"provider_default\"}")?);
    let result = client.subscriptions().preview_plan_change("1", params).await?;
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

Documented HTTP responses: 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## confirm_plan_change

Confirm a subscription plan change

[API reference](https://sell.app/docs/api/subscriptions/confirm-plan-change) · Effect: **consequential**

```rust
pub async fn confirm_plan_change(
        &self,
        product_subscription: &str,
        params: ConfirmPlanChangeParams,
    ) -> Result<String, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `ConfirmPlanChangeParams` | Yes |

Returns: `String`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::ConfirmPlanChangeParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ConfirmPlanChangeParams::new(serde_json::from_str("{\"target_variant_id\":4321,\"preview_token\":\"subprev_9c4b2f\"}")?);
    let result = client.subscriptions().confirm_plan_change("1", params).await?;
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

Documented HTTP responses: 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## preview_renewal_date

Preview a subscription renewal date change

[API reference](https://sell.app/docs/api/subscriptions/preview-renewal-date-change) · Effect: **consequential**

```rust
pub async fn preview_renewal_date(
        &self,
        product_subscription: &str,
        params: PreviewRenewalDateParams,
    ) -> Result<SdkPreviewSubscriptionRenewalDateChangeResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `PreviewRenewalDateParams` | Yes |

Returns: `SdkPreviewSubscriptionRenewalDateChangeResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::PreviewRenewalDateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = PreviewRenewalDateParams::new(serde_json::from_str("{\"renewal_date\":\"2026-10-01T12:00:00Z\",\"reason\":\"Align Maya's membership with the monthly reading circle.\"}")?);
    let result = client.subscriptions().preview_renewal_date("1", params).await?;
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

## confirm_renewal_date

Confirm a subscription renewal date change

[API reference](https://sell.app/docs/api/subscriptions/confirm-renewal-date-change) · Effect: **consequential**

```rust
pub async fn confirm_renewal_date(
        &self,
        product_subscription: &str,
        params: ConfirmRenewalDateParams,
    ) -> Result<SdkConfirmSubscriptionRenewalDateChangeResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `ConfirmRenewalDateParams` | Yes |

Returns: `SdkConfirmSubscriptionRenewalDateChangeResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::ConfirmRenewalDateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ConfirmRenewalDateParams::new(serde_json::from_str("{\"renewal_date\":\"2026-10-01T12:00:00Z\",\"preview_token\":\"subprev_project_library_55\",\"reason\":\"Align Maya's membership with the monthly reading circle.\"}")?);
    let result = client.subscriptions().confirm_renewal_date("1", params).await?;
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

## list_subscriptions

List subscriptions

[API reference](https://sell.app/docs/api/subscriptions/read-subscriptions) · Effect: **read**

```rust
pub async fn list_subscriptions(
        &self,
        params: ListSubscriptionsParams,
    ) -> Result<SdkListSubscriptionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListSubscriptionsParams` | Yes |

Returns: `SdkListSubscriptionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::ListSubscriptionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListSubscriptionsParams::default();
    let result = client.subscriptions().list_subscriptions(params).await?;
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

## search_subscriptions

Search subscriptions

[API reference](https://sell.app/docs/api/subscriptions/read-subscriptions) · Effect: **read**

```rust
pub async fn search_subscriptions(
        &self,
        params: SearchSubscriptionsParams,
    ) -> Result<SdkSearchSubscriptionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchSubscriptionsParams` | Yes |

Returns: `SdkSearchSubscriptionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::SearchSubscriptionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchSubscriptionsParams::new(serde_json::from_str("{\"search\":\"maya.chen@example.com\",\"status\":\"active\"}")?);
    let result = client.subscriptions().search_subscriptions(params).await?;
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

## get_subscription

Retrieve a subscription

[API reference](https://sell.app/docs/api/subscriptions/read-subscriptions) · Effect: **read**

```rust
pub async fn get_subscription(
        &self,
        product_subscription: &str,
        params: GetSubscriptionParams,
    ) -> Result<SdkGetSubscriptionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `GetSubscriptionParams` | Yes |

Returns: `SdkGetSubscriptionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions::GetSubscriptionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetSubscriptionParams::default();
    let result = client.subscriptions().get_subscription("991", params).await?;
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

