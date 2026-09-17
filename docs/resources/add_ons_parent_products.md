# add_ons_parent_products

[All resources](../methods.md)

## list

List an add-on's parent products

[API reference](https://sell.app/docs/api/add-ons/list-parent-products) · Effect: **read**

```rust
pub async fn list(
        &self,
        addon: &str,
        params: ListParams,
    ) -> Result<SdkListAddOnSParentProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListAddOnSParentProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::add_ons_parent_products::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.add_ons_parent_products().list("1", params).await?;
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

Replace an add-on's parent products

[API reference](https://sell.app/docs/api/add-ons/replace-parent-products) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        addon: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceAddOnSParentProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceAddOnSParentProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::add_ons_parent_products::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"resources\":[121,120]}")?);
    let result = client.add_ons_parent_products().replace("410", params).await?;
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

