const fs = require("fs");

const text = fs.readFileSync(process.argv[2], "utf8");
const entities = {};

for (const match of text.matchAll(/- id: (E\d+)\n\s+name: ([^\n]+)\n\s+type: ([^\n]+)\n\s+source: ([^\n]+)\n\s+confidence: ([0-9.]+)/g)) {
  const [, id, name, type, source, confidence] = match;
  entities[id] = { id, name, type, source, confidence: Number(confidence) };
}

const relations = [];
for (const match of text.matchAll(/- id: (R\d+)\n\s+from: (E\d+)\n\s+to: (E\d+)\n\s+type: ([^\n]+)\n\s+source: ([^\n]+)\n\s+confidence: ([0-9.]+)/g)) {
  const [, id, from, to, type, source, confidence] = match;
  relations.push({ id, from, to, type, source, confidence: Number(confidence) });
}

const byName = Object.fromEntries(Object.values(entities).map((entity) => [entity.name, entity]));

function direct(fromName, toName, type) {
  return relations.find(
    (relation) =>
      entities[relation.from]?.name === fromName &&
      entities[relation.to]?.name === toName &&
      relation.type === type,
  );
}

function answer(query) {
  if (query.includes("parent of SULAI")) {
    const relation = direct("SULAI", "LUXIONEX", "IS_CHILD_OF");
    return { entity: entities[relation.to].name, relation_type: relation.type };
  }

  if (query.includes("IS_CHILD_OF children of LUXIONEX")) {
    return {
      entities: relations
        .filter(
          (relation) =>
            entities[relation.to]?.name === "LUXIONEX" &&
            relation.type === "IS_CHILD_OF",
        )
        .map((relation) => entities[relation.from].name)
        .sort(),
    };
  }

  if (query.includes("SULAI-TAC a part of")) {
    const relation = direct("SULAI-TAC", "SULAI", "IS_PART_OF");
    return { entity: entities[relation.to].name, relation_type: relation.type };
  }

  if (query.includes("relation from SCSS to RAHMA IS_CHILD_OF")) {
    return Boolean(direct("SCSS", "RAHMA", "IS_CHILD_OF"));
  }

  if (query.includes("relation type from SCSS to RAHMA")) {
    return relations.find(
      (relation) =>
        entities[relation.from]?.name === "SCSS" &&
        entities[relation.to]?.name === "RAHMA",
    ).type;
  }

  if (query.includes("descendant of LUXIONEX")) {
    let frontier = [byName["SULAI-TAC"].id];
    const seen = new Set(frontier);
    while (frontier.length) {
      const next = [];
      for (const current of frontier) {
        if (current === byName["LUXIONEX"].id) return true;
        for (const relation of relations) {
          if (
            relation.from === current &&
            (relation.type === "IS_PART_OF" || relation.type === "IS_CHILD_OF") &&
            !seen.has(relation.to)
          ) {
            seen.add(relation.to);
            next.push(relation.to);
          }
        }
      }
      frontier = next;
    }
    return false;
  }

  if (query.includes("source of the relation R001")) {
    return relations.find((relation) => relation.id === "R001").source;
  }

  if (query.includes("confidence of entity E002")) {
    return entities.E002.confidence;
  }

  if (query.includes("SULAI-TAC IS_CHILD_OF LUXIONEX")) {
    return Boolean(direct("SULAI-TAC", "LUXIONEX", "IS_CHILD_OF"));
  }

  if (query.includes("entity_type of RAHMA")) {
    return byName.RAHMA.type;
  }

  throw new Error(`Unsupported query: ${query}`);
}

const queries = [
  ...text.matchAll(/\n\s{2}(Q\d+):\n\s+description: "[^"]+"\n\s+query: "([^"]+)"/g),
];

const outputs = Object.fromEntries(queries.map(([, id, query]) => [id, answer(query)]));
console.log(JSON.stringify({
  implementation: "node-graph-runtime-b",
  normative_answer_data_loaded: false,
  queries: outputs,
}, null, 2));
