# Influences

Here, we'll try to explain how Lamin was influenced by other projects & tools.

This page is, for now, just a stub.

## Workflow managers

Lamin complements workflow managers with its focus on interactive analyses, biological entities & provenance beyond deterministic workflows (app uploads & notebooks). We encourage using a workflow manager to manage scheduling, execution, error & parameter handling of workflows and integrating successful executions into LaminDB for full provenance tracking.

Despite Lamin's different scope, the workflow manager [redun](https://github.com/insitro/redun) greatly influenced LaminDB. In particular, naming choices in LaminDB's `File` class (`.hash`, `.stage()`) & hashing strategies for sets are inspired by redun's File class.

Similar to redun, Lamin tries to achieve idempotency but for different use cases & using largely differing designs.

Like redun & git, LaminDB is a distributed system in which any LaminDB instance can exchange & share data with any other LaminDB instance. (Currently, this feature is built into the design, but not yet fully implemented.)

LaminDB hasn't knowingly been influenced by other workflow managers.
