# orders_line_items

[All resources](../methods.md)

## list

List an order's line items

[API reference](https://sell.app/docs/api/order-line-items/list-an-orders-line-items) · Effect: **read**

```rust
pub async fn list(
        &self,
        order: &str,
        params: ListParams,
    ) -> Result<SdkListOrderSLineItemsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListOrderSLineItemsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders_line_items::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.orders_line_items().list("4001", params).await?;
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

Search an order's line items

[API reference](https://sell.app/docs/api/order-line-items/search-an-orders-line-items) · Effect: **read**

```rust
pub async fn search(
        &self,
        order: &str,
        params: SearchParams,
    ) -> Result<SdkSearchOrderSLineItemsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `SearchParams` | Yes |

Returns: `SdkSearchOrderSLineItemsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders_line_items::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{}")?);
    let result = client.orders_line_items().search("4001", params).await?;
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

Retrieve an order's line item

[API reference](https://sell.app/docs/api/order-line-items/retrieve-an-orders-line-item) · Effect: **read**

```rust
pub async fn get(
        &self,
        order: &str,
        line_item: &str,
        params: GetParams,
    ) -> Result<SdkGetOrderSLineItemResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| line_item | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetOrderSLineItemResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::orders_line_items::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.orders_line_items().get("4001", "9001", params).await?;
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

