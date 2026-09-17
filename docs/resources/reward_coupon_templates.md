# reward_coupon_templates

[All resources](../methods.md)

## list

List reward coupon templates

[API reference](https://sell.app/docs/api/reward-coupon-templates/list-reward-coupon-templates) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListRewardCouponTemplatesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListRewardCouponTemplatesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_coupon_templates::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.reward_coupon_templates().list(params).await?;
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

## create

Create a reward coupon template

[API reference](https://sell.app/docs/api/reward-coupon-templates/create-a-reward-coupon-template) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateRewardCouponTemplateResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateRewardCouponTemplateResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_coupon_templates::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"name\":\"Launch Lab thank you\",\"type\":\"PERCENTAGE\",\"discount\":\"10.00\",\"store_wide\":true,\"redemption_mode\":\"customer_locked\",\"is_active\":false,\"listing_ids\":[]}")?);
    let result = client.reward_coupon_templates().create(params).await?;
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

## search

Search reward coupon templates

[API reference](https://sell.app/docs/api/reward-coupon-templates/search-reward-coupon-templates) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchRewardCouponTemplatesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchRewardCouponTemplatesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_coupon_templates::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.reward_coupon_templates().search(params).await?;
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

Retrieve a reward coupon template

[API reference](https://sell.app/docs/api/reward-coupon-templates/retrieve-a-reward-coupon-template) · Effect: **read**

```rust
pub async fn get(
        &self,
        reward_coupon_template: &str,
        params: GetParams,
    ) -> Result<SdkGetRewardCouponTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetRewardCouponTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_coupon_templates::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.reward_coupon_templates().get("1", params).await?;
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

## replace

Update a reward coupon template

[API reference](https://sell.app/docs/api/reward-coupon-templates/update-a-reward-coupon-template) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        reward_coupon_template: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceRewardCouponTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceRewardCouponTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_coupon_templates::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"is_active\":false}")?);
    let result = client.reward_coupon_templates().replace("1", params).await?;
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

Update a reward coupon template

[API reference](https://sell.app/docs/api/reward-coupon-templates/update-a-reward-coupon-template) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        reward_coupon_template: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateRewardCouponTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateRewardCouponTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_coupon_templates::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"is_active\":false}")?);
    let result = client.reward_coupon_templates().update("1", params).await?;
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

