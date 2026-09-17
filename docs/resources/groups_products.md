# groups_products

[All resources](../methods.md)

## add

Add products to group

[API reference](https://sell.app/docs/api/groups/add-products-to-group) · Effect: **consequential**

```rust
pub async fn add(
        &self,
        group: &str,
        params: AddParams,
    ) -> Result<SdkAddProductsToGroupResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `&str` | Yes |
| params | `AddParams` | Yes |

Returns: `SdkAddProductsToGroupResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::groups_products::AddParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = AddParams::new(serde_json::from_str("{\"resources\":[1]}")?);
    let result = client.groups_products().add("1", params).await?;
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

## remove

Remove products from group

[API reference](https://sell.app/docs/api/groups/remove-products-from-group) · Effect: **consequential**

```rust
pub async fn remove(
        &self,
        group: &str,
        params: RemoveParams,
    ) -> Result<SdkRemoveProductsFromGroupResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `&str` | Yes |
| params | `RemoveParams` | Yes |

Returns: `SdkRemoveProductsFromGroupResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::groups_products::RemoveParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RemoveParams::new(serde_json::from_str("{\"resources\":[1]}")?);
    let result = client.groups_products().remove("1", params).await?;
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

List all products within group

[API reference](https://sell.app/docs/api/groups/list-all-products-within-group) · Effect: **read**

```rust
pub async fn list(
        &self,
        group: &str,
        params: ListParams,
    ) -> Result<SdkListProductsWithinGroupResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListProductsWithinGroupResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::groups_products::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.groups_products().list("1", params).await?;
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

Replace ordered group products

[API reference](https://sell.app/docs/api/groups/list-all-products-within-group) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        group: &str,
        params: ReplaceParams,
    ) -> Result<SdkSyncGroupProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkSyncGroupProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::groups_products::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"product_ids\":[120,121]}")?);
    let result = client.groups_products().replace("42", params).await?;
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

List specific product within group

[API reference](https://sell.app/docs/api/groups/list-specific-product-within-group) · Effect: **read**

```rust
pub async fn get(
        &self,
        group: &str,
        product: &str,
        params: GetParams,
    ) -> Result<SdkGetProductWithinGroupResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `&str` | Yes |
| product | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetProductWithinGroupResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::groups_products::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.groups_products().get("1", "1", params).await?;
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

## search

Search products within group

[API reference](https://sell.app/docs/api/groups/search-products-within-group) · Effect: **read**

```rust
pub async fn search(
        &self,
        group: &str,
        params: SearchParams,
    ) -> Result<SdkSearchProductsWithinGroupResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `&str` | Yes |
| params | `SearchParams` | Yes |

Returns: `SdkSearchProductsWithinGroupResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::groups_products::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.groups_products().search("1", params).await?;
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

