# feedback

[All resources](../methods.md)

## list

List all feedback

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::feedback::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.feedback().list(params).await?;
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

## get

Retrieve specific feedback

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn get(
        &self,
        feedback: &str,
    ) -> Result<SdkGetFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `&str` | Yes |

Returns: `SdkGetFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.feedback().get("1").await?;
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

## reply

Reply to feedback

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```rust
pub async fn reply(
        &self,
        feedback: &str,
        params: ReplyParams,
    ) -> Result<SdkReplyToFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `&str` | Yes |
| params | `ReplyParams` | Yes |

Returns: `SdkReplyToFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::feedback::ReplyParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplyParams::new(serde_json::from_str("{\"reply\":\"Please contact support if you need help with your download.\"}")?);
    let result = client.feedback().reply("1", params).await?;
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

Search feedback

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::feedback::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.feedback().search(params).await?;
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

## v_2_list_feedback

List all feedback

[API reference](https://sell.app/docs/api/feedback/list-all-feedback) · Effect: **read**

```rust
pub async fn v_2_list_feedback(
        &self,
        params: V2ListFeedbackParams,
    ) -> Result<SdkV2ListFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2ListFeedbackParams` | Yes |

Returns: `SdkV2ListFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::feedback::V2ListFeedbackParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ListFeedbackParams::default();
    let result = client.feedback().v_2_list_feedback(params).await?;
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

## v_2_search_feedback

Search feedback

[API reference](https://sell.app/docs/api/feedback/search-feedback) · Effect: **read**

```rust
pub async fn v_2_search_feedback(
        &self,
        params: V2SearchFeedbackParams,
    ) -> Result<SdkV2SearchFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `V2SearchFeedbackParams` | Yes |

Returns: `SdkV2SearchFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::feedback::V2SearchFeedbackParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2SearchFeedbackParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.feedback().v_2_search_feedback(params).await?;
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

## v_2_get_feedback

Retrieve specific feedback

[API reference](https://sell.app/docs/api/feedback/retrieve-specific-feedback) · Effect: **read**

```rust
pub async fn v_2_get_feedback(
        &self,
        feedback: &str,
        params: V2GetFeedbackParams,
    ) -> Result<SdkV2GetFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `&str` | Yes |
| params | `V2GetFeedbackParams` | Yes |

Returns: `SdkV2GetFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::feedback::V2GetFeedbackParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2GetFeedbackParams::default();
    let result = client.feedback().v_2_get_feedback("1", params).await?;
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

## v_2_replace_feedback

Reply to feedback

[API reference](https://sell.app/docs/api/feedback) · Effect: **consequential**

```rust
pub async fn v_2_replace_feedback(
        &self,
        feedback: &str,
        params: V2ReplaceFeedbackParams,
    ) -> Result<SdkV2ReplaceFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `&str` | Yes |
| params | `V2ReplaceFeedbackParams` | Yes |

Returns: `SdkV2ReplaceFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::feedback::V2ReplaceFeedbackParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplaceFeedbackParams::new(serde_json::from_str("{\"reply\":\"Please contact support if you need help with your download.\"}")?);
    let result = client.feedback().v_2_replace_feedback("1", params).await?;
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

## v_2_reply_to_feedback

Reply to feedback

[API reference](https://sell.app/docs/api/feedback/reply-to-feedback) · Effect: **consequential**

```rust
pub async fn v_2_reply_to_feedback(
        &self,
        feedback: &str,
        params: V2ReplyToFeedbackParams,
    ) -> Result<SdkV2ReplyToFeedbackResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `&str` | Yes |
| params | `V2ReplyToFeedbackParams` | Yes |

Returns: `SdkV2ReplyToFeedbackResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::feedback::V2ReplyToFeedbackParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = V2ReplyToFeedbackParams::new(serde_json::from_str("{\"reply\":\"Please contact support if you need help with your download.\"}")?);
    let result = client.feedback().v_2_reply_to_feedback("1", params).await?;
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

