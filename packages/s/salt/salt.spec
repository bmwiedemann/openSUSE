#
# spec file for package salt
#
# Copyright (c) 2024 SUSE LLC
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


%global debug_package %{nil}

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1600
%define _alternatives 1
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "testsuite"
%define psuffix -test
%else
%define psuffix %{nil}
%endif

%if 0%{?suse_version} > 1210 || 0%{?rhel} >= 7 || 0%{?fedora} >= 28
%bcond_without systemd
%else
%bcond_with    systemd
%endif
%if 0%{?suse_version} > 1110
%bcond_without bash_completion
%bcond_without fish_completion
%bcond_without zsh_completion
%else
%bcond_with    bash_completion
%bcond_with    fish_completion
%bcond_with    zsh_completion
%endif
%bcond_without docs
%bcond_with    builddocs

%if %{without systemd}
%define service_del_preun echo %{*}
%endif
%if 0%{?sle_version} >= 150700
%{?sle15_python_module_pythons}
%else
%{?sle15allpythons}
%endif
%define skip_python2 1
%if 0%{?rhel} == 8 || (0%{?suse_version} == 1500 && 0%{?sle_version} < 150400)
%define singlespec_compat 1
%define __python3_bin_suffix 3.6
%if 0%{?rhel} == 8
%define __python3 /usr/libexec/platform-python
%else
%define __python3 /usr/bin/python3
%endif
%define python_module() python3-%**
%define python_files() -n python3-%1
%define python_subpackages %{nil}
%define python_sitelib %python3_sitelib
%define python_expand(+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=) %{lua: \
local args = rpm.expand("%**")\
local python_bin = rpm.expand("%__python3")\
local python_bin_suffix = rpm.expand("%__python3_bin_suffix")\
args = args:gsub("$python_bin_suffix", python_bin_suffix)\
args = args:gsub("$python_sitelib", "python3_sitelib")\
args = args:gsub("$python", python_bin)\
print(rpm.expand(args .. "\\n"))\
}
%endif
Name:           salt%{psuffix}
Version:        3006.0
Release:        0
Summary:        A parallel remote execution system
License:        Apache-2.0
Group:          System/Management
URL:            https://saltproject.io/
Source:         v%{version}.tar.gz
Source1:        README.SUSE
Source2:        salt-tmpfiles.d
Source3:        html.tar.bz2
Source4:        update-documentation.sh
Source5:        travis.yml
Source6:        transactional_update.conf

### SALT PATCHES LIST BEGIN
### IMPORTANT: The line above is used as a snippet marker. Do not touch it.

# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/88f40fff3b81edaa55f37949f56c67112ca2dcad
Patch1:         run-salt-master-as-dedicated-salt-user.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/cdecbbdf5db3f1cb6b603916fecd80738f5fae9a
Patch2:         run-salt-api-as-user-salt-bsc-1064520.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/c44b897eb1305c6b9c341fc16f729d2293ab24e4
Patch3:         activate-all-beacons-sources-config-pillar-grains.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/3c83bab3da101223c99af1f9ee2f3bf5e97be3f8
Patch4:         avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/1b9a160f578cf446f5ae622a450d23022e7e3ca5
Patch5:         fix-bsc-1065792.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/fec7f65b4debede8cf0eef335182fce2206e200d
Patch6:         enable-passing-a-unix_socket-for-mysql-returners-bsc.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/90
Patch7:         add-environment-variable-to-know-if-yum-is-invoked-f.patch

#### SUSE CAPABILITIES - unified ####
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/commit/713ccfdc5c6733495d3ce7f26a8cfeddb8e9e9c4
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/commit/b713d0b3031faadc17cd9cf09977ccc19e50bef7
Patch8:         add-custom-suse-capabilities-as-grains.patch
###########

#### SUSE SLES-ES SUPPORT ####
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/57166
Patch9:         fix-for-suse-expanded-support-detection.patch
############

#### ADLER - unified ####
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48812
# (closed upstream in favor of different solution - might affect server_id)
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/159
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/73e357d7eee19a73cade22becb30d9689cae27ba
Patch10:        use-adler32-algorithm-to-compute-string-checksums.patch
###########

#### X509 - unified ####
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/56819
Patch11:        x509-fixes-111.patch
###########

# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/58054
Patch12:        do-not-load-pip-state-if-there-is-no-3rd-party-depen.patch

#### SALT SUPPORT - unified ####
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/57054
Patch13:        early-feature-support-config.patch
###########

# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/57071
Patch14:        make-aptpkg.list_repos-compatible-on-enabled-disable.patch

### DEBIAN INFO_INSTALLED - unified ###
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50453
# (master PR not yet created - codejam)
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50453
#                     https://github.com/saltstack/salt/commit/e20362f6f053eaa4144583604e6aac3d62838419
# Can be dropped one pull/50453 is in released version.
Patch15:        debian-info_installed-compatibility-50453.patch
###########

# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/pull/116 (missing upstream PR to master)
Patch16:        return-the-expected-powerpc-os-arch-bsc-1117995.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51119 (master PR not yet created)
Patch17:        fix-issue-2068-test.patch
# PATCH_FIX_OPENSUSE Temporary fix allowing "id_" and "force" params while upstrem figures it out
Patch18:        temporary-fix-extend-the-whitelist-of-allowed-comman.patch

### FQDNS ####
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51384 (master PR not yet created)
Patch19:        include-aliases-in-the-fqdns-grains.patch
###########

#### BATCH ASYNC - unified #####
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/60269
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50546
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51863
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/139
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/141
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/144
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52855
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/6af07030a502c427781991fc9a2b994fa04ef32e
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/002543df392f65d95dbc127dc058ac897f2035ed
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/commit/55d8a777d6a9b19c959e14a4060e5579e92cd106
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/commit/8378bb24a5a53973e8dba7658b8b3465d967329f
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/pull/182
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/pull/190
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/pull/217
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/commit/8a23030d347b7487328c0395f5e30ef29daf1455
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/commit/a38adfa2efe40c2b1508b685af0b5d28a6bbcfc8
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/commit/b4c401cfe6031b61e27f7795bfa1aca6e8341e52
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/320
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/commit/25b4e3ea983b2606b2fb3d3c0e42f9840208bf84 (cleanup local code)
Patch20:        async-batch-implementation.patch
###########

# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52743
Patch21:        switch-firewalld-state-to-use-change_interface.patch

### STANDALONE FORMULA CONFIGURATION ###
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/8ad65d6fa39edc7fc1967e2df1f3db0aa7df4d11
Patch22:        add-standalone-configuration-file-for-enabling-packa.patch
#############

# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/177
# (deviation from upstream - we should probably port this)
Patch23:        restore-default-behaviour-of-pkg-list-return.patch
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/pull/186 (missing upstream PR to master)
Patch24:        read-repo-info-without-using-interpolation-bsc-11356.patch
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/pull/191 (missing upstream PR to master)
Patch25:        let-salt-ssh-use-platform-python-binary-in-rhel8-191.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/a18ac47b75550bd55f4ca91dc221ed408881984c
Patch26:        make-setup.py-script-to-not-require-setuptools-9.1.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/228 (missing upstream PR)
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/da936daeebd701e147707ad814c07bfc259d4be (not yet upstream PR)
Patch27:        add-publish_batch-to-clearfuncs-exposed-methods.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/57779
Patch28:        info_installed-works-without-status-attr-now.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/58552
Patch29:        zypperpkg-ignore-retcode-104-for-search-bsc-1176697-.patch

# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/275 (missing upstream PR)
Patch30:        bsc-1176024-fix-file-directory-user-and-group-owners.patch

#### NO VENDOR CHANGE ####
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/60421
Patch31:        allow-vendor-change-option-with-zypper.patch
###########

# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/58784
Patch32:        add-migrated-state-and-gpg-key-management-functions-.patch

### BEACON CONFIG ###
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/5ea2f10b15684dd417bad858642faafc92cd382
# (revert https://github.com/saltstack/salt/pull/58655)
Patch33:        revert-fixing-a-use-case-when-multiple-inotify-beaco.patch
###########

# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/298 (missing upstream PR)
Patch34:        fix-salt.utils.stringutils.to_str-calls-to-make-it-w.patch

# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/307 (missing upstream PR)
Patch35:        add-sleep-on-exception-handling-on-minion-connection.patch

### SALT-SSH PROCESSING TARGETS ###
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/336 (missing upstream PR)
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/353 (missing upstream PR)
Patch36:        update-target-fix-for-salt-ssh-to-process-targets-li.patch
############

# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/58503
Patch37:        fix-missing-minion-returns-in-batch-mode-360.patch

#### OPENSCAP ENHANCE ####
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/59756
Patch38:        enhance-openscap-module-add-xccdf_eval-call-386.patch
###############

# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/413 (missing upstream PR)
Patch39:        don-t-use-shell-sbin-nologin-in-requisites.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/432 (missing upstream PR)
Patch40:        fix-traceback.print_exc-calls-for-test_pip_state-432.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/415 (missing upstream PR)
Patch41:        prevent-pkg-plugins-errors-on-missing-cookie-path-bs.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61180
Patch42:        dnfnotify-pkgset-plugin-implementation-3002.2-450.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/456 (missing upstream PR)
Patch43:        fix-the-regression-for-yumnotify-plugin-456.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/482
Patch44:        drop-serial-from-event.unpack-in-cli.batch_async.patch

### SALT-SSH WITH SALT BUNDLE ###
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61715 (ssh_pre_flight_args)
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/493
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/497
Patch45:        add-salt-ssh-support-with-venv-salt-minion-3004-493.patch
Patch46:        prevent-shell-injection-via-pre_flight_script_args-4.patch
###############

# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/501
Patch47:        fix-salt-ssh-opts-poisoning-bsc-1197637-3004-501.patch

# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/505
Patch48:        prevent-affection-of-ssh.opts-with-lazyloader-bsc-11.patch

# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/506
Patch49:        fix-regression-with-depending-client.ssh-on-psutil-b.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62109
Patch50:        use-salt-bundle-in-dockermod.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61984
Patch51:        save-log-to-logfile-with-docker.build.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/534
Patch52:        fix-ownership-of-salt-thin-directory-when-using-the-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62209
Patch53:        add-support-for-gpgautoimport-539.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62519
Patch54:        change-the-delimeters-to-prevent-possible-tracebacks.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62898
Patch55:        pass-the-context-to-pillar-ext-modules.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/c6be36eeea49ee0d0641da272087305f79c32c99 (not yet upstream)
# Fix problem caused by: https://github.com/openSUSE/salt/pull/493 (Patch47) affecting only 3005.1.
Patch56:        use-rlock-to-avoid-deadlocks-in-salt-ssh.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61064
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/5e3ff4d662321c237ddd5b2c5c83f35a84af594c (not PR to master yet)
Patch57:        fixes-for-python-3.10-502.patch
# PATCH-FIX-OPENSUSE: https://github.com/openSUSE/salt/pull/571
Patch58:        control-the-collection-of-lvm-grains-via-config.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/63460
Patch59:        3005.1-implement-zypper-removeptf-573.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/63460
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/578
Patch60:        skip-package-names-without-colon-bsc-1208691-578.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/c0fae09e5a4f6997a60007d970c7c6a5614d9102
Patch61:        fix-version-detection-and-avoid-building-and-testing.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64113
Patch62:        make-sure-the-file-client-is-destroyed-upon-used.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/581
Patch63:        avoid-conflicts-with-dependencies-versions-bsc-12116.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64369
Patch64:        define-__virtualname__-for-transactional_update-modu.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/587
Patch65:        make-master_tops-compatible-with-salt-3000-and-older.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/583
Patch66:        tornado-fix-an-open-redirect-in-staticfilehandler-cv.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/580
Patch67:        fix-some-issues-detected-in-salt-support-cli-module-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64510
Patch68:        3006.0-prevent-_pygit2.giterror-error-loading-known_.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64300
Patch69:        fix-utf8-handling-in-pass-renderer-and-make-it-more-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/63403
Patch70:        zypper-pkgrepo-alreadyconfigured-585.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64530
Patch71:        fix-the-regression-of-user.present-state-when-group-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64179
Patch72:        fix-regression-multiple-values-for-keyword-argument-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64554
Patch73:        mark-salt-3006-as-released-586.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64599
Patch74:        prevent-possible-exceptions-on-salt.utils.user.get_g.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/592
Patch75:        fix-tests-to-make-them-running-with-salt-testsuite.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/f82860b8ad3ee786762fa02fa1a6eaf6e24dc8d4
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/65020
Patch76:        do-not-fail-on-bad-message-pack-message-bsc-1213441-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64510 (dropped at patch 91)
Patch77:        make-sure-configured-user-is-properly-set-by-salt-bs.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64959
Patch78:        fixed-gitfs-cachedir_basename-to-avoid-hash-collisio.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/600
Patch79:        revert-usage-of-long-running-req-channel-bsc-1213960.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/65238
Patch80:        write-salt-version-before-building-when-using-with-s.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/65036
Patch81:        fix-calculation-of-sls-context-vars-when-trailing-do.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/594
Patch82:        implement-the-calling-for-batch-async-from-the-salt-.patch
# PATCH-FIX_UPSTREAM: https://github.com/tornadoweb/tornado/pull/2277
Patch83:        only-call-native_str-on-curl_debug-message-in-tornad.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/65204
Patch84:        use-salt-call-from-salt-bundle-with-transactional_up.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/65181
Patch85:        improve-salt.utils.json.find_json-bsc-1213293.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/65266
Patch86:        fix-optimization_order-opt-to-prevent-test-fails.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65232
Patch87:        allow-all-primitive-grain-types-for-autosign_grains-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65482
Patch88:        fix-cve-2023-34049-bsc-1215157.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65017
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65136
Patch89:        fix-gitfs-__env__-and-improve-cache-cleaning-bsc-119.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65435
Patch90:        dereference-symlinks-to-set-proper-__cli-opt-bsc-121.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/614 (revert patch 77)
Patch91:        revert-make-sure-configured-user-is-properly-set-by-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65488
Patch92:        enable-keepalive-probes-for-salt-ssh-executions-bsc-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65644
Patch93:        prefer-unittest.mock-for-python-versions-that-are-su.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/620
Patch94:        fix-the-aptpkg.py-unit-test-failure.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65092
Patch95:        update-__pillar__-during-pillar_refresh.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65969
Patch96:        fix-cve-2024-22231-and-cve-2024-22232-bsc-1219430-bs.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65009
Patch97:        fixed-keyerror-in-logs-when-running-a-state-that-fai.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65562
Patch98:        improve-pip-target-override-condition-with-venv_pip_.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65819
Patch99:        allow-kwargs-for-fileserver-roots-update-bsc-1218482.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66048
Patch100:       discover-both-.yml-and-.yaml-playbooks-bsc-1211888.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66130
Patch101:       fix-problematic-tests-and-allow-smooth-tests-executi.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/628
Patch102:       make-importing-seco.range-thread-safe-bsc-1211649.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66130
Patch103:       fix-tests-failures-and-errors-when-detected-on-vm-ex.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66234 (modified at Patch106)
Patch104:       decode-oscap-byte-stream-to-string-bsc-1219001.patch
### Commits to make Salt compatible with Python 3.11 (and 3.6)
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/d92b5423464f93da6e3feb47d05a9acef8da75f9
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/60b36489225f958772b6a2f99d8fe6ae33ee9d73
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/eee0eca5e48922e5e404f812ced08ca7484bb568
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/991f7cf0a7baf08a31194ce52f4ec08290db8e52
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/2688c86f45eea9f8a6b916fcdf8eb94b3f5e185b
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/a1873a1d6d50d1769ddef528d7442e38aba9de23
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/commit/c7ecccb0a080ca9cca097f760ef0992ab34f82df
Patch105:       fix-salt-warnings-and-testuite-for-python-3.11-635.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/639
Patch106:       switch-oscap-encoding-to-utf-8-639.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65982
Patch107:       remove-unused-import-causing-delays-on-starting-salt.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66024
Patch108:       make-logging-calls-lighter.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66034
Patch109:       improve-broken-events-catching-and-reporting.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/633
Patch110:       make-salt-master-self-recoverable-on-killing-eventpu.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66158
Patch111:       make-reactor-engine-less-blocking-the-eventpublisher.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/638
Patch112:       prevent-possible-exception-in-tornado.concurrent.fut.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66455
Patch113:       remove-redundant-_file_find-call-to-the-master.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/646
Patch114:       skip-tests-for-unsupported-algorithm-on-old-openssl-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/652
Patch115:       add-missing-contextvars-dependency-in-salt.version.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/640
Patch116:       prevent-oom-with-high-amount-of-batch-async-calls-bs.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65983
Patch117:       do-not-call-the-async-wrapper-calls-with-the-separat.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66494
Patch118:       speed-up-salt.matcher.confirm_top-by-using-__context.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66593
Patch119:       several-fixes-for-tests-to-avoid-errors-and-failures.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/656
Patch120:       provide-systemd-timer-unit.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66630
Patch121:       skip-certain-tests-if-necessary-and-mark-some-flaky-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66647
Patch122:       fix-status.diskusage-and-exclude-some-tests-to-run-w.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/65077
Patch123:       fix-user.list_groups-omits-remote-groups.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66695
Patch124:       some-more-small-tests-fixes-enhancements-661.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/666
Patch125:       test_vultrpy-adjust-test-expectation-to-prevent-fail.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/66698
Patch126:       firewalld-normalize-new-rich-rules-before-comparing-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/669
Patch127:       skip-more-tests-related-to-old-openssl-algorithms.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/662
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66730
Patch128:       make-tests-compatible-with-venv-bundle.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66743
Patch129:       replace-use-of-pygit2-deprecated-and-removed-1.15.0-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/671
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/64173
Patch130:       join-masters-if-it-is-a-list-671.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66509
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/0c3ebc0795f9c2adec90118281343cae3070e0f6
Patch131:       remove-redundant-run_func-from-salt.master.mworker._.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66818
Patch132:       improve-error-handling-with-different-openssl-versio.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66856
Patch133:       avoid-crash-on-wrong-output-of-systemctl-version-bsc.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66861
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/675
Patch134:       fix-test_system-flaky-setup_teardown-fn.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/676
Patch135:       fix-test_debian-to-work-in-our-infrastructure-676.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/677
Patch136:       fix-deprecated-code-677.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66780
Patch137:       fix-the-selinux-context-for-salt-minion-service-bsc-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66510
Patch138:       prevent-using-syncwrapper-with-no-reason.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66742
Patch139:       use-cachedir-for-extension_modules-in-salt-call-bsc-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/680
Patch140:       revert-the-change-making-reactor-less-blocking-bsc-1.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66649
Patch141:       allow-namedloadercontexts-to-be-returned-from-loader.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/d54407ba6dc664e5e5f3f613e27ae24f828c9648
Patch142:       avoid-explicit-reading-of-etc-salt-minion-bsc-122035.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/682
Patch143:       fix-x509-test-fails-on-old-openssl-systems-682.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/684
Patch144:       fix-x509-private-key-tests-and-test_suse-on-sle12-68.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/685
Patch145:       enhance-cleanup-mechanism-after-salt-bundle-upgrade-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/9683260d61668da8559ecde6caf63a52fedd8790
Patch146:       handle-logger-flushing-already-closed-file-686.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66422
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66757
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66760
Patch147:       make-minion-reconnecting-on-changing-master-ip-bsc-1.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/690
Patch148:       revert-setting-selinux-context-for-minion-service-bs.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66899
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/698
Patch149:       fix-issues-that-break-salt-in-python-3.12-and-3.13-6.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67181
Patch150:       fix-virtual-grains-for-vms-running-on-nutanix-ahv-bs.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67023
Patch151:       enhance-find_json-garbage-filtering-bsc-1231605-688.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67105
Patch152:       update-for-deprecation-of-hex-in-pygit2-1.15.0-and-a.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67186
Patch153:       fix-failed-to-stat-root-.gitconfig-issue-on-gitfs-bs.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/58f448405b7f46505b2047ecda72abb42b6df9d1
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/79d4ff772a162b5b8e602e3437c13b90a25bc190
Patch154:       fix-tests-failures-after-repo.saltproject.io-depreca.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60269
Patch155:       backport-batch-async-fixes-and-improvements-701.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/560ab52ccf94c7974d5a418dfbba7409e0493066
Patch156:       fixed-file-client-private-attribute-reference-on-sal.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67734
Patch157:       set-virtual-grain-in-podman-systemd-container-703.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67066
Patch158:       repair-fstab_present-test-mode-702.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67746
Patch159:       make-_auth-calls-visible-with-master-stats-696.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/65843
Patch160:       repair-virt_query-outputter-655.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67754
Patch161:       remove-password-from-shell-after-functional-text-mat.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/692
Patch162:       add-deb822-apt-source-format-support-692.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/678
Patch163:       remove-deprecated-code-from-x509.certificate_managed.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67782
Patch164:       make-x509-module-compatible-with-m2crypto-0.44.0.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67776
Patch165:       implement-multiple-inventory-for-ansible.targets.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67797
Patch166:       ensure-the-correct-crypt-module-is-loaded.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67796
Patch167:       detect-openeuler-as-redhat-family-os.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/710
Patch168:       fix-deb822-nonetype-object-has-no-attribute-split-71.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/67933
Patch169:       fix-refresh-of-osrelease-and-related-grains-on-pytho.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/86245dc12c0705b5579a15dcb70724244e574d73
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/715
Patch170:       fix-debian-tests-715.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/790304df995ad2415bf550cc8489230360da1bd7
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/716
Patch171:       fix-ubuntu-24.04-specific-failures-716.patch
# PATCH-FIX_UPSTREAM: https://github.com/tornadoweb/tornado/commit/b39b892bf78fe8fea01dd45199aa88307e7162f3
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/718
Patch172:       fix-of-cve-2025-47287-bsc-1243268-718.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68047
Patch173:       add-subsystem-filter-to-udev.exportdb-bsc-1236621-71.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/compare/v3006.11..v3006.12
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68083
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68084
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68085
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68089
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/0519a4cc6b6aac58e5358037ae61436e30b07c17
Patch174:       several-fixes-for-security-issues.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68125
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/721
Patch175:       fix-tests-issues-in-salt-shaker-environments-721.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/722
Patch176:       add-minion_legacy_req_warnings-option-to-avoid-noisy.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68246
Patch177:       fix-the-tests-failing-on-almalinux-10-and-other-clon.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/66630
Patch178:       fix-functional.states.test_user-for-sles-16-and-micr.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68247
Patch179:       improve-sl-micro-6.2-detection-with-grains.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/728
Patch180:       modify-readme-for-opensuse-728.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68331
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/729
Patch181:       even-more-reliable-pillar-timeout-test.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/730
Patch182:       add-python3.11-as-preferable-for-salt-ssh-to-avoid-t.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/68366
Patch183:       allow-libgit2-to-guess-sysdir-homedir-successfully-b.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/732
Patch184:       use-versioned-python-interpreter-for-salt-ssh.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/735
Patch185:       do-not-break-signature-verification-on-latest-m2cryp.patch

