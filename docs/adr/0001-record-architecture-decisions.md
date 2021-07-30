# Recording Architecture Decisions

- **Status:** Accepted
- **Last Modified:**: 2021-07-30
- **Related Issue:** #9
- **Deciders:** @widal001
- **Tags:** ADRs

## Context and Problem Statement

Important decisions about the structure of a codebase, the tools or platforms adopted, and the scope or vision of a product are made all throughout a project's lifecycle. Often these decisions are made and changed blindly with little record of why that decision was made, making it difficult for other collaborators and even the original decision makers to understand the justification behind that decision in the future.

_What is the best way to document key architectural decisions made within the project so that future contributors can understand the justification for those decisions?
_
## Decision Drivers <!-- RECOMMENDED -->

- **Explicit:** Important decisions about the project architecture should be clear and unambiguous
- **Documented:** There should be a written record describing which decisions are made
- **Accessible:** Decision records should be centrally located, searchable, and accessible to non-technical audiences
- **Portable:** The decision records should be able to travel with the code when it's forked, cloned, etc.
- **Maintainable:** The system we adopt should be easy to maintain or amend as needed.

## Considered Options

- ADRs in the repo `docs/` folder
- Comments and docstrings in the code itself
- Articles in the project Wiki tab

## Decision Outcome <!-- REQUIRED -->

Decisions will be documented using Architecture Decision Records (ADRs) as described by [Joel Parker Henderson](joel) and the [ADR GitHub organization](https://adr.github.io/). The template for this project's ADRs will be adapted from the [MADR template](adrs).

### Positive Consequences <!-- OPTIONAL -->

- ADRs travel with the repo when it's cloned, forked, etc.
- ADRs can be incorporated in the Issue and PR workflow
- Changes to ADRs will be listed in the project's commit history
- ADRs written in Markdown are accessible to non-technical audiences

### Negative Consequences <!-- OPTIONAL -->

- Certain urgent decisions may take longer to finalize if they need to be documented and agreed upon, slowing down
- Unless regularly maintained and complied with, it could be easy for the ADRs to become out of sync with the actual decisions made about the architecture

## Pros and Cons of the Options <!-- OPTIONAL -->

### Comments and Docstrings

- **Pro**
  - Decisions live alongside the code that implements them
  - Docstrings travel with the code when it's forked, cloned, etc.
  - Changes to docstrings and comments are part of the commit history
- **Cons**
  - Not very accessible to non-technical audiences
  - Not centralized and difficult to search for
  - Hard to see the sequential evolution of decisions

### Project Wiki

Documenting decisions in the Wiki tab on the project repository in GitHub.

- **Pro**
  - Wikis are fairly searchable and accessible to non-technical audiences
- **Cons**
  - Wikis are not forked with the main repo
  - Changes to the Wiki aren't easily integrated with the PR and Issue workflow
  - Changes to the Wiki aren't a part of the project's commit history

## Links <!-- OPTIONAL -->

- [ADR GitHub Organization](adr)
- [Joel Parker Henderson's ADR repo](joel)
- [GitHub Blog - Why Write ADRs](github)

[adr]: https://adr.github.io/
[joel]: https://github.com/joelparkerhenderson/architecture-decision-record#what-is-an-architecture-decision-record
[madr]: https://adr.github.io/madr/#the-template
[github]: https://github.blog/2020-08-13-why-write-adrs/
