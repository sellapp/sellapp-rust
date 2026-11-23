# wallet_overview

[All resources](../methods.md)

## get

Retrieve the wallet overview

[API reference](https://sell.app/docs/api/wallet/wallet-overview) · Effect: **read**

```rust
pub async fn get(
        &self,
        params: GetParams,
    ) -> Result<SdkGetWalletOverviewResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetParams` | Yes |

Returns: `SdkGetWalletOverviewResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_overview::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.wallet_overview().get(params).await?;
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

