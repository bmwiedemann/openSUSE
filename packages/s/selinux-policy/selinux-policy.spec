#
# spec file for package selinux-policy
#
# Copyright (c) 2025 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# There are almost no SUSE specific modifications available in the policy, so we utilize the
# ones used by redhat and include also the SUSE specific ones (distro_suse_to_distro_redhat.patch)
%define distro redhat
%define ubac n
%define polyinstatiate n
%define monolithic n
%define BUILD_TARGETED 1
%define BUILD_MINIMUM 1
# At the moment we don't build the MLS policy. We didn't do any testing for this and have no
# confidence that it works. Feel free to branch the package and enable it, but be aware that
# you're on your own
%define BUILD_MLS 0

%define POLICYCOREUTILSVER %(rpm -q --qf %%{version} policycoreutils)
%define CHECKPOLICYVER %POLICYCOREUTILSVER

Summary:        SELinux policy configuration
License:        GPL-2.0-or-later
Group:          System/Management
Name:           selinux-policy
Version:        20260605
Release:        0
Source0:        %{name}-%{version}.tar.xz
Source1:        container.fc
Source2:        container.te
Source3:        container.if
Source4:        selinux-policy.rpmlintrc
Source5:        README.Update
Source6:        update.sh
Source7:        debug-build.sh
# ATTENTION! PED-12492 (bsc#1221342) is the implementation of a _temporary_ fix for PED-12491
# "Make SELinux packaging compliant with atomic/image based updates".
# PED-12492 (bsc#1221342) moves the store-root of SELinux from /var/lib/selinux to /etc/selinux completely.
# The proper implementation of PED-12491 should be done upstream and is tracked via PED-12493.
#
# PED-12492 (bsc#1221342): cleanoldsepoldir.service runs on every boot
# and checks if all snapper snapshots are migrated to /etc.
# If that is the case, it will delete the old /var/lib/selinux folder.
Source8:        cleanoldsepoldir.service.in
Source9:        cleanoldsepoldir.sh

Source18:       modules-minimum.lst

Source60:       selinux-policy.conf

Source91:       Makefile.devel
Source95:       macros.selinux-policy

URL:            https://github.com/openSUSE/selinux-policy
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version} < 1600
%define python_for_executables python311
BuildRequires:  %{python_for_executables}
BuildRequires:  %{python_for_executables}-policycoreutils
%else
BuildRequires:  %{primary_python}
BuildRequires:  %{python_module policycoreutils}
%endif
BuildRequires:  checkpolicy
BuildRequires:  fdupes
BuildRequires:  gawk
BuildRequires:  libxml2-tools
BuildRequires:  m4
BuildRequires:  policycoreutils
BuildRequires:  policycoreutils-devel
# we need selinuxenabled
Requires(pre):  policycoreutils >= %{POLICYCOREUTILSVER}
Requires(pre):  pam-config
# PED-12492 (bsc#1221342): Depend on libsemanage package that has configured /etc/selinux as store-root
Provides:       %{name}-storeroot-etc
Conflicts:      (libsemanage-conf without libsemanage-conf-storeroot-etc)
%if %{suse_version} >= 1600
# PED-12492 (boo#1221342): for >= 1600 the systemd-presets-common-SUSE will enable cleanoldsepoldir.service
# Users on older unsupported versions need to manually enable cleanoldsepoldir.service.
Conflicts:      (systemd-presets-common-SUSE without systemd-presets-common-SUSE-selinux-storeroot-etc-service)
%endif

Requires(posttrans): pam-config
Requires(posttrans): selinux-tools
Requires(posttrans): /usr/bin/sha512sum
Recommends:     audit
Recommends:     selinux-tools
# for audit2allow
Recommends:     python3-policycoreutils
Recommends:     container-selinux
Recommends:     policycoreutils-python-utils
Recommends:     selinux-autorelabel

%define common_params DISTRO=%{distro} UBAC=%{ubac} DIRECT_INITRC=n MONOLITHIC=%{monolithic} MLS_CATS=1024 MCS_CATS=1024

%define makeCmds() \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 bare \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 conf \
install -p -m0644 ./dist/%1/booleans.conf ./policy/booleans.conf \
install -p -m0644 ./dist/%1/users ./policy/users \

%define makeModulesConf() \
install -p -m0644 ./dist/%1/modules.conf ./policy/modules.conf \

