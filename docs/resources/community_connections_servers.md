# community_connections_servers

[All resources](../methods.md)

## get

Retrieve a community server

[API reference](https://sell.app/docs/api/community-connections/community-server) · Effect: **read**

```rust
pub async fn get(
        &self,
        platform: &str,
        server: &str,
        params: GetParams,
    ) -> Result<SdkGetCommunityServerResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `&str` | Yes |
| server | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetCommunityServerResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections_servers::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.community_connections_servers().get("discord", "server_ship_room", params).await?;
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

Remove a community server

[API reference](https://sell.app/docs/api/community-connections/community-server) · Effect: **consequential**

```rust
pub async fn remove(
        &self,
        platform: &str,
        server: &str,
        params: RemoveParams,
    ) -> Result<SdkRemoveCommunityServerResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `&str` | Yes |
| server | `&str` | Yes |
| params | `RemoveParams` | Yes |

Returns: `SdkRemoveCommunityServerResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections_servers::RemoveParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RemoveParams::new(serde_json::from_str("{\"affected_variant_ids\":[902]}")?);
    let result = client.community_connections_servers().remove("discord", "server_ship_room", params).await?;
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

