# community_connections_slack

[All resources](../methods.md)

## list_channels

List Slack available channels

[API reference](https://sell.app/docs/api/community-connections/slack-channels) · Effect: **read**

```rust
pub async fn list_channels(
        &self,
        params: ListChannelsParams,
    ) -> Result<SdkListSlackAvailableChannelsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListChannelsParams` | Yes |

Returns: `SdkListSlackAvailableChannelsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections_slack::ListChannelsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListChannelsParams::default();
    let result = client.community_connections_slack().list_channels(params).await?;
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

## add_channel

Add a Slack channel

[API reference](https://sell.app/docs/api/community-connections/slack-channels) · Effect: **consequential**

```rust
pub async fn add_channel(
        &self,
        params: AddChannelParams,
    ) -> Result<SdkAddSlackChannelResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `AddChannelParams` | Yes |

Returns: `SdkAddSlackChannelResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections_slack::AddChannelParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = AddChannelParams::new(serde_json::from_str("{\"channel_id\":\"C07LAUNCHVIP\"}")?);
    let result = client.community_connections_slack().add_channel(params).await?;
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

## replace_invite_link

Update Slack workspace invite link

[API reference](https://sell.app/docs/api/community-connections/slack-invite-link) · Effect: **consequential**

```rust
pub async fn replace_invite_link(
        &self,
        params: ReplaceInviteLinkParams,
    ) -> Result<SdkReplaceSlackWorkspaceInviteLinkResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceInviteLinkParams` | Yes |

Returns: `SdkReplaceSlackWorkspaceInviteLinkResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::community_connections_slack::ReplaceInviteLinkParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceInviteLinkParams::new(serde_json::from_str("{\"invite_link\":\"https://join.slack.com/t/launch-lab/shared_invite/zt-2abc123\"}")?);
    let result = client.community_connections_slack().replace_invite_link(params).await?;
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

