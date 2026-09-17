# invoices

[All resources](../methods.md)

## list

List all invoices

[API reference](https://sell.app/docs/api/invoices/list-all-invoices) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListInvoicesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListInvoicesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.invoices().list(params).await?;
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

Create an invoice

[API reference](https://sell.app/docs/api/invoices/create-an-invoice) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateInvoiceResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateInvoiceResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"customer_email\":\"maya.chen@example.com\",\"payment_method\":\"STRIPE\",\"product_variants\":{\"4321\":{\"quantity\":1}}}")?);
    let result = client.invoices().create(params).await?;
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

## search

Search invoices

[API reference](https://sell.app/docs/api/invoices/search-invoices) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchInvoicesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchInvoicesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"id\":\"1\",\"sort\":\"-created_at\"}")?);
    let result = client.invoices().search(params).await?;
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

Retrieve an invoice

[API reference](https://sell.app/docs/api/invoices/retrieve-an-invoice) · Effect: **read**

```rust
pub async fn get(
        &self,
        invoice: &str,
        params: GetParams,
    ) -> Result<SdkGetInvoiceResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetInvoiceResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.invoices().get("1", params).await?;
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

## go_to_checkout

Create a checkout session

[API reference](https://sell.app/docs/api/invoices/create-a-checkout-session) · Effect: **consequential**

```rust
pub async fn go_to_checkout(
        &self,
        invoice: &str,
        params: GoToCheckoutParams,
    ) -> Result<SdkCreateCheckoutSessionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `GoToCheckoutParams` | Yes |

Returns: `SdkCreateCheckoutSessionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::GoToCheckoutParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GoToCheckoutParams::default();
    let result = client.invoices().go_to_checkout("9001", params).await?;
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_deliverables

View invoice deliverables

[API reference](https://sell.app/docs/api/invoices/view-invoice-deliverables) · Effect: **read**

```rust
pub async fn get_deliverables(
        &self,
        invoice: &str,
        params: GetDeliverablesParams,
    ) -> Result<SdkGetInvoiceDeliverablesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `GetDeliverablesParams` | Yes |

Returns: `SdkGetInvoiceDeliverablesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::GetDeliverablesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetDeliverablesParams::default();
    let result = client.invoices().get_deliverables("1234", params).await?;
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

Mark pending invoice completed

[API reference](https://sell.app/docs/api/invoices/mark-pending-invoice-completed) · Effect: **consequential**

```rust
pub async fn mark_completed(
        &self,
        invoice: &str,
        params: MarkCompletedParams,
    ) -> Result<SdkMarkPendingInvoiceCompletedResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `MarkCompletedParams` | Yes |

Returns: `SdkMarkPendingInvoiceCompletedResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::MarkCompletedParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = MarkCompletedParams::new(serde_json::from_str("{\"expected_status\":\"PENDING\"}")?);
    let result = client.invoices().mark_completed("1", params).await?;
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

Mark pending invoice voided

[API reference](https://sell.app/docs/api/invoices/mark-pending-invoice-voided) · Effect: **consequential**

```rust
pub async fn mark_voided(
        &self,
        invoice: &str,
        params: MarkVoidedParams,
    ) -> Result<SdkMarkPendingInvoiceVoidedResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `MarkVoidedParams` | Yes |

Returns: `SdkMarkPendingInvoiceVoidedResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::MarkVoidedParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = MarkVoidedParams::new(serde_json::from_str("{\"expected_status\":\"PENDING\"}")?);
    let result = client.invoices().mark_voided("1", params).await?;
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

## issue_replacement

Issue replacement for completed invoice

[API reference](https://sell.app/docs/api/invoices/issue-replacement-for-completed-invoice) · Effect: **consequential**

```rust
pub async fn issue_replacement(
        &self,
        invoice: &str,
        params: IssueReplacementParams,
    ) -> Result<SdkIssueReplacementForCompletedInvoiceResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `IssueReplacementParams` | Yes |

Returns: `SdkIssueReplacementForCompletedInvoiceResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::IssueReplacementParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = IssueReplacementParams::new(serde_json::from_str("{\"product_variants\":[117214]}")?);
    let result = client.invoices().issue_replacement("1", params).await?;
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

Update invoice status

[API reference](https://sell.app/docs/api/invoices/update-invoice-status) · Effect: **consequential**

```rust
pub async fn update_status(
        &self,
        invoice: &str,
        params: UpdateStatusParams,
    ) -> Result<SdkUpdateInvoiceStatusResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `UpdateStatusParams` | Yes |

Returns: `SdkUpdateInvoiceStatusResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::UpdateStatusParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateStatusParams::new(serde_json::from_str("{\"status\":\"REVIEW\",\"expected_status\":\"PENDING\"}")?);
    let result = client.invoices().update_status("1", params).await?;
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

## create_refund

Create invoice refund

[API reference](https://sell.app/docs/api/invoices/refund-an-invoice) · Effect: **consequential**

```rust
pub async fn create_refund(
        &self,
        invoice: &str,
        params: CreateRefundParams,
    ) -> Result<SdkCreateInvoiceRefundResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `CreateRefundParams` | Yes |

Returns: `SdkCreateInvoiceRefundResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::CreateRefundParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateRefundParams::new(serde_json::from_str("{\"amount\":\"12.50\"}")?);
    let result = client.invoices().create_refund("1", params).await?;
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

## retry_fulfillment

Create fulfillment retry

[API reference](https://sell.app/docs/api/invoices/retry-invoice-fulfillment) · Effect: **consequential**

```rust
pub async fn retry_fulfillment(
        &self,
        invoice: &str,
        params: RetryFulfillmentParams,
    ) -> Result<SdkCreateFulfillmentRetryResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `RetryFulfillmentParams` | Yes |

Returns: `SdkCreateFulfillmentRetryResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::RetryFulfillmentParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RetryFulfillmentParams::new(serde_json::from_str("{}")?);
    let result = client.invoices().retry_fulfillment("1", params).await?;
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

## retry_dynamic_delivery

Create dynamic delivery retry

[API reference](https://sell.app/docs/api/invoices/retry-dynamic-delivery) · Effect: **consequential**

```rust
pub async fn retry_dynamic_delivery(
        &self,
        invoice: &str,
        params: RetryDynamicDeliveryParams,
    ) -> Result<SdkCreateDynamicDeliveryRetryResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `RetryDynamicDeliveryParams` | Yes |

Returns: `SdkCreateDynamicDeliveryRetryResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::RetryDynamicDeliveryParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RetryDynamicDeliveryParams::new(serde_json::from_str("{\"delivered_product_id\":42}")?);
    let result = client.invoices().retry_dynamic_delivery("1", params).await?;
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

## notify_fulfillment

Create fulfillment notifications

[API reference](https://sell.app/docs/api/invoices/resend-invoice-deliverables) · Effect: **consequential**

```rust
pub async fn notify_fulfillment(
        &self,
        invoice: &str,
        params: NotifyFulfillmentParams,
    ) -> Result<SdkCreateFulfillmentNotificationsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `&str` | Yes |
| params | `NotifyFulfillmentParams` | Yes |

Returns: `SdkCreateFulfillmentNotificationsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::invoices::NotifyFulfillmentParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = NotifyFulfillmentParams::new(serde_json::from_str("{}")?);
    let result = client.invoices().notify_fulfillment("1", params).await?;
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

