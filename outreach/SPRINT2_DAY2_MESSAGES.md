# Sprint 2 Day 2 exact pastes — 2026-09-04

Transmit from `eventheoddsfoundry@gmail.com` / operator LinkedIn. This runtime cannot send mail.

## N5 — PwC Sustainability Assurance (Horn / Wieman / Redlin)

To: heather.horn@pwc.com, valerie.wieman@pwc.com, logan.a.redlin@pwc.com  
(Source: PwC letters to CARB 20 Mar 2025 and 27 Oct 2025; PwC In Brief US2026-02, 26 Mar 2026)  
From: Jacarri Sanders / Even The Odds Foundry <eventheoddsfoundry@gmail.com>  
Subject: SB 253 limited-assurance source artifact — 20-min technical review of a signed Scope 2 receipt?

Heather / Valerie / Logan —

PwC already told CARB (20 Mar 2025 comment letter; Oct 27 2025 template letter) that assurance quality depends on experienced, independent, credentialled work under public standards. Your Mar 26 2026 In Brief (US2026-02) is explicit that the 2027+ rulemaking is about calculation specificity and assurance, not another inventory platform.

The gap I keep hitting is the source document the engagement team is asked to rely on when the Scope 2 number was produced by a model, a dispatch optimizer, or an ESG agent. Utility bills and unsigned platform exports leave the assurer trusting the reporter's host.

I built a portable receipt: Ed25519-signed, Merkle-chained, over hash(inputs)+hash(method / prompt)+hash(output)+engine identity. An assurer can recompute the root without trusting the reporter's host. It is meant to sit in the engagement file next to the inventory, not replace PwC's opinion.

One ask: 20 minutes to mark whether that artifact is usable as a source document under AT-C 210 / ISAE 3000 workpapers for an SB 253 limited-assurance engagement, or where the shape fails. A useful no is a good outcome.

I will not claim a PwC client, a PwC pilot, or a $2.4B customer result. Modeled CAISO RTM figures in the public repos are constrained simulations, not fleet savings.

Proof:
https://github.com/jabrahns-source/vera-enterprise-engine
https://github.com/jabrahns-source/kerna-ledger

Jacarri Sanders / Even The Odds Foundry
eventheoddsfoundry@gmail.com
https://github.com/jabrahns-source

— Jacarri

Fallback channel: LinkedIn to Heather Horn / Valerie Wieman / Logan Redlin only. Do not invent additional @pwc.com addresses. Deanna Byrne (deanna.marie.byrne@pwc.com) is valid on the Mar 2025 letter if you already have a thread; do not add her as a cold fourth without cause.

## N6 — ERM CVS

Subject: Portable signed Scope 2 receipt as source evidence for SB 253 limited assurance — 20-min review?

Beth / Heather —

ERM CVS's SB 253 readiness question is the right one: can underlying source data be traced and independently reviewed? Limited assurance is not the 2026 filing problem. It is the 2027 problem. I am not offering another inventory build. I am offering a portable source artifact the verifier can check without expanding the reporter's attestation surface.

The artifact is an Ed25519-signed Merkle-chained receipt over the calculation (or inference) an assurer is being asked to limited-assure: hash of inputs, method, output, and engine identity. Open implementation, not a slide deck.

One ask: 20 minutes to mark usable-as-source vs fail points against ISO 14064-3 / ISAE 3000 procedures you already run. If the answer is "keep evidence in the IMP and workpapers; do not accept an external receipt," that is a useful no.

I will not claim an ERM CVS engagement or a CARB endorsement.

Proof:
https://github.com/jabrahns-source/vera-enterprise-engine
https://github.com/jabrahns-source/GridPulse

Jacarri Sanders / Even The Odds Foundry
eventheoddsfoundry@gmail.com

— Jacarri

Channel: ERM CVS public contact form first. Use beth.wyke@ermcvs.com / heather.i.moore@ermcvs.com only if you independently hold those byline addresses. This block did not re-verify them on a live ERM page. Do not guess @erm.com aliases.
