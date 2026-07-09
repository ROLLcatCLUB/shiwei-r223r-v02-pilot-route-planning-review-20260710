# R223R component trigger safety gate

## Status model

Allowed component trigger statuses:

```text
already_registered
candidate_from_R222D_pool
new_surface_candidate
unregistered_do_not_execute
```

## Routing rules

| status | pilot behavior | teacher default behavior |
| --- | --- | --- |
| already_registered | may appear in review ledger | translated into natural classroom action |
| candidate_from_R222D_pool | may appear in review ledger | translated into natural classroom action |
| new_surface_candidate | ledger only | no direct name in teacher default draft |
| unregistered_do_not_execute | ledger only | no direct name or execution implication |

## Hard fails

Pilot must stop if:

- a component status appears as a teacher-facing button
- a new surface candidate is treated as registered
- an unregistered component enters teacher default draft
- teacher default draft reads like a component shelf
- component preview implies classroom runtime execution

## Required note

Every R223S artifact must say:

```text
COMPONENTS_ARE_REVIEW_METADATA_ONLY
NO_REAL_COMPONENT_EXECUTION
R222D_COMPONENT_LIBRARY_UNMODIFIED
```

