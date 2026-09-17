# Rust examples

See the connected workflow source in `catalog.rs`.

The catalog, checkout, and upload workflow helpers change real data when given a live client. Their native documentation tests use fixture transports and dummy credentials. Catalog steps pass the created product ID into retrieval and update; checkout retrieves the order before starting its provider checkout; upload retrieves the file using the returned file ID. Do not retry a lost checkout response without first checking the order. Use a separate client for each store's credentials.


Start with one product, move on to a few pages, then see how a failed request is reported. Each program uses the crate in this checkout, so there's no registry installation to arrange.

Run from the SDK root after setting `SELLAPP_API_KEY`, `SELLAPP_STORE`, and `SELLAPP_API_BASE_URL`. Choose `https://sell.app/api` for your real store data, or a local mock server. All examples require configuration and disable automatic retries.

```sh
cargo run --example first_request
cargo run --example pagination
cargo run --example errors
```

- [First request](first_request.rs): one product's ID and title, or an empty-store message.
- [Pagination](pagination.rs): up to three pages of products.
- [Errors](errors.rs): a read request with API status, message, and request ID handling.

`cargo test --test documentation_test` executes the exact example functions against a localhost mock with dummy credentials. `cargo check --examples` compiles the complete executable programs. These verification commands never fall back to the production API.

[Back to onboarding](../README.md)
