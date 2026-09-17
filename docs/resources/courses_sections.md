# courses_sections

[All resources](../methods.md)

## create

Create a course section

[API reference](https://sell.app/docs/api/courses/manage-course-sections) · Effect: **write**

```rust
pub async fn create(
        &self,
        course: &str,
        params: CreateParams,
    ) -> Result<SdkCreateCourseSectionResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| params | `CreateParams` | Yes |

Returns: `SdkCreateCourseSectionResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_sections::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"title\":\"Getting started\"}")?);
    let result = client.courses_sections().create("string_example", params).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace

Update a course section

[API reference](https://sell.app/docs/api/courses/manage-course-sections) · Effect: **write**

```rust
pub async fn replace(
        &self,
        course: &str,
        section: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceCourseSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| section | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceCourseSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_sections::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"title\":\"Getting started\"}")?);
    let result = client.courses_sections().replace("string_example", "1", params).await?;
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

Update a course section

[API reference](https://sell.app/docs/api/courses/manage-course-sections) · Effect: **write**

```rust
pub async fn update(
        &self,
        course: &str,
        section: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateCourseSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| section | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateCourseSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_sections::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"title\":\"Getting started\"}")?);
    let result = client.courses_sections().update("string_example", "1", params).await?;
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

Delete a course section

[API reference](https://sell.app/docs/api/courses/manage-course-sections) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        course: &str,
        section: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteCourseSectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| section | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteCourseSectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_sections::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.courses_sections().delete("string_example", "1", params).await?;
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

## reorder

Reorder course sections

[API reference](https://sell.app/docs/api/courses/reorder-course-sections) · Effect: **consequential**

```rust
pub async fn reorder(
        &self,
        course: &str,
        params: ReorderParams,
    ) -> Result<SdkReorderCourseSectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| params | `ReorderParams` | Yes |

Returns: `SdkReorderCourseSectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_sections::ReorderParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReorderParams::new(serde_json::from_str("{\"resources\":[501,502]}")?);
    let result = client.courses_sections().reorder("string_example", params).await?;
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

