# Implementation — Node Graph Runtime B

This runtime was implemented independently in JavaScript/Node.js as a separate in-memory graph evaluator for the RSB-0001 reproduction.

It consumes only:

- the canonical graph embedded in RSB-0001;
- the query text Q01–Q10.

It does not parse or load the normative expected-answer fields from RSB-0001.

Implementation characteristics:

- Node.js standard library only.
- Entity-name indexing and relation filtering.
- Direct typed-relation lookup for direct queries.
- Iterative frontier traversal for the descendant query.
- Source and confidence fields read directly from graph records.

The runtime source is `scripts/rsb_0001/node_runtime_b.js`.
