# Trigger Overlap Audit v0.1.1

## Main rule
Route by **intent specificity**, not by keyword count.

### Conflict: `hyrox-coach` vs new core skills
If the user explicitly asks about current capability, limitation, adaptation target, Hybrid classification, or race-state pacing, route directly to the relevant core skill. `hyrox-coach` should not answer those questions itself.

### Conflict: `hyrox-needs-profile` vs `capability-gap-analysis`
If the question is about what HYROX requires, use `hyrox-needs-profile`. If the question compares an athlete with those demands, use `capability-gap-analysis`.

### Conflict: method selector vs `adaptation-target-selector`
If the user has already specified the target (e.g. maximal strength), use the method selector directly. If the user is asking what adaptation to pursue, use `adaptation-target-selector` first.

### Conflict: planning vs assessment
Do not generate a plan when a clear assessment/diagnostic question has not yet been answered, unless the user explicitly asks for a provisional plan and the uncertainty is clearly labeled.