### IMPORTANT: The line below is used as a snippet marker. Do not touch it.
### SALT PATCHES LIST END

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  logrotate
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

%if 0%{?_alternatives}
Requires:       %{name}-call = %{version}-%{release}
%else
Requires:       python3-%{name} = %{version}-%{release}
%endif
Obsoletes:      python2-%{name}

# The "salt" package obsoletes "python3-salt" in SLE15SP7+
%if 0%{?sle_version} >= 150700
Obsoletes:      python3-%{name}
%endif

Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Provides:       user(salt)
Provides:       group(salt)

%if 0%{?suse_version}
Requires(pre):  shadow
%endif

%if 0%{?suse_version}
Requires(pre):  dbus-1
%else
Requires(pre):  dbus
%endif

Requires:       logrotate
Requires:       procps

%if 0%{?suse_version} >= 1500
Requires:       iproute2
%else
%if 0%{?suse_version}
Requires:       net-tools
%else
Requires:       iproute
%endif
%endif

%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%endif

%if %{with fish_completion}
%define fish_dir %{_datadir}/fish/
%define fish_completions_dir %{_datadir}/fish/completions/
%endif

%if %{with bash_completion}
%if 0%{?suse_version} >= 1140
BuildRequires:  bash-completion
%else
BuildRequires:  bash
%endif
%endif

%if %{with zsh_completion}
BuildRequires:  zsh
%endif

%define python_subpackage_only 1
%python_subpackages

%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in
the world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds or even thousands of individual
servers, handle them quickly and through a simple and manageable interface.

%if "%{flavor}" != "testsuite"

%if 0%{?singlespec_compat}
%package -n python3-salt
%else
%package -n python-salt
%endif
Summary:        python3 library for salt
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
BuildRequires:  python-rpm-macros
%if 0%{?rhel} == 8
BuildRequires:  platform-python
%else
BuildRequires:  %{python_module base}
%endif
BuildRequires:  %{python_module setuptools}
# requirements/base.txt
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  python3-jinja2
BuildRequires:  python3-m2crypto
BuildRequires:  python3-markupsafe
BuildRequires:  python3-msgpack > 0.3
BuildRequires:  python3-zmq >= 2.2.0
%else
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  %{python_module msgpack-python > 0.3}
BuildRequires:  %{python_module pyzmq > 2.2.0}
%if 0%{?suse_version} >= 1500
BuildRequires:  %{python_module M2Crypto}
%else
BuildRequires:  %{python_module pycrypto >= 2.6.1}
%endif
%endif
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module requests >= 1.0.0}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module looseversion}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module contextvars}

# requirements/zeromq.txt
%if %{with test}
BuildRequires:  %{python_module boto >= 2.32.1}
BuildRequires:  %{python_module mock if %python-base < 3.8}
BuildRequires:  %{python_module moto >= 0.3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module salt-testing >= 2015.2.16}
BuildRequires:  %{python_module unittest2}
BuildRequires:  %{python_module xml}
%endif
%if %{with builddocs}
BuildRequires:  %{python_module sphinx}
%endif
%if 0%{?rhel} == 8
Requires:       platform-python
%else
%if 0%{?singlespec_compat}
Requires:       %{python_module base}
%else
Requires:       python-base
%endif
%endif

%if 0%{?_alternatives}
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
%endif

# requirements/base.txt
%if 0%{?rhel} || 0%{?fedora}
Requires:       python3-jinja2
Requires:       python3-m2crypto
Requires:       python3-markupsafe
Requires:       python3-msgpack > 0.3
Requires:       python3-zmq >= 2.2.0

%if 0%{?rhel} >= 8 || 0%{?fedora} >= 30
Requires:       dnf
Requires:       python3-dnf-plugins-core
%endif
%else # SUSE
%if 0%{?singlespec_compat}
Requires:       %{python_module Jinja2}
Requires:       %{python_module MarkupSafe}
Requires:       %{python_module msgpack-python > 0.3}
%if 0%{?suse_version} >= 1500
Requires:       %{python_module M2Crypto}
%else
Requires:       %{python_module pycrypto >= 2.6.1}
%endif
Requires:       %{python_module pyzmq >= 2.2.0}
%else
Requires:       python-Jinja2
Requires:       python-MarkupSafe
Requires:       python-msgpack-python > 0.3
%if 0%{?suse_version} >= 1500
Requires:       python-M2Crypto
%else
Requires:       python-pycrypto >= 2.6.1
%endif
Requires:       python-pyzmq >= 2.2.0
%endif
%endif # end of RHEL / SUSE specific section
%if 0%{?singlespec_compat}
Recommends:     %{python_module jmespath}
Requires:       %{python_module PyYAML}
Requires:       %{python_module psutil}
Requires:       %{python_module requests >= 1.0.0}
Requires:       %{python_module distro}
Requires:       %{python_module looseversion}
Requires:       %{python_module packaging}
Requires:       %{python_module contextvars}
%if 0%{?suse_version}
# required for zypper.py
Requires:       %{python_module rpm}
# requirements/opt.txt (not all)
# Suggests:     python-MySQL-python  ## Disabled for now, originally Recommended
Suggests:       %{python_module timelib}
Suggests:       %{python_module gnupg}
%endif
%else
Recommends:     python-jmespath
Requires:       python-PyYAML
Requires:       python-psutil
Requires:       python-requests >= 1.0.0
Requires:       python-distro
Requires:       python-looseversion
Requires:       python-packaging
Requires:       python-contextvars
%if 0%{?suse_version}
# required for zypper.py
Requires:       python-rpm
# requirements/opt.txt (not all)
# Suggests:     python-MySQL-python  ## Disabled for now, originally Recommended
Suggests:       python-timelib
Suggests:       python-gnupg
# requirements/zeromq.txt
%endif
%endif
#
%if 0%{?suse_version}
# python-xml is part of python-base in all rhel versions
%if 0%{?singlespec_compat}
Requires:       %{python_module xml}
Requires:       %{python_module zypp-plugin}
Suggests:       %{python_module Mako}
Recommends:     %{python_module netaddr}
Recommends:     %{python_module pyinotify}
%else
Requires:       python-xml
Requires:       python-zypp-plugin
Suggests:       python-Mako
Recommends:     python-netaddr
Recommends:     python-pyinotify
%endif
Requires(pre):  libzypp(plugin:system) >= 0
%endif

# Required by Salt modules
Requires:       iputils
Requires:       sudo
Requires:       file
Recommends:     man
%if 0%{?singlespec_compat}
Recommends:     %{python_module passlib}
%else
Recommends:     python-passlib
%endif

%if 0%{?singlespec_compat}
Provides:       bundled(%{python_module tornado}) = 4.5.3
%else
Provides:       bundled(python-tornado) = 4.5.3
%endif

Provides:       %{name}-call = %{version}-%{release}

%if 0%{?singlespec_compat}
%description -n python3-salt
%else
%description -n python-salt
%endif
Python3 specific files for salt

%package api
Summary:        The api for Salt a parallel remote execution system
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if 0%{?suse_version}
%if 0%{?sle_version} >= 150400
Requires:       %{python_module CherryPy >= 3.2.2 if %python-salt}
%else
Requires:       python3-CherryPy >= 3.2.2
%endif
%else
Requires:       python3-cherrypy >= 3.2.2
%endif

%description api
salt-api is a modular interface on top of Salt that can provide a variety of entry points into a running Salt system.

