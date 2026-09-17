# wallet_transactions

[All resources](../methods.md)

## list

List wallet transactions

[API reference](https://sell.app/docs/api/wallet/retrieve-customer-wallet) · Effect: **read**

```rust
pub async fn list(
        &self,
        customer: &str,
        params: ListParams,
    ) -> Result<SdkListWalletTransactionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListWalletTransactionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_transactions::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.wallet_transactions().list("42", params).await?;
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

