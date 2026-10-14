# subscriptions_actions

[All resources](../methods.md)

## list

List subscription actions

[API reference](https://sell.app/docs/api/subscriptions/list-subscription-actions) · Effect: **read**

```rust
pub async fn list(
        &self,
        product_subscription: &str,
        params: ListParams,
    ) -> Result<SdkListSubscriptionActionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListSubscriptionActionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions_actions::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.subscriptions_actions().list("124", params).await?;
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

## get

Retrieve a subscription action

[API reference](https://sell.app/docs/api/subscriptions/retrieve-a-subscription-action) · Effect: **read**

```rust
pub async fn get(
        &self,
        product_subscription: &str,
        action: &str,
        params: GetParams,
    ) -> Result<SdkGetSubscriptionActionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| action | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetSubscriptionActionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions_actions::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.subscriptions_actions().get("124", "4192", params).await?;
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

## dismiss

Dismiss a subscription action

[API reference](https://sell.app/docs/api/subscriptions/dismiss-a-subscription-action) · Effect: **consequential**

```rust
pub async fn dismiss(
        &self,
        product_subscription: &str,
        action: &str,
        params: DismissParams,
    ) -> Result<SdkDismissSubscriptionActionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `&str` | Yes |
| action | `&str` | Yes |
| params | `DismissParams` | Yes |

Returns: `SdkDismissSubscriptionActionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::subscriptions_actions::DismissParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DismissParams::new(serde_json::from_str("{\"note\":\"Confirmed with the customer that they no longer want the upgrade.\"}")?);
    let result = client.subscriptions_actions().dismiss("124", "4207", params).await?;
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

