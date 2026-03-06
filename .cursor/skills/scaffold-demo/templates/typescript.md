# TypeScript demo template

## Structure

```
typescript-{framework}/
├── README.md
├── Dockerfile
├── index.ts
├── package.json
└── index.test.ts
```

## Dockerfile

```dockerfile
FROM oven/bun:latest
WORKDIR /app
COPY . .
RUN bun install
CMD ["bun", "run", "index.ts"]
```

## Test

```typescript
import { expect, test } from "bun:test";

test("hello", () => {
  expect(true).toBe(true);
});
```
