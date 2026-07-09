# R223R teacher default view acceptance criteria

## Required

Teacher default view must read like a mature teacher manuscript:

- lesson positioning
- teaching objectives
- key/difficult points
- preparation
- lesson structure
- teaching process
- design intent
- assessment/evidence
- board/screen structure when applicable

## Must not show

Teacher default view must not show these backend terms:

- practice_pattern_type
- demonstration_type
- micro_practice_type
- appreciation_scaffold_type
- creation_phase
- student_practice_output
- technique_breakthrough_point
- time_control_point
- component_trigger
- screen_trigger
- learning_sheet_fields
- evidence_outputs
- teacher_support_density

## Style guard

Teacher default view should use teacher-readable phrases:

- "本课在单元中的位置"
- "教学过程"
- "教师可以这样引导"
- "学生可能会..."
- "教师可追问..."
- "这一环节留下..."

It must avoid ledger phrases:

- "activated_adapter_fields"
- "candidate_from_R222D_pool"
- "new_surface_candidate"
- "unregistered_do_not_execute"

## Acceptance result

Teacher default view passes only if:

```text
FIELD_LABEL_LEAKAGE = 0
COMPONENT_SHELF_VISIBLE = false
MATURE_MANUSCRIPT_SHAPE = true
SAMPLE_CONTAMINATION = false
```

