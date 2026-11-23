# support_automation_settings

[All resources](../methods.md)

## get

Retrieve support automation settings

[API reference](https://sell.app/docs/api/support-automation-settings/retrieve-support-automation-settings) · Effect: **read**

```rust
pub async fn get(
        &self,
        params: GetParams,
    ) -> Result<SdkGetSupportAutomationSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetParams` | Yes |

Returns: `SdkGetSupportAutomationSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_settings::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.support_automation_settings().get(params).await?;
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

## replace

Update support automation settings

[API reference](https://sell.app/docs/api/support-automation-settings/update-support-automation-settings) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        params: ReplaceParams,
    ) -> Result<SdkReplaceSupportAutomationSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceSupportAutomationSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_settings::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"automation_enabled\":true,\"daily_refund_cap_cents\":5000,\"expected_automation_enabled\":false,\"expected_daily_refund_cap_cents\":null}")?);
    let result = client.support_automation_settings().replace(params).await?;
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

## update

Update support automation settings

[API reference](https://sell.app/docs/api/support-automation-settings/update-support-automation-settings) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        params: UpdateParams,
    ) -> Result<SdkUpdateSupportAutomationSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateSupportAutomationSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_automation_settings::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"automation_enabled\":true,\"daily_refund_cap_cents\":5000,\"expected_automation_enabled\":false,\"expected_daily_refund_cap_cents\":null}")?);
    let result = client.support_automation_settings().update(params).await?;
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

