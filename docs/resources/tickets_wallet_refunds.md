# tickets_wallet_refunds

[All resources](../methods.md)

## list_options

List a ticket's wallet refund options

[API reference](https://sell.app/docs/api/tickets/list-ticket-wallet-refund-options) · Effect: **read**

```rust
pub async fn list_options(
        &self,
        ticket: &str,
        params: ListOptionsParams,
    ) -> Result<SdkV2ListTicketWalletRefundOptionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `ListOptionsParams` | Yes |

Returns: `SdkV2ListTicketWalletRefundOptionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_wallet_refunds::ListOptionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListOptionsParams::default();
    let result = client.tickets_wallet_refunds().list_options("312", params).await?;
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

## list

List a ticket's wallet refunds

[API reference](https://sell.app/docs/api/tickets/list-ticket-wallet-refunds) · Effect: **read**

```rust
pub async fn list(
        &self,
        ticket: &str,
        params: ListParams,
    ) -> Result<SdkV2ListTicketWalletRefundsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkV2ListTicketWalletRefundsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_wallet_refunds::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.tickets_wallet_refunds().list("312", params).await?;
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

## create

Refund a ticket to the customer's wallet

[API reference](https://sell.app/docs/api/tickets/refund-ticket-to-wallet) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        ticket: &str,
        params: CreateParams,
    ) -> Result<SdkV2RefundTicketToWalletResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| params | `CreateParams` | Yes |

Returns: `SdkV2RefundTicketToWalletResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_wallet_refunds::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"invoice_id\":5120,\"amount_cents\":500,\"expected_refundable_cents\":1999,\"customer_note\":\"We added $5.00 to your store wallet for the trouble with your download link.\"}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.tickets_wallet_refunds().create_with_options("312", params, Some(&request_options)).await?;
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

## reverse

Reverse a ticket's wallet refund

[API reference](https://sell.app/docs/api/tickets/reverse-ticket-wallet-refund) · Effect: **consequential**

```rust
pub async fn reverse(
        &self,
        ticket: &str,
        wallet_refund: &str,
        params: ReverseParams,
    ) -> Result<SdkV2ReverseTicketWalletRefundResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `&str` | Yes |
| wallet_refund | `&str` | Yes |
| params | `ReverseParams` | Yes |

Returns: `SdkV2ReverseTicketWalletRefundResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::tickets_wallet_refunds::ReverseParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReverseParams::new(serde_json::from_str("{\"reason\":\"Issued on the wrong ticket.\"}")?);
    let result = client.tickets_wallet_refunds().reverse("312", "7001", params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

