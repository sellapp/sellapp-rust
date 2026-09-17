# community_connections

[All resources](../methods.md)

## list

List community connections

[API reference](https://sell.app/docs/api/community-connections) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListCommunityConnectionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListCommunityConnectionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.community_connections().list(params).await?;
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

## start

Start a community connection

[API reference](https://sell.app/docs/api/community-connections) · Effect: **consequential**

```rust
pub async fn start(
        &self,
        platform: &str,
        params: StartParams,
    ) -> Result<SdkStartCommunityConnectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `&str` | Yes |
| params | `StartParams` | Yes |

Returns: `SdkStartCommunityConnectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections::StartParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = StartParams::new(serde_json::from_str("{\"mode\":\"official_bot\"}")?);
    let result = client.community_connections().start("discord", params).await?;
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

## poll

Poll a community connection

[API reference](https://sell.app/docs/api/community-connections) · Effect: **read**

```rust
pub async fn poll(
        &self,
        platform: &str,
        params: PollParams,
    ) -> Result<SdkPollCommunityConnectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `&str` | Yes |
| params | `PollParams` | Yes |

Returns: `SdkPollCommunityConnectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections::PollParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = PollParams::new("string_example");
    let result = client.community_connections().poll("discord", params).await?;
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

## complete

Complete a community connection

[API reference](https://sell.app/docs/api/community-connections) · Effect: **consequential**

```rust
pub async fn complete(
        &self,
        platform: &str,
        params: CompleteParams,
    ) -> Result<SdkCompleteCommunityConnectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `&str` | Yes |
| params | `CompleteParams` | Yes |

Returns: `SdkCompleteCommunityConnectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections::CompleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CompleteParams::new(serde_json::from_str("{\"status_token\":\"replace-with-token-from-connection-start\",\"server_id\":\"replace-with-returned-server-id\"}")?);
    let result = client.community_connections().complete("whatsapp", params).await?;
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

## verify

Verify a community connection

[API reference](https://sell.app/docs/api/community-connections) · Effect: **consequential**

```rust
pub async fn verify(
        &self,
        platform: &str,
        params: VerifyParams,
    ) -> Result<SdkVerifyCommunityConnectionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `&str` | Yes |
| params | `VerifyParams` | Yes |

Returns: `SdkVerifyCommunityConnectionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections::VerifyParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = VerifyParams::default();
    let result = client.community_connections().verify("discord", params).await?;
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

## disconnect

Disconnect a community platform

[API reference](https://sell.app/docs/api/community-connections) · Effect: **consequential**

```rust
pub async fn disconnect(
        &self,
        platform: &str,
        params: DisconnectParams,
    ) -> Result<SdkDisconnectCommunityPlatformResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `&str` | Yes |
| params | `DisconnectParams` | Yes |

Returns: `SdkDisconnectCommunityPlatformResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections::DisconnectParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DisconnectParams::default();
    let result = client.community_connections().disconnect("discord", params).await?;
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

