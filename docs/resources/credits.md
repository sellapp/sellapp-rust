# credits

[All resources](../methods.md)

## record

Record a credit transaction

[API reference](https://sell.app/docs/api/credits/record-a-credit-transaction) · Effect: **consequential**

```rust
pub async fn record(
        &self,
        params: RecordParams,
    ) -> Result<SdkRecordCreditTransactionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `RecordParams` | Yes |

Returns: `SdkRecordCreditTransactionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::credits::RecordParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RecordParams::new(serde_json::from_str("{\"customer_id\":125,\"product_id\":120,\"kind\":\"grant\",\"amount_units\":1000,\"idempotency_key\":\"credits-grant-01992a65\",\"reason\":\"Launch cohort allocation\"}")?);
    let result = client.credits().record(params).await?;
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

Documented HTTP responses: 200, 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

