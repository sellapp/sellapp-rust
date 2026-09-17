# bundle_items

[All resources](../methods.md)

## get

Retrieve a bundle item

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```rust
pub async fn get(
        &self,
        bundle: &str,
        item: &str,
        params: GetParams,
    ) -> Result<SdkGetBundleItemResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| bundle | `&str` | Yes |
| item | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetBundleItemResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bundle_items::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.bundle_items().get("1", "2", params).await?;
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

## list

List bundle items

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```rust
pub async fn list(
        &self,
        bundle: &str,
        params: ListParams,
    ) -> Result<SdkListBundleItemsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| bundle | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListBundleItemsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bundle_items::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.bundle_items().list("1", params).await?;
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

## attach

Attach bundle items

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```rust
pub async fn attach(
        &self,
        bundle: &str,
        params: AttachParams,
    ) -> Result<SdkAttachBundleItemsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| bundle | `&str` | Yes |
| params | `AttachParams` | Yes |

Returns: `SdkAttachBundleItemsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bundle_items::AttachParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = AttachParams::new(serde_json::from_str("{\"resources\":{\"1\":{\"quantity\":1}}}")?);
    let result = client.bundle_items().attach("1", params).await?;
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

## detach

Detach bundle items

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```rust
pub async fn detach(
        &self,
        bundle: &str,
        params: DetachParams,
    ) -> Result<SdkDetachBundleItemsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| bundle | `&str` | Yes |
| params | `DetachParams` | Yes |

Returns: `SdkDetachBundleItemsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::bundle_items::DetachParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DetachParams::new(serde_json::from_str("{\"resources\":[1]}")?);
    let result = client.bundle_items().detach("1", params).await?;
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

