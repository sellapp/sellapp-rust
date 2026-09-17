# product_variants_booking

[All resources](../methods.md)

## list_availability

List booking availability

[API reference](https://sell.app/docs/api/product-variants/list-booking-availability) · Effect: **read**

```rust
pub async fn list_availability(
        &self,
        product: &str,
        variant: &str,
        params: ListAvailabilityParams,
    ) -> Result<SdkListBookingAvailabilityResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ListAvailabilityParams` | Yes |

Returns: `SdkListBookingAvailabilityResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_booking::ListAvailabilityParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListAvailabilityParams::default();
    let result = client.product_variants_booking().list_availability("1", "1", params).await?;
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

## create_hold

Create a booking hold

[API reference](https://sell.app/docs/api/product-variants/create-booking-hold) · Effect: **consequential**

```rust
pub async fn create_hold(
        &self,
        product: &str,
        variant: &str,
        params: CreateHoldParams,
    ) -> Result<SdkCreateBookingHoldResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `CreateHoldParams` | Yes |

Returns: `SdkCreateBookingHoldResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_booking::CreateHoldParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateHoldParams::new(serde_json::from_str("{\"slot_start_at\":\"2026-06-22T14:00:00+00:00\",\"quantity\":1,\"customer_key\":\"visitor-session-123\",\"meta\":{\"customer_timezone\":\"America/New_York\"}}")?);
    let result = client.product_variants_booking().create_hold("1", "1", params).await?;
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

## release_hold

Release a booking hold

[API reference](https://sell.app/docs/api/product-variants/release-booking-hold) · Effect: **consequential**

```rust
pub async fn release_hold(
        &self,
        product: &str,
        hold: &str,
        params: ReleaseHoldParams,
    ) -> Result<SdkReleaseBookingHoldResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| hold | `&str` | Yes |
| params | `ReleaseHoldParams` | Yes |

Returns: `SdkReleaseBookingHoldResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_booking::ReleaseHoldParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReleaseHoldParams::new(serde_json::from_str("{\"customer_key\":\"visitor-session-123\"}")?);
    let result = client.product_variants_booking().release_hold("1", "string_example", params).await?;
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

Retrieve booking configuration

[API reference](https://sell.app/docs/api/bookings/retrieve-booking-configuration) · Effect: **read**

```rust
pub async fn get(
        &self,
        product: &str,
        variant: &str,
        params: GetParams,
    ) -> Result<SdkGetBookingConfigurationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetBookingConfigurationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_booking::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.product_variants_booking().get("41", "73", params).await?;
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

Update booking configuration

[API reference](https://sell.app/docs/api/bookings/update-booking-configuration) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        product: &str,
        variant: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceBookingConfigurationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceBookingConfigurationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_booking::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"timezone\":\"Europe/London\",\"duration_minutes\":60,\"capacity_per_slot\":1,\"min_notice_minutes\":1440,\"max_advance_days\":60}")?);
    let result = client.product_variants_booking().replace("41", "73", params).await?;
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

Update booking configuration

[API reference](https://sell.app/docs/api/bookings/update-booking-configuration) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        product: &str,
        variant: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateBookingConfigurationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateBookingConfigurationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_booking::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"timezone\":\"Europe/London\",\"duration_minutes\":60,\"capacity_per_slot\":1,\"min_notice_minutes\":1440,\"max_advance_days\":60}")?);
    let result = client.product_variants_booking().update("41", "73", params).await?;
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

