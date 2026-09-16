/* Tree-sitter shim for the opencode shell tool (see the native-tree-sitter
 * patch). libtree-sitter passes TSNode by value, which bun:ffi cannot marshal,
 * so the walk happens here and one JSON string crosses the FFI boundary:
 *   node := [type, isNamed, startByte, endByte, [node...]]
 */
#include <tree_sitter/api.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { char *buf; size_t len, cap; } sb;

static void sb_put(sb *b, const char *s, size_t n) {
    if (b->len + n + 1 > b->cap) {
        size_t c = b->cap ? b->cap * 2 : 4096;
        while (c < b->len + n + 1) c *= 2;
        b->buf = realloc(b->buf, c);
        b->cap = c;
    }
    memcpy(b->buf + b->len, s, n);
    b->len += n;
    b->buf[b->len] = 0;
}

static void sb_str(sb *b, const char *s) {
    sb_put(b, "\"", 1);
    for (; *s; s++) {
        unsigned char c = (unsigned char)*s;
        if (c == '"' || c == '\\') { char e[2] = {'\\', (char)c}; sb_put(b, e, 2); }
        else if (c < 0x20) { char e[8]; int n = snprintf(e, sizeof e, "\\u%04x", c); sb_put(b, e, (size_t)n); }
        else sb_put(b, s, 1);
    }
    sb_put(b, "\"", 1);
}

static void dump(sb *b, TSTreeCursor *c) {
    TSNode n = ts_tree_cursor_current_node(c);
    char tmp[64];
    sb_put(b, "[", 1);
    sb_str(b, ts_node_type(n));
    int len = snprintf(tmp, sizeof tmp, ",%d,%u,%u,[", ts_node_is_named(n) ? 1 : 0,
                       ts_node_start_byte(n), ts_node_end_byte(n));
    sb_put(b, tmp, (size_t)len);
    if (ts_tree_cursor_goto_first_child(c)) {
        int first = 1;
        do {
            if (!first) sb_put(b, ",", 1);
            first = 0;
            dump(b, c);
        } while (ts_tree_cursor_goto_next_sibling(c));
        ts_tree_cursor_goto_parent(c);
    }
    sb_put(b, "]]", 2);
}

TSParser *ocshim_parser_new(const TSLanguage *lang) {
    TSParser *p = ts_parser_new();
    if (!ts_parser_set_language(p, lang)) { ts_parser_delete(p); return NULL; }
    return p;
}

void ocshim_parser_delete(TSParser *p) { ts_parser_delete(p); }

char *ocshim_parse(TSParser *p, const char *src, uint32_t len) {
    TSTree *t = ts_parser_parse_string(p, NULL, src, len);
    if (!t) return NULL;
    TSTreeCursor c = ts_tree_cursor_new(ts_tree_root_node(t));
    sb b = {0};
    dump(&b, &c);
    ts_tree_cursor_delete(&c);
    ts_tree_delete(t);
    return b.buf;
}

void ocshim_free(char *s) { free(s); }

uint32_t ocshim_abi_version(const TSLanguage *lang) { return ts_language_abi_version(lang); }