%define installCmds() \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 base.pp \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 validate modules \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} install \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} install-appconfig \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} SEMODULE="%{_sbindir}/semodule -p %{buildroot} -X 100 " load \
%{__mkdir} -p %{buildroot}%{_sysconfdir}/selinux/%1/logins \
%{__mkdir} -p %{buildroot}%{_sysconfdir}/selinux/%1/active/modules/{1,2,4}00 \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs \
install -m0644 ./config/file_contexts.subs_dist %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files \
install -m0644 ./dist/%1/setrans.conf %{buildroot}%{_sysconfdir}/selinux/%1/setrans.conf \
install -m0644 ./dist/customizable_types %{buildroot}%{_sysconfdir}/selinux/%1/contexts/customizable_types \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.bin \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local.bin \
install -p -m0644 ./dist/booleans.subs_dist %{buildroot}%{_sysconfdir}/selinux/%1 \
rm -f %{buildroot}%{_datadir}/selinux/%1/*pp*  \
%{_bindir}/sha512sum %{buildroot}%{_sysconfdir}/selinux/%1/policy/policy.* | cut -d' ' -f 1 > %{buildroot}%{_sysconfdir}/selinux/%1/.policy.sha512; \
rm -rf %{buildroot}%{_sysconfdir}/selinux/%1/contexts/netfilter_contexts  \
rm -rf %{buildroot}%{_sysconfdir}/selinux/%1/modules/active/policy.kern \
rm -f %{buildroot}%{_sysconfdir}/selinux/%1/active/*.linked \
%nil

%define fileList() \
%defattr(-,root,root) \
%dir %{_sysconfdir}/selinux/%1 \
%config(noreplace) %{_sysconfdir}/selinux/%1/setrans.conf \
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/seusers \
%dir %{_sysconfdir}/selinux/%1/logins \
%dir %{_sysconfdir}/selinux/%1/active \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/semanage.read.LOCK \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/semanage.trans.LOCK \
%dir %attr(700,root,root) %{_sysconfdir}/selinux/%1/active/modules \
%dir %{_sysconfdir}/selinux/%1/active/modules/100 \
%dir %{_sysconfdir}/selinux/%1/active/modules/200 \
%dir %{_sysconfdir}/selinux/%1/active/modules/400 \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/active/modules/100/base \
%dir %{_sysconfdir}/selinux/%1/policy/ \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/policy/policy.* \
%{_sysconfdir}/selinux/%1/.policy.sha512 \
%dir %{_sysconfdir}/selinux/%1/contexts \
%config %{_sysconfdir}/selinux/%1/contexts/customizable_types \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/securetty_types \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/dbus_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/x_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/default_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/virtual_domain_context \
%config %{_sysconfdir}/selinux/%1/contexts/virtual_image_context \
%config %{_sysconfdir}/selinux/%1/contexts/lxc_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/systemd_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/sepgsql_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/openssh_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/snapperd_contexts \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/default_type \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/failsafe_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/initrc_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/removable_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/userhelper_context \
%dir %{_sysconfdir}/selinux/%1/contexts/files \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.bin \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.homedirs \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.homedirs.bin \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local.bin \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs \
%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs_dist \
%{_sysconfdir}/selinux/%1/booleans.subs_dist \
%config %{_sysconfdir}/selinux/%1/contexts/files/media \
%dir %{_sysconfdir}/selinux/%1/contexts/users \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/root \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/guest_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/xguest_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/user_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/staff_u \
%dir %{_datadir}/selinux/%1 \
%dir %{_datadir}/selinux/packages/%1 \
%{_datadir}/selinux/%1/base.lst \
%{_datadir}/selinux/%1/modules.lst \
%{_datadir}/selinux/%1/nonbasemodules.lst \
%dir %{_sysconfdir}/selinux/%1 \
%{_sysconfdir}/selinux/%1/active/commit_num \
%{_sysconfdir}/selinux/%1/active/users_extra \
%{_sysconfdir}/selinux/%1/active/homedir_template \
%{_sysconfdir}/selinux/%1/active/seusers \
%{_sysconfdir}/selinux/%1/active/file_contexts \
%{_sysconfdir}/selinux/%1/active/policy.kern \
%{_sysconfdir}/selinux/%1/active/modules_checksum \
%ghost %{_sysconfdir}/selinux/%1/active/policy.linked \
%ghost %{_sysconfdir}/selinux/%1/active/seusers.linked \
%ghost %{_sysconfdir}/selinux/%1/active/users_extra.linked \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/active/file_contexts.homedirs \
%nil

%define relabel() \
. %{_sysconfdir}/selinux/config; \
FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
if selinuxenabled; then \
  if [ $? = 0 ] && [ "${SELINUXTYPE}" = %1 ] && [ -f ${FILE_CONTEXT}.pre ]; then \
    %{_sbindir}/fixfiles -C ${FILE_CONTEXT}.pre restore 2> /dev/null; \
    rm -f ${FILE_CONTEXT}.pre; \
  fi; \
  /sbin/restorecon -e /run/media -R /root /var/log /var/run %{_sysconfdir}/passwd* %{_sysconfdir}/group* %{_sysconfdir}/*shadow* 2> /dev/null; \
fi;

%define preMigration() \
# PED-12492 (bsc#1221342): Snapper rollbacks can cause snapshots to still require the old /var/lib/selinux location. \
# This part checks the state of the system and creates marker files for the rest of the migration. \
# If necessary, it will create a backup of /var/lib/selinux. \
previous_selinux_modules_dir="/var/lib/selinux"; \
if [ %1 -ne 1 ] || [[ "$(ls -A ${previous_selinux_modules_dir} 2>/dev/null)" ]]; then \
    check_tmpfiles=(%{_sysconfdir}/selinux/{temp_selinux_modules_dir_created,selinux_modules_migrated-%2,var_lib_selinux_deleted}); \
    check_btrfs_snapshot_etc=0; \
    is_btrfs=0; \
    # check if / is btrfs \
    if findmnt -t btrfs / > /dev/null 2>&1; then \
        is_btrfs=1; \
        # check if /etc is on a snapshotted root subvolume \
        if [[ $(btrfs subvolume list / | grep -c "\@/etc") -gt 0 ]]; then \
            check_btrfs_snapshot_etc=1; \
            if [[ ! -f "${check_tmpfiles[1]}" || ! -f "${check_tmpfiles[2]}" ]]; then \
                echo "--- WARNING: Non-default installation with separate subvolume for \\`/etc\\` detected. ---"; \
                echo "---          Migration will continue but in case of rollback - manual intervention might be needed. ---"; \
            elif [ -f "${check_tmpfiles[1]}" ]; then \
                echo "---          If your system has non-snapshotted subvolume \\`/etc\\`, you need to reinstall selinux-policy packages after rollback."; \
            elif [ -f "${check_tmpfiles[2]}" ]; then \
                echo "--- INFO: SELinux policy modules are stored in \\`/etc/selinux\\`. ---"; \
                echo "---       and \\`/var/lib/selinux\\` removed. No interaction needed. ---"; \
            fi; \
        fi; \
    else \
        if [[ ! -f "${check_tmpfiles[1]}" || ! -f "${check_tmpfiles[2]}" ]]; then \
            echo "--- WARNING: Non-default installation with no btrfs \\`/\\` detected. ---"; \
            echo "---          Migration will continue but in case of selinux-policy downgrade - manual intervention might be needed. ---"; \
            echo "---          \\`/var/lib/selinux\\` will be deleted one month after migration ---"; \
        elif [ -f "${check_tmpfiles[2]}" ]; then \
            echo "--- INFO: SELinux policy modules are stored in \\`/etc/selinux\\`. ---"; \
            echo "---       and \\`/var/lib/selinux\\` removed. No interaction needed. ---"; \
	fi ; \
    fi; \
#------\
    # check if /var/lib/selinux has been migrated and print info \
    if [[ ! -f "${check_tmpfiles[1]}" && ! -f "${check_tmpfiles[2]}" ]]; then \
        echo; \
        echo "--- WARNING: Beware this package changes installation of SELinux modules (and copy custom ones for smooth transition) from \\`/var/lib/selinux\\` to \\`/etc/selinux\\` ---"; \
        echo "---          Also it installs service \\`cleanoldsepoldir.service\\` and script in \\`%{_libexecdir}/selinux\\` which helps you to identify not migrated modules \(just in case of corner cases\). ---"; \
        echo "---          On boot service will run a script to check snapshots and DELETE \\`/var/lib/selinux\\` when no snapshots use this directory. ---"; \
        echo; \
        if [ "${is_btrfs}" -eq 0 ]; then \
            echo "INFO: No btrfs on \\`/\\`, \\`/var/lib/selinux\\` backup needed."; \
        elif [ "${check_btrfs_snapshot_etc}" -eq 0 ]; then \
            echo "INFO: \\`/etc\\` on snapshotted root, \\`/var/lib/selinux\\` backup needed."; \
        else \
            echo "INFO: \\`/etc\\` on separated subvolume, \\`/var/lib/selinux\\` backup needed."; \
        fi; \
        # check /var/lib/dir state and create tmp directory of SELinux policy \
        touch %{_sysconfdir}/selinux/selinux_migration_pending-%2; \
        temp_selinux_module_dir="/var/lib/selinux_tmpbck"; \
        if [ -d "${previous_selinux_modules_dir}" ]; then \
            echo "INFO: Creating tmp copy of \\`/var/lib/selinux\\` to keep previous rollbacks work for selinux-policy-%2."; \
	    mkdir -p "${temp_selinux_module_dir}" && cp -a ${previous_selinux_modules_dir}/. ${temp_selinux_module_dir}/; \
            echo "DO NOT DELETE THIS FILE - Part of SELinux policy migration - it will be deleted after installation of the package." > %{_sysconfdir}/selinux/temp_selinux_modules_dir_created; \
	else \
	    echo "ERROR: ${previous_selinux_modules_dir} does not exists."; \
        fi; \
    else \
      # reminder when new update package arrives \
        if [ -f "${check_tmpfiles[1]}" ]; then \
            echo "INFO: SELinux policy store root already in \\`/etc/selinux\\`."; \
            echo "--- In case of issues with custom SELinux modules you can run \\`%{_libexecdir}/selinux/cleanoldsepoldir.sh --check-custom-selinux-modules\\` or RE-APPLY them manually. ---"; \
            echo "--- Backup of modules if exists is in \\`/var/lib/selinux/{minimum,sandbox,targeted,}/active\\`. --- "; \
            echo "--- \\`/var/lib/selinux\\` will be automaticaly DELETED once there are no snapshots with old path. ---"; \
        fi; \
        if [ -f "${check_tmpfiles[2]}" ]; then \
            echo "INFO: SELinux policy modules are stored in \\`/etc/selinux\\`."; \
            echo "      and \\`/var/lib/selinux\\` removed. No interaction needed."; \
        fi; \
    fi; \
else \
    # in case of clean installation of the package create migration marker files \
    if [ ! -f "%{_sysconfdir}/selinux/selinux_modules_migrated-%2" ]; then \
        echo "DO NOT DELETE THIS FILE - Part of SELinux policy root path migration from \\'/var/lib/selinux\\' to \\'/etc/selinux\\'." > %{_sysconfdir}/selinux/selinux_modules_migrated-%2; \
    else \
        echo "INFO: Marker file selinux_modules_migrated-%2 exists."\
    fi;\
fi;\
%nil

%define postMigration() \
# PED-12492 (bsc#1221342): Snapper rollbacks can cause snapshots to still require the old /var/lib/selinux location. \
# This part copies the custom local SELinux changes to /etc/selinux. \
current_selinux_modules_dir="%{_sysconfdir}/selinux"; \
if [[ %1 -ne 1  || -f "${current_selinux_modules_dir}/selinux_migration_pending-%2" ]]; then \
    # rename tmp dir /var/lib/selinux_tmpbck to old /var/lib/selinux so we can keep it in case of rollback \
    check_tmpfiles=(%{_sysconfdir}/selinux/{temp_selinux_modules_dir_created,selinux_modules_migrated-%2,var_lib_selinux_deleted}); \
    custom_local_files_relative_path="/selinux/%2/active"; \
    previous_selinux_modules_dir="%{_sharedstatedir}/selinux"; \
    temp_selinux_module_dir="/var/lib/selinux_tmpbck"; \
    # Copy custom modules and local modifications to keep smooth transition to /etc/selinux for for selinux-policy-%2 \
    if [[ -f "${check_tmpfiles[0]}" && ! -f "${check_tmpfiles[1]}" && ! -f "${check_tmpfiles[2]}" ]]; then \
        if [ -d "${previous_selinux_modules_dir}" ]; then \
            if [ -f "${current_selinux_modules_dir}/selinux_migration_pending-%2" ]; then \
                # Copy local modifications (.local files) \
                check_local_files="pkeys ibendports ports interfaces nodes booleans seusers users users_extra file_contexts"; \
                for f in ${check_local_files}; do \
                    [ -e "${temp_selinux_module_dir}/%2/active/${f}.local" ] && \
                    cp -f "${temp_selinux_module_dir}/%2/active/${f}.local" "${current_selinux_modules_dir}/%2/active/${f}.local"; \
                done; \
                # Copy custom modules (200, 400, disabled) \
                echo "INFO: Copying custom modules from ${previous_selinux_modules_dir} to ${current_selinux_modules_dir} for selinux-policy-%2."; \
                if [ -d "${temp_selinux_module_dir}/%2/active/modules" ]; then \
                    for d in 200 400 disabled; do \
                        [ -d "${temp_selinux_module_dir}/%2/active/modules/${d}" ] && \
                        cp -a "${temp_selinux_module_dir}/%2/active/modules/${d}" "${current_selinux_modules_dir}/%2/active/modules/"; \
                    done; \
                fi; \
               # Finalize this flavor \
                echo "DO NOT DELETE THIS FILE - Part of SELinux policy migration" > ${current_selinux_modules_dir}/selinux_modules_migrated-%2 && \
                rm --preserve-root=all -f "${current_selinux_modules_dir}/selinux_migration_pending-%2"; \
            fi; \
            # Copy /var/lib/selinux_tmpback to /var/lib/selinux when no flavors missing migration \
	    if ! ls "${current_selinux_modules_dir}"/ 2>/dev/null | grep -qE "selinux_migration_pending-(minimum|mls|targeted)$"; then \
                if [[ "$(ls -A ${temp_selinux_module_dir} 2>/dev/null)" ]]; then \
                    echo "INFO: All flavors migrated. Restoring /var/lib/selinux."; \
                    find "${previous_selinux_modules_dir}" -mindepth 1 -delete 2>/dev/null && \
                    cp -a "${temp_selinux_module_dir}/." "${previous_selinux_modules_dir}/" && \
                    rm --preserve-root=all -rf "${temp_selinux_module_dir}" && \
                    rm --preserve-root=all -f "${current_selinux_modules_dir}"/temp_selinux_modules_dir_created; \
                    # check for possible not migrated custom modules \
                    if [ ! -f "${check_tmpfiles[2]}" ]; then \
                        [ -f "%{_libexecdir}/selinux/cleanoldsepoldir.sh" ] && %{_libexecdir}/selinux/cleanoldsepoldir.sh --check-custom-selinux-modules; \
                    fi; \
                else \
                    echo "ERROR: Backup dir empty. Migration failure."; \
                    exit 1; \
                fi; \
	    else \
                echo "INFO: Not all flavors migrated. Not restoring /var/lib/selinux."; \
            fi; \
        else \
            echo "ERROR: ${previous_selinux_modules_dir} does not exists."; \
            exit 1; \
        fi; \
    fi; \
fi; \
%nil

%define postunMigration() \
# PED-12492 (bsc#1221342): Snapper rollbacks can cause snapshots to still require the old /var/lib/selinux location. \
# This part delete marker files per flavor. \
if [ "$1" = 0 ]; then \
    check_tmpfiles=(%{_sysconfdir}/selinux/{temp_selinux_modules_dir_created,selinux_migration_pending-%2,selinux_modules_migrated-%2,var_lib_selinux_deleted}); \
    current_selinux_modules_dir="%{_sysconfdir}/selinux"; \
    for i in "${check_tmpfiles[@]}"; do \
       [ -f "${i}" ] && rm --preserve-root=all "${i}" \
    done \
    # TBD - cleanup *.local files" \
fi; \
%nil

%define preInstall() \
if [ "$1" -ne 1 ] && [ -s %{_sysconfdir}/selinux/config ]; then \
  . %{_sysconfdir}/selinux/config; \
  FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
  if [ "${SELINUXTYPE}" = %1 ] && [ -f ${FILE_CONTEXT} ]; then \
    [ -f ${FILE_CONTEXT}.pre ] || cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.pre; \
  fi; \
  touch %{_sysconfdir}/selinux/%1/.rebuild; \
  if [ -e %{_sysconfdir}/selinux/%1/.policy.sha512 ]; then \
    POLICY_FILE=$(ls %{_sysconfdir}/selinux/%1/policy/policy.* | sort | head -1); \
    sha512=$(sha512sum "$POLICY_FILE" | cut -d ' ' -f 1); \
    checksha512=$(cat %{_sysconfdir}/selinux/%1/.policy.sha512); \
    if [ "$sha512" = "$checksha512" ] ; then \
      rm %{_sysconfdir}/selinux/%1/.rebuild; \
    fi; \
  fi; \
fi; \
%nil

%define postInstall() \
. %{_sysconfdir}/selinux/config; \
if [ -e %{_sysconfdir}/selinux/%2/.rebuild ]; then \
  rm %{_sysconfdir}/selinux/%2/.rebuild; \
  /usr/sbin/semodule -B -n -s %2 2> /dev/null; \
fi; \
%postInstallRelabel %1 %2

%define postInstallRelabel() \
if [ -n "${TRANSACTIONAL_UPDATE}" ]; then \
  touch /etc/selinux/.autorelabel ; \
else \
  if [ "${SELINUXTYPE}" = "%2" ]; then \
    if selinuxenabled; then \
      load_policy; \
    else \
      # probably a first install of the policy \
      true; \
    fi; \
  fi; \
  if selinuxenabled; then \
    if [ %1 -eq 1 ]; then \
      /sbin/restorecon -R /root /var/log /run /etc/passwd* /etc/group* /etc/*shadow* 2> /dev/null; \
    else \
      %relabel %2 ; \
    fi; \
  else \
    # run fixfiles on next boot \
    touch /etc/selinux/.autorelabel ; \
  fi; \
fi; \
%nil

%define postInstallMinimum() \
modules=$(cat %{_datadir}/selinux/minimum/modules.lst); \
basemodules=$(cat %{_datadir}/selinux/minimum/base.lst); \
enabledmodules=$(cat %{_datadir}/selinux/minimum/modules-enabled.lst); \
mkdir -p %{_sysconfdir}/selinux/minimum/active/modules/disabled; \
if [ "$1" -eq 1 ]; then \
    for p in $modules; do \
        touch %{_sysconfdir}/selinux/minimum/active/modules/disabled/"$p"; \
    done; \
    for p in $basemodules $enabledmodules; do \
        rm -f %{_sysconfdir}/selinux/minimum/active/modules/disabled/"$p"; \
    done; \
    printf "login -m  -s unconfined_u -r s0-s0:c0.c1023 __default__\\nlogin -m  -s unconfined_u -r s0-s0:c0.c1023 root\\n" | %{_sbindir}/semanage import -S minimum -f -; \
    /sbin/restorecon -R /root /var/log /var/run 2> /dev/null; \
    %{_sbindir}/semodule -B -s minimum 2> /dev/null; \
else \
    instpackages=$(cat %{_datadir}/selinux/minimum/instmodules.lst); \
    for p in $modules; do \
        touch %{_sysconfdir}/selinux/minimum/active/modules/disabled/"$p"; \
    done; \
    for p in $instpackages snapper dbus kerberos nscd rtkit; do \
        rm -f %{_sysconfdir}/selinux/minimum/active/modules/disabled/"$p"; \
    done; \
    %{_sbindir}/semodule -B -s minimum 2> /dev/null; \
fi; \
%postInstallRelabel $1 minimum \
%nil

%define modulesList() \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "module" { printf "%%s ", $1 }' ./policy/modules.conf > %{buildroot}%{_datadir}/selinux/%1/modules.lst \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "base" { printf "%%s ", $1 }' ./policy/modules.conf > %{buildroot}%{_datadir}/selinux/%1/base.lst \

%define nonBaseModulesList() \
modules=$(cat %{buildroot}%{_datadir}/selinux/%1/modules.lst); \
for i in $modules; do \
  if [ "$i" != "sandbox" ]; then \
    echo "%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/active/modules/100/$i" >> %{buildroot}%{_datadir}/selinux/%1/nonbasemodules.lst ; \
  fi; \
done;

%description
A complete SELinux policy that can be used as the system policy for a variety
of systems and used as the basis for creating other policies.

%files
%defattr(-,root,root,-)
%license COPYING
%dir %{_datadir}/selinux
%dir %{_datadir}/selinux/packages
%dir %{_sysconfdir}/selinux
%dir %{_sharedstatedir}/selinux
%ghost %config(noreplace) %{_sysconfdir}/selinux/config
%{_tmpfilesdir}/selinux-policy.conf
%{_rpmconfigdir}/macros.d/macros.selinux-policy
%{_unitdir}/cleanoldsepoldir.service
%{_libexecdir}/selinux/cleanoldsepoldir.sh

%package sandbox
Summary:        SELinux policy sandbox
Group:          System/Management
Requires(pre):  selinux-policy-targeted = %{version}-%{release}

%description sandbox
SELinux sandbox policy used for the policycoreutils-sandbox package

%files sandbox
%verify(not md5 size mtime) %{_datadir}/selinux/packages/sandbox.pp

%post sandbox
rm -f %{_sysconfdir}/selinux/*/modules/active/modules/sandbox.pp.disabled 2>/dev/null
rm -f %{_sysconfdir}/selinux/*/active/modules/disabled/sandbox 2>/dev/null
%{_sbindir}/semodule -n -X 100 -i %{_datadir}/selinux/packages/sandbox.pp 2> /dev/null
if %{_sbindir}/selinuxenabled ; then
  %{_sbindir}/load_policy
fi;
exit 0

%preun sandbox
if [ "$1" -eq 0 ] ; then
  %{_sbindir}/semodule -n -d sandbox 2>/dev/null
  if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/load_policy
  fi;
fi;
exit 0

%prep

# set up selinux-policy
%autosetup -n %{name}-%{version} -p1

# dirty hack for container-selinux, because selinux-policy won't build without it
# upstream does not want to include it in main policy tree:
# see discussion in https://github.com/containers/container-selinux/issues/186
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3}; do
  cp $i policy/modules/services/
done

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/selinux
touch %{buildroot}%{_sysconfdir}/selinux/config
mkdir -p %{buildroot}%{_tmpfilesdir}
cp %{SOURCE60} %{buildroot}%{_tmpfilesdir}

# Adjust and install RPM macro file
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -m 644 %{SOURCE95} %{buildroot}%{_rpmconfigdir}/macros.d/
sed -i 's|SELINUXPOLICYVERSION|%{version}-%{release}|' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy
sed -i 's|SELINUXSTOREPATH|%{_sysconfdir}/selinux|' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy

# Always create policy module package directories
mkdir -p %{buildroot}%{_datadir}/selinux/{targeted,mls,minimum,modules}/
mkdir -p %{buildroot}%{_sharedstatedir}/selinux/{targeted,mls,minimum,modules}/

mkdir -p %{buildroot}%{_datadir}/selinux/packages/{targeted,mls,minimum,modules}/

make clean
%if %{BUILD_TARGETED}
%makeCmds targeted mcs allow
%makeModulesConf targeted
%installCmds targeted mcs allow
# recreate sandbox.pp
rm -rf %{buildroot}%{_sysconfdir}/selinux/targeted/active/modules/100/sandbox
%make_build %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs sandbox.pp
mv sandbox.pp %{buildroot}%{_datadir}/selinux/packages/sandbox.pp
%modulesList targeted
%nonBaseModulesList targeted
%endif

%if %{BUILD_MINIMUM}
%makeCmds minimum mcs allow
%makeModulesConf targeted
%installCmds minimum mcs allow
# Sandbox is only targeted
rm -f %{buildroot}%{_sysconfdir}/selinux/minimum/modules/active/modules/sandbox.pp
rm -rf %{buildroot}%{_sysconfdir}/selinux/minimum/active/modules/100/sandbox
install -p -m 644 %{SOURCE18} %{buildroot}%{_datadir}/selinux/minimum/modules-enabled.lst
%modulesList minimum
%nonBaseModulesList minimum
%endif

%if %{BUILD_MLS}
%makeCmds mls mls deny
%makeModulesConf mls
%installCmds mls mls deny
%modulesList mls
%nonBaseModulesList mls
%endif

# Install devel
mkdir -p %{buildroot}%{_mandir}
cp -R  man/* %{buildroot}%{_mandir}
make %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs DESTDIR=%{buildroot} PKGNAME=%{name} install-docs
make %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs DESTDIR=%{buildroot} PKGNAME=%{name} install-headers
mkdir %{buildroot}%{_datadir}/selinux/devel/
mv %{buildroot}%{_datadir}/selinux/targeted/include %{buildroot}%{_datadir}/selinux/devel/include
mkdir %{buildroot}%{_datadir}/selinux/devel/include/distributed
install -m 644 %{SOURCE91} %{buildroot}%{_datadir}/selinux/devel/Makefile
install -m 644 doc/example.* %{buildroot}%{_datadir}/selinux/devel/
install -m 644 doc/policy.* %{buildroot}%{_datadir}/selinux/devel/
%{_bindir}/sepolicy manpage -a -p %{buildroot}%{_datadir}/man/man8/ -w -r %{buildroot}
mkdir %{buildroot}%{_datadir}/selinux/devel/html
mv %{buildroot}%{_datadir}/man/man8/*.html %{buildroot}%{_datadir}/selinux/devel/html
mv %{buildroot}%{_datadir}/man/man8/style.css %{buildroot}%{_datadir}/selinux/devel/html
rm %{buildroot}%{_mandir}/man8/container_selinux.8*
rm %{buildroot}%{_datadir}/selinux/devel/include/services/container.if
%fdupes -s %{buildroot}%{_mandir}
# Due to PED-12492 (bsc#1221342): hard link identical files in stead of hard copy
# to fix rpmlint duplicate-files-waste error.
%fdupes -s %{buildroot}%{_sysconfdir}/selinux/targeted/contexts
%fdupes -s %{buildroot}%{_sysconfdir}/selinux/minimum/contexts


# PED-12492 (bsc#1221342): install service file and script to check old snaphsots.
sed "s|@LIBEXECDIR@|%{_libexecdir}|g" %{_sourcedir}/cleanoldsepoldir.service.in > cleanoldsepoldir.service
install -D -m 644 cleanoldsepoldir.service %{buildroot}%{_unitdir}/cleanoldsepoldir.service
install -D -m 754 %{SOURCE9} %{buildroot}%{_libexecdir}/selinux/cleanoldsepoldir.sh

%pre
%service_add_pre cleanoldsepoldir.service

%post
if [ ! -s %{_sysconfdir}/selinux/config ]; then
  # new install, use old sysconfig file if that exists,
  # else create new one.
  if [ -f  %{_sysconfdir}/sysconfig/selinux-policy ]; then
    mv %{_sysconfdir}/sysconfig/selinux-policy %{_sysconfdir}/selinux/config
  else
    echo "
# This file controls the state of SELinux on the system.
# SELinux can be completly disabled with the \"selinux=0\" kernel
# commandline option.
#
# SELINUX= can take one of these two values:
#     enforcing  - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
# Previously SELinux could be disabled by changing the value to
# 'disabled'. This is deprecated and should not be used anymore.
# If you want to disable SELinux add 'selinux=0' to the kernel
# command line. For details see
# https://github.com/SELinuxProject/selinux-kernel/wiki/DEPRECATE-runtime-disable
SELINUX=enforcing
# SELINUXTYPE= can take one of these three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected.
SELINUXTYPE=targeted

" > %{_sysconfdir}/selinux/config
  fi
  ln -sf ../selinux/config %{_sysconfdir}/sysconfig/selinux-policy
  %{_sbindir}/restorecon %{_sysconfdir}/selinux/config 2> /dev/null || :
fi
%tmpfiles_create %_tmpfilesdir/selinux-policy.conf
if [ "$1" -eq 1 ]; then
  pam-config -a --selinux
fi
%if 0%{?is_opensuse}
# 2025-04-07 cahu:
# Extremely ugly Workaround for t-u module removal issue
# (see bsc#1221342 bsc#1238062 bsc#1230643 bsc#1230938)
# This removes empty module folders in /var/lib/selinux that
# are created by microOS' create-dirs-from-rpmdb on rollback when the
# current policy has dropped the module that was still contained in an older
# snapshot. That means the removed module will also NOT be contained
# in previous snapshots. Also this can cause warnings during install due to rpmdb
# still containing the path that was deleted, which should go away in the subsequent
# installations.
# Can be dropped once PED-12491 is implemented.
if [ -n "${TRANSACTIONAL_UPDATE}" ]; then
  for p in targeted minimum mls; do
    if [ -d %{_sysconfdir}/selinux/$p/active/modules/100 ]; then
      find %{_sysconfdir}/selinux/$p/active/modules/100 -type d -empty -delete -print
    fi
  done
fi
%endif

%service_add_post cleanoldsepoldir.service
exit 0

%define post_un() \
# disable selinux if we uninstall a policy and it's the used one \
if [ "$1" -eq 0 ]; then \
  if [ -s %{_sysconfdir}/selinux/config ]; then \
    . %{_sysconfdir}/selinux/config > /dev/null 2>&1 || true ; \
  fi; \
  if [ "$SELINUXTYPE" = "$2" ]; then \
    %{_sbindir}/setenforce 0 2> /dev/null ; \
    if [ -s %{_sysconfdir}/selinux/config ]; then \
      sed -i 's/^SELINUX=.*/SELINUX=permissive/g' %{_sysconfdir}/selinux/config ; \
    fi; \
  fi; \
  pam-config -d --selinux ; \
fi; \

