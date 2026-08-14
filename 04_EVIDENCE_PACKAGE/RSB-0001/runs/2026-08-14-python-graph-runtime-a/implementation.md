# Implementation — Python Graph Runtime A

This runtime was implemented as an independent in-memory graph evaluator for the RSB-0001 reproduction.

It consumes only:

- the canonical graph embedded in RSB-0001;
- the query text Q01–Q10.

It does not parse or load the normative expected-answer fields from RSB-0001.

Implementation characteristics:

- Python standard library only.
- Entity/relation indexing in memory.
- Direct typed-relation lookup for direct queries.
- Breadth-first traversal for the descendant query.
- Source and confidence fields read directly from graph records.

The runtime source is `scripts/rsb_0001/python_runtime_a.py`.
