{
  "targets": [
    {
      "target_name": "tree_sitter_hcl_binding",
      "include_dirs": [
        "src",
        "dialects/terraform/src"
      ],
      "sources": [
        "src/parser.c",
        "src/scanner.c",
        "dialects/terraform/src/parser.c",
        "dialects/terraform/src/scanner.c"
      ],
      "conditions": [
        ["OS!='win'", {
          "cflags_c": ["-std=c11"]
        }]
      ]
    }
  ]
}
