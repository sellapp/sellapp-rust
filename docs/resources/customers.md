# customers

[All resources](../methods.md)

## list

List customers

[API reference](https://sell.app/docs/api/customers/list-customers) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListCustomersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListCustomersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customers::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.customers().list(params).await?;
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

## create_customer

Create a customer

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **consequential**

```rust
pub async fn create_customer(
        &self,
        params: CreateCustomerParams,
    ) -> Result<SdkCreateCustomerResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateCustomerParams` | Yes |

Returns: `SdkCreateCustomerResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customers::CreateCustomerParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateCustomerParams::new(serde_json::from_str("{\"id\":314,\"email\":\"maya.chen@example.com\",\"external_id\":\"crm_maya_314\",\"name\":\"Maya Chen\",\"locale\":\"en-GB\",\"metadata\":{\"plan\":\"standard\",\"seats\":3}}")?);
    let result = client.customers().create_customer(params).await?;
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

## search

Search customers

[API reference](https://sell.app/docs/api/customers/search-customers) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchCustomersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchCustomersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customers::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":125}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.customers().search(params).await?;
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

Retrieve a customer

[API reference](https://sell.app/docs/api/customers/retrieve-customer) · Effect: **read**

```rust
pub async fn get(
        &self,
        customer: &str,
        params: GetParams,
    ) -> Result<SdkGetCustomerResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetCustomerResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customers::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.customers().get("125", params).await?;
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

## update_customer

Update a customer

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **consequential**

```rust
pub async fn update_customer(
        &self,
        customer: &str,
        params: UpdateCustomerParams,
    ) -> Result<SdkUpdateCustomerResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `&str` | Yes |
| params | `UpdateCustomerParams` | Yes |

Returns: `SdkUpdateCustomerResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customers::UpdateCustomerParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateCustomerParams::new(serde_json::from_str("{\"locale\":\"en-US\"}")?);
    let result = client.customers().update_customer("314", params).await?;
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

## get_customer_by_external_id

Retrieve a customer by external ID

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **read**

```rust
pub async fn get_customer_by_external_id(
        &self,
        external_id: &str,
        params: GetCustomerByExternalIdParams,
    ) -> Result<SdkGetCustomerResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `&str` | Yes |
| params | `GetCustomerByExternalIdParams` | Yes |

Returns: `SdkGetCustomerResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customers::GetCustomerByExternalIdParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetCustomerByExternalIdParams::default();
    let result = client.customers().get_customer_by_external_id("314", params).await?;
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

## upsert_by_external_id

Create or update a customer by external ID

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **consequential**

```rust
pub async fn upsert_by_external_id(
        &self,
        external_id: &str,
        params: UpsertByExternalIdParams,
    ) -> Result<SdkUpsertCustomerResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `&str` | Yes |
| params | `UpsertByExternalIdParams` | Yes |

Returns: `SdkUpsertCustomerResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customers::UpsertByExternalIdParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpsertByExternalIdParams::new(serde_json::from_str("{\"email\":\"maya.chen@example.com\",\"name\":\"Maya Chen\"}")?);
    let result = client.customers().upsert_by_external_id("crm_maya_314", params).await?;
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update_customer_by_external_id

Update a customer by external ID

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **consequential**

```rust
pub async fn update_customer_by_external_id(
        &self,
        external_id: &str,
        params: UpdateCustomerByExternalIdParams,
    ) -> Result<SdkUpdateCustomerResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `&str` | Yes |
| params | `UpdateCustomerByExternalIdParams` | Yes |

Returns: `SdkUpdateCustomerResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customers::UpdateCustomerByExternalIdParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateCustomerByExternalIdParams::new(serde_json::from_str("{\"locale\":\"en-US\"}")?);
    let result = client.customers().update_customer_by_external_id("314", params).await?;
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

