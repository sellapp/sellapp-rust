# products_addons

[All resources](../methods.md)

## list

List a product's add-ons

[API reference](https://sell.app/docs/api/add-ons/list-product-add-ons) · Effect: **read**

```rust
pub async fn list(
        &self,
        product: &str,
        params: ListParams,
    ) -> Result<SdkListProductSAddOnsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListProductSAddOnsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products_addons::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.products_addons().list("120", params).await?;
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

Replace a product's add-ons

[API reference](https://sell.app/docs/api/add-ons/replace-product-add-ons) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        product: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceProductSAddOnsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceProductSAddOnsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products_addons::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"resources\":[411,410]}")?);
    let result = client.products_addons().replace("120", params).await?;
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

