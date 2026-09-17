# oauth_management

[All resources](../methods.md)

## get_oauth_installation

Read your CLI connection

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```rust
pub async fn get_oauth_installation(
        &self,
    ) -> Result<SdkGetOAuthInstallationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `SdkGetOAuthInstallationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_access_token(std::env::var("SELLAPP_ACCESS_TOKEN")?);
    let result = client.oauth_management().get_oauth_installation().await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "oauthAccessToken": [
      "admin"
    ]
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## delete_oauth_installation

Disconnect your CLI connection

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```rust
pub async fn delete_oauth_installation(&self) -> Result<(), Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `()`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_access_token(std::env::var("SELLAPP_ACCESS_TOKEN")?);
    let result = client.oauth_management().delete_oauth_installation().await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "oauthAccessToken": [
      "admin"
    ]
  }
]
```

Documented HTTP responses: 204, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

