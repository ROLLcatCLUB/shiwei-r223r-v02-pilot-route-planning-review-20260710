# R223R v0.2 candidate pilot route plan

stage_id: 1013R_R223R_V0_2_CANDIDATE_PILOT_ROUTE_PLANNING  
status: pilot_route_planning_only  
source: R223P-5 + R223Q  
decision_target: PASS_CONTINUE_TO_R223S_OPT_IN_SANDBOX_ROUTE_SPEC

## 1. 当前判断

R223Q 已证明 R223M classroom event standard v0.2 candidate 可以在 fixture/sandbox generation regression 中生成：

- teacher default draft
- review ledger
- unit intensity aware classroom expansion
- component trigger status ledger
- screen / learning sheet / evidence mapping

但 R223Q 没有授权正式发布 v0.2，也没有授权接入正式备课室 UI、R97B 路由、runtime、provider/model、prompt 或数据库。

因此 R223R 只规划一个最小 pilot route，不做实现。

## 2. pilot route 推荐形态

推荐进入下一阶段的形式是：

```text
opt-in sandbox route spec
+ fixture-only / non-persistent preview
+ teacher_confirmed=false
+ formal_apply_allowed=false
+ v0.1 / v0.2 candidate side-by-side comparison
```

不推荐直接进入：

```text
formal R97B route
production generation chain
database-backed draft creation
prompt/provider/runtime integration
```

## 3. pilot 的目的

R223S 若被放行，只应验证：

1. v0.2 candidate 是否在最小 sandbox preview 中仍能保持教师默认稿可读。
2. v0.2 candidate 是否比 v0.1 更好表达大单元课时位置和实践强度。
3. review ledger 是否足够支撑后续大屏、组件、学习单和评价证据。
4. teacher default draft 是否不暴露后端字段和组件货架。
5. opt-in preview 是否可以安全删除，不影响正式备课室。

## 4. 最小试点数据

试点样本沿用 R223Q 三样本，不新增真实生成服务：

| sample_id | title | route purpose |
| --- | --- | --- |
| M_stationery | 我为文具代言 第三阶段 智造·新朋友 | high practice creation density |
| N_paper_print | 有趣的纸印 | material / technique preparation |
| O_color_collision | 色彩的碰撞 | visual language intro and experiment |

## 5. 成功标准

R223S 只有在以下条件全部满足时，才可继续：

- 只读 preview 可以展示 teacher default draft 和 review ledger 摘要。
- v0.1 / v0.2 candidate 对照清楚，但不暗示 v0.2 已发布。
- teacher default draft 保持成熟教师文稿形态。
- review ledger 保留 unit intensity router、practice pattern、component status、screen/sheet/evidence mapping。
- component trigger 不进入默认稿，不暗示真实执行。
- 所有输出可删除、可回滚、无数据库写入。

## 6. 当前禁止

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI = BLOCKED
R97B_ROUTE = BLOCKED
FRONTEND_BACKEND_IMPLEMENTATION = BLOCKED
RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED
LESSON_BODY_WRITEBACK = BLOCKED
FORMAL_APPLY = BLOCKED
```

