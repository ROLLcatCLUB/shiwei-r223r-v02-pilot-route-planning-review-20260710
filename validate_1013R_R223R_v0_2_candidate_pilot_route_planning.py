import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223R_v0_2_candidate_pilot_route_plan.md",
    "R223R_pilot_scope_and_blocked_scope.md",
    "R223R_v0_1_vs_v0_2_comparison_plan.md",
    "R223R_teacher_default_view_acceptance_criteria.md",
    "R223R_review_ledger_acceptance_criteria.md",
    "R223R_component_trigger_safety_gate.md",
    "R223R_unit_intensity_router_acceptance_gate.md",
    "R223R_rollback_and_hold_conditions.md",
    "R223R_decision_report.md",
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
]

BOUNDARY_FALSE_KEYS = [
    "schema_v0_2_published",
    "formal_ui",
    "r97b_modified",
    "formal_route_added",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "lesson_body_written",
    "r222d_component_library_modified",
    "formal_apply",
]

REQUIRED_DECISIONS = [
    "PASS_CONTINUE_TO_R223S_OPT_IN_SANDBOX_ROUTE_SPEC",
    "HOLD_FOR_R223Q_GENERATION_RECHECK",
    "HOLD_FORMAL_V0_2_NOT_READY",
]

REQUIRED_BLOCKED_TERMS = [
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "FORMAL_UI = BLOCKED",
    "R97B_ROUTE = BLOCKED",
    "RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED",
    "LESSON_BODY_WRITEBACK = BLOCKED",
]

def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")

def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).exists():
            failures.append(f"missing required file: {name}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("stage_id") != "1013R_R223R_V0_2_CANDIDATE_PILOT_ROUTE_PLANNING":
            failures.append("manifest stage_id mismatch")
        checks += 1
        if manifest.get("decision") != "PASS_CONTINUE_TO_R223S_OPT_IN_SANDBOX_ROUTE_SPEC":
            failures.append("manifest decision mismatch")
        boundaries = manifest.get("boundaries", {})
        for key in BOUNDARY_FALSE_KEYS:
            checks += 1
            if boundaries.get(key) is not False:
                failures.append(f"boundary must be false: {key}")

    combined = "\n".join(read_text(name) for name in REQUIRED_FILES if (ROOT / name).exists())

    for decision in REQUIRED_DECISIONS:
        checks += 1
        if decision not in combined:
            failures.append(f"missing allowed decision output: {decision}")

    for term in REQUIRED_BLOCKED_TERMS:
        checks += 1
        if term not in combined:
            failures.append(f"missing blocked boundary term: {term}")

    required_phrases = [
        "fixture-only",
        "non-persistent preview",
        "teacher_confirmed=false",
        "formal_apply_allowed=false",
        "v0.1 / v0.2",
        "teacher default draft",
        "review ledger",
        "component trigger",
        "unit_phase_role",
        "practice_intensity",
        "rollback",
        "opt-in sandbox",
    ]
    for phrase in required_phrases:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing required phrase: {phrase}")

    banned_authorizations = [
        "R223M_STANDARD_V0_2 = PUBLISHED",
        "FORMAL_UI = ALLOWED",
        "R97B_ROUTE = ALLOWED",
        "formal_apply_allowed=true",
        "teacher_confirmed=true",
    ]
    for phrase in banned_authorizations:
        checks += 1
        if phrase in combined:
            failures.append(f"forbidden authorization phrase present: {phrase}")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223S_OPT_IN_SANDBOX_ROUTE_SPEC",
    }
    (ROOT / "validate_1013R_R223R_v0_2_candidate_pilot_route_planning_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)

if __name__ == "__main__":
    main()

