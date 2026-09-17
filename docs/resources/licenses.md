# licenses

[All resources](../methods.md)

## activate

Activate a license key

[API reference](https://sell.app/docs/api/licenses/activate-a-license-key) · Effect: **consequential**

```rust
pub async fn activate(
        &self,
        params: ActivateParams,
    ) -> Result<SdkActivateLicenseKeyResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ActivateParams` | Yes |

Returns: `SdkActivateLicenseKeyResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::licenses::ActivateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ActivateParams::new(serde_json::from_str("{\"license_key\":\"01965f1d-f038-7116-b57f-9e7ecb4e7b8f\",\"instance_name\":\"Grace Wilson\"}")?);
    let result = client.licenses().activate(params).await?;
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

## validate

Validate a license key

[API reference](https://sell.app/docs/api/licenses/validate-a-license-key) · Effect: **consequential**

```rust
pub async fn validate(
        &self,
        params: ValidateParams,
    ) -> Result<SdkValidateLicenseKeyResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ValidateParams` | Yes |

Returns: `SdkValidateLicenseKeyResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::licenses::ValidateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ValidateParams::new(serde_json::from_str("{\"license_key\":\"01965f1d-f038-7116-b57f-9e7ecb4e7b8f\"}")?);
    let result = client.licenses().validate(params).await?;
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

## list

List all license keys

[API reference](https://sell.app/docs/api/licenses/list-all-license-keys) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListLicenseKeysResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListLicenseKeysResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::licenses::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.licenses().list(params).await?;
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

## get

Retrieve a license key

[API reference](https://sell.app/docs/api/licenses/retrieve-a-license-key) · Effect: **read**

```rust
pub async fn get(
        &self,
        license_key: &str,
        params: GetParams,
    ) -> Result<SdkGetLicenseKeyResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetLicenseKeyResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::licenses::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.licenses().get("1", params).await?;
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

Update a license key

[API reference](https://sell.app/docs/api/licenses/update-a-license-key) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        license_key: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateLicenseKeyResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateLicenseKeyResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::licenses::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"limit\":10,\"active\":false}")?);
    let result = client.licenses().update("1", params).await?;
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

## deactivate_license

Deactivate a license instance

[API reference](https://sell.app/docs/api/licenses/deactivate-a-license) · Effect: **consequential**

```rust
pub async fn deactivate_license(
        &self,
        params: DeactivateLicenseParams,
    ) -> Result<SdkDeactivateLicenseResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `DeactivateLicenseParams` | Yes |

Returns: `SdkDeactivateLicenseResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::licenses::DeactivateLicenseParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeactivateLicenseParams::new(serde_json::from_str("{\"license_key\":\"SELL-LICENSE-REDACTED\",\"instance_id\":\"laptop-maya\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.licenses().deactivate_license_with_options(params, Some(&request_options)).await?;
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

