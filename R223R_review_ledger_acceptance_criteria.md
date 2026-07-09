# R223R review ledger acceptance criteria

## Required ledger fields

Each review ledger must retain:

- sample_id
- title
- unit_phase_role
- lesson_position_in_unit
- practice_intensity
- student_work_time_ratio
- teacher_support_density
- event_id
- event_name
- primary_pattern
- secondary_patterns
- activated_adapter_fields
- component_trigger
- component_trigger.status
- screen_trigger
- learning_sheet_fields
- evidence_outputs
- teacher_confirmation_required

## Ledger separation rule

Review ledger is not teacher default draft.

The ledger may contain backend terms, candidate statuses and structured evidence mappings. The teacher default draft may not expose them directly.

## Completeness requirement

For each sample:

- at least 4 classroom events
- at least 3 component trigger entries
- at least 3 screen trigger entries
- at least 3 learning sheet field entries
- at least 3 evidence output entries
- all component triggers must have status

## Safety requirement

`new_surface_candidate` and `unregistered_do_not_execute` may exist in ledger, but must not become:

- teacher default text labels
- clickable UI controls
- implied executable components
- formal R222D component registry additions

