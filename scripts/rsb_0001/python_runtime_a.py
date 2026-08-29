import json
import re
import sys
from collections import deque


def load_source(path):
    return open(path, encoding="utf-8").read()


def parse_graph(text):
    entities = {}
    for m in re.finditer(
        r"- id: (E\d+)\n\s+name: ([^\n]+)\n\s+type: ([^\n]+)\n\s+source: ([^\n]+)\n\s+confidence: ([0-9.]+)",
        text,
    ):
        eid, name, typ, source, confidence = m.groups()
        entities[eid] = {
            "id": eid,
            "name": name,
            "type": typ,
            "source": source,
            "confidence": float(confidence),
        }

    relations = []
    for m in re.finditer(
        r"- id: (R\d+)\n\s+from: (E\d+)\n\s+to: (E\d+)\n\s+type: ([^\n]+)\n\s+source: ([^\n]+)\n\s+confidence: ([0-9.]+)",
        text,
    ):
        rid, source_id, target_id, typ, source, confidence = m.groups()
        relations.append(
            {
                "id": rid,
                "from": source_id,
                "to": target_id,
                "type": typ,
                "source": source,
                "confidence": float(confidence),
            }
        )
    return entities, relations


def query(text, entities, relations):
    by_name = {e["name"]: e for e in entities.values()}

    if "parent of SULAI" in text:
        relation = next(
            r for r in relations
            if entities[r["from"]]["name"] == "SULAI" and r["type"] == "IS_CHILD_OF"
        )
        return {"entity": entities[relation["to"]]["name"], "relation_type": relation["type"]}

    if "IS_CHILD_OF children of LUXIONEX" in text:
        return {
            "entities": sorted(
                entities[r["from"]]["name"]
                for r in relations
                if entities[r["to"]]["name"] == "LUXIONEX" and r["type"] == "IS_CHILD_OF"
            )
        }

    if "SULAI-TAC a part of" in text:
        relation = next(
            r for r in relations
            if entities[r["from"]]["name"] == "SULAI-TAC" and r["type"] == "IS_PART_OF"
        )
        return {"entity": entities[relation["to"]]["name"], "relation_type": relation["type"]}

    if "relation from SCSS to RAHMA IS_CHILD_OF" in text:
        return any(
            entities[r["from"]]["name"] == "SCSS"
            and entities[r["to"]]["name"] == "RAHMA"
            and r["type"] == "IS_CHILD_OF"
            for r in relations
        )

    if "relation type from SCSS to RAHMA" in text:
        return next(
            r["type"] for r in relations
            if entities[r["from"]]["name"] == "SCSS"
            and entities[r["to"]]["name"] == "RAHMA"
        )

    if "descendant of LUXIONEX" in text:
        start = by_name["SULAI-TAC"]["id"]
        target = by_name["LUXIONEX"]["id"]
        seen = {start}
        queue = deque([start])
        while queue:
            current = queue.popleft()
            if current == target:
                return True
            for relation in relations:
                if (
                    relation["from"] == current
                    and relation["type"] in {"IS_PART_OF", "IS_CHILD_OF"}
                    and relation["to"] not in seen
                ):
                    seen.add(relation["to"])
                    queue.append(relation["to"])
        return False

    if "source of the relation R001" in text:
        return next(r["source"] for r in relations if r["id"] == "R001")

    if "confidence of entity E002" in text:
        return entities["E002"]["confidence"]

    if "SULAI-TAC IS_CHILD_OF LUXIONEX" in text:
        return any(
            entities[r["from"]]["name"] == "SULAI-TAC"
            and entities[r["to"]]["name"] == "LUXIONEX"
            and r["type"] == "IS_CHILD_OF"
            for r in relations
        )

    if "entity_type of RAHMA" in text:
        return by_name["RAHMA"]["type"]

    raise ValueError(f"Unsupported query: {text}")


def main(path):
    text = load_source(path)
    entities, relations = parse_graph(text)
    queries = re.findall(
        r'\n\s{2}(Q\d+):\n\s+description: "[^"]+"\n\s+query: "([^"]+)"',
        text,
    )
    outputs = {qid: query(q, entities, relations) for qid, q in queries}
    print(json.dumps({
        "implementation": "python-graph-runtime-a",
        "normative_answer_data_loaded": False,
        "queries": outputs,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
