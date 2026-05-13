#!/bin/bash
# pcp-stash-relocate.sh
#
# Removes packaged content from /var/lib/pcp/ in the buildroot and emits
# systemd-tmpfiles snippets that recreate the /var/lib/pcp tree at boot.
#
# Required for transactional-update / immutable-OS targets (openSUSE
# MicroOS, SLE Micro), where /var is a separate writable subvolume from
# the read-only /usr snapshot. Package-shipped content under /var/lib/pcp
# would not survive a snapshot rollback and triggers rpmlint's
# dir-or-file-outside-snapshot warning.
#
# Two cases are handled, distinguished by what is in the buildroot at
# each path:
#
#   1. Symlink case (PMDAs, base pcp, pcp-conf, pcp-gui, pcp-zeroconf,
#      pcp-devel). PCP's upstream install places real files under
#      /usr/libexec/pcp/... and seeds /var/lib/pcp/... with symlinks
#      pointing back to them. We read each symlink's target, delete the
#      symlink from the buildroot, and emit:
#          L+ /var/lib/pcp/<path> - - - - <absolute-target>
#      The real targets remain in /usr/libexec where upstream put them.
#
#   2. Relocation case (pcp-testsuite). The testsuite ships ~5500 real
#      files under /var/lib/pcp/testsuite/. We move each file to
#      /usr/share/pcp/stash/testsuite/<path> and emit:
#          L+ /var/lib/pcp/<path> - - - - /usr/share/pcp/stash/<path>
#
# Directories under /var/lib/pcp/ that are explicitly listed in the
# .list files become 'd' tmpfiles entries so they exist as real dirs at
# boot (necessary for the L+ symlinks to be created inside them).
#
# Per-list files are rewritten in place so RPM's %files directive can
# read them back via -f. Each /var/lib/pcp/... entry becomes either:
#   <stash-path>    %ghost <legacy-path>           (relocated file)
#   <empty>         %ghost <legacy-path>           (deleted symlink)
#   <empty>         %ghost %dir <legacy-path>      (deleted/empty dir)
# The tmpfiles snippet path is appended as a normal file entry.
#
# Usage:
#   pcp-stash-relocate.sh \
#       --buildroot   <path>     # %{buildroot}
#       --legacy-root <path>     # /var/lib/pcp (repeatable; pass once
#                                #   per legacy prefix to scan, e.g. add
#                                #   --legacy-root /var/log/pcp)
#       --stash-root  <path>     # /usr/share/pcp/stash
#       --listdir     <path>     # dir containing the *.list files
#       --tmpfilesdir <path>     # dir where pcp-*-stash.conf files land
#                                #   (relative to --buildroot)

set -euo pipefail

BUILDROOT=
LEGACY_ROOTS=()
STASH_ROOT=
LISTDIR=
TMPFILESDIR=
SKIP_LISTS=

die() {
    printf 'pcp-stash-relocate: error: %s\n' "$*" >&2
    exit 1
}

while [ $# -gt 0 ]; do
    case "$1" in
        --buildroot)   BUILDROOT=$2; shift 2 ;;
        --legacy-root) LEGACY_ROOTS+=("$2"); shift 2 ;;
        --stash-root)  STASH_ROOT=$2; shift 2 ;;
        --listdir)     LISTDIR=$2; shift 2 ;;
        --tmpfilesdir) TMPFILESDIR=$2; shift 2 ;;
        --skip)        SKIP_LISTS="$SKIP_LISTS $2"; shift 2 ;;
        -h|--help)     sed -n '2,/^# Usage/p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *)             die "unknown argument: $1" ;;
    esac
done

