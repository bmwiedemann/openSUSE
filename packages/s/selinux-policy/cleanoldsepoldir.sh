#!/bin/bash
# Copyright (C) 2025 SUSE Linux
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# This utility safely clean up the legacy /var/lib/selinux directory after migration.

# Helper function to find active SELinux modules.
_get_modules() {
    local search_dir="$1"
    local -n return_array=$2
    local temp_modules=()

    for policy in minimum sandbox targeted; do
        local modules_path="${search_dir}/${policy}/active/modules"
        if [[ -d "$modules_path" ]]; then
            mapfile -t current_modules < <(find "$modules_path" -maxdepth 2 -type d '!' -empty | grep -vE '/(modules/|100|200|400|disabled)$')
            temp_modules+=("${current_modules[@]}")
        fi
    done
    IFS=$'\n' read -r -d '' -a return_array < <(printf "%s\n" "${temp_modules[@]}" | sort -u && printf '\0')
}

# Checks for custom SELinux modules that may not have been migrated.
check_custom_selinux_modules () {
    echo "INFO: Checking for possibly not migrated custom selinux modules in /var/lib/selinux/..."
    local old_selinux_dir="/var/lib/selinux"
    local new_selinux_dir="${target_dir}"
    local custom_package_dir="/usr/share/selinux/packages"
    local old_modules_unique
    _get_modules "$old_selinux_dir" old_modules_unique
    local new_modules_unique
    _get_modules "$new_selinux_dir" new_modules_unique
    local custom_modules=()
    if [ -d "${custom_package_dir}" ]; then
        mapfile -t current_modules < <(find "${custom_package_dir}" -maxdepth 2 -type f '!' -empty)
        custom_modules+=("${current_modules[@]}")
    fi
    IFS=$'\n' read -r -d '' -a custom_modules_unique < <(printf "%s\n" "${custom_modules[@]}" | sort -u && printf '\0')
    # Compare the old and new module lists to identify any missing modules.
    local missing_modules=()
    local modules_with_packages=()
    local modules_without_packages=()
    local -A new_modules_lookup
    for new_module_path in "${new_modules_unique[@]}"; do
        new_modules_lookup["$(basename "$new_module_path")"]=1
    done
    for old_module_path in "${old_modules_unique[@]}"; do
        local old_module_basename
        old_module_basename=$(basename "$old_module_path")
        if [[ -z "${new_modules_lookup[$old_module_basename]}" ]]; then
            missing_modules+=("$old_module_basename (module dir: $old_module_path)")
        fi
    done
    # For each missing module, check if it belongs to an installed RPM package.
    if [ ${#missing_modules[@]} -eq 0 ]; then
        echo "INFO: No custom modules missing from migration."
    else
        echo "INFO: Found possible missing custom selinux modules:"
        for module_info in "${missing_modules[@]}"; do
            local package_found="false"
            local module_basename="${module_info%% *}"
            for custom_module_path in "${custom_modules_unique[@]}"; do
                if [[ "$custom_module_path" =~ ${module_basename}.pp.(bz2|gz)$ ]]; then
                    local rpm_owner
                    rpm_owner=$(rpm -qf --queryformat "%{NAME}" "${custom_module_path}" 2>/dev/null)
                    if [[ -n "$rpm_owner" ]]; then
                        modules_with_packages+=("$module_info (from package: $rpm_owner)")
                        package_found="true"
                        break
                    fi
                fi
            done
            if [[ "$package_found" == "false" ]]; then
                modules_without_packages+=("$module_info")
            fi
        done
        # Print a report categorizing the missing modules for the user.
        echo "---"
        echo "These modules have corresponding packages; try reinstalling them:"
        if [ ${#modules_with_packages[@]} -eq 0 ]; then
            echo " (None)"
        else
            printf " * %s\n" "${modules_with_packages[@]}"
        fi
        echo
        echo "These modules do not have corresponding packages available:"
        if [ ${#modules_without_packages[@]} -eq 0 ]; then
            echo " (None)"
        else
            printf " * %s\n" "${modules_without_packages[@]}"
        fi
        echo ""
        echo "- modules in 100 dir by default comes with system policy package update -"
        echo "---"
    fi
    echo
}

# Deletes the old /var/lib/selinux directory and updates marker files.
delete_var_lib_selinux () {
    if [ ! -d "/var/lib/selinux" ]; then
        echo "INFO: Directory \`/var/lib/selinux\` does not exist. Nothing to do."
        return
    fi
    echo "INFO: Deleting /var/lib/selinux..."
    if find /var/lib/selinux -depth -print -delete; then
        echo "INFO: Successfully deleted /var/lib/selinux."
        rm --preserve-root=all -f "${target_dir}/selinux_modules_migrated-"{minimum,mls,targeted} && \
        echo "DO NOT DELETE THIS FILE - Part of SELinux policy root path migration on transactional or snapshoted systems." > "${target_dir}/${target_file_deletion}"
    else
        echo "ERROR: Failed to delete /var/lib/selinux." >&2
        exit 1
    fi
}

# Checks a specific location (snapshot or overlay) for the migration marker file.
check_for_flag_file() {
    local type_str="$1"
    local number="$2"
    local base_path="$3"
    local suffix="$4"

    echo -n "  Checking ${type_str} ${number}... "

    # Check each possible policy type marker inside the snapshot
    for policy in minimum mls targeted; do
        local full_path="${base_path}/${number}${suffix}${target_dir}/selinux_modules_migrated-${policy}"
        if [[ -f "${full_path}" ]]; then
            echo "Found."
            return 0
        fi
    done

    echo "Not found."
    return 1
}


## Main function

# Definitions
target_dir="/etc/selinux"
target_files_migration=( "${target_dir}/selinux_modules_migrated-"{minimum,mls,targeted} )
marker_file_found=false
target_file_deletion="var_lib_selinux_deleted"

# Handle specific flags first
if [[ "$1" == "--check-custom-selinux-modules" ]]; then
    check_custom_selinux_modules
    exit 0
elif [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "This script checks if it is safe to remove the old /var/lib/selinux directory."
    echo
    echo "Usage:"
    echo "  $0 (Checks snapshots and deletes /var/lib/selinux if safe)"
    echo "  $0 --check-custom-selinux-modules (Checks for unmigrated custom modules)"
    echo "  $0 -h|--help (Displays this help message)"
    exit 0
elif [[ -n "$1" ]]; then
    echo "Wrong parameter: $1. Use -h for help."
    exit 1
fi

# --- Default Execution: Check system and decide whether to delete ---

# Run essential pre-checks that can end the script early
for marker in "${target_files_migration[@]}"; do
    if [[ -f "$marker" ]]; then
        marker_file_found=true
        break
    fi
done

if [ -n "${TRANSACTIONAL_UPDATE}" ]; then
    echo "ERROR: Cannot run in transactional-update shell." >&2
    exit 1
fi
if [ -f "${target_dir}/${target_file_deletion}" ]; then
    echo "INFO: Cleanup already completed (${target_file_deletion} exists). Nothing to do."
    exit 0
fi
if [[ "$marker_file_found" == "false" ]]; then
    echo "INFO: Migration has not occurred yet, one of ${target_files_migration[*]} is missing). Nothing to do."
    exit 0
fi

# Perform safety checks based on system type
btrfs_check_passed=false
overlayfs_check_passed=true
is_btrfs_system=false

if [[ -x "$(command -v snapper)" ]]; then
    is_btrfs_system=true
    echo "INFO: Checking all Btrfs snapshots for migration marker file..."
    snapshots_without_file=()
    snapshot_list=$(snapper --no-headers --machine-readable csv list | awk -F, '$3 >= 1 {print $3}')

    if [[ -z "$snapshot_list" ]]; then
        echo "INFO: No snapshots found. Btrfs check passed."
        btrfs_check_passed=true
    else
        mapfile -t snapshots <<< "$snapshot_list"
        for snapshot_num in "${snapshots[@]}"; do
            if ! check_for_flag_file "snapshot" "$snapshot_num" "/.snapshots" "/snapshot"; then
                snapshots_without_file+=("$snapshot_num")
            fi
        done

        if [[ ${#snapshots_without_file[@]} -eq 0 ]]; then
            echo "INFO: All snapshots contain the migration file. Btrfs check passed."
            btrfs_check_passed=true
        fi
    fi

    # Perform conditional legacy OverlayFS check
    tu_path=$(command -v transactional-update)
    if [[ -n "$tu_path" ]]; then
        tu_version=$(transactional-update --version | awk '/transactional-update/ {print $NF}')
        if [[ "${tu_version%%.*}" -lt "5" ]]; then
            echo "INFO: Detected legacy transactional-update < 5."
            overlay_dir="/var/lib/overlay"
            if [ -d "$overlay_dir" ] && compgen -G "${overlay_dir}/*/etc" &> /dev/null; then
                echo "INFO: /etc is managed by OverlayFS."
            else
                echo "INFO: /etc is not managed by OverlayFS. Skipping check."
            fi
        fi
    fi
else
    # Fallback: No snapper. Check if root is Btrfs.
    root_fs=""
    if command -v findmnt &> /dev/null; then
        root_fs=$(findmnt -n -o FSTYPE /)
    else
        root_fs=$(awk '$2 == "/" {print $3}' /proc/mounts)
    fi

    if [[ "$root_fs" != "btrfs" ]]; then
        echo "INFO: snapper not found and root is not Btrfs ($root_fs). Checking marker file age..."
        latest_marker_time=0
        for marker in "${target_files_migration[@]}"; do
            if [[ -f "$marker" ]]; then
                mtime=$(stat -c %Y "$marker")
                [[ $mtime -gt $latest_marker_time ]] && latest_marker_time=$mtime
            fi
        done

        if [[ $latest_marker_time -eq 0 ]]; then
            echo "INFO: No migration markers found."
        else
            current_time=$(date +%s)
            age_days=$(( (current_time - latest_marker_time) / 86400 ))
            if [[ $age_days -ge 30 ]]; then
                echo "INFO: Migration markers are $age_days days old (>= 30). Safe to proceed."
                btrfs_check_passed=true
            else
                echo "INFO: Migration markers are only $age_days days old. Waiting for 30 days."
            fi
        fi
    else
        echo "ERROR: snapper command not found on a Btrfs system. This script requires snapper for Btrfs." >&2
        exit 1
    fi
fi

# Make the final decision based on the results of all checks
echo "---"
if [[ "$btrfs_check_passed" == "true" && "$overlayfs_check_passed" == "true" ]]; then
    echo "INFO: All checks passed. It is safe to proceed with deletion."
    delete_var_lib_selinux
else
    echo "WARNING: Cannot delete /var/lib/selinux. One or more checks failed:"
    if [[ "$is_btrfs_system" == "true" ]]; then
        if [[ "$btrfs_check_passed" == "false" ]]; then
            echo -n " - The following Btrfs snapshot(s) are not migrated: "
            printf " %s" "${snapshots_without_file[@]}"
            echo
        fi
        if [[ "$overlayfs_check_passed" == "false" ]]; then
            echo " - Issue with OverlayFS."
        fi
    else
        echo " - Migration markers are only ${age_days:-0} days old. Waiting for 30 days (root is ${root_fs:-unknown})."
    fi
fi
exit 0
