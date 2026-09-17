# store_custom_domains

[All resources](../methods.md)

## list

List custom domains

[API reference](https://sell.app/docs/api/store-settings/list-custom-domains) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListCustomDomainsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListCustomDomainsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_custom_domains::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.store_custom_domains().list(params).await?;
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

## connect

Connect a custom domain

[API reference](https://sell.app/docs/api/store-settings/connect-custom-domain) · Effect: **consequential**

```rust
pub async fn connect(
        &self,
        params: ConnectParams,
    ) -> Result<SdkConnectCustomDomainResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ConnectParams` | Yes |

Returns: `SdkConnectCustomDomainResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_custom_domains::ConnectParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ConnectParams::new(serde_json::from_str("{\"domain\":\"example.com\"}")?);
    let result = client.store_custom_domains().connect(params).await?;
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

## get

Retrieve a custom domain

[API reference](https://sell.app/docs/api/store-settings/manage-custom-domain) · Effect: **read**

```rust
pub async fn get(
        &self,
        custom_domain: &str,
        params: GetParams,
    ) -> Result<SdkGetCustomDomainResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_domain | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetCustomDomainResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_custom_domains::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.store_custom_domains().get("1", params).await?;
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

Disconnect a custom domain

[API reference](https://sell.app/docs/api/store-settings/manage-custom-domain) · Effect: **consequential**

```rust
pub async fn disconnect(
        &self,
        custom_domain: &str,
        params: DisconnectParams,
    ) -> Result<SdkDisconnectCustomDomainResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_domain | `&str` | Yes |
| params | `DisconnectParams` | Yes |

Returns: `SdkDisconnectCustomDomainResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_custom_domains::DisconnectParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DisconnectParams::default();
    let result = client.store_custom_domains().disconnect("1", params).await?;
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

## refresh

Refresh custom domain status

[API reference](https://sell.app/docs/api/store-settings/refresh-custom-domain) · Effect: **consequential**

```rust
pub async fn refresh(
        &self,
        custom_domain: &str,
        params: RefreshParams,
    ) -> Result<SdkRefreshCustomDomainStatusResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_domain | `&str` | Yes |
| params | `RefreshParams` | Yes |

Returns: `SdkRefreshCustomDomainStatusResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_custom_domains::RefreshParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RefreshParams::default();
    let result = client.store_custom_domains().refresh("1", params).await?;
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

