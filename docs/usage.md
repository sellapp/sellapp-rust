# Rust usage notes

Once the first product appears in your terminal, the next questions are usually how to fetch the rest and what to do when a request fails. Here's the behavior to build around.

## Timeouts, retries, and idempotency

The default timeout is 60 seconds per attempt. Retries default to 3 additional attempts for HTTP 408, 409, 429, 5xx, and send-time transport errors. GET, HEAD, OPTIONS, PUT, and DELETE are replayable; other methods retry only when the operation declares idempotency support and `RequestOptions.idempotency_key` is nonblank. OAuth protocol operations and customer-session creation never retry automatically, including after a lost response. The default HTTP client does not follow redirects; inspect raw status and Location before starting a separate credential-free download. A custom reqwest client must also disable redirects to preserve this behavior. The timeout can be overridden with `RequestOptions.timeout`; `max_retries` overrides the client's retry count.

Retries use bounded exponential backoff with jitter. Numeric and HTTP-date `Retry-After` values are honored up to the same 30-second cap. Set `with_max_retries(0)` or per-request `max_retries: Some(0)` when an application needs exactly one attempt.

An idempotency key identifies one intended change, allowing an API operation that supports it to recognize a repeated request. The SDK does not generate these keys. Supply `RequestOptions.idempotency_key` where the API operation declares support, and reuse the key for retries of that logical change.

The request timeout bounds each attempt rather than a complete retry sequence. Use your application's async timeout/cancellation mechanism to bound the whole awaited operation. Dropping its future stops awaiting it; it cannot undo a request already processed by the server.

## Errors and request IDs

`Error::Authentication(Box<ApiError>)` represents HTTP 401 failures; `Error::Api(Box<ApiError>)` represents other API failures. Both expose `error_type`, `code`, `message`, `status`, `param`, `request_id`, `docs_url`, `retry_after`, the decoded/raw body, and response headers. Except for message and status, fields are optional. Request IDs prefer the response body and fall back to `X-Request-ID`.

Other variants distinguish `Transport`, `Timeout`, `Serialization`, `Validation`, `Configuration`, and `Builder` failures. Matching a variant makes the next step explicit. The [complete error example](../examples/errors.rs) prints an API failure for inspection; an application can propagate it or choose its own recovery policy.

## Models and pagination

Successful responses are schema-validated before decoding. Unknown response fields are retained in `additional_properties`. Optional nullable model fields use `Option<Option<T>>`: absent, explicit null, and a value are distinct. Required nullable fields use `Option<T>`.

The [pagination program](../examples/pagination.rs) uses the API's page numbers and metadata, makes only read requests, and deliberately limits itself to three pages. It never follows arbitrary response URLs. Each page request can fail independently; `?` returns the failure instead of presenting incomplete data as a completed walk.

[Back to onboarding](../README.md)

## Client configuration

Use `Client::from_env()?` to read both credentials from the environment, or `Client::new(api_key, store)` to supply them directly. The explicit constructor does not consult the environment. Credentials are checked before each request against that operation's requirements. OAuth business calls require a store; OAuth profile, store discovery, and installation calls omit `X-STORE`. Anonymous calls carry no seller credentials.

| Builder method | Behavior |
| --- | --- |
| `with_access_token(token)` | Selects OAuth access-token authentication and clears the API key |
| `with_customer_session(token)` | Separate customer-portal credential; per-request `RequestOptions.customer_session` takes precedence |
| `with_browser_session(cookie)` | Explicit cookie for browser-session OAuth operations |
| `with_client_credentials(id, secret)` | HTTP Basic for a registered confidential OAuth client; do not also send body client credentials |
| `with_base_url(url)` | Defaults to `https://sell.app/api` |
| `with_timeout(Duration::from_secs(30))` | Takes `std::time::Duration`; default 60 seconds per attempt |
| `with_max_retries(0)` | Disables retries; default 3 retries after the initial attempt |
| `with_http_client(client)` | Supplies your own `reqwest::Client` |

Operations are async and return `Result<T, sellapp::Error>`. Reuse a client across requests; cloning also reuses reqwest's connection pool. Each `*_with_options` method accepts `Option<&RequestOptions>` for per-request timeout, retries, headers, and an idempotency key. Every HTTP operation also has a `*_raw` variant returning the typed value with status, headers, and request ID. Multipart operations send byte-vector fields as binary parts; `RequestOptions.multipart_files` can supply replayable filesystem paths or named byte buffers.

## More than one page, less than a mystery

The API sends long lists in pages, so one response doesn't have to carry your whole catalog. `products().list` returns one page: `data` contains products, while `links` and `meta` describe the listing. Set `ListParams.page` to ask for the next page.

The [pagination example](https://github.com/sellapp/sellapp-rust/blob/main/examples/pagination.rs) reads up to three pages and stops at `meta.last_page`. The runtime also provides a bounded numbered-page stream helper that detects cycles and surfaces later-page failures.

The [error example](https://github.com/sellapp/sellapp-rust/blob/main/examples/errors.rs) shows what to do when the answer is a failure: match `Error::Api` or `Error::Timeout`, print a useful message, and keep the response's request ID when available. That ID helps identify the request you're investigating. Before you add requests that change data, read the [usage notes](https://github.com/sellapp/sellapp-rust/blob/main/docs/usage.md) for the idempotency rules.
