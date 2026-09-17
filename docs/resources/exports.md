# exports

[All resources](../methods.md)

## list_exports

List exports

[API reference](https://sell.app/docs/api/exports) · Effect: **read**

```rust
pub async fn list_exports(
        &self,
        params: ListExportsParams,
    ) -> Result<SdkListExportsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListExportsParams` | Yes |

Returns: `SdkListExportsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::exports::ListExportsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListExportsParams::default();
    let result = client.exports().list_exports(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create_export

Create an export

[API reference](https://sell.app/docs/api/exports) · Effect: **consequential**

```rust
pub async fn create_export(
        &self,
        params: CreateExportParams,
    ) -> Result<SdkCreateExportResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateExportParams` | Yes |

Returns: `SdkCreateExportResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::exports::CreateExportParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateExportParams::new(serde_json::from_str("{\"type\":\"sales\",\"format\":\"csv\",\"parameters\":{\"from\":\"2026-08-01\",\"to\":\"2026-08-31\"}}")?);
    let result = client.exports().create_export(params).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_export

Retrieve an export

[API reference](https://sell.app/docs/api/exports) · Effect: **read**

```rust
pub async fn get_export(
        &self,
        export: &str,
        params: GetExportParams,
    ) -> Result<SdkGetExportResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| export | `&str` | Yes |
| params | `GetExportParams` | Yes |

Returns: `SdkGetExportResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::exports::GetExportParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetExportParams::default();
    let result = client.exports().get_export("01992a65-e064-71ba-b38f-902b7966a6be", params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## download_export

Download an export

[API reference](https://sell.app/docs/api/exports) · Effect: **read**

```rust
pub async fn download_export(
        &self,
        export: &str,
        params: DownloadExportParams,
    ) -> Result<(), Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| export | `&str` | Yes |
| params | `DownloadExportParams` | Yes |

Returns: `()`.

```rs
use sellapp::Client;
use sellapp::resources::exports::DownloadExportParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DownloadExportParams::new(serde_json::from_str("1788513423")?, "2c91df645a086ec399153a932b741f809d2b85c69740eaf3612384ebfb913a65");
    let result = client.exports().download_export("01992a65-e064-71ba-b38f-902b7966a6be", params).await?;
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

Documented HTTP responses: 302, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

