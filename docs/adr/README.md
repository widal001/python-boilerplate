# Architecture Decision Records (ADRs)


## About ADRs

### Why do we need to document architecture decisions?



### What constitutes an architecture decision?

Almost all of engineering and code development involves making choices, so how do you know when a particular choices rises to the level of an architecture decision and requires an ADR?

>An Architectural Decision (AD) is a software design choice that addresses a functional or non-functional requirement that is architecturally significant.
>
>Source: [ADR GitHub Organization](adr)

Another way to recognize when making a decision related to your project constitutes an architecture decision is to ask yourself three questions about that decision:

1. Does this decision affect the structure, direction, or outcome of the project?
1. Would someone unfamiliar with the project ask me to explain why I made this decision?
1. Were there other viable alternatives I could have chosen?

If you answer "Yes" to at least one of these questions, then you've likely just made an architectural decision, and you should create an ADR to explain why you made that choice. Other contributors (and your future self) will thank you for it.

### Examples of architecture decisions

While architecture decisions come in all shapes and sizes, some common examples include:

- Setting up the repository's main file structure
- Selecting a critical library, tool, or platform
- Adopting a certain analytical framework or algorithm
- Choosing _not_ to build a particular feature

## ADR Process

TODO: Create an ADR for proposing, approving, and accepting an ADR.

## Acknowledgements and Further Reading

- [ADR GitHub Organization](adr)
- [Joel Parker Henderson's ADR repo](joel)
- [GitHub Blog - Why Write ADRs](github)

[adr]: https://adr.github.io/
[joel]: https://github.com/joelparkerhenderson/architecture-decision-record#what-is-an-architecture-decision-record
[github]: https://github.blog/2020-08-13-why-write-adrs/
