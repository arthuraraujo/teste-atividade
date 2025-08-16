---
inclusion: always
---

# Task Guidelines for Personal Projects

## Project Context
- Solo developer working on personal/small projects
- NOT enterprise-level development
- Prioritize shipping over perfect architecture
- Proof of Concept (POC) mindset unless explicitly stated otherwise

## Development Philosophy
- Simple, direct solutions over complex "best practices"
- Start with the most obvious solution that works
- Value pragmatism over theoretical perfection
- Iterate and improve only when actually needed

## Implementation Guidelines

### Code Organization
- Prefer single files over multiple files when reasonable
- Keep related functionality together
- Use flat directory structures when possible
- Avoid unnecessary abstraction layers

### Dependencies and Frameworks
- No frameworks unless absolutely necessary
- Prefer built-in language features over external libraries
- Use minimal dependencies to reduce complexity
- Choose well-established, simple libraries when needed

### Configuration and Defaults
- Hardcode reasonable defaults instead of building configuration systems
- Add configuration only when values actually need to change
- Use environment variables for deployment-specific values only
- Avoid over-engineering configuration management

### Error Handling
- Handle obvious error cases that will likely occur
- Don't build complex error handling for edge cases
- Use simple try/catch or basic validation
- Log errors clearly for debugging

## What to Avoid

### Over-Engineering
- Don't add abstractions until actually needed
- Don't build for imaginary future requirements
- Don't suggest design patterns unless problem requires them
- Don't optimize prematurely

### Complexity Creep
- Avoid unnecessary interfaces and abstract classes
- Don't create elaborate folder structures for small projects
- Skip complex build processes unless required
- Avoid over-documenting simple code

### Enterprise Patterns
- Skip dependency injection containers for simple projects
- Avoid repository patterns for straightforward data access
- Don't implement complex logging frameworks
- Skip elaborate testing strategies for POCs

## When to Upgrade Approach
- When the project grows beyond personal use
- When multiple developers join
- When reliability becomes critical
- When explicitly requested by user