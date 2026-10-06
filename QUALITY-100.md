# v0.5.0 Quality Ledger — 100 fixes

This ledger records the 100 concrete checks/improvements covered by the v0.5.0 hardening pass.

## Manifest and package contract (1–20)

1. Bumped package version to 0.5.0.
2. Kept the portable root manifest canonical.
3. Kept the Codex compatibility manifest supported.
4. Added package author metadata.
5. Added repository metadata.
6. Added required developer display metadata.
7. Kept display name within directory limits.
8. Kept short description within directory limits.
9. Tightened long-description scope.
10. Clarified authorized-use limitation in listing copy.
11. Expanded accurate discovery keywords.
12. Normalized capability labels.
13. Limited capability labels to the documented maximum.
14. Kept capability labels one-line and concise.
15. Reduced starter prompts to three focused cases.
16. Enforced starter-prompt uniqueness.
17. Kept starter prompts below submission length limits.
18. Preserved Developer Tools category.
19. Preserved valid six-digit brand color.
20. Synchronized portable and compatibility OpenAI metadata.

## Skill architecture and routing (21–40)

21. Preserved 11 focused Skills rather than one monolith.
22. Enforced direct-child Skill layout.
23. Enforced SKILL.md presence.
24. Enforced non-empty Skill instructions.
25. Enforced Skill name metadata.
26. Enforced Skill description metadata.
27. Enforced unique Skill names.
28. Enforced combined plugin/Skill identity length.
29. Kept seeker-project as the general router.
30. Kept CLI reference separate from mutation workflows.
31. Kept diagnostics separate from runtime testing.
32. Kept local-lab testing explicit rather than implicit.
33. Kept data-flow auditing read-only by default.
34. Kept artifact review privacy-oriented.
35. Kept template review transparent-use oriented.
36. Kept privacy hardening opt-in.
37. Kept upstream review read-only by default.
38. Preserved host-workspace-operator for host-native file work.
39. Preserved sandbox-python-executor for deterministic checks.
40. Added CI enforcement for required baseline Skills.

## Safety and privacy (41–60)

41. Retained localhost/owned-device/consenting-participant boundary.
42. Retained synthetic-fixture-first guidance.
43. Prohibited deceptive third-party collection.
44. Prohibited concealed collection purpose.
45. Prohibited covert exfiltration workflows.
46. Kept precise location classified as sensitive.
47. Kept public IP/device fingerprint data classified as sensitive.
48. Kept Telegram/webhook credentials classified as sensitive.
49. Kept generated CSV/KML artifacts classified as sensitive.
50. Kept sensitive runtime artifacts out of Git via .gitignore.
51. Preserved redaction before sharing.
52. Preserved loopback-only synthetic fixture target.
53. Added regression coverage preventing 0.0.0.0 in the fixture.
54. Preserved warning about upstream all-interface PHP binding.
55. Preserved recommendation for loopback hardening.
56. Preserved no-tunnel behavior in local-lab Skill.
57. Preserved neutral template guidance.
58. Preserved no service-impersonation guidance for new templates.
59. Preserved no-hidden-collection guidance.
60. Kept safety boundary visible in public metadata.

## Validation and CI (61–80)

61. Replaced permissive manifest checks with fail-closed checks.
62. Added strict plugin-name validation.
63. Added strict semantic-version validation.
64. Added description presence/length validation.
65. Added author.name validation.
66. Added manifest name-parity validation.
67. Added manifest version-parity validation.
68. Added compatibility skills-path validation.
69. Added OpenAI interface presence validation.
70. Added manifest interface-parity validation.
71. Added listing field length validation.
72. Added capability-array validation.
73. Added starter-prompt validation.
74. Added brand-color validation.
75. Added logo/composer path validation.
76. Enforced that .codex-plugin contains only plugin.json.
77. Added square-SVG viewBox validation.
78. Added Unicode/case path-collision detection.
79. Added symlink/transient-file/secret-shaped-file rejection.
80. Added per-file size guard.

## Tests, release hygiene, and documentation (81–100)

81. Added a Python unittest suite.
82. Added a validator self-test.
83. Added manifest parity regression test.
84. Added loopback-only fixture regression test.
85. Added artifact-redaction regression test.
86. Added non-Seeker static-audit rejection test.
87. Added helper-script bytecode compilation in CI.
88. Added least-privilege GitHub Actions permissions.
89. Added workflow concurrency cancellation.
90. Added a five-minute CI timeout.
91. Added workflow_dispatch for manual verification.
92. Kept push validation on main.
93. Kept pull-request validation.
94. Added CHANGELOG.md.
95. Added this auditable 100-item quality ledger.
96. Added MIT license for the plugin's own source.
97. Clarified upstream Seeker is not bundled.
98. Clarified GitHub main is the development source of truth.
99. Separated package validation from public-directory approval.
100. Corrected the repository name and canonical repository metadata after successfully removing the accidental leading hyphen.
