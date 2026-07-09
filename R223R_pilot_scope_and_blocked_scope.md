# R223R pilot scope and blocked scope

## Allowed in next-stage pilot spec

R223S may plan, but not yet implement:

- independent opt-in sandbox route
- fixture-only preview data
- non-persistent preview state
- teacher_confirmed=false
- formal_apply_allowed=false
- side-by-side v0.1 / v0.2 candidate comparison
- teacher default draft display
- review ledger summary display
- unit_phase_role / practice_intensity explanation
- component trigger status as review-only metadata
- screen / learning sheet / evidence mapping as review-only metadata

## Allowed pilot surfaces

| surface | allowed status | note |
| --- | --- | --- |
| teacher default draft | preview_only | no lesson body writeback |
| review ledger | preview_only / folded by default | no full field wall in teacher view |
| unit intensity router | visible as explanation | must not become teacher-facing jargon |
| component trigger status | review-only | no execution affordance |
| screen/sheet/evidence mapping | review-only or light note | no route binding |

## Blocked scope

The following remain blocked:

- formal R97B route
- official prep room UI integration
- frontend/backend implementation
- provider/model/runtime connection
- prompt modification
- database persistence
- lesson body writeback
- R223M standard v0.2 publication
- R222D component library modification
- existing R223M/N/O draft mutation
- classroom component execution
- formal apply

## Safety flags required in every R223S artifact

```json
{
  "schema_v0_2_published": false,
  "pilot_route_type": "opt_in_sandbox_spec_only",
  "fixture_only": true,
  "non_persistent_preview": true,
  "teacher_confirmed": false,
  "formal_apply_allowed": false,
  "r97b_modified": false,
  "runtime_connected": false,
  "database_written": false
}
```