%package cloud
Summary:        Generic cloud provisioning tool for Saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if 0%{?suse_version}
%if 0%{?sle_version} >= 150400
Requires:       %{python_module apache-libcloud if %python-salt}
Recommends:     %{python_module botocore if %python-salt}
Recommends:     %{python_module netaddr if %python-salt}
%else
Requires:       python3-apache-libcloud
Recommends:     python3-botocore
Recommends:     python3-netaddr
%endif
%else
Requires:       python3-apache-libcloud
%endif

%description cloud
public cloud VM management system
provision virtual machines on various public clouds via a cleanly
controlled profile and mapping system.

%if %{with docs}
%package doc
Summary:        Documentation for salt, a parallel remote execution system
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
This contains the documentation of salt, it is an offline version of http://docs.saltstack.com.
%endif

%package master
Summary:        The management component of Saltstack with zmq protocol supported
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
%if 0%{?suse_version}
%if 0%{?sle_version} >= 150400
Recommends:     %{python_module pygit2 >= 0.20.3 if %python-salt}
%else
Recommends:     python3-pygit2 >= 0.20.3
%endif
%endif
%ifarch %{ix86} x86_64
%if 0%{?suse_version}
%if 0%{?suse_version} > 1110
Requires:       dmidecode
%else
Requires:       pmtools
%endif
%endif
%endif
%if %{with systemd}
%{?systemd_requires}
BuildRequires:  systemd
%endif

%description master
The Salt master is the central server to which all minions connect.
Enabled commands to remote systems to be called in parallel rather
than serially.

%package minion
Summary:        The client component for Saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
Requires:       (%{name}-transactional-update = %{version}-%{release} if read-only-root-fs)
%endif

%if %{with systemd}
%{?systemd_requires}
%endif

%description minion
Salt minion is queried and controlled from the master.
Listens to the salt master and execute the commands.

%package proxy
Summary:        Component for salt that enables controlling arbitrary devices
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
%if %{with systemd}
%{?systemd_requires}
%endif

%description proxy
Proxy minions are a developing Salt feature that enables controlling devices that,
for whatever reason, cannot run a standard salt-minion.
Examples include network gear that has an API but runs a proprietary OS,
devices with limited CPU or memory, or devices that could run a minion, but for
security reasons, will not.

%package syndic
Summary:        The syndic component for saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if %{with systemd}
%{?systemd_requires}
%endif

%description syndic
Salt syndic is the master-of-masters for salt
The master of masters for salt-- it enables
the management of multiple masters at a time..

%package ssh
Summary:        Management component for Saltstack with ssh protocol
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if 0%{?suse_version}
Recommends:     sshpass
%endif
%if %{with systemd}
%{?systemd_requires}
%endif

%description ssh
Salt ssh is a master running without zmq.
it enables the management of minions over a ssh connection.

%if %{with bash_completion}
%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description bash-completion
Bash command line completion support for %{name}.

%endif

%if %{with fish_completion}
%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}

%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description fish-completion
Fish command line completion support for %{name}.
%endif

%if %{with zsh_completion}
%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description zsh-completion
Zsh command line completion support for %{name}.

%endif

%package standalone-formulas-configuration
Summary:        Standalone Salt configuration to make the packaged formulas available for the Salt master
Group:          System/Management
Requires:       %{name}
Provides:       salt-formulas-configuration
Conflicts:      otherproviders(salt-formulas-configuration)

%description standalone-formulas-configuration
This package adds the standalone configuration for the Salt master in order to make the packaged Salt formulas available on the Salt master

%package transactional-update
Summary:        Transactional update executor configuration
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-minion = %{version}-%{release}
Requires:       tar

%description transactional-update
For transactional systems, like MicroOS, Salt can operate
transparently if the executor "transactional-update" is registered in
list of active executors.  This package add the configuration file.

%endif

%if "%{flavor}" == "testsuite"

%if 0%{?singlespec_compat}
%package -n python3-salt-testsuite
%else
%package -n python-salt-testsuite
%endif
Summary:        Unit and integration tests for Salt

%if 0%{?rhel} == 8
BuildRequires:  platform-python
%else
BuildRequires:  %{python_module base}
%endif
BuildRequires:  %{python_module setuptools}

Requires:       salt = %{version}
%if 0%{?singlespec_compat}
Requires:       %{python_module CherryPy}
Requires:       %{python_module Genshi}
Requires:       %{python_module Mako}
%if !0%{?suse_version} > 1600 || 0%{?centos}
Requires:       %{python_module boto}
%endif
Requires:       %{python_module boto3}
Requires:       %{python_module docker}
%if 0%{?suse_version} < 1600
Requires:       %{python_module mock}
%endif
Requires:       %{python_module pygit2}
Requires:       %{python_module pytest >= 7.0.1}
Requires:       %{python_module pytest-httpserver}
Requires:       %{python_module pytest-salt-factories >= 1.0.0~rc21}
Requires:       %{python_module pytest-subtests}
Requires:       %{python_module testinfra}
Requires:       %{python_module yamllint}
Requires:       %{python_module pip}
%else
Requires:       python-CherryPy
Requires:       python-Genshi
Requires:       python-Mako
%if !0%{?suse_version} > 1600 || 0%{?centos}
Requires:       python-boto
%endif
Requires:       python-boto3
Requires:       python-docker
%if 0%{?suse_version} < 1600
Requires:       python-mock
%endif
Requires:       python-pygit2
Requires:       python-pytest >= 7.0.1
Requires:       python-pytest-httpserver
Requires:       python-pytest-salt-factories >= 1.0.0~rc21
Requires:       python-pytest-subtests
Requires:       python-testinfra
Requires:       python-yamllint
Requires:       python-pip
%endif
Requires:       docker
Requires:       openssh
Requires:       git

Obsoletes:      %{name}-tests

%if 0%{?singlespec_compat}
%description -n python3-salt-testsuite
%else
%description -n python-salt-testsuite
%endif
Collection of unit, functional, and integration tests for %{name}.

%endif

%prep
%setup -q -n salt-%{version}-suse
cp %{S:1} .
cp %{S:5} ./.travis.yml
cp %{S:6} .
%autopatch -p1

%build
%if "%{flavor}" != "testsuite"

# Putting /usr/bin at the front of $PATH is needed for RHEL/RES 7. Without this
# change, the RPM will require /bin/python, which is not provided by any package
# on RHEL/RES 7.
%if 0%{?fedora} || 0%{?rhel}
export PATH=/usr/bin:$PATH
%endif
%{python_expand #
$python setup.py --with-salt-version=%{version} --salt-transport=both build
mv build _build.%{$python_bin_suffix}
}

%if %{with docs} && %{without builddocs}
# extract docs from the tarball
mkdir -p doc/_build
pushd doc/_build/
tar xfv %{S:3}
popd
%endif

%if %{with docs} && %{with builddocs}
## documentation
cd doc && make html && rm _build/html/.buildinfo && rm _build/html/_images/proxy_minions.png && cd _build/html && chmod -R -x+X *
%endif

%endif

%install
%if "%{flavor}" != "testsuite"