[ -n "$BUILDROOT" ]      || die "--buildroot is required"
[ ${#LEGACY_ROOTS[@]} -gt 0 ] || die "at least one --legacy-root is required"
[ -n "$STASH_ROOT" ]     || die "--stash-root is required"
[ -n "$LISTDIR" ]        || die "--listdir is required"
[ -n "$TMPFILESDIR" ]    || die "--tmpfilesdir is required"

[ -d "$BUILDROOT" ] || die "buildroot does not exist: $BUILDROOT"
for lr in "${LEGACY_ROOTS[@]}"; do
    [ -d "$BUILDROOT$lr" ] || die "legacy root does not exist in buildroot: $BUILDROOT$lr"
done
[ -d "$LISTDIR" ] || die "listdir does not exist: $LISTDIR"

mkdir -p "$BUILDROOT$STASH_ROOT"
mkdir -p "$BUILDROOT$TMPFILESDIR"

# Helper: classify whether $1 starts with any of the legacy roots.
# Echoes the matching prefix on success, nothing on failure.
match_legacy_root() {
    local path=$1 lr
    for lr in "${LEGACY_ROOTS[@]}"; do
        case "$path" in
            "$lr"|"$lr"/*) printf '%s\n' "$lr"; return 0 ;;
        esac
    done
    return 1
}

# ---------------------------------------------------------------------------
# Per-path permission overrides for 'd' (directory) entries.
#
# Most directories are recreated as 0755 root:root. A small number need
# pcp:pcp ownership and 0775 mode for the runtime services to write into
# them. Add entries here as needed; lookup is by exact absolute path.
# ---------------------------------------------------------------------------

PERM_OVERRIDES=$(cat <<'EOF'
/var/lib/pcp/config/pmie     0775 pcp pcp
/var/lib/pcp/config/pmlogger 0775 pcp pcp
/var/lib/pcp/config/pmda     0775 pcp pcp
/var/lib/pcp/tmp             0775 pcp pcp
/var/lib/pcp/tmp/bash        0775 pcp pcp
/var/lib/pcp/tmp/json        0775 pcp pcp
/var/lib/pcp/tmp/mmv         0775 pcp pcp
/var/lib/pcp/tmp/pmie        0775 pcp pcp
/var/lib/pcp/tmp/pmlogger    0775 pcp pcp
/var/lib/pcp/tmp/pmproxy     0775 pcp pcp
/var/log/pcp                 0775 pcp pcp
/var/log/pcp/pmcd            0775 pcp pcp
/var/log/pcp/pmlogger        0775 pcp pcp
/var/log/pcp/pmie            0775 pcp pcp
/var/log/pcp/pmproxy         0775 pcp pcp
/var/log/pcp/pmfind          0775 pcp pcp
EOF
)

lookup_perms() {
    # echoes "<mode> <user> <group>" for the given absolute path,
    # defaults to 0755 root root if no override.
    local path=$1 line p m u g
    local mode=0755 user=root group=root
    while IFS= read -r line; do
        [ -n "$line" ] || continue
        read -r p m u g <<<"$line"
        if [ "$p" = "$path" ]; then
            mode=$m; user=$u; group=$g
            break
        fi
    done <<<"$PERM_OVERRIDES"
    printf '%s %s %s\n' "$mode" "$user" "$group"
}

# ---------------------------------------------------------------------------
# Resolve a (possibly relative) symlink target to an absolute path,
# interpreting the target as it would be from the LEGACY-side location
# (not the buildroot location). e.g. for a symlink at
#   <buildroot>/var/lib/pcp/pmns/root_pmcd
# whose target is "../../../../usr/libexec/pcp/pmns/root_pmcd",
# the absolute resolution is "/usr/libexec/pcp/pmns/root_pmcd".
# ---------------------------------------------------------------------------

resolve_symlink_target() {
    # $1 = absolute legacy path of the symlink (e.g. /var/lib/pcp/pmns/foo)
    # $2 = raw symlink target (relative or absolute)
    local linkpath=$1 target=$2 dir combined part
    case "$target" in
        /*) printf '%s\n' "$target" ;;
        *)
            dir=$(dirname "$linkpath")
            combined="$dir/$target"
            local IFS=/
            local -a stack=()
            for part in $combined; do
                case "$part" in
                    ''|.) ;;
                    ..)
                        if [ ${#stack[@]} -gt 0 ]; then
                            unset 'stack[${#stack[@]}-1]'
                        fi
                        ;;
                    *) stack+=("$part") ;;
                esac
            done
            printf '/%s\n' "${stack[*]}"
            ;;
    esac
}

# ---------------------------------------------------------------------------
# Process each .list file.
# ---------------------------------------------------------------------------

shopt -s nullglob
for listfile in "$LISTDIR"/*.list; do
    listname=$(basename "$listfile" .list)

    # Skip intermediate lists that the spec merges into a final list.
    # Their content is already represented in the merged list, so
    # processing them here would create orphan tmpfiles snippets that
    # no %files block claims.
    skip=0
    for s in $SKIP_LISTS; do
        if [ "$s" = "$listname" ]; then
            skip=1
            break
        fi
    done
    if [ $skip -eq 1 ]; then
        continue
    fi

    tmpfile_snippet="$BUILDROOT$TMPFILESDIR/pcp-${listname}-stash.conf"

    work_dir=$(mktemp -d)
    trap 'rm -rf "$work_dir"' EXIT

    files_to_relocate=$work_dir/files     # real files: move to stash
    links_to_remove=$work_dir/links       # symlinks: just delete
    dirs_listed=$work_dir/dirs            # explicit directory entries
    : > "$files_to_relocate"
    : > "$links_to_remove"
    : > "$dirs_listed"

    while IFS= read -r raw; do
        case "$raw" in ''|\#*) continue ;; esac

        path=$(printf '%s' "$raw" | sed -E '
            s/^[[:space:]]+//
            s/^%attr\([^)]*\)[[:space:]]+//
            s/^%config(\([^)]*\))?[[:space:]]+//
            s/^%dir[[:space:]]+//
            s/^%doc[[:space:]]+//
            s/^%ghost[[:space:]]+//
            s/^%verify\([^)]*\)[[:space:]]+//
        ')

        if ! match_legacy_root "$path" >/dev/null; then
            continue
        fi

        bp="$BUILDROOT$path"
        if [ -L "$bp" ]; then
            target=$(readlink "$bp")
            abs_target=$(resolve_symlink_target "$path" "$target")
            printf '%s\t%s\n' "$path" "$abs_target" >> "$links_to_remove"
        elif [ -f "$bp" ]; then
            printf '%s\n' "$path" >> "$files_to_relocate"
        elif [ -d "$bp" ]; then
            printf '%s\n' "$path" >> "$dirs_listed"
        else
            # Path is in the .list but not in the buildroot. Treat as a
            # directory that should exist at boot (defensive).
            printf '%s\n' "$path" >> "$dirs_listed"
        fi
    done < "$listfile"

    if [ ! -s "$files_to_relocate" ] && [ ! -s "$links_to_remove" ] \
       && [ ! -s "$dirs_listed" ]; then
        rm -rf "$work_dir"
        trap - EXIT
        continue
    fi

    # ----------------------------------------------------------------------
    # Phase 1a: copy real files from <buildroot><legacy>/foo to
    #           <buildroot><stash>/foo. We use cp -a (not mv) so the
    #           original path remains in the buildroot — RPM needs it
    #           there to read metadata for the %ghost entry that the
    #           rewritten list will reference.
    # ----------------------------------------------------------------------
    sort -u "$files_to_relocate" -o "$files_to_relocate"
    while IFS= read -r path; do
        lr=$(match_legacy_root "$path") || continue
        rel=${path#"$lr"/}
        src="$BUILDROOT$lr/$rel"
        dst="$BUILDROOT$STASH_ROOT/$rel"
        if [ ! -e "$src" ] && [ ! -L "$src" ]; then
            continue
        fi
        mkdir -p "$(dirname "$dst")"
        cp -a "$src" "$dst"
    done < "$files_to_relocate"

    # ----------------------------------------------------------------------
    # Phase 1b: do NOT delete symlinks from the buildroot.
    #
    # RPM's %files processing requires every path (including %ghost
    # paths) to physically exist in the buildroot so it can read mode/
    # owner/mtime metadata. The symlinks are %ghost'd in the rewritten
    # list, which prevents their content from being shipped in the .rpm
    # payload, but the path itself must remain present at %files time.
    # systemd-tmpfiles will recreate them at boot from the snippet.
    # ----------------------------------------------------------------------
    sort -u "$links_to_remove" -o "$links_to_remove"

    # ----------------------------------------------------------------------
    # Phase 2: emit the tmpfiles snippet.
    # Format reference: tmpfiles.d(5)
    #   d  /path  mode user group age -
    #   L+ /path  -    -    -    -    /target
    # Directories first (sorted by depth so parents precede children),
    # then symlinks.
    # ----------------------------------------------------------------------
    {
        printf '# Auto-generated by pcp-stash-relocate.sh — do not edit.\n'
        printf '# Recreates legacy /var paths at boot for the following roots:\n'
        for lr in "${LEGACY_ROOTS[@]}"; do
            printf '#   %s\n' "$lr"
        done
        printf '# Source list: %s\n\n' "$listname.list"

        # Collect directories that need a 'd' entry. We only emit 'd'
        # for directories explicitly named in the input list — this
        # subpackage's own dirs. Parent directories above those are NOT
        # walked here: systemd-tmpfiles(5) implicitly creates leading
        # directories for any L+/d entry as 0755 root:root, and emitting
        # them ourselves would claim ownership of paths that belong to
        # other subpackages (triggering rpmlint's tmpfile-not-in-filelist).
        sort -u "$dirs_listed" | awk '{ print length, $0 }' | sort -n | cut -d' ' -f2- | \
        while IFS= read -r d; do
            read -r mode user group <<<"$(lookup_perms "$d")"
            printf 'd %-50s %s %s %s -\n' "$d" "$mode" "$user" "$group"
        done

        # Symlinks for relocated real files (target = stash path).
        while IFS= read -r path; do
            lr=$(match_legacy_root "$path") || continue
            rel=${path#"$lr"/}
            target="$STASH_ROOT/$rel"
            printf 'L+ %-50s - - - - %s\n' "$path" "$target"
        done < "$files_to_relocate"

        # Symlinks for previously-shipped symlinks (target preserved).
        while IFS=$'\t' read -r path target; do
            printf 'L+ %-50s - - - - %s\n' "$path" "$target"
        done < "$links_to_remove"
    } > "$tmpfile_snippet"

    # ----------------------------------------------------------------------
    # Phase 3: rewrite the .list file.
    # ----------------------------------------------------------------------
    rewritten="$work_dir/list.rewritten"
    : > "$rewritten"
    while IFS= read -r raw; do
        case "$raw" in
            ''|\#*)
                printf '%s\n' "$raw" >> "$rewritten"
                continue
                ;;
        esac

        path=$(printf '%s' "$raw" | sed -E '
            s/^[[:space:]]+//
            s/^%attr\([^)]*\)[[:space:]]+//
            s/^%config(\([^)]*\))?[[:space:]]+//
            s/^%dir[[:space:]]+//
            s/^%doc[[:space:]]+//
            s/^%ghost[[:space:]]+//
            s/^%verify\([^)]*\)[[:space:]]+//
        ')

        if lr=$(match_legacy_root "$path"); then
            if grep -Fxq "$path" "$files_to_relocate"; then
                stash_path="$STASH_ROOT${path#"$lr"}"
                stash_line=${raw//"$path"/"$stash_path"}
                printf '%s\n' "$stash_line" >> "$rewritten"
                printf '%%ghost %s\n' "$raw" >> "$rewritten"
            else
                # Symlink or directory: emit %ghost for the legacy side.
                case "$raw" in
                    *%ghost*) printf '%s\n' "$raw" >> "$rewritten" ;;
                    *)        printf '%%ghost %s\n' "$raw" >> "$rewritten" ;;
                esac
                # If this is a directory and the corresponding stash-side
                # directory exists in the buildroot (i.e. was created as a
                # parent of relocated files), emit a stash-side %dir so RPM
                # owns it. Without this, OBS's check-filelist flags the
                # directory as unowned.
                if [ -d "$BUILDROOT$path" ] && \
                   [ -d "$BUILDROOT$STASH_ROOT${path#"$lr"}" ]; then
                    stash_path="$STASH_ROOT${path#"$lr"}"
                    printf '%%dir %s\n' "$stash_path" >> "$rewritten"
                fi
            fi
        else
            printf '%s\n' "$raw" >> "$rewritten"
        fi
    done < "$listfile"

    printf '%s/pcp-%s-stash.conf\n' "$TMPFILESDIR" "$listname" >> "$rewritten"
    mv "$rewritten" "$listfile"

    rm -rf "$work_dir"
    trap - EXIT
done

# Note: we deliberately do NOT remove empty directories from the legacy
# buildroot tree. %ghost and %ghost %dir entries in the rewritten lists
# still require the path to physically exist in the buildroot, even
# though the content/dir won't be packaged — RPM reads file metadata
# (mode, owner, mtime) from the buildroot path. A bulk
# 'find -empty -delete' here would strip out exactly the dirs that
# %files now references via %ghost.

exit 0
