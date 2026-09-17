# bookings_calendar_events

[All resources](../methods.md)

## list

List booking date overrides

[API reference](https://sell.app/docs/api/bookings/list-booking-date-overrides) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListBookingDateOverridesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListBookingDateOverridesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bookings_calendar_events::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.bookings_calendar_events().list(params).await?;
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

## set

Set booking date availability

[API reference](https://sell.app/docs/api/bookings/set-booking-date-availability) · Effect: **consequential**

```rust
pub async fn set(
        &self,
        params: SetParams,
    ) -> Result<SdkSetBookingDateAvailabilityResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SetParams` | Yes |

Returns: `SdkSetBookingDateAvailabilityResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bookings_calendar_events::SetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SetParams::new(serde_json::from_str("{\"product_variant_id\":73,\"dates\":[\"2028-03-26\",\"2028-03-27\"],\"available\":false}")?);
    let result = client.bookings_calendar_events().set(params).await?;
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

