# coupons

[All resources](../methods.md)

## list

List all coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.coupons().list(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create

Create a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateCouponResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateCouponResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"code\":\"PLAN10\",\"type\":\"PERCENTAGE\",\"discount\":10,\"store_wide\":false,\"products\":[123,456],\"product_variants\":[1001,1002]}")?);
    let result = client.coupons().create(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 201, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn get(
        &self,
        coupon: &str,
        params: GetParams,
    ) -> Result<SdkGetCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.coupons().get("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace

Update a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        coupon: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"store_wide\":false,\"products\":[123],\"product_variants\":[1001,1002]}")?);
    let result = client.coupons().replace("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update

Update a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        coupon: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"store_wide\":false,\"products\":[123],\"product_variants\":[1001,1002]}")?);
    let result = client.coupons().update("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## delete

Delete a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        coupon: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.coupons().delete("1", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.coupons().search(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_create

Batch create coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn batch_create(
        &self,
        params: BatchCreateParams,
    ) -> Result<SdkBatchCreateCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchCreateParams` | Yes |

Returns: `SdkBatchCreateCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::BatchCreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchCreateParams::new(serde_json::from_str("{\"resources\":[{\"code\":\"STARTER10\",\"type\":\"PERCENTAGE\",\"discount\":10,\"store_wide\":false,\"products\":[123],\"product_variants\":[1001]}]}")?);
    let result = client.coupons().batch_create(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 201, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_update

Batch update coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn batch_update(
        &self,
        params: BatchUpdateParams,
    ) -> Result<SdkBatchUpdateCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchUpdateParams` | Yes |

Returns: `SdkBatchUpdateCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::BatchUpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchUpdateParams::new(serde_json::from_str("{\"resources\":{\"1\":{\"store_wide\":false,\"products\":[123],\"product_variants\":[1001,1002]}}}")?);
    let result = client.coupons().batch_update(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_delete

Batch delete coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn batch_delete(
        &self,
        params: BatchDeleteParams,
    ) -> Result<SdkBatchDeleteCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchDeleteParams` | Yes |

Returns: `SdkBatchDeleteCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::BatchDeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchDeleteParams::new(serde_json::from_str("{\"resources\":[1,2]}")?);
    let result = client.coupons().batch_delete(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_list_coupons

List all coupons

[API reference](https://sell.app/docs/api/coupons/list-all-coupons) · Effect: **read**

```rust
pub async fn v_2_list_coupons(
        &self,
        params: V2ListCouponsParams,
    ) -> Result<SdkV2ListCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2ListCouponsParams` | Yes |

Returns: `SdkV2ListCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2ListCouponsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ListCouponsParams::default();
    let result = client.coupons().v_2_list_coupons(params).await?;
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

## v_2_create_coupon

Create a coupon

[API reference](https://sell.app/docs/api/coupons/create-a-coupon) · Effect: **consequential**

```rust
pub async fn v_2_create_coupon(
        &self,
        params: V2CreateCouponParams,
    ) -> Result<SdkV2CreateCouponResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2CreateCouponParams` | Yes |

Returns: `SdkV2CreateCouponResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2CreateCouponParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2CreateCouponParams::new(serde_json::from_str("{\"code\":\"PLAN10\",\"type\":\"PERCENTAGE\",\"discount\":10,\"store_wide\":false,\"products\":[123,456],\"product_variants\":[1001,1002]}")?);
    let result = client.coupons().v_2_create_coupon(params).await?;
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

## v_2_search_coupons

Search coupons

[API reference](https://sell.app/docs/api/coupons/search-coupons) · Effect: **read**

```rust
pub async fn v_2_search_coupons(
        &self,
        params: V2SearchCouponsParams,
    ) -> Result<SdkV2SearchCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2SearchCouponsParams` | Yes |

Returns: `SdkV2SearchCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2SearchCouponsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2SearchCouponsParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.coupons().v_2_search_coupons(params).await?;
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

## v_2_get_coupon

Retrieve a coupon

[API reference](https://sell.app/docs/api/coupons/retrieve-a-coupon) · Effect: **read**

```rust
pub async fn v_2_get_coupon(
        &self,
        coupon: &str,
        params: V2GetCouponParams,
    ) -> Result<SdkV2GetCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `&str` | Yes |
| params | `V2GetCouponParams` | Yes |

Returns: `SdkV2GetCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2GetCouponParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2GetCouponParams::default();
    let result = client.coupons().v_2_get_coupon("1", params).await?;
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

## v_2_replace_coupon

Update a coupon

[API reference](https://sell.app/docs/api/coupons/update-a-coupon) · Effect: **consequential**

```rust
pub async fn v_2_replace_coupon(
        &self,
        coupon: &str,
        params: V2ReplaceCouponParams,
    ) -> Result<SdkV2ReplaceCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `&str` | Yes |
| params | `V2ReplaceCouponParams` | Yes |

Returns: `SdkV2ReplaceCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2ReplaceCouponParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplaceCouponParams::new(serde_json::from_str("{\"store_wide\":false,\"products\":[123],\"product_variants\":[1001,1002]}")?);
    let result = client.coupons().v_2_replace_coupon("1", params).await?;
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

## v_2_update_coupon

Update a coupon

[API reference](https://sell.app/docs/api/coupons/update-a-coupon) · Effect: **consequential**

```rust
pub async fn v_2_update_coupon(
        &self,
        coupon: &str,
        params: V2UpdateCouponParams,
    ) -> Result<SdkV2UpdateCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `&str` | Yes |
| params | `V2UpdateCouponParams` | Yes |

Returns: `SdkV2UpdateCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2UpdateCouponParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2UpdateCouponParams::new(serde_json::from_str("{\"store_wide\":false,\"products\":[123],\"product_variants\":[1001,1002]}")?);
    let result = client.coupons().v_2_update_coupon("1", params).await?;
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

## v_2_delete_coupon

Delete a coupon

[API reference](https://sell.app/docs/api/coupons/delete-a-coupon) · Effect: **consequential**

```rust
pub async fn v_2_delete_coupon(
        &self,
        coupon: &str,
        params: V2DeleteCouponParams,
    ) -> Result<SdkV2DeleteCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `&str` | Yes |
| params | `V2DeleteCouponParams` | Yes |

Returns: `SdkV2DeleteCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2DeleteCouponParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2DeleteCouponParams::default();
    let result = client.coupons().v_2_delete_coupon("1", params).await?;
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

## v_2_batch_create_coupons

Batch create coupons

[API reference](https://sell.app/docs/api/coupons/batch-create-coupons) · Effect: **consequential**

```rust
pub async fn v_2_batch_create_coupons(
        &self,
        params: V2BatchCreateCouponsParams,
    ) -> Result<SdkV2BatchCreateCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2BatchCreateCouponsParams` | Yes |

Returns: `SdkV2BatchCreateCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2BatchCreateCouponsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2BatchCreateCouponsParams::new(serde_json::from_str("{\"resources\":[{\"code\":\"STARTER10\",\"type\":\"PERCENTAGE\",\"discount\":10,\"store_wide\":false,\"products\":[123],\"product_variants\":[1001]}]}")?);
    let result = client.coupons().v_2_batch_create_coupons(params).await?;
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

Documented HTTP responses: 200, 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v_2_batch_update_coupons

Batch update coupons

[API reference](https://sell.app/docs/api/coupons/batch-update-coupons) · Effect: **consequential**

```rust
pub async fn v_2_batch_update_coupons(
        &self,
        params: V2BatchUpdateCouponsParams,
    ) -> Result<SdkV2BatchUpdateCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2BatchUpdateCouponsParams` | Yes |

Returns: `SdkV2BatchUpdateCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2BatchUpdateCouponsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2BatchUpdateCouponsParams::new(serde_json::from_str("{\"resources\":{\"1\":{\"store_wide\":false,\"products\":[123],\"product_variants\":[1001,1002]}}}")?);
    let result = client.coupons().v_2_batch_update_coupons(params).await?;
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

## v_2_batch_delete_coupons

Batch delete coupons

[API reference](https://sell.app/docs/api/coupons/batch-delete-coupons) · Effect: **consequential**

```rust
pub async fn v_2_batch_delete_coupons(
        &self,
        params: V2BatchDeleteCouponsParams,
    ) -> Result<SdkV2BatchDeleteCouponsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2BatchDeleteCouponsParams` | Yes |

Returns: `SdkV2BatchDeleteCouponsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::coupons::V2BatchDeleteCouponsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2BatchDeleteCouponsParams::new(serde_json::from_str("{\"resources\":[1,2]}")?);
    let result = client.coupons().v_2_batch_delete_coupons(params).await?;
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

