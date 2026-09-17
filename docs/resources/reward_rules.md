# reward_rules

[All resources](../methods.md)

## list

List reward rules

[API reference](https://sell.app/docs/api/reward-rules/list-reward-rules) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListRewardRulesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListRewardRulesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_rules::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.reward_rules().list(params).await?;
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

Create a reward rule

[API reference](https://sell.app/docs/api/reward-rules/create-a-reward-rule) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateRewardRuleResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateRewardRuleResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_rules::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"name\":\"Launch Lab regular\",\"is_active\":false,\"trigger_type\":\"PURCHASE_COUNT\",\"trigger_threshold\":3,\"outputs\":[{\"type\":\"BADGE\",\"label\":\"Launch Lab regular\",\"color\":\"violet\"}]}")?);
    let result = client.reward_rules().create(params).await?;
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

Search reward rules

[API reference](https://sell.app/docs/api/reward-rules/search-reward-rules) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchRewardRulesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchRewardRulesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_rules::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.reward_rules().search(params).await?;
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

Retrieve a reward rule

[API reference](https://sell.app/docs/api/reward-rules/retrieve-a-reward-rule) · Effect: **read**

```rust
pub async fn get(
        &self,
        reward_rule: &str,
        params: GetParams,
    ) -> Result<SdkGetRewardRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetRewardRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_rules::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.reward_rules().get("1", params).await?;
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

Update a reward rule

[API reference](https://sell.app/docs/api/reward-rules/update-a-reward-rule) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        reward_rule: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceRewardRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceRewardRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_rules::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"is_active\":false}")?);
    let result = client.reward_rules().replace("1", params).await?;
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

Update a reward rule

[API reference](https://sell.app/docs/api/reward-rules/update-a-reward-rule) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        reward_rule: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateRewardRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateRewardRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::reward_rules::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"is_active\":false}")?);
    let result = client.reward_rules().update("1", params).await?;
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

