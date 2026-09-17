# licenses_instances

[All resources](../methods.md)

## list

List license instances

[API reference](https://sell.app/docs/api/license-instances/list-license-instances) · Effect: **read**

```rust
pub async fn list(
        &self,
        license_key: &str,
        params: ListParams,
    ) -> Result<SdkListLicenseKeyInstancesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListLicenseKeyInstancesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::licenses_instances::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.licenses_instances().list("1", params).await?;
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

## get

Retrieve a license instance

[API reference](https://sell.app/docs/api/license-instances/retrieve-a-license-instance) · Effect: **read**

```rust
pub async fn get(
        &self,
        license_key: &str,
        instance: &str,
        params: GetParams,
    ) -> Result<SdkGetLicenseInstanceResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `&str` | Yes |
| instance | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetLicenseInstanceResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::licenses_instances::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.licenses_instances().get("1", "9ebd37af-2077-42f9-9f88-d96cfc6ef1a8", params).await?;
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

