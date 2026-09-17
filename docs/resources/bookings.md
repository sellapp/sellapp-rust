# bookings

[All resources](../methods.md)

## list

List appointments

[API reference](https://sell.app/docs/api/bookings/list-appointments) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListAppointmentsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListAppointmentsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bookings::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.bookings().list(params).await?;
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

## search

Search appointments

[API reference](https://sell.app/docs/api/bookings/search-appointments) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchAppointmentsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchAppointmentsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bookings::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":\"018f61d6-1c46-7b42-8a94-522bc6b5c53f\"}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.bookings().search(params).await?;
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

Retrieve an appointment

[API reference](https://sell.app/docs/api/bookings/retrieve-an-appointment) · Effect: **read**

```rust
pub async fn get(
        &self,
        booking: &str,
        params: GetParams,
    ) -> Result<SdkGetAppointmentResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetAppointmentResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bookings::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.bookings().get("018f61d6-1c46-7b42-8a94-522bc6b5c53f", params).await?;
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

Update an appointment

[API reference](https://sell.app/docs/api/bookings/update-an-appointment) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        booking: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateAppointmentResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateAppointmentResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bookings::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"slot_start_at\":\"2028-03-27T10:00:00+01:00\",\"timezone\":\"Europe/London\"}")?);
    let result = client.bookings().update("018f61d6-1c46-7b42-8a94-522bc6b5c53f", params).await?;
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

## cancel

Cancel an appointment

[API reference](https://sell.app/docs/api/bookings/update-an-appointment) · Effect: **consequential**

```rust
pub async fn cancel(
        &self,
        booking: &str,
        params: CancelParams,
    ) -> Result<SdkCancelAppointmentResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `&str` | Yes |
| params | `CancelParams` | Yes |

Returns: `SdkCancelAppointmentResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bookings::CancelParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CancelParams::new(serde_json::from_str("{\"status\":\"cancelled\"}")?);
    let result = client.bookings().cancel("018f61d6-1c46-7b42-8a94-522bc6b5c53f", params).await?;
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

