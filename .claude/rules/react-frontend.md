---
globs: "**/*.tsx,**/*.ts"
---

# React / TypeScript Frontend Conventions

## Code Style
- Use functional components with hooks — no class components.
- Enable TypeScript strict mode. No `any` types unless unavoidable (add a `// TODO: type properly` comment).
- Use named exports, not default exports (easier to refactor and search).
- Props: define an interface above the component, named `[Component]Props`.
- State management: use React hooks (`useState`, `useReducer`, `useContext`) first. Only add external state libs if justified.
- Side effects: use `useEffect` with explicit dependency arrays. Extract complex effects into custom hooks in `hooks/`.
- API calls: centralize in `services/` using a typed API client. Components never call `fetch` directly.
- Styling: use CSS Modules or Tailwind — no inline styles except for truly dynamic values.
- Testing: use Vitest + React Testing Library. Test behavior, not implementation details.
- Accessibility: all interactive elements must have accessible labels. Use semantic HTML elements.
- File naming: `PascalCase.tsx` for components, `camelCase.ts` for utilities and hooks.

## Documentation
- Every component file must have a JSDoc comment at the top describing the component's purpose, when to use it, and any important behavior.
- All Props interfaces must have a JSDoc comment on each prop explaining what it controls and any constraints.
- Custom hooks must have a JSDoc comment explaining what state/behavior they encapsulate, parameters, and return values.
- Utility functions must have JSDoc comments with `@param` and `@returns` tags.
- Complex logic (state machines, derived calculations, non-trivial effects) must have inline comments explaining the "why".
- Keep a `README.md` in each major directory (`components/`, `hooks/`, `services/`, `pages/`) describing the directory's purpose and listing key exports.
- Use `@example` JSDoc tags for non-obvious component usage patterns.
- Update documentation when changing component APIs — props changes must be reflected in JSDoc.
