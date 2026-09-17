# promotions

[All resources](../methods.md)

## list

List promotions

[API reference](https://sell.app/docs/api/promotions/list-promotions) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListPromotionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListPromotionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.promotions().list(params).await?;
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

Create a promotion

[API reference](https://sell.app/docs/api/promotions/create-promotion) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreatePromotionResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreatePromotionResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"name\":\"Ship Week\",\"status\":\"active\",\"starts_at\":\"2026-08-01T00:00:00Z\",\"ends_at\":\"2026-08-08T00:00:00Z\",\"priority\":1,\"is_stackable\":false,\"max_redemptions\":500,\"phases\":[{\"discount_type\":\"percentage\",\"discount_value\":\"20\",\"ends_at\":\"2026-08-04T00:00:00Z\",\"max_redemptions\":200,\"minimum_amount\":\"10\"},{\"discount_type\":\"fixed\",\"discount_value\":\"5\",\"ends_at\":null,\"max_redemptions\":null,\"minimum_amount\":\"25\"}]}")?);
    let result = client.promotions().create(params).await?;
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

Search promotions

[API reference](https://sell.app/docs/api/promotions/search-promotions) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchPromotionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchPromotionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.promotions().search(params).await?;
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

Retrieve a promotion

[API reference](https://sell.app/docs/api/promotions/retrieve-promotion) · Effect: **read**

```rust
pub async fn get(
        &self,
        promotion: &str,
        params: GetParams,
    ) -> Result<SdkGetPromotionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetPromotionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.promotions().get("1", params).await?;
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

Update a promotion

[API reference](https://sell.app/docs/api/promotions/update-promotion) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        promotion: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplacePromotionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplacePromotionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"name\":\"One More Sprint\",\"is_stackable\":true}")?);
    let result = client.promotions().replace("1", params).await?;
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

Update a promotion

[API reference](https://sell.app/docs/api/promotions/update-promotion) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        promotion: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdatePromotionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdatePromotionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"name\":\"One More Sprint\",\"is_stackable\":true}")?);
    let result = client.promotions().update("1", params).await?;
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

Delete a promotion

[API reference](https://sell.app/docs/api/promotions/delete-promotion) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        promotion: &str,
        params: DeleteParams,
    ) -> Result<SdkDeletePromotionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeletePromotionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.promotions().delete("1", params).await?;
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

## restore

Restore a promotion

[API reference](https://sell.app/docs/api/promotions/restore-promotion) · Effect: **consequential**

```rust
pub async fn restore(
        &self,
        promotion: &str,
        params: RestoreParams,
    ) -> Result<SdkRestorePromotionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `&str` | Yes |
| params | `RestoreParams` | Yes |

Returns: `SdkRestorePromotionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions::RestoreParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RestoreParams::new(serde_json::from_str("{\"name\":\"Ship Week\",\"status\":\"active\",\"starts_at\":\"2026-08-01T00:00:00Z\",\"ends_at\":\"2026-08-08T00:00:00Z\",\"priority\":1,\"is_stackable\":false,\"max_redemptions\":500,\"phases\":[{\"discount_type\":\"percentage\",\"discount_value\":\"20\",\"ends_at\":\"2026-08-04T00:00:00Z\",\"max_redemptions\":200,\"minimum_amount\":\"10\"},{\"discount_type\":\"fixed\",\"discount_value\":\"5\",\"ends_at\":null,\"max_redemptions\":null,\"minimum_amount\":\"25\"}]}")?);
    let result = client.promotions().restore("1", params).await?;
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