%{python_expand #
mv _build.%{$python_bin_suffix} build
$python setup.py --salt-transport=both install --prefix=%{_prefix} --root=%{buildroot}
mv build _build.%{$python_bin_suffix}

DEF_PYPATH=_build.%{$python_bin_suffix}/scripts-*/

rm -f %{buildroot}%{_bindir}/*
for script in $DEF_PYPATH/*; do
  install -m 0755 $script %{buildroot}%{_bindir}
done
}

## create missing directories
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/cloud
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/jobs
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/proc
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/queues
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/roots
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/syndics
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/tokens
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/minion/extmod
install -Dd -m 0750 %{buildroot}%{_localstatedir}/log/salt
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.maps.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.profiles.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.providers.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/master.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/minion.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_autosign
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_denied
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_pre
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_rejected
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/minion
install -Dd -m 0750 %{buildroot}/srv/pillar
install -Dd -m 0750 %{buildroot}/srv/salt
install -Dd -m 0750 %{buildroot}/srv/spm
install -Dd -m 0750 %{buildroot}/var/lib/salt
install -Dd -m 0755 %{buildroot}%{_docdir}/salt
install -Dd -m 0755 %{buildroot}%{_sbindir}
%if 0%{?suse_version} > 1500
install -Dd -m 0755 %{buildroot}%{_distconfdir}/logrotate.d
%else
install -Dd -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
%endif

# Install salt-support profiles
%{python_expand #
install -Dpm 0644 salt/cli/support/profiles/* %{buildroot}%{$python_sitelib}/salt/cli/support/profiles
}

%endif

%if "%{flavor}" == "testsuite"
# Install Salt tests
%{python_expand #
install -Dd %{buildroot}%{$python_sitelib}/salt-testsuite
cp -a tests %{buildroot}%{$python_sitelib}/salt-testsuite/
# Remove runtests.py which is not used as deprecated method of running the tests
rm %{buildroot}%{$python_sitelib}/salt-testsuite/tests/runtests.py
# Copy conf files to the testsuite as they are used by the tests
cp -a conf %{buildroot}%{$python_sitelib}/salt-testsuite/
}
%endif

%if "%{flavor}" != "testsuite"

## Install Zypper plugins only on SUSE machines
%if 0%{?suse_version}
install -Dd -m 0750 %{buildroot}%{_prefix}/lib/zypp/plugins/commit
%{__install} scripts/suse/zypper/plugins/commit/zyppnotify %{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif

# Install DNF plugin only on RH machines
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 8
install -Dd %{buildroot}%{python3_sitelib}/dnf-plugins
install -Dd %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__
install -Dd %{buildroot}%{_sysconfdir}/dnf/plugins
%{__install} scripts/suse/dnf/plugins/dnfnotify.py %{buildroot}%{python3_sitelib}/dnf-plugins
%{__install} scripts/suse/dnf/plugins/dnfnotify.conf %{buildroot}%{_sysconfdir}/dnf/plugins
%{__python3} -m compileall -d %{python3_sitelib}/dnf-plugins %{buildroot}%{python3_sitelib}/dnf-plugins/dnfnotify.py
%{__python3} -O -m compileall -d %{python3_sitelib}/dnf-plugins %{buildroot}%{python3_sitelib}/dnf-plugins/dnfnotify.py
%endif

## install init and systemd scripts
%if %{with systemd}
install -Dpm 0644 pkg/old/suse/salt-master.service %{buildroot}%{_unitdir}/salt-master.service
%if 0%{?suse_version}
install -Dpm 0644 pkg/old/suse/salt-minion.service %{buildroot}%{_unitdir}/salt-minion.service
%else
install -Dpm 0644 pkg/old/suse/salt-minion.service.rhel7 %{buildroot}%{_unitdir}/salt-minion.service
%endif
install -Dpm 0644 pkg/common/salt-syndic.service %{buildroot}%{_unitdir}/salt-syndic.service
install -Dpm 0644 pkg/old/suse/salt-api.service    %{buildroot}%{_unitdir}/salt-api.service
install -Dpm 0644 pkg/common/salt-proxy@.service %{buildroot}%{_unitdir}/salt-proxy@.service
ln -s service %{buildroot}%{_sbindir}/rcsalt-master
ln -s service %{buildroot}%{_sbindir}/rcsalt-syndic
ln -s service %{buildroot}%{_sbindir}/rcsalt-minion
ln -s service %{buildroot}%{_sbindir}/rcsalt-api
install -Dpm 644 %{S:2}                   %{buildroot}/usr/lib/tmpfiles.d/salt.conf
%endif

#
## install config files
install -Dpm 0640 conf/minion %{buildroot}%{_sysconfdir}/salt/minion
touch  -m 0640 -r conf/minion %{buildroot}%{_sysconfdir}/salt/minion_id # ghost file
install -Dpm 0640 conf/master %{buildroot}%{_sysconfdir}/salt/master
install -Dpm 0640 conf/roster %{buildroot}%{_sysconfdir}/salt/roster
install -Dpm 0640 conf/cloud %{buildroot}%{_sysconfdir}/salt/cloud
install -Dpm 0640 conf/cloud.profiles %{buildroot}%{_sysconfdir}/salt/cloud.profiles
install -Dpm 0640 conf/cloud.providers %{buildroot}%{_sysconfdir}/salt/cloud.providers
install -Dpm 0640 transactional_update.conf %{buildroot}%{_sysconfdir}/salt/minion.d/transactional_update.conf
#
%if 0%{?suse_version} > 1500
install -Dpm 0644  pkg/old/suse/salt-common.logrotate %{buildroot}%{_distconfdir}/logrotate.d/salt
%else
install -Dpm 0644  pkg/old/suse/salt-common.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/salt
%endif
#
%if 0%{?suse_version} <= 1500
## install SuSEfirewall2 rules
install -Dpm 0644  pkg/old/suse/salt.SuSEfirewall2 %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/salt
%endif
#
## install completion scripts
%if %{with bash_completion}
install -Dpm 0644 pkg/common/salt.bash %{buildroot}%{_sysconfdir}/bash_completion.d/salt
%endif
%if %{with zsh_completion}
install -Dpm 0644 pkg/common/salt.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/salt
%endif

%if %{with fish_completion}
mkdir -p %{buildroot}%{fish_completions_dir}
install -Dpm 0644 pkg/common/fish-completions/* %{buildroot}%{fish_completions_dir}
%endif

# Standalone Salt formulas configuration
install -Dd -m 0750 %{buildroot}%{_prefix}/share/salt-formulas
install -Dd -m 0750 %{buildroot}%{_prefix}/share/salt-formulas/states
install -Dd -m 0750 %{buildroot}%{_prefix}/share/salt-formulas/metadata
install -Dpm 0640 conf/suse/standalone-formulas-configuration.conf %{buildroot}%{_sysconfdir}/salt/master.d
install -Dpm 0640 conf/suse/standalone-formulas-configuration.conf %{buildroot}%{_sysconfdir}/salt/minion.d

%if 0%{?suse_version} > 1020
%fdupes %{buildroot}%{_docdir}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if 0%{?_alternatives}
%python_clone -a %{buildroot}%{_bindir}/salt-call
%python_clone -a %{buildroot}%{_bindir}/salt-support
%python_clone -a %{buildroot}%{_bindir}/spm
install -Dd -m 0750 %{buildroot}%{_exec_prefix}/libexec/salt
for SALT_SCRIPT in salt salt-api salt-cloud salt-cp salt-key salt-master salt-minion salt-proxy salt-run salt-ssh salt-syndic; do
    mv "%{buildroot}%{_bindir}/${SALT_SCRIPT}" "%{buildroot}%{_exec_prefix}/libexec/salt/"
%python_clone -a %{buildroot}%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}
    ln -s "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}" "%{buildroot}%{_bindir}/${SALT_SCRIPT}"
done
mv "%{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify" "%{buildroot}%{_exec_prefix}/libexec/salt/"
%python_clone -a %{buildroot}%{_exec_prefix}/libexec/salt/zyppnotify
ln -s "%{_exec_prefix}/libexec/salt/zyppnotify" "%{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify"
%endif

%endif

%check
%if %{with test}
%{python_expand #
$python setup.py test --runtests-opts=-u
}
%endif

%if "%{flavor}" != "testsuite"

%pre
S_HOME="/var/lib/salt"
S_PHOME="/srv/salt"
getent passwd salt | grep $S_PHOME >/dev/null && usermod -d $S_HOME salt
getent group salt >/dev/null || %{_sbindir}/groupadd -r salt
getent passwd salt >/dev/null || %{_sbindir}/useradd -r -g salt -d $S_HOME -s /bin/false -c "salt-master daemon" salt
if [[ -d "$S_PHOME/.ssh" ]]; then
    mv $S_PHOME/.ssh $S_HOME
fi
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
test -f %{_sysconfdir}/logrotate.d/salt.rpmsave && mv -v %{_sysconfdir}/logrotate.d/salt.rpmsave %{_sysconfdir}/logrotate.d/salt.rpmsave.old ||:
%endif

%post
%if %{with systemd}
systemd-tmpfiles --create /usr/lib/tmpfiles.d/salt.conf || true
%else
dbus-uuidgen --ensure
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
test -f %{_sysconfdir}/logrotate.d/salt.rpmsave && mv -v %{_sysconfdir}/logrotate.d/salt.rpmsave %{_sysconfdir}/logrotate.d/salt ||:
test -f %{_sysconfdir}/logrotate.d/salt.rpmsave.old && mv -v %{_sysconfdir}/logrotate.d/salt.rpmsave.old %{_sysconfdir}/logrotate.d/salt.rpmsave ||:
%endif

%preun proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-proxy@.service
%else
%systemd_preun salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-proxy
%endif
%endif

%pre proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-proxy@.service
%endif
%endif

%post proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-proxy@.service
%else
%systemd_post salt-proxy@.service
%endif
%endif

%postun proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-proxy@.service
%else
%systemd_postun_with_restart salt-proxy@.service
%endif
%endif

%preun syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-syndic.service
%else
%systemd_preun salt-syndic.service
%endif
%endif

%pre syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-syndic.service
%endif
%endif

%post syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-syndic.service
%else
%systemd_post salt-syndic.service
%endif
%endif

%postun syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-syndic.service
%else
%systemd_postun_with_restart salt-syndic.service
%endif
%endif

%preun master
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-master.service
%else
%systemd_preun salt-master.service
%endif
%endif

%pre master
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-master.service
%endif
%endif

%post master
if [ $1 -eq 2 ] ; then
  # Upgrading from an earlier version.  If this is from 2014, where daemons
  # ran as root, we need to chown some stuff to salt in order for the new
  # version to actually work.  It seems a manual restart of salt-master may
  # still be required, but at least this will actually work given the file
  # ownership is correct.
  # Symlinks are excluded to avoid possible user escalation (bsc#1157465) (CVE-2019-18897).
  for file in master.{pem,pub} ; do
    [ -f /etc/salt/pki/master/$file ] && [ ! -L /etc/salt/pki/master/$file ] && chown --no-dereference salt /etc/salt/pki/master/$file
  done
  MASTER_CACHE_DIR="/var/cache/salt/master"
  [ -d $MASTER_CACHE_DIR ] && find $MASTER_CACHE_DIR -type d | xargs -r chown --no-dereference salt:salt
  [ -d $MASTER_CACHE_DIR ] && find $MASTER_CACHE_DIR -type f | xargs -r chown --no-dereference salt:salt
  [ -f $MASTER_CACHE_DIR/.root_key ] && chown --no-dereference root:root $MASTER_CACHE_DIR/.root_key
  true
fi
%if %{with systemd}
systemd_ver=$(rpm -q systemd --queryformat="%%{VERSION}")
if [ "${systemd_ver%%.*}" -lt 228 ]; then
  # On systemd < 228 the 'TasksTask' attribute is not available.
  # Removing TasksMax from salt-master.service on SLE12SP1 LTSS (bsc#985112)
  sed -i '/TasksMax=infinity/d' %{_unitdir}/salt-master.service
fi
%if 0%{?suse_version}
%service_add_post salt-master.service
%else
%systemd_post salt-master.service
%endif
%endif

%postun master
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-master.service
%else
%systemd_postun_with_restart salt-master.service
%endif
%endif

%preun minion
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-minion.service
%else
%systemd_preun salt-minion.service
%endif
%endif

%pre minion
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-minion.service
%endif
%endif

%post minion
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-minion.service
%else
%systemd_post salt-minion.service
%endif
%endif

%postun minion
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-minion.service
%else
%systemd_postun_with_restart salt-minion.service
%endif
%endif

%preun api
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-api.service
%else
%systemd_preun salt-api.service
%endif
%else
%stop_on_removal
%endif

%pre api
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-api.service
%endif
%endif

%post api
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-api.service
%else
%systemd_post salt-api.service
%endif
%endif

%postun api
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-api.service
%else
%systemd_postun_with_restart salt-api.service
%endif
%endif

%if 0%{?_alternatives}
%pre -n python-salt
for SALT_SCRIPT in salt-call salt-support spm; do
    [ -h "%{_bindir}/${SALT_SCRIPT}" ] || rm -f "%{_bindir}/${SALT_SCRIPT}"
    if [ "$1" -gt 0 ] && [ -f /usr/sbin/update-alternatives ]; then
        update-alternatives --quiet --remove "${SALT_SCRIPT}" "%{_bindir}/${SALT_SCRIPT}-%{python_bin_suffix}"
    fi
done
for SALT_SCRIPT in salt salt-api salt-cloud salt-cp salt-key salt-master salt-minion salt-proxy salt-run salt-ssh salt-syndic zyppnotify; do
    [ -h "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}" ] || rm -f "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}"
    if [ "$1" -gt 0 ] && [ -f /usr/sbin/update-alternatives ]; then
        update-alternatives --quiet --remove "${SALT_SCRIPT}" "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}-%{python_bin_suffix}"
    fi
done

%if ! %{with libalternatives}
%post -n python-salt
if [ -f /usr/sbin/update-alternatives ]; then
    for SALT_SCRIPT in salt-call salt-support spm; do
        update-alternatives --quiet --install "%{_bindir}/${SALT_SCRIPT}" "${SALT_SCRIPT}" \
            "%{_bindir}/${SALT_SCRIPT}-%{python_bin_suffix}" %{python_version_nodots}
    done
    for SALT_SCRIPT in salt salt-api salt-cloud salt-cp salt-key salt-master salt-minion salt-proxy salt-run salt-ssh salt-syndic zyppnotify; do
        update-alternatives --quiet --install "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}" "${SALT_SCRIPT}" \
            "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}-%{python_bin_suffix}" %{python_version_nodots}
    done
fi

%postun -n python-salt
if [ -f /usr/sbin/update-alternatives ]; then
    for SALT_SCRIPT in salt-call salt-support spm; do
        if [ ! -e "%{_bindir}/${SALT_SCRIPT}-%{python_bin_suffix}" ]; then
            update-alternatives --quiet --remove "${SALT_SCRIPT}" "%{_bindir}/${SALT_SCRIPT}-%{python_bin_suffix}"
        fi
    done
    for SALT_SCRIPT in salt salt-api salt-cloud salt-cp salt-key salt-master salt-minion salt-proxy salt-run salt-ssh salt-syndic zyppnotify; do
        if [ ! -e "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}-%{python_bin_suffix}" ]; then
            update-alternatives --quiet --remove "${SALT_SCRIPT}" "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}-%{python_bin_suffix}"
        fi
    done
fi
%endif
%endif

%if 0%{?singlespec_compat}
%posttrans -n %{python_module salt}
%else
%posttrans -n python-salt
%endif

%if %{with libalternatives}
# restore symlinks to alts after migration from update-alternatives to alts
# in cases where the old package flavor (based u-a) is removed in favor of
# new python flavor (bsc#1250755).
# i.a. python3-salt (3.6 using u-a) -> python313-salt (3.13 using alts)
if [ -f /usr/bin/alts ]; then
    for SALT_SCRIPT in salt-call salt-support spm; do
        if [ ! -e "%{_bindir}/${SALT_SCRIPT}" ]; then
            ln -sf alts "%{_bindir}/${SALT_SCRIPT}"
        fi
    done
    for SALT_SCRIPT in salt salt-api salt-cloud salt-cp salt-key salt-master salt-minion salt-proxy salt-run salt-ssh salt-syndic zyppnotify; do
        if [ ! -e "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}" ]; then
            ln -sf ../../bin/alts "%{_exec_prefix}/libexec/salt/${SALT_SCRIPT}"
        fi
    done
fi
%endif

# force re-generate a new thin.tgz
rm -f %{_localstatedir}/cache/salt/master/thin/version
rm -f %{_localstatedir}/cache/salt/minion/thin/version

%files api
%defattr(-,root,root)
%{_bindir}/salt-api
%if %{with systemd}
%{_sbindir}/rcsalt-api
%{_unitdir}/salt-api.service
%endif
%{_mandir}/man1/salt-api.1.*

%files cloud
%defattr(-,root,root)
%{_bindir}/salt-cloud
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.maps.d
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.profiles.d
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.providers.d
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud.profiles
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud.providers
%dir               %attr(0750, root, salt) %{_localstatedir}/cache/salt/cloud
%{_mandir}/man1/salt-cloud.1.*

%files ssh
%defattr(-,root,root)
%{_bindir}/salt-ssh
%{_mandir}/man1/salt-ssh.1.gz

%files syndic
%defattr(-,root,root)
%{_bindir}/salt-syndic
%{_mandir}/man1/salt-syndic.1.gz
%if %{with systemd}
%{_sbindir}/rcsalt-syndic
%{_unitdir}/salt-syndic.service
%endif

%files minion
%defattr(-,root,root)
%{_bindir}/salt-minion
%{_mandir}/man1/salt-minion.1.gz
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/salt/minion
%config(noreplace) %attr(0640, root, root) %ghost %{_sysconfdir}/salt/minion_id
%dir               %attr(0750, root, root) %{_sysconfdir}/salt/minion.d/
%dir               %attr(0750, root, root) %{_sysconfdir}/salt/pki/minion/
%dir               %attr(0750, root, root) %{_localstatedir}/cache/salt/minion/
%if %{with systemd}
%{_sbindir}/rcsalt-minion
%endif

# Install plugin only on SUSE machines
%if 0%{?suse_version}
%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif

# Install DNF plugin only on RH machines
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 8
%{python3_sitelib}/dnf-plugins/dnfnotify.py
%{python3_sitelib}/dnf-plugins/__pycache__/dnfnotify.*
%{_sysconfdir}/dnf/plugins/dnfnotify.conf
%endif

%if %{with systemd}
%{_unitdir}/salt-minion.service
%endif

%files proxy
%defattr(-,root,root)
%{_bindir}/salt-proxy
%{_mandir}/man1/salt-proxy.1.gz
%if %{with systemd}
%{_unitdir}/salt-proxy@.service
%endif

%files master
%defattr(-,root,root)
%{_bindir}/salt
%{_bindir}/salt-master
%{_bindir}/salt-cp
%{_bindir}/salt-key
%{_bindir}/salt-run
%{_mandir}/man1/salt-master.1.gz
%{_mandir}/man1/salt-cp.1.gz
%{_mandir}/man1/salt-key.1.gz
%{_mandir}/man1/salt-run.1.gz
%{_mandir}/man7/salt.7.gz
%if 0%{?suse_version} <= 1500
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/salt
%endif
%if %{with systemd}
%{_sbindir}/rcsalt-master
%{_unitdir}/salt-master.service
%endif
#
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/master
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/roster
%dir               %attr(0755, root, salt) %{_sysconfdir}/salt/master.d/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_autosign/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_denied/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_pre/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_rejected/
%dir               %attr(0755, salt, salt) /var/lib/salt
%dir               %attr(0755, root, salt) /srv/salt
%dir               %attr(0755, root, salt) /srv/pillar
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/jobs/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/proc/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/queues/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/roots/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/syndics/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/tokens/

%files
%defattr(-,root,root,-)
%{_bindir}/spm
%if ! 0%{?_alternatives}
%{_bindir}/salt-call
%endif
%{_bindir}/salt-support
%{_mandir}/man1/salt-call.1.gz
%{_mandir}/man1/spm.1.gz
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/salt
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/salt
%endif
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc AUTHORS README.rst README.SUSE
#
%dir        %attr(0750, root, salt) %{_sysconfdir}/salt
%dir        %attr(0750, root, salt) %{_sysconfdir}/salt/pki
%dir        %attr(0750, salt, salt) %{_localstatedir}/log/salt
%dir        %attr(0750, root, salt) %{_localstatedir}/cache/salt
%dir        %attr(0750, root, salt) /srv/spm
%if %{with systemd}
/usr/lib/tmpfiles.d/salt.conf
%endif
%{_mandir}/man1/salt.1.*

%files %{python_files salt}
%defattr(-,root,root,-)
%if 0%{?_alternatives}
%python_alternative %{_bindir}/salt-call
%python_alternative %{_bindir}/salt-support
%python_alternative %{_bindir}/spm
%dir %{_exec_prefix}/libexec
%dir %attr(0755, root, root) %{_exec_prefix}/libexec/salt
%python_alternative %{_exec_prefix}/libexec/salt/salt
%python_alternative %{_exec_prefix}/libexec/salt/salt-api
%python_alternative %{_exec_prefix}/libexec/salt/salt-cloud
%python_alternative %{_exec_prefix}/libexec/salt/salt-cp
%python_alternative %{_exec_prefix}/libexec/salt/salt-key
%python_alternative %{_exec_prefix}/libexec/salt/salt-master
%python_alternative %{_exec_prefix}/libexec/salt/salt-minion
%python_alternative %{_exec_prefix}/libexec/salt/salt-proxy
%python_alternative %{_exec_prefix}/libexec/salt/salt-run
%python_alternative %{_exec_prefix}/libexec/salt/salt-ssh
%python_alternative %{_exec_prefix}/libexec/salt/salt-syndic
%python_alternative %{_exec_prefix}/libexec/salt/zyppnotify
%endif

%dir %{python_sitelib}/salt
%dir %{python_sitelib}/salt-*.egg-info
%{python_sitelib}/salt/*
%{python_sitelib}/salt-*.egg-info/*

%if %{with docs}
%files doc
%defattr(-,root,root)
%doc doc/_build/html
%endif

%if %{with bash_completion}
%files bash-completion
%defattr(-,root,root)
%dir %{_sysconfdir}/bash_completion.d/
%config %{_sysconfdir}/bash_completion.d/%{name}
%endif

%if %{with zsh_completion}
%files zsh-completion
%defattr(-,root,root)
%dir %{_sysconfdir}/zsh_completion.d/
%config %{_sysconfdir}/zsh_completion.d/%{name}
%endif

%if %{with fish_completion}
%files fish-completion
%defattr(-,root,root)
%{fish_completions_dir}/salt*
%dir %{fish_completions_dir}
%dir %{fish_dir}
%endif

%files standalone-formulas-configuration
%defattr(-,root,root)
%dir               %attr(0755, root, salt) %{_sysconfdir}/salt/master.d/
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/master.d/standalone-formulas-configuration.conf
%dir               %attr(0750, root, root) %{_sysconfdir}/salt/minion.d/
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/salt/minion.d/standalone-formulas-configuration.conf
%dir               %attr(0755, root, salt) %{_prefix}/share/salt-formulas/
%dir               %attr(0755, root, salt) %{_prefix}/share/salt-formulas/states/
%dir               %attr(0755, root, salt) %{_prefix}/share/salt-formulas/metadata/

%files transactional-update
%defattr(-,root,root)
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/salt/minion.d/transactional_update.conf

%endif

%if "%{flavor}" == "testsuite"
%files %{python_files salt-testsuite}
%{python_sitelib}/salt-testsuite
%endif

%changelog
