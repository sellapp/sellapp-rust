# sections

[All resources](../methods.md)

## list

List all sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.sections().list(params).await?;
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

Create a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateSectionResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateSectionResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"title\":\"Founder resources\",\"hidden\":false}")?);
    let result = client.sections().create(params).await?;
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

Retrieve a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn get(
        &self,
        section: &str,
    ) -> Result<SdkGetSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |

Returns: `SdkGetSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.sections().get("1").await?;
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

Update a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        section: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"title\":\"Founder resources\",\"hidden\":false}")?);
    let result = client.sections().replace("1", params).await?;
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

Update a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        section: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"title\":\"Founder resources\",\"hidden\":false}")?);
    let result = client.sections().update("1", params).await?;
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

Delete a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        section: &str,
    ) -> Result<SdkDeleteSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |

Returns: `SdkDeleteSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.sections().delete("1").await?;
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

## replace_order

Replace section order

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn replace_order(
        &self,
        params: ReplaceOrderParams,
    ) -> Result<SdkReplaceSectionOrderResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceOrderParams` | Yes |

Returns: `SdkReplaceSectionOrderResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::ReplaceOrderParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceOrderParams::new(serde_json::from_str("{\"resources\":[3,1,2]}")?);
    let result = client.sections().replace_order(params).await?;
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

## replace_products

Replace section products

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn replace_products(
        &self,
        section: &str,
        params: ReplaceProductsParams,
    ) -> Result<SdkReplaceSectionProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `ReplaceProductsParams` | Yes |

Returns: `SdkReplaceSectionProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::ReplaceProductsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceProductsParams::new(serde_json::from_str("{\"resources\":[3,1,2]}")?);
    let result = client.sections().replace_products("1", params).await?;
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

## replace_groups

Replace section groups

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn replace_groups(
        &self,
        section: &str,
        params: ReplaceGroupsParams,
    ) -> Result<SdkReplaceSectionGroupsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `ReplaceGroupsParams` | Yes |

Returns: `SdkReplaceSectionGroupsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::ReplaceGroupsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceGroupsParams::new(serde_json::from_str("{\"resources\":[3,1,2]}")?);
    let result = client.sections().replace_groups("1", params).await?;
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

Search sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.sections().search(params).await?;
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

Batch create sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn batch_create(
        &self,
        params: BatchCreateParams,
    ) -> Result<SdkBatchCreateSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchCreateParams` | Yes |

Returns: `SdkBatchCreateSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::BatchCreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchCreateParams::new(serde_json::from_str("{\"resources\":[{\"title\":\"Featured\",\"hidden\":false}]}")?);
    let result = client.sections().batch_create(params).await?;
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

Batch update sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn batch_update(
        &self,
        params: BatchUpdateParams,
    ) -> Result<SdkBatchUpdateSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchUpdateParams` | Yes |

Returns: `SdkBatchUpdateSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::BatchUpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchUpdateParams::new(serde_json::from_str("{\"resources\":{\"1\":{\"title\":\"Featured\",\"hidden\":false}}}")?);
    let result = client.sections().batch_update(params).await?;
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

Batch delete sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn batch_delete(
        &self,
        params: BatchDeleteParams,
    ) -> Result<SdkBatchDeleteSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchDeleteParams` | Yes |

Returns: `SdkBatchDeleteSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::BatchDeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchDeleteParams::new(serde_json::from_str("{\"resources\":[1,2]}")?);
    let result = client.sections().batch_delete(params).await?;
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

## v_2_list_sections

List all sections