%preun
%service_del_preun cleanoldsepoldir.service

%postun
if [ "$1" = 0 ]; then
  %{_sbindir}/setenforce 0 2> /dev/null
  if [ -s %{_sysconfdir}/selinux/config ]; then
    sed -i 's/^SELINUX=.*/SELINUX=permissive/g' %{_sysconfdir}/selinux/config
  fi

  # PED-12492 (bsc#1221342): cleanup of marker_files in /etc/selinux"
  check_tmpfiles=(%{_sysconfdir}/selinux/{temp_selinux_modules_dir_created,selinux_modules_migrated-minimum, selinux_modules_migrated-mls, selinux_modules_migrated-targeted,var_lib_selinux_deleted})
  current_selinux_modules_dir="%{_sysconfdir}/selinux"
  for i in $check_tmpfiles; do
     [[ -f "${current_selinux_modules_dir}/${i}" ]] && rm --preserve-root=all ${current_selinux_modules_dir}/{i}
  done
fi

%service_del_postun cleanoldsepoldir.service

exit 0

%package devel
Summary:        SELinux policy devel
Group:          System/Management
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       /usr/bin/make
Requires:       checkpolicy >= %{CHECKPOLICYVER}
Requires:       m4
Requires(post): policycoreutils-devel >= %{POLICYCOREUTILSVER}

