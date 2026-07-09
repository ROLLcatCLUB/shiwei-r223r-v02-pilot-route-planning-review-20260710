# R223R unit intensity router acceptance gate

## Router fields

The pilot route must preserve:

```json
{
  "unit_phase_role": "intro_understanding | technique_preparation | practice_creation | showcase_evaluation | transfer_closure",
  "lesson_position_in_unit": "early | middle | late | final",
  "practice_intensity": "low | medium | high",
  "student_work_time_ratio": "low | medium | high",
  "teacher_support_density": "light | normal | heavy"
}
```

## Expected routing effects

| route | expected classroom expansion |
| --- | --- |
| intro_understanding / medium | more observation, language, concept and light experiment; not a heavy making workshop |
| technique_preparation / medium | material/technique trials, demonstration, small evidence records |
| practice_creation / high | longer student work time, teacher巡看, rescue strategies, process evidence and final expression |
| showcase_evaluation / medium | evidence selection, peer language, teacher synthesis and transfer |

## Pilot acceptance

The pilot passes this gate if:

1. Different unit_phase_role values produce visibly different teacher manuscript density.
2. Practice_creation/high is heavier than intro_understanding/medium.
3. Technique_preparation/medium includes technique trials without becoming full project creation.
4. The router affects teacher support density and evidence expectations.
5. The router does not expose backend labels in teacher default view.

## Hold conditions

Hold if all samples produce the same pattern:

```text
导入 → 观察 → 示范 → 练习 → 展示
```

without unit role differences.

