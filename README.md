# SellApp Rust SDK

Bring your catalog into a Rust application, then build from there. The SellApp SDK turns async method calls into API requests and response data into Rust types, ready for you to inspect and use.

Start with a read-only request that prints one product's ID and title.

Already know your way around? Jump to [configuration](https://github.com/sellapp/sellapp-rust/blob/main/docs/usage.md#client-configuration), [usage details](https://github.com/sellapp/sellapp-rust/blob/main/docs/usage.md), or the [method index](https://github.com/sellapp/sellapp-rust/blob/main/docs/methods.md).

## Install

Use a current stable Rust toolchain. This crate uses Rust edition 2024; a minimum supported Rust version has not yet been established for its full dependency graph.

Create an application, then add the SDK and Tokio, the runtime used by the async example:

```sh
cargo new sellapp-example
cd sellapp-example
cargo add sellapp-sdk@0.1.1 --rename sellapp
cargo add tokio@1 --features macros,rt-multi-thread
```

The SDK is published as `sellapp-sdk` on [crates.io](https://crates.io/crates/sellapp-sdk). The dependency is named `sellapp` in your application, matching the Rust imports below. Your `Cargo.toml` will contain:

```toml
[dependencies]
sellapp = { package = "sellapp-sdk", version = "0.1.1" }
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

## Your first request

Your API key identifies you; your store slug selects the store. Give the key the `listing` ability, which grants access to the catalog. For a storefront at `launch-lab.sell.app`, the slug is `launch-lab`.

Set `SELLAPP_API_KEY` and `SELLAPP_STORE` as environment variables: settings your terminal passes to the program. This keeps your key out of source files and Git history. The [authentication guide](https://sell.app/docs/api/authentication) helps you get those values ready.

This complete program asks for one product and prints its ID and title. No products yet? The empty-store message still means the request worked. Save it as `src/main.rs` in the application above, or run the included [first-request example](https://github.com/sellapp/sellapp-rust/blob/main/examples/first_request.rs).

`.await` waits for the response; `?` passes a failure back to the caller. On success, `page.data` holds the products. That's the part to replace with your own application logic once the connection works.

```rust
use sellapp::{Client, Error};
use sellapp::resources::products::ListParams;

pub async fn first_request(client: &Client) -> Result<Vec<(i64, String)>, Error> {
    let page = client.products().list(ListParams {
        limit: Some(1),
        ..Default::default()
    }).await?;
    let products: Vec<_> = page.data.into_iter().map(|p| (p.id, p.title)).collect();
    for (id, title) in &products {
        println!("{id}: {title}");
    }
    if products.is_empty() {
        println!("No products yet. Your connection is ready.");
    }
    Ok(products)
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Require a deliberate destination for this runnable example.
    let base_url = std::env::var("SELLAPP_API_BASE_URL")?;
    let client = Client::from_env()?.with_base_url(base_url).with_max_retries(0);
    first_request(&client).await?;
    Ok(())
}
```

From your application directory, replace the example key and slug with your own and run these commands in a Bash-compatible shell:

```sh
export SELLAPP_API_KEY=sk_example_replace_me
export SELLAPP_STORE=launch-lab
export SELLAPP_API_BASE_URL=https://sell.app/api
cargo run
```

This reads your real store's catalog without changing it. The example asks you to choose the URL explicitly, so missing configuration cannot send a surprise request. `SELLAPP_API_BASE_URL` is an example setting, not an SDK environment setting.

## Account access and first-store setup

Create a user-owned key in [API keys](https://sell.app/user/api-tokens), even
before you have a store. Enable `account:read` for identity, store discovery and
permission inspection, and `stores:create` separately for store creation.
Identity, discovery, store detail by ID and creation omit `X-STORE`; permission
inspection and business requests select a store explicitly.

An unrestricted key covers current and future accessible stores. A selected-store
key covers only its fixed list; an empty list covers none. Membership and role
changes still apply. Selected-store keys cannot create stores. Existing keys do
not gain abilities automatically; `*` satisfies the new abilities while retaining
membership, role and restriction checks.

The [account guide](https://sell.app/docs/api/authentication#discover-your-account-before-selecting-a-store)
shows first-store creation, required idempotency keys, and bounded reads across
several stores with partial failures. Creation returns an ID and slug; use the
slug for subsequent product requests. Find your language's methods in the
[resource reference](https://github.com/sellapp/sellapp-rust/blob/main/docs/methods.md). CLI and MCP connections retain browser OAuth.

## If the request fails

| Result | Next step |
| --- | --- |
| Empty product list | The read succeeded. Create a product when you are ready. |
| 401 | Check the selected credential and whether it has expired or been revoked. |
| 403 | Check the key's listing ability, selected-store restrictions and the account's current store permissions. Official CLI OAuth also requires its active grant. |
| 400 with a missing-store message | Set SELLAPP_STORE to an authorized store slug. |
| 429 | Follow Retry-After and the SDK's documented retry behavior. |

Keep the request ID when reporting an API failure. Never include credentials.

## Three useful next actions

1. [Create and edit a product](https://github.com/sellapp/sellapp-rust/blob/main/docs/resources/products.md): exact signatures and complete examples.
2. [Read orders or create a checkout](https://github.com/sellapp/sellapp-rust/blob/main/docs/resources/orders.md): inspect permissions and effects before changing a purchase.
3. [Read more than one page](https://github.com/sellapp/sellapp-rust/blob/main/docs/usage.md): pagination, request controls, errors, and retry behavior.

## Reference and examples

- [Resource reference](https://github.com/sellapp/sellapp-rust/blob/main/docs/methods.md)
- [Runnable examples](https://github.com/sellapp/sellapp-rust/blob/main/examples/README.md)
- [API documentation](https://sell.app/docs/api)

## Support and releases

Find available packages and installation instructions in the [SDK guide](https://sell.app/docs/api/sdks).
[Report an SDK issue](https://github.com/sellapp/sellapp-rust/issues).
Include the SDK version, runtime version, and a redacted reproduction.
Licensed under [MIT](https://github.com/sellapp/sellapp-rust/blob/main/LICENSE.txt); see [third-party notices](https://github.com/sellapp/sellapp-rust/blob/main/NOTICE.txt).