%description devel
SELinux policy development package

%files devel
%defattr(-,root,root,-)
%dir %{_datadir}/selinux/devel
%dir %{_datadir}/selinux/devel/html/
%doc %{_datadir}/selinux/devel/html/*
%dir %{_datadir}/selinux/devel/include
%dir %{_datadir}/selinux/devel/include/distributed
%{_datadir}/selinux/devel/include/*
%{_datadir}/selinux/devel/Makefile
%{_datadir}/selinux/devel/example.*
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/sepolgen/interface_info

%post devel
%{_sbindir}/selinuxenabled && %{_bindir}/sepolgen-ifgen 2>/dev/null
exit 0

%package doc
Summary:        SELinux policy documentation
Group:          System/Management
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       /usr/bin/xdg-open

%description doc
SELinux policy documentation and man page package

%files doc
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}
%doc %{_datadir}/man/ru/man8/*
%doc %{_datadir}/man/man8/*
%{_datadir}/selinux/devel/policy.*

%if %{BUILD_TARGETED}
%package targeted
Summary:        SELinux targeted base policy
Group:          System/Management
Provides:       selinux-policy-base = %{version}-%{release}
Requires(pre):  coreutils
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       selinux-policy = %{version}-%{release}

%description targeted
SELinux policy targeted base module.

%pre targeted
%preInstall targeted
%preMigration $1 targeted

# move from %posttrans to %post fixes boo#1264463
%post targeted
%postMigration $1 targeted

%posttrans targeted
%postInstall $1 targeted
exit 0

%postun targeted
%postunMigration $1 targeted
%post_un $1 targeted
exit 0

%triggerin -- libpcre2-8-0
%{_sbindir}/selinuxenabled && %{_sbindir}/semodule -nB 2> /dev/null
exit 0

%files targeted -f %{buildroot}%{_datadir}/selinux/targeted/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/targeted/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/targeted/contexts/users/sysadm_u
%fileList targeted
%endif

%if %{BUILD_MINIMUM}
%package minimum
Summary:        SELinux minimum base policy
Group:          System/Management
Provides:       selinux-policy-base = %{version}-%{release}
Requires(post): policycoreutils >= %{POLICYCOREUTILSVER}
Requires(post): policycoreutils-python-utils >= %{POLICYCOREUTILSVER}
Requires(pre):  coreutils
Requires(pre):  /usr/bin/awk
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       selinux-policy = %{version}-%{release}

%description minimum
SELinux policy minimum base module.

%pre minimum
%preInstall minimum
%preMigration $1 minimum
if [ "$1" -ne 1 ]; then
  %{_sbindir}/semodule -s minimum --list-modules=full | awk '{ if ($4 != "disabled") print $2; }' > %{_datadir}/selinux/minimum/instmodules.lst
fi


# move from %posttrans to %post fixes boo#1264463
%post minimum
%postMigration $1 minimum

%posttrans minimum
%postInstallMinimum $1
exit 0

%postun minimum
%postunMigration $1 minimum
%post_un $1 minimum
exit 0

%files minimum -f %{buildroot}%{_datadir}/selinux/minimum/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/minimum/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/minimum/contexts/users/sysadm_u
%{_datadir}/selinux/minimum/modules-enabled.lst
%fileList minimum
%endif

%if %{BUILD_MLS}
%package mls
Summary:        SELinux mls base policy
Group:          System/Management
Provides:       selinux-policy-base = %{version}-%{release}
Requires:       policycoreutils-newrole >= %{POLICYCOREUTILSVER}
Requires:       setransd
Requires(pre):  policycoreutils >= %{POLICYCOREUTILSVER}
Requires(pre):  coreutils
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       selinux-policy = %{version}-%{release}

%description mls
SELinux policy mls base module.

%pre mls
%preInstall mls
%preMigration $1 mls

# move from %posttrans to %post fixes boo#1264463
%post mls
%postMigration $1 mls

%posttrans mls
%postInstall $1 mls

%postun mls
%postunMigration $1 mls
%post_un $1 mls
exit 0

%files mls -f %{buildroot}%{_datadir}/selinux/mls/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/mls/contexts/users/unconfined_u
%fileList mls
%endif

%changelog
