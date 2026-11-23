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

## get_checkout

Retrieve checkout settings

[API reference](https://sell.app/docs/api/store-settings/checkout-settings) · Effect: **read**

```rust
pub async fn get_checkout(
        &self,
        params: GetCheckoutParams,
    ) -> Result<SdkGetCheckoutSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetCheckoutParams` | Yes |

Returns: `SdkGetCheckoutSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::GetCheckoutParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetCheckoutParams::default();
    let result = client.store_settings().get_checkout(params).await?;
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

## replace_checkout

Update checkout settings

[API reference](https://sell.app/docs/api/store-settings/checkout-settings) · Effect: **consequential**

```rust
pub async fn replace_checkout(
        &self,
        params: ReplaceCheckoutParams,
    ) -> Result<SdkReplaceCheckoutSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceCheckoutParams` | Yes |

Returns: `SdkReplaceCheckoutSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplaceCheckoutParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceCheckoutParams::new(serde_json::from_str("{\"shopping_cart_enabled\":true,\"customer_email_required\":true,\"allow_vpn_purchases\":true,\"blacklist_on_dispute\":true,\"minimum_spend\":\"5.00\",\"billing_descriptor\":\"LAUNCH LAB\",\"attempts_per_customer\":5,\"attempts_per_ip\":20,\"attempts_per_email\":null,\"attempts_per_fingerprint\":null,\"rate_limit_window_seconds\":3600,\"crypto\":{\"underpaid_percentage\":2,\"minimum_confirmations\":2}}")?);
    let result = client.store_settings().replace_checkout(params).await?;
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

## update_checkout

Update checkout settings

[API reference](https://sell.app/docs/api/store-settings/checkout-settings) · Effect: **consequential**

```rust
pub async fn update_checkout(
        &self,
        params: UpdateCheckoutParams,
    ) -> Result<SdkUpdateCheckoutSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateCheckoutParams` | Yes |

Returns: `SdkUpdateCheckoutSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdateCheckoutParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateCheckoutParams::new(serde_json::from_str("{\"minimum_spend\":\"10.00\",\"attempts_per_email\":10}")?);
    let result = client.store_settings().update_checkout(params).await?;
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

## get_taxes

Retrieve tax settings

[API reference](https://sell.app/docs/api/store-settings/tax-settings) · Effect: **read**

```rust
pub async fn get_taxes(
        &self,
        params: GetTaxesParams,
    ) -> Result<SdkGetTaxSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetTaxesParams` | Yes |

Returns: `SdkGetTaxSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::GetTaxesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetTaxesParams::default();
    let result = client.store_settings().get_taxes(params).await?;
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

## replace_taxes

Update tax settings

[API reference](https://sell.app/docs/api/store-settings/tax-settings) · Effect: **consequential**

```rust
pub async fn replace_taxes(
        &self,
        params: ReplaceTaxesParams,
    ) -> Result<SdkReplaceTaxSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceTaxesParams` | Yes |

Returns: `SdkReplaceTaxSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplaceTaxesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceTaxesParams::new(serde_json::from_str("{\"vat_enabled\":true,\"vat_inclusive_pricing\":true,\"collect_billing_details\":false}")?);
    let result = client.store_settings().replace_taxes(params).await?;
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

## update_taxes

Update tax settings

[API reference](https://sell.app/docs/api/store-settings/tax-settings) · Effect: **consequential**

```rust
pub async fn update_taxes(
        &self,
        params: UpdateTaxesParams,
    ) -> Result<SdkUpdateTaxSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateTaxesParams` | Yes |

Returns: `SdkUpdateTaxSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdateTaxesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateTaxesParams::new(serde_json::from_str("{\"vat_inclusive_pricing\":true}")?);
    let result = client.store_settings().update_taxes(params).await?;
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

## get_customer_emails

Retrieve customer email settings

[API reference](https://sell.app/docs/api/store-settings/customer-email-settings) · Effect: **read**

```rust
pub async fn get_customer_emails(
        &self,
        params: GetCustomerEmailsParams,
    ) -> Result<SdkGetCustomerEmailSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetCustomerEmailsParams` | Yes |

Returns: `SdkGetCustomerEmailSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::GetCustomerEmailsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetCustomerEmailsParams::default();
    let result = client.store_settings().get_customer_emails(params).await?;
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

## replace_customer_emails

Update customer email settings

[API reference](https://sell.app/docs/api/store-settings/customer-email-settings) · Effect: **consequential**

```rust
pub async fn replace_customer_emails(
        &self,
        params: ReplaceCustomerEmailsParams,
    ) -> Result<SdkReplaceCustomerEmailSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceCustomerEmailsParams` | Yes |

Returns: `SdkReplaceCustomerEmailSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplaceCustomerEmailsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceCustomerEmailsParams::new(serde_json::from_str("{\"send_delivery_email\":true,\"send_payment_failure_email\":false}")?);
    let result = client.store_settings().replace_customer_emails(params).await?;
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

## update_customer_emails

Update customer email settings

[API reference](https://sell.app/docs/api/store-settings/customer-email-settings) · Effect: **consequential**

```rust
pub async fn update_customer_emails(
        &self,
        params: UpdateCustomerEmailsParams,
    ) -> Result<SdkUpdateCustomerEmailSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateCustomerEmailsParams` | Yes |

Returns: `SdkUpdateCustomerEmailSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdateCustomerEmailsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateCustomerEmailsParams::new(serde_json::from_str("{\"send_payment_failure_email\":false}")?);
    let result = client.store_settings().update_customer_emails(params).await?;
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

## get_store_alerts

Retrieve store alert settings

[API reference](https://sell.app/docs/api/store-settings/store-alert-settings) · Effect: **read**

```rust
pub async fn get_store_alerts(
        &self,
        params: GetStoreAlertsParams,
    ) -> Result<SdkGetStoreAlertSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetStoreAlertsParams` | Yes |

Returns: `SdkGetStoreAlertSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::GetStoreAlertsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetStoreAlertsParams::default();
    let result = client.store_settings().get_store_alerts(params).await?;
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

## replace_store_alerts

Update store alert settings

[API reference](https://sell.app/docs/api/store-settings/store-alert-settings) · Effect: **consequential**

```rust
pub async fn replace_store_alerts(
        &self,
        params: ReplaceStoreAlertsParams,
    ) -> Result<SdkReplaceStoreAlertSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceStoreAlertsParams` | Yes |

Returns: `SdkReplaceStoreAlertSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplaceStoreAlertsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceStoreAlertsParams::new(serde_json::from_str("{\"sale_emails_enabled\":false}")?);
    let result = client.store_settings().replace_store_alerts(params).await?;
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

## update_store_alerts

Update store alert settings

[API reference](https://sell.app/docs/api/store-settings/store-alert-settings) · Effect: **consequential**

```rust
pub async fn update_store_alerts(
        &self,
        params: UpdateStoreAlertsParams,
    ) -> Result<SdkUpdateStoreAlertSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateStoreAlertsParams` | Yes |

Returns: `SdkUpdateStoreAlertSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdateStoreAlertsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateStoreAlertsParams::new(serde_json::from_str("{\"sale_emails_enabled\":false}")?);
    let result = client.store_settings().update_store_alerts(params).await?;
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

## get_personalization

Retrieve personalization settings

[API reference](https://sell.app/docs/api/store-settings/personalization-settings) · Effect: **read**

```rust
pub async fn get_personalization(
        &self,
        params: GetPersonalizationParams,
    ) -> Result<SdkGetPersonalizationSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetPersonalizationParams` | Yes |

Returns: `SdkGetPersonalizationSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::GetPersonalizationParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetPersonalizationParams::default();
    let result = client.store_settings().get_personalization(params).await?;
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

## replace_personalization

Update personalization settings

[API reference](https://sell.app/docs/api/store-settings/personalization-settings) · Effect: **consequential**

```rust
pub async fn replace_personalization(
        &self,
        params: ReplacePersonalizationParams,
    ) -> Result<SdkReplacePersonalizationSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplacePersonalizationParams` | Yes |

Returns: `SdkReplacePersonalizationSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplacePersonalizationParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplacePersonalizationParams::new(serde_json::from_str("{\"support_email\":\"support@launch-lab.example.com\",\"trustpilot_email\":null,\"sender_name\":\"Launch Lab\",\"sender_email\":\"orders@launch-lab.example.com\",\"store_address\":\"651 N Broad St, Suite 206\",\"store_city\":\"Middletown\",\"store_state\":\"Delaware\",\"store_zip\":\"19709\",\"store_country\":\"United States\",\"store_tax\":\"EIN 98-7654321\",\"back_link_label\":\"Back to Launch Lab\",\"back_link_url\":\"https://launch-lab.example.com\"}")?);
    let result = client.store_settings().replace_personalization(params).await?;
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

## update_personalization

Update personalization settings

[API reference](https://sell.app/docs/api/store-settings/personalization-settings) · Effect: **consequential**

```rust
pub async fn update_personalization(
        &self,
        params: UpdatePersonalizationParams,
    ) -> Result<SdkUpdatePersonalizationSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdatePersonalizationParams` | Yes |

Returns: `SdkUpdatePersonalizationSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdatePersonalizationParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdatePersonalizationParams::new(serde_json::from_str("{\"back_link_label\":\"Return to the shop\",\"back_link_url\":\"https://launch-lab.example.com/shop\"}")?);
    let result = client.store_settings().update_personalization(params).await?;
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

## replace_crypto_checkout

Update crypto checkout settings

[API reference](https://sell.app/docs/api/store-settings/crypto-checkout-settings) · Effect: **consequential**

```rust
pub async fn replace_crypto_checkout(
        &self,
        params: ReplaceCryptoCheckoutParams,
    ) -> Result<SdkReplaceCryptoCheckoutSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceCryptoCheckoutParams` | Yes |

Returns: `SdkReplaceCryptoCheckoutSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::ReplaceCryptoCheckoutParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceCryptoCheckoutParams::new(serde_json::from_str("{\"underpaid_percentage\":1,\"minimum_confirmations\":3}")?);
    let result = client.store_settings().replace_crypto_checkout(params).await?;
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

## update_crypto_checkout

Update crypto checkout settings

[API reference](https://sell.app/docs/api/store-settings/crypto-checkout-settings) · Effect: **consequential**

```rust
pub async fn update_crypto_checkout(
        &self,
        params: UpdateCryptoCheckoutParams,
    ) -> Result<SdkUpdateCryptoCheckoutSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `UpdateCryptoCheckoutParams` | Yes |

Returns: `SdkUpdateCryptoCheckoutSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_settings::UpdateCryptoCheckoutParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateCryptoCheckoutParams::new(serde_json::from_str("{\"minimum_confirmations\":3}")?);
    let result = client.store_settings().update_crypto_checkout(params).await?;
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

