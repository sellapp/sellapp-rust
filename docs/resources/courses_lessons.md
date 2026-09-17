# courses_lessons

[All resources](../methods.md)

## create

Create a course lesson

[API reference](https://sell.app/docs/api/courses/manage-course-lessons) · Effect: **write**

```rust
pub async fn create(
        &self,
        course: &str,
        section: &str,
        params: CreateParams,
    ) -> Result<SdkCreateCourseLessonResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| section | `&str` | Yes |
| params | `CreateParams` | Yes |

Returns: `SdkCreateCourseLessonResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_lessons::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"title\":\"Welcome\",\"type\":\"text\",\"content\":\"Welcome to Launch Lab.\",\"is_published\":false}")?);
    let result = client.courses_lessons().create("string_example", "1", params).await?;
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

Update a course lesson

[API reference](https://sell.app/docs/api/courses/manage-course-lessons) · Effect: **write**

```rust
pub async fn replace(
        &self,
        course: &str,
        lesson: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceCourseLessonResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| lesson | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceCourseLessonResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_lessons::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"title\":\"Welcome\",\"is_published\":false}")?);
    let result = client.courses_lessons().replace("string_example", "1", params).await?;
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

Update a course lesson

[API reference](https://sell.app/docs/api/courses/manage-course-lessons) · Effect: **write**

```rust
pub async fn update(
        &self,
        course: &str,
        lesson: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateCourseLessonResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| lesson | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateCourseLessonResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_lessons::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"title\":\"Welcome\",\"is_published\":false}")?);
    let result = client.courses_lessons().update("string_example", "1", params).await?;
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

Delete a course lesson

[API reference](https://sell.app/docs/api/courses/manage-course-lessons) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        course: &str,
        lesson: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteCourseLessonResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| lesson | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteCourseLessonResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_lessons::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.courses_lessons().delete("string_example", "1", params).await?;
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

Reorder course lessons

[API reference](https://sell.app/docs/api/courses/reorder-course-lessons) · Effect: **consequential**

```rust
pub async fn reorder(
        &self,
        course: &str,
        params: ReorderParams,
    ) -> Result<SdkReorderCourseLessonsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `&str` | Yes |
| params | `ReorderParams` | Yes |

Returns: `SdkReorderCourseLessonsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::courses_lessons::ReorderParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReorderParams::new(serde_json::from_str("{\"resources\":[{\"id\":601,\"section_id\":501},{\"id\":602,\"section_id\":501}]}")?);
    let result = client.courses_lessons().reorder("string_example", params).await?;
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

