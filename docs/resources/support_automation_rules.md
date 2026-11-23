# support_automation_rules

[All resources](../methods.md)

## list

List support automation rules

[API reference](https://sell.app/docs/api/support-automation-rules/list-support-automation-rules) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListSupportAutomationRulesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListSupportAutomationRulesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_rules::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.support_automation_rules().list(params).await?;
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

Create a support automation rule

[API reference](https://sell.app/docs/api/support-automation-rules/create-a-support-automation-rule) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateSupportAutomationRuleResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateSupportAutomationRuleResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_rules::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"name\":\"Expired download links\",\"response_template_id\":32,\"match_reason_source\":\"store\",\"match_reason_code\":\"download-link-expired\",\"match_product_ids\":[120],\"match_max_order_total_cents\":5000,\"max_prior_support_refund_count\":0,\"action_refund_kind\":\"partial\",\"action_refund_percent_basis\":5000,\"action_refund_cap_cents\":1000,\"action_close_outcome\":\"refunded_partial\"}")?);
    let result = client.support_automation_rules().create(params).await?;
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

Retrieve a support automation rule

[API reference](https://sell.app/docs/api/support-automation-rules/retrieve-a-support-automation-rule) · Effect: **read**

```rust
pub async fn get(
        &self,
        support_automation_rule: &str,
        params: GetParams,
    ) -> Result<SdkGetSupportAutomationRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_automation_rule | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetSupportAutomationRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_rules::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.support_automation_rules().get("7", params).await?;
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

Update a support automation rule

[API reference](https://sell.app/docs/api/support-automation-rules/update-a-support-automation-rule) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        support_automation_rule: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceSupportAutomationRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_automation_rule | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceSupportAutomationRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_rules::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"name\":\"Expired download links, first refund only\",\"clear\":[\"match_max_order_total_cents\"],\"expected_updated_at\":\"2026-07-03T09:20:00.000000Z\"}")?);
    let result = client.support_automation_rules().replace("7", params).await?;
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

Update a support automation rule

[API reference](https://sell.app/docs/api/support-automation-rules/update-a-support-automation-rule) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        support_automation_rule: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateSupportAutomationRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_automation_rule | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateSupportAutomationRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_rules::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"name\":\"Expired download links, first refund only\",\"clear\":[\"match_max_order_total_cents\"],\"expected_updated_at\":\"2026-07-03T09:20:00.000000Z\"}")?);
    let result = client.support_automation_rules().update("7", params).await?;
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

## update_state

Update a support automation rule state

[API reference](https://sell.app/docs/api/support-automation-rules/change-a-support-automation-rule-state) · Effect: **consequential**

```rust
pub async fn update_state(
        &self,
        support_automation_rule: &str,
        params: UpdateStateParams,
    ) -> Result<SdkUpdateSupportAutomationRuleStateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_automation_rule | `&str` | Yes |
| params | `UpdateStateParams` | Yes |

Returns: `SdkUpdateSupportAutomationRuleStateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_rules::UpdateStateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateStateParams::new(serde_json::from_str("{\"state\":\"active\",\"expected_updated_at\":\"2026-07-03T09:20:00.000000Z\"}")?);
    let result = client.support_automation_rules().update_state("1", params).await?;
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

## reorder

Reorder support automation rules

[API reference](https://sell.app/docs/api/support-automation-rules/reorder-support-automation-rules) · Effect: **consequential**

```rust
pub async fn reorder(
        &self,
        params: ReorderParams,
    ) -> Result<SdkReorderSupportAutomationRulesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReorderParams` | Yes |

Returns: `SdkReorderSupportAutomationRulesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_rules::ReorderParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReorderParams::new(serde_json::from_str("{\"ordered_rule_ids\":[7]}")?);
    let result = client.support_automation_rules().reorder(params).await?;
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

## dry_run

Dry run support automation rules

[API reference](https://sell.app/docs/api/support-automation-rules/dry-run-support-automation-rules) · Effect: **read**

```rust
pub async fn dry_run(
        &self,
        params: DryRunParams,
    ) -> Result<SdkDryRunSupportAutomationRulesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `DryRunParams` | Yes |

Returns: `SdkDryRunSupportAutomationRulesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_rules::DryRunParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DryRunParams::new(serde_json::from_str("4821")?);
    let result = client.support_automation_rules().dry_run(params).await?;
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

