# Sprint 2 Day 3 exact-paste — N3 CoSAI + X

Paste unchanged. Summaries are a lie.

## Channel A — GitHub (preferred third-party bind)

Target: https://github.com/cosai-oasis/ws1-supply-chain/issues/4  
Fallback: new issue on same repo, or comment on #5.

Title if new issue:

`Inference-time signed receipts as a WS1 claim type — composition with model-signing RFC and TRACE Trust Records`

Body:

```
Composition question for the signed-ML-artifact claim model (not a product pitch).

WS1's RFC treats producer-signed attestations over model/dataset artifacts as the trust layer (Sigstore / claimant model). That covers training-time provenance. Inference-time outputs used as evidence in a downstream control environment (limited-assurance workpapers, agent tool transcripts, Scope 2 calculation files) still sit outside the signed bundle unless the claim set is extended.

Concrete bind I am asking the workstream to mark:

1. Should an inference / calculation receipt — Ed25519 (or Sigstore) over hash(inputs) || hash(method-or-model-id) || hash(output) || engine-identity, Merkle-chained so a third party can recompute the root without the reporter's host — be treated as a first-class claim type under this RFC, or kept as an application-layer artifact outside WS1?
2. If in-scope: which field set already in the model-signing claim should be reused vs. added (model_digest, dataset_digest, tool_transcript.hash, policy_id, data_class)?
3. Composition with LF TRACE Trust Records: bind TRACE policy / data_class / tool_transcript.hash into the receipt, or keep TRACE and the receipt as separate layers with only a hash link?

A useful no ("keep inference receipts out of WS1; they belong in C2PA / application evidence") is a good outcome. I am not asking CoSAI to endorse a vendor format.

Open implementation used only so the question is not abstract:
https://github.com/jabrahns-source/vera-enterprise-engine
https://github.com/jabrahns-source/kerna-ledger-verified

Jacarri Sanders / Even The Odds Foundry
eventheoddsfoundry@gmail.com
```

## Channel B — WS1 mailing list

1. Empty mail to `cosai-supply-chain-ws+subscribe@lists.oasis-open-projects.org`
2. Confirm the handshake.
3. Post the same body to `cosai-supply-chain-ws@lists.oasis-open-projects.org`
   Subject: `Inference-time signed receipts as a WS1 claim type — composition with model-signing RFC + TRACE`

Do **not** post to `cosai-op@` (moderator-only).

## Channel C — one X post, not a launch thread

Attach GridPulse/VERA receipt screenshot. Text:

```
Signed inference/calculation receipt (Ed25519 + Merkle root an auditor can recompute without the host).

Question for people writing TRACE Trust Records and CoSAI WS1 model-signing claims:

Do you bind TRACE policy / data_class / tool_transcript.hash *into* the receipt, or keep TRACE and the receipt as separate layers with only a hash link?

Useful no is a good outcome. Not a product launch.

https://github.com/jabrahns-source/vera-enterprise-engine
https://github.com/cosai-oasis/ws1-supply-chain/issues/4
```