[API reference](https://sell.app/docs/api/sections/list-all-sections) · Effect: **read**

```rust
pub async fn v_2_list_sections(
        &self,
        params: V2ListSectionsParams,
    ) -> Result<SdkV2ListSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2ListSectionsParams` | Yes |

Returns: `SdkV2ListSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2ListSectionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ListSectionsParams::default();
    let result = client.sections().v_2_list_sections(params).await?;
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

## v_2_create_section

Create a section

[API reference](https://sell.app/docs/api/sections/create-a-section) · Effect: **write**

```rust
pub async fn v_2_create_section(
        &self,
        params: V2CreateSectionParams,
    ) -> Result<SdkV2CreateSectionResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2CreateSectionParams` | Yes |

Returns: `SdkV2CreateSectionResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2CreateSectionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2CreateSectionParams::new(serde_json::from_str("{\"title\":\"Founder resources\",\"hidden\":false}")?);
    let result = client.sections().v_2_create_section(params).await?;
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

## v_2_search_sections

Search sections

[API reference](https://sell.app/docs/api/sections/search-sections) · Effect: **read**

```rust
pub async fn v_2_search_sections(
        &self,
        params: V2SearchSectionsParams,
    ) -> Result<SdkV2SearchSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2SearchSectionsParams` | Yes |

Returns: `SdkV2SearchSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2SearchSectionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2SearchSectionsParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.sections().v_2_search_sections(params).await?;
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

## v_2_get_section

Retrieve a section

[API reference](https://sell.app/docs/api/sections/retrieve-a-section) · Effect: **read**

```rust
pub async fn v_2_get_section(
        &self,
        section: &str,
        params: V2GetSectionParams,
    ) -> Result<SdkV2GetSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `V2GetSectionParams` | Yes |

Returns: `SdkV2GetSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2GetSectionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2GetSectionParams::default();
    let result = client.sections().v_2_get_section("1", params).await?;
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

## v_2_replace_section

Update a section

[API reference](https://sell.app/docs/api/sections/update-a-section) · Effect: **write**

```rust
pub async fn v_2_replace_section(
        &self,
        section: &str,
        params: V2ReplaceSectionParams,
    ) -> Result<SdkV2ReplaceSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `V2ReplaceSectionParams` | Yes |

Returns: `SdkV2ReplaceSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2ReplaceSectionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplaceSectionParams::new(serde_json::from_str("{\"title\":\"Founder resources\",\"hidden\":false}")?);
    let result = client.sections().v_2_replace_section("1", params).await?;
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

## v_2_update_section

Update a section

[API reference](https://sell.app/docs/api/sections/update-a-section) · Effect: **write**

```rust
pub async fn v_2_update_section(
        &self,
        section: &str,
        params: V2UpdateSectionParams,
    ) -> Result<SdkV2UpdateSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `V2UpdateSectionParams` | Yes |

Returns: `SdkV2UpdateSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2UpdateSectionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2UpdateSectionParams::new(serde_json::from_str("{\"title\":\"Founder resources\",\"hidden\":false}")?);
    let result = client.sections().v_2_update_section("1", params).await?;
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

## v_2_delete_section

Delete a section

[API reference](https://sell.app/docs/api/sections/delete-a-section) · Effect: **consequential**

```rust
pub async fn v_2_delete_section(
        &self,
        section: &str,
        params: V2DeleteSectionParams,
    ) -> Result<SdkV2DeleteSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `V2DeleteSectionParams` | Yes |

Returns: `SdkV2DeleteSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2DeleteSectionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2DeleteSectionParams::default();
    let result = client.sections().v_2_delete_section("1", params).await?;
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

## v_2_batch_create_sections

Batch create sections

[API reference](https://sell.app/docs/api/sections/batch-create-sections) · Effect: **consequential**

```rust
pub async fn v_2_batch_create_sections(
        &self,
        params: V2BatchCreateSectionsParams,
    ) -> Result<SdkV2BatchCreateSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2BatchCreateSectionsParams` | Yes |

Returns: `SdkV2BatchCreateSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2BatchCreateSectionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2BatchCreateSectionsParams::new(serde_json::from_str("{\"resources\":[{\"title\":\"Featured\",\"hidden\":false}]}")?);
    let result = client.sections().v_2_batch_create_sections(params).await?;
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

## v_2_batch_update_sections

Batch update sections

[API reference](https://sell.app/docs/api/sections/batch-update-sections) · Effect: **consequential**

```rust
pub async fn v_2_batch_update_sections(
        &self,
        params: V2BatchUpdateSectionsParams,
    ) -> Result<SdkV2BatchUpdateSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2BatchUpdateSectionsParams` | Yes |

Returns: `SdkV2BatchUpdateSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2BatchUpdateSectionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2BatchUpdateSectionsParams::new(serde_json::from_str("{\"resources\":{\"1\":{\"title\":\"Featured\",\"hidden\":false}}}")?);
    let result = client.sections().v_2_batch_update_sections(params).await?;
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

## v_2_batch_delete_sections

Batch delete sections

[API reference](https://sell.app/docs/api/sections/batch-delete-sections) · Effect: **consequential**

```rust
pub async fn v_2_batch_delete_sections(
        &self,
        params: V2BatchDeleteSectionsParams,
    ) -> Result<SdkV2BatchDeleteSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2BatchDeleteSectionsParams` | Yes |

Returns: `SdkV2BatchDeleteSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2BatchDeleteSectionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2BatchDeleteSectionsParams::new(serde_json::from_str("{\"resources\":[1,2]}")?);
    let result = client.sections().v_2_batch_delete_sections(params).await?;
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

## v_2_replace_section_order

Replace section order

[API reference](https://sell.app/docs/api/sections/order-sections) · Effect: **consequential**

```rust
pub async fn v_2_replace_section_order(
        &self,
        params: V2ReplaceSectionOrderParams,
    ) -> Result<SdkV2ReplaceSectionOrderResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2ReplaceSectionOrderParams` | Yes |

Returns: `SdkV2ReplaceSectionOrderResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2ReplaceSectionOrderParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplaceSectionOrderParams::new(serde_json::from_str("{\"resources\":[3,1,2]}")?);
    let result = client.sections().v_2_replace_section_order(params).await?;
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

## v_2_replace_section_products

Replace section products

[API reference](https://sell.app/docs/api/sections/replace-section-products) · Effect: **consequential**

```rust
pub async fn v_2_replace_section_products(
        &self,
        section: &str,
        params: V2ReplaceSectionProductsParams,
    ) -> Result<SdkV2ReplaceSectionProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `V2ReplaceSectionProductsParams` | Yes |

Returns: `SdkV2ReplaceSectionProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2ReplaceSectionProductsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplaceSectionProductsParams::new(serde_json::from_str("{\"resources\":[3,1,2]}")?);
    let result = client.sections().v_2_replace_section_products("1", params).await?;
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

## v_2_replace_section_groups

Replace section groups

[API reference](https://sell.app/docs/api/sections/replace-section-groups) · Effect: **consequential**

```rust
pub async fn v_2_replace_section_groups(
        &self,
        section: &str,
        params: V2ReplaceSectionGroupsParams,
    ) -> Result<SdkV2ReplaceSectionGroupsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `&str` | Yes |
| params | `V2ReplaceSectionGroupsParams` | Yes |

Returns: `SdkV2ReplaceSectionGroupsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::sections::V2ReplaceSectionGroupsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplaceSectionGroupsParams::new(serde_json::from_str("{\"resources\":[3,1,2]}")?);
    let result = client.sections().v_2_replace_section_groups("1", params).await?;
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

