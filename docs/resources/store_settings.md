# store_settings

[All resources](../methods.md)

## get

Retrieve store settings

[API reference](https://sell.app/docs/api/store-settings/retrieve-store-settings) · Effect: **read**

```rust
pub async fn get(
        &self,
        params: GetParams,
    ) -> Result<SdkGetStoreSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetParams` | Yes |

Returns: `SdkGetStoreSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.store_settings().get(params).await?;
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

## replace_general

Update general store settings

[API reference](https://sell.app/docs/api/store-settings/update-general-settings) · Effect: **consequential**

```rust
pub async fn replace_general(
        &self,
        params: ReplaceGeneralParams,
    ) -> Result<SdkReplaceGeneralStoreSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceGeneralParams` | Yes |

Returns: `SdkReplaceGeneralStoreSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplaceGeneralParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceGeneralParams::new(serde_json::from_str("{\"name\":\"Launch Lab\",\"visibility\":\"HIDDEN\",\"timezone\":\"Europe/London\",\"currency\":\"USD\"}")?);
    let result = client.store_settings().replace_general(params).await?;
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

## update_general

Update general store settings

[API reference](https://sell.app/docs/api/store-settings/update-general-settings) · Effect: **consequential**

```rust
pub async fn update_general(
        &self,
        params: UpdateGeneralParams,
    ) -> Result<SdkUpdateGeneralStoreSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateGeneralParams` | Yes |

Returns: `SdkUpdateGeneralStoreSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdateGeneralParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateGeneralParams::new(serde_json::from_str("{\"name\":\"Launch Lab\"}")?);
    let result = client.store_settings().update_general(params).await?;
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

## replace_analytics

Update analytics settings

[API reference](https://sell.app/docs/api/store-settings/update-analytics-settings) · Effect: **consequential**

```rust
pub async fn replace_analytics(
        &self,
        params: ReplaceAnalyticsParams,
    ) -> Result<SdkReplaceAnalyticsSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceAnalyticsParams` | Yes |

Returns: `SdkReplaceAnalyticsSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplaceAnalyticsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceAnalyticsParams::new(serde_json::from_str("{\"ga4_measurement_id\":null}")?);
    let result = client.store_settings().replace_analytics(params).await?;
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

## update_analytics

Update analytics settings

[API reference](https://sell.app/docs/api/store-settings/update-analytics-settings) · Effect: **consequential**

```rust
pub async fn update_analytics(
        &self,
        params: UpdateAnalyticsParams,
    ) -> Result<SdkUpdateAnalyticsSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateAnalyticsParams` | Yes |

Returns: `SdkUpdateAnalyticsSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdateAnalyticsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateAnalyticsParams::new(serde_json::from_str("{\"ga4_measurement_id\":null}")?);
    let result = client.store_settings().update_analytics(params).await?;
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

## replace_marketing

Update marketing settings

[API reference](https://sell.app/docs/api/store-settings/update-marketing-settings) · Effect: **consequential**

```rust
pub async fn replace_marketing(
        &self,
        params: ReplaceMarketingParams,
    ) -> Result<SdkReplaceMarketingSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceMarketingParams` | Yes |

Returns: `SdkReplaceMarketingSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplaceMarketingParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceMarketingParams::new(serde_json::from_str("{\"abandoned_cart\":{\"enabled\":false}}")?);
    let result = client.store_settings().replace_marketing(params).await?;
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

## update_marketing

Update marketing settings

[API reference](https://sell.app/docs/api/store-settings/update-marketing-settings) · Effect: **consequential**

```rust
pub async fn update_marketing(
        &self,
        params: UpdateMarketingParams,
    ) -> Result<SdkUpdateMarketingSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateMarketingParams` | Yes |

Returns: `SdkUpdateMarketingSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdateMarketingParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateMarketingParams::new(serde_json::from_str("{\"abandoned_cart\":{\"enabled\":false}}")?);
    let result = client.store_settings().update_marketing(params).await?;
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

