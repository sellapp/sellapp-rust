# oauth

[All resources](../methods.md)

## get_oauth_authorization_server_metadata

Read OAuth server metadata

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```rust
pub async fn get_oauth_authorization_server_metadata(
        &self,
    ) -> Result<SdkGetOAuthAuthorizationServerMetadataResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |

Returns: `SdkGetOAuthAuthorizationServerMetadataResponseValue200ApplicationJson`.

```rs
use sellapp::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let result = client.oauth().get_oauth_authorization_server_metadata().await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[]
```

Documented HTTP responses: 200, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_oauth_authorization_request

Review CLI authorization

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```rust
pub async fn get_oauth_authorization_request(
        &self,
        params: GetOAuthAuthorizationRequestParams,
    ) -> Result<String, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetOAuthAuthorizationRequestParams` | Yes |

Returns: `String`.

```rs
use sellapp::Client;
use sellapp::resources::oauth::GetOAuthAuthorizationRequestParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetOAuthAuthorizationRequestParams::new("code", "01992a65-e064-71ba-b38f-902b7966a6be", "http://127.0.0.1:49152/callback", "RANDOM_STATE", "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM", "S256");
    let result = client.oauth().get_oauth_authorization_request(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[]
```

Documented HTTP responses: 200, 302, 400, 401, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## approve_oauth_authorization

Approve CLI access

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```rust
pub async fn approve_oauth_authorization(
        &self,
        params: ApproveOAuthAuthorizationParams,
    ) -> Result<(), Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ApproveOAuthAuthorizationParams` | Yes |

Returns: `()`.

```rs
use sellapp::Client;
use sellapp::resources::oauth::ApproveOAuthAuthorizationParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_browser_session(std::env::var("SELLAPP_BROWSER_SESSION")?);
    let mut params = ApproveOAuthAuthorizationParams::new(serde_json::from_str("{\"auth_token\":\"CONSENT_AUTH_TOKEN\",\"client_id\":\"01992a65-e064-71ba-b38f-902b7966a6be\",\"state\":\"RANDOM_STATE\",\"_token\":\"CSRF_TOKEN\"}")?);
    let result = client.oauth().approve_oauth_authorization(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "oauthBrowserSession": []
  }
]
```

Documented HTTP responses: 302, 400, 401, 403, 419, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## deny_oauth_authorization

Deny CLI access

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```rust
pub async fn deny_oauth_authorization(
        &self,
        params: DenyOAuthAuthorizationParams,
    ) -> Result<(), Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `DenyOAuthAuthorizationParams` | Yes |

Returns: `()`.

```rs
use sellapp::Client;
use sellapp::resources::oauth::DenyOAuthAuthorizationParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?).with_browser_session(std::env::var("SELLAPP_BROWSER_SESSION")?);
    let mut params = DenyOAuthAuthorizationParams::new(serde_json::from_str("{\"auth_token\":\"CONSENT_AUTH_TOKEN\",\"_token\":\"CSRF_TOKEN\"}")?);
    let result = client.oauth().deny_oauth_authorization(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "oauthBrowserSession": []
  }
]
```

Documented HTTP responses: 302, 400, 401, 419, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## exchange_oauth_token

Exchange or refresh OAuth tokens

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```rust
pub async fn exchange_oauth_token(
        &self,
        params: ExchangeOAuthTokenParams,
    ) -> Result<SdkExchangeOAuthTokenResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ExchangeOAuthTokenParams` | Yes |

Returns: `SdkExchangeOAuthTokenResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::oauth::ExchangeOAuthTokenParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ExchangeOAuthTokenParams::new(serde_json::from_str("{\"client_id\":\"01992a65-e064-71ba-b38f-902b7966a6be\",\"grant_type\":\"authorization_code\",\"code\":\"AUTHORIZATION_CODE\",\"redirect_uri\":\"http://127.0.0.1:49152/callback\",\"code_verifier\":\"dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk\"}")?);
    let result = client.oauth().exchange_oauth_token(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {},
  {
    "oauthClientBasic": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## revoke_oauth_token

Revoke an OAuth token

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```rust
pub async fn revoke_oauth_token(
        &self,
        params: RevokeOAuthTokenParams,
    ) -> Result<Vec<serde_json::Value>, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `RevokeOAuthTokenParams` | Yes |

Returns: `Vec<serde_json::Value>`.

```rs
use sellapp::Client;
use sellapp::resources::oauth::RevokeOAuthTokenParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("", "").with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RevokeOAuthTokenParams::new(serde_json::from_str("{\"client_id\":\"01992a65-e064-71ba-b38f-902b7966a6be\",\"token\":\"REFRESH_TOKEN\",\"token_type_hint\":\"refresh_token\"}")?);
    let result = client.oauth().revoke_oauth_token(params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {},
  {
    "oauthClientBasic": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

