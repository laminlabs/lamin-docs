New features.

- ✨ Implement groupby endpoint [PR](https://github.com/laminlabs/laminhub/pull/893) [@fredericenard](https://github.com/fredericenard)

API and Database Improvements.

- ♻️ Improve API schema [PR](https://github.com/laminlabs/laminhub/pull/914) [@fredericenard](https://github.com/fredericenard)
- 🚚 Turn `storage.instance_id` into a foreign key to `instance`, remove unique constraint on `storage.root` [PR](https://github.com/laminlabs/laminhub/pull/897) [@falexwolf](https://github.com/falexwolf)
- 🗃️ Turn schema.json into a nullable field [PR](https://github.com/laminlabs/laminhub/pull/886) [@fredericenard](https://github.com/fredericenard)

Security Enhancements.

- 🔒 Fix permission vulnerability [PR](https://github.com/laminlabs/laminhub/pull/928) [@fredericenard](https://github.com/fredericenard)
- 🔒 Prevent excessive resource consumption from malicious attack [PR](https://github.com/laminlabs/laminhub/pull/919) [@fredericenard](https://github.com/fredericenard)

User experience and Documentation.

- 💡 Add comment about security within the edge function [PR](https://github.com/laminlabs/laminhub/pull/929) [@fredericenard](https://github.com/fredericenard)
- 👷 Refactor doc-changes [PR](https://github.com/laminlabs/laminhub/pull/860) [@falexwolf](https://github.com/falexwolf)
- 💄 Add details in hover card [PR](https://github.com/laminlabs/laminhub/pull/748) [@chaichontat](https://github.com/chaichontat)

Bug Fixes.

- 🐛 Fix collection filter [PR](https://github.com/laminlabs/laminhub/pull/933) [@chaichontat](https://github.com/chaichontat)
- 🐛 Remove duplicated collections [PR](https://github.com/laminlabs/laminhub/pull/917) [@chaichontat](https://github.com/chaichontat)
- 🐛 Fix loguru integration in Sentry [PR](https://github.com/laminlabs/laminhub/pull/913) [@fredericenard](https://github.com/fredericenard)
- 💚 Fix test_router_relations_artifact [PR](https://github.com/laminlabs/laminhub/pull/907) [@fredericenard](https://github.com/fredericenard)
- 🐛 Fix transfer instance ownership [PR](https://github.com/laminlabs/laminhub/pull/888) [@fredericenard](https://github.com/fredericenard)
- 🐛 Fix sentry issues [PR](https://github.com/laminlabs/laminhub/pull/879) [@chaichontat](https://github.com/chaichontat)
- 🐛 Stop settings from flickering [PR](https://github.com/laminlabs/laminhub/pull/858) [@chaichontat](https://github.com/chaichontat)

CI/CD and Development Workflow.

- 👷 Allow automerge for all branches [PR](https://github.com/laminlabs/laminhub/pull/937) [@chaichontat](https://github.com/chaichontat)
- 🔥 Remove Husky [PR](https://github.com/laminlabs/laminhub/pull/923) [@chaichontat](https://github.com/chaichontat)
- 👷 Use loguru for stack traces and keep logs from CI [PR](https://github.com/laminlabs/laminhub/pull/908) [@chaichontat](https://github.com/chaichontat)
- 👷 Refactor pre-commit setup with auto-fix [PR](https://github.com/laminlabs/laminhub/pull/892) [@chaichontat](https://github.com/chaichontat)
- ✅ Preventing reusing same instance name when testing instance creation [PR](https://github.com/laminlabs/laminhub/pull/875) [@fredericenard](https://github.com/fredericenard)

Dependency Updates.

- ⬆️ Upgrade to pydantic v2 [PR](https://github.com/laminlabs/laminhub/pull/922) [@falexwolf](https://github.com/falexwolf)
- ⬆️ Update UI dependencies [PR](https://github.com/laminlabs/laminhub/pull/910) [@chaichontat](https://github.com/chaichontat)
- ⬆️ Upgrade lamindb [PR](https://github.com/laminlabs/laminhub/pull/887) [@fredericenard](https://github.com/fredericenard)

Refactoring.

- 🚚 Fix misclassification of permissions_cache test [PR](https://github.com/laminlabs/laminhub/pull/930) [@fredericenard](https://github.com/fredericenard)
- ♻️ Base supabase handler [PR](https://github.com/laminlabs/laminhub/pull/927) [@fredericenard](https://github.com/fredericenard)
- 🔥 Remove latest report [PR](https://github.com/laminlabs/laminhub/pull/911) [@chaichontat](https://github.com/chaichontat)
- ♻️ Refactor env variables access [PR](https://github.com/laminlabs/laminhub/pull/873) [@fredericenard](https://github.com/fredericenard)
- ♻️ Refactor query builder [PR](https://github.com/laminlabs/laminhub/pull/819) [@fredericenard](https://github.com/fredericenard)
