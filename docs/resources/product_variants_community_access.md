# product_variants_community_access

[All resources](../methods.md)

## replace

Replace variant community access

[API reference](https://sell.app/docs/api/product-variants/replace-variant-community-access) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        variant: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceVariantCommunityAccessResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceVariantCommunityAccessResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_community_access::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"community\":{\"platform\":\"discord\",\"server_id\":\"1187040134912155648\",\"role_ids\":[\"1187040299781210112\"],\"required\":true,\"remove_on_expire\":true},\"expected_updated_at\":\"2024-01-10T18:47:22.000000Z\"}")?);
    let result = client.product_variants_community_access().replace("1", "2", params).await?;
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

