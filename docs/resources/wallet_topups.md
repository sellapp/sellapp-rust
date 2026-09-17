# wallet_topups

[All resources](../methods.md)

## create

Create a wallet top-up payment link

[API reference](https://sell.app/docs/api/wallet/create-wallet-top-up) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        customer: &str,
        params: CreateParams,
    ) -> Result<SdkCreateWalletTopUpResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `&str` | Yes |
| params | `CreateParams` | Yes |

Returns: `SdkCreateWalletTopUpResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_topups::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"amount_cents\":2500,\"payment_method\":\"STRIPE\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.wallet_topups().create_with_options("42", params, Some(&request_options)).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

