# Day 5 exact pastes — 2026-08-31

Transmit from `eventheoddsfoundry@gmail.com` / operator LinkedIn. This runtime cannot send mail.

## D5-1 — CARB Climate Disclosure (public comment, not a sale)

To: ClimateDisclosure@arb.ca.gov  
From: Jacarri Sanders / Even The Odds Foundry <eventheoddsfoundry@gmail.com>  
Subject: Written comment — independently verifiable Scope 2 calculation receipts (July 21, 2026 workshop proposals / 2027+ rulemaking)

I am submitting a written comment on the July 21, 2026 workshop proposals for SB 253 reporting and assurance beginning in 2027. This is a comment, not a product solicitation.

Comment

1. Limited assurance over Scope 1 and Scope 2 in 2027 will only be as strong as the source artifacts the assurer can re-derive. Utility bills, platform exports, and unsigned model outputs leave the assurer trusting the operator. CARB should permit, and for modeled or AI-assisted Scope 2 calculations should encourage, an independently verifiable calculation receipt: digital signature over hash(inputs)+hash(method)+hash(output)+model-or-engine identity, with a Merkle root an assurer can recompute without access to the reporter’s systems.

2. This is compatible with the standards CARB staff listed (AT-C 210, ISAE 3000/3410, ISO 14064-3, AA1000AS, ISSA 5000). Those standards already require sufficient appropriate evidence. A signed, hash-chained receipt is evidence. It is not a new assurance standard and CARB does not need to invent one.

3. I am not asking CARB to mandate a vendor format. I am asking staff to state, in the forthcoming draft text or staff report, that cryptographic calculation receipts are an acceptable class of source document for Scope 2 (and, later, for any AI-assisted inventory step), provided the assurer can independently recompute the root.

4. I built an open implementation so the comment is not abstract: Ed25519-signed, Merkle-chained receipts (VERA Enterprise Engine; Kerna-Ledger). Anyone can inspect the code. I do not claim a CARB pilot, a CARB endorsement, or a customer fleet result.

Proof (implementation, not a filing):
https://github.com/jabrahns-source/vera-enterprise-engine
https://github.com/jabrahns-source/kerna-ledger

One ask of staff: written acknowledgment that this comment was received on the 2027+ workshop docket, and whether cryptographic calculation receipts will be treated as in-scope evidence or ruled out.

Jacarri Sanders  
Even The Odds Foundry  
eventheoddsfoundry@gmail.com  
https://github.com/jabrahns-source

## D5-2 — PwC Sustainability Assurance

Subject: SB 253 limited-assurance source artifact — 20-min technical review of a signed Scope 2 receipt?

Deanna / Heather / Kevin —

PwC already told CARB (20 Mar 2025 comment letter) that assurance quality depends on experienced, independent, credentialled work under public standards. The July 21, 2026 workshop puts limited assurance over Scope 1 and Scope 2 on the 2027 reports. The gap I keep hitting is not another inventory platform. It is the source document the engagement team is asked to rely on when the number was produced by a model, a dispatch optimizer, or an ESG agent.

I built a portable receipt: Ed25519-signed, Merkle-chained, over hash(inputs)+hash(method / prompt)+hash(output)+engine identity. An assurer can recompute the root without trusting the reporter’s host. It is meant to sit in the engagement file next to the inventory, not replace PwC’s opinion.

One ask: 20 minutes to mark whether that artifact is usable as a source document under AT-C 210 / ISAE 3000 workpapers for an SB 253 limited-assurance engagement, or where the shape fails. A useful no is a good outcome.

I will not claim a PwC client, a PwC pilot, or a $2.4B customer result. Modeled CAISO RTM figures in the public repos are constrained simulations, not fleet savings.

Proof:
https://github.com/jabrahns-source/vera-enterprise-engine
https://github.com/jabrahns-source/kerna-ledger

Jacarri Sanders / Even The Odds Foundry  
eventheoddsfoundry@gmail.com  
https://github.com/jabrahns-source

— Jacarri

Channel: LinkedIn to Deanna Byrne / Heather Horn / Kevin O’Connell, or a PwC mailbox you already have. Do not invent @pwc.com.

## D5-3 — ERM CVS

Subject: Portable signed Scope 2 receipt as source evidence for SB 253 limited assurance — 20-min review?

Beth / Heather —

ERM CVS’s SB 253 note already asks the right readiness question: can underlying source data be traced and independently reviewed? Limited assurance is not enforced on the 2026 filing; it is the 2027 problem. I am not offering another inventory build. I am offering a portable source artifact the verifier can check without expanding the reporter’s attestation surface.

The artifact is an Ed25519-signed Merkle-chained receipt over the calculation (or inference) an assurer is being asked to limited-assure: hash of inputs, method, output, and engine identity. Open implementation, not a slide deck.

One ask: 20 minutes to mark usable-as-source vs fail points against ISO 14064-3 / ISAE 3000 procedures you already run. If the answer is “keep evidence in the IMP and workpapers; do not accept an external receipt,” that is a useful no.

I will not claim an ERM CVS engagement or a CARB endorsement.

Proof:
https://github.com/jabrahns-source/vera-enterprise-engine
https://github.com/jabrahns-source/GridPulse

Jacarri Sanders / Even The Odds Foundry  
eventheoddsfoundry@gmail.com

— Jacarri

Channel: beth.wyke@ermcvs.com and heather.i.moore@ermcvs.com (public article bylines) or the ERM CVS contact form.
