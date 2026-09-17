# upsell_offers

[All resources](../methods.md)

## list

List upsell offers

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListUpsellOffersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListUpsellOffersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::upsell_offers::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.upsell_offers().list(params).await?;
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

Create an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateUpsellOfferResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateUpsellOfferResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::upsell_offers::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"name\":\"One More Feature\",\"description\":\"Offer the advanced package with additional resources.\",\"is_active\":true,\"source_listing_id\":120,\"source_variant_id\":880,\"minimum_order_total_usd_cents\":1000,\"maximum_order_total_usd_cents\":25000,\"available_for_days\":14,\"max_accepts_per_customer\":1,\"items\":[{\"target_listing_id\":121,\"target_variant_id\":881,\"headline\":\"Upgrade today\",\"description\":\"Unlock dark mode, webhooks, and the premium launch checklist.\",\"discount_type\":\"percentage\",\"discount_value\":\"15.00\",\"maximum_discount_amount\":\"25.00\"}]}")?);
    let result = client.upsell_offers().create(params).await?;
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

Search upsell offers

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchUpsellOffersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchUpsellOffersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::upsell_offers::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":71}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.upsell_offers().search(params).await?;
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

Retrieve an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```rust
pub async fn get(
        &self,
        upsell_offer: &str,
        params: GetParams,
    ) -> Result<SdkGetUpsellOfferResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetUpsellOfferResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::upsell_offers::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.upsell_offers().get("71", params).await?;
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

Update an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        upsell_offer: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceUpsellOfferResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceUpsellOfferResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::upsell_offers::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"name\":\"One More Feature 2.0\",\"is_active\":false,\"expected_version\":1}")?);
    let result = client.upsell_offers().replace("71", params).await?;
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

Update an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        upsell_offer: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateUpsellOfferResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateUpsellOfferResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::upsell_offers::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"name\":\"One More Feature 2.0\",\"is_active\":false,\"expected_version\":1}")?);
    let result = client.upsell_offers().update("71", params).await?;
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

## delete

Delete an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        upsell_offer: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteUpsellOfferResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteUpsellOfferResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::upsell_offers::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.upsell_offers().delete("71", params).await?;
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

