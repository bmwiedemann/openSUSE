#
# spec file for package salt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%global debug_package %{nil}

%if 0%{?suse_version} > 1210 || 0%{?rhel} >= 7 || 0%{?fedora} >=28
%bcond_without systemd
%else
%bcond_with    systemd
%endif
%{!?python3_sitelib: %global python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%if 0%{?suse_version} > 1110
%bcond_without bash_completion
%bcond_without fish_completion
%bcond_without zsh_completion
%else
%bcond_with    bash_completion
%bcond_with    fish_completion
%bcond_with    zsh_completion
%endif
%bcond_with    test
%bcond_without docs
%bcond_with    builddocs

Name:           salt
Version:        3002.2
Release:        0
Summary:        A parallel remote execution system
License:        Apache-2.0
Group:          System/Management
Url:            http://saltstack.org/
Source:         v%{version}.tar.gz
Source1:        README.SUSE
Source2:        salt-tmpfiles.d
Source3:        html.tar.bz2
Source4:        update-documentation.sh
Source5:        travis.yml

Patch1:         run-salt-master-as-dedicated-salt-user.patch
Patch2:         run-salt-api-as-user-salt-bsc-1064520.patch
Patch3:         activate-all-beacons-sources-config-pillar-grains.patch
Patch4:         avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
Patch5:         fix-bsc-1065792.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46684
Patch6:         add-saltssh-multi-version-support-across-python-inte.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46890
Patch7:         fall-back-to-pymysql.patch
# PATCH-FIX_OPENSUSE bsc#1091371
Patch8:         enable-passing-a-unix_socket-for-mysql-returners-bsc.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47638
Patch9:         add-all_versions-parameter-to-include-all-installed-.patch
# PATCH-FIX_OPENSUSE bsc#1057635
Patch10:        add-environment-variable-to-know-if-yum-is-invoked-f.patch
# PATCH-FIX_OPENSUSE
Patch11:        add-custom-suse-capabilities-as-grains.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48294
Patch12:        fix-zypper.list_pkgs-to-be-aligned-with-pkg-state.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49063
Patch13:        integration-of-msi-authentication-with-azurearm-clou.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49538
Patch14:        fix-for-suse-expanded-support-detection.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48812
Patch15:        use-adler32-algorithm-to-compute-string-checksums.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49497
Patch16:        x509-fixes-111.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49696
Patch17:        loosen-azure-sdk-dependencies-in-azurearm-cloud-driv.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49737
Patch18:        do-not-load-pip-state-if-there-is-no-3rd-party-depen.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49815
Patch19:        fix-ipv6-scope-bsc-1108557.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49480
Patch20:        early-feature-support-config.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49936
Patch21:        make-profiles-a-package.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49946
Patch22:        add-cpe_name-for-osversion-grain-parsing-u-49946.patch
# PATCH-FIX_OPENSUSE: Fix unit test for grains core
Patch23:        fix-unit-test-for-grains-core.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50095
Patch24:        support-config-non-root-permission-issues-fixes-u-50.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50018
Patch25:        add-multi-file-support-and-globbing-to-the-filetree-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49761
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50201
Patch26:        fixes-cve-2018-15750-cve-2018-15751.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50417
Patch27:        fix-git_pillar-merging-across-multiple-__env__-repos.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50523
Patch28:        get-os_arch-also-without-rpm-package-installed.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50392
Patch29:        make-aptpkg.list_repos-compatible-on-enabled-disable.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50453
Patch30:        debian-info_installed-compatibility-50453.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50773
Patch31:        add-hold-unhold-functions.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50401
# NOTE: This is a techpreview as well as in Fluorine! Release only in Neon.
Patch32:        add-supportconfig-module-for-remote-calls-and-saltss.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/116
Patch33:        return-the-expected-powerpc-os-arch-bsc-1117995.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51108
Patch34:        remove-arch-from-name-when-pkg.list_pkgs-is-called-w.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51119
Patch35:        fix-issue-2068-test.patch
# PATCH_FIX_OPENSUSE: Temporary fix allowing "id_" and "force" params while upstrem figures it out
Patch36:        temporary-fix-extend-the-whitelist-of-allowed-comman.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51382
Patch37:        don-t-call-zypper-with-more-than-one-no-refresh.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50109
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/pull/121
Patch38:        add-virt.all_capabilities.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51384
Patch39:        include-aliases-in-the-fqdns-grains.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50546
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51863
Patch40:        async-batch-implementation.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52527
Patch41:        calculate-fqdns-in-parallel-to-avoid-blockings-bsc-1.patch
#PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/139
Patch42:       fix-async-batch-race-conditions.patch
#PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/141
Patch43:       add-batch_presence_ping_timeout-and-batch_presence_p.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52527
Patch44:       use-threadpool-from-multiprocessing.pool-to-avoid-le.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52888
Patch45:       do-not-crash-when-there-are-ipv6-established-connect.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/144
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/52855
Patch46:       fix-async-batch-multiple-done-events.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/52743
Patch47:       switch-firewalld-state-to-use-change_interface.patch
# PATCH-FIX_OPENSUSE
Patch48:       add-standalone-configuration-file-for-enabling-packa.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53293
Patch49:       do-not-break-repo-files-with-multiple-line-values-on.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53159
Patch50:       batch.py-avoid-exception-when-minion-does-not-respon.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53471
Patch51:       fix-zypper-pkg.list_pkgs-expectation-and-dpkg-mockin.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/161
Patch52:       provide-the-missing-features-required-for-yomi-yet-o.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53661
Patch53:       do-not-make-ansiblegate-to-crash-on-python3-minions.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53693
Patch54:       allow-passing-kwargs-to-pkg.list_downloaded-bsc-1140.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53661
Patch55:       prevent-ansiblegate-unit-tests-to-fail-on-ubuntu.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54048
Patch56:       avoid-traceback-when-http.query-request-cannot-be-pe.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53992
#                     https://github.com/saltstack/salt/pull/53996
#                     https://github.com/saltstack/salt/pull/54022
#                     https://github.com/saltstack/salt/pull/54024
Patch57:       accumulated-changes-required-for-yomi-165.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/159
Patch58:       move-server_id-deprecation-warning-to-reduce-log-spa.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54077
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/166
Patch59:       fix-aptpkg-systemd-call-bsc-1143301.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/170
Patch60:       strip-trailing-from-repo.uri-when-comparing-repos-in.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/177
Patch61:       restore-default-behaviour-of-pkg-list-return.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/172
Patch62:       implement-network.fqdns-module-function-bsc-1134860-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/6af07030a502c427781991fc9a2b994fa04ef32e
Patch63:       fix-memory-leak-produced-by-batch-async-find_jobs-me.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/002543df392f65d95dbc127dc058ac897f2035ed
Patch64:       improve-batch_async-to-release-consumed-memory-bsc-1.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54077
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/44a91c2ce6df78d93ce0ef659dedb0e41b1c2e04
Patch65:       prevent-systemd-run-description-issue-when-running-a.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/55d8a777d6a9b19c959e14a4060e5579e92cd106
Patch66:       use-current-ioloop-for-the-localclient-instance-of-b.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/8378bb24a5a53973e8dba7658b8b3465d967329f
Patch67:       fix-failing-unit-tests-for-batch-async.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53326
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54954
Patch68:       accumulated-changes-from-yomi-167.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/180
Patch69:       fix-a-wrong-rebase-in-test_core.py-180.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/182
Patch70:       remove-unnecessary-yield-causing-badyielderror-bsc-1.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/186
Patch71:       read-repo-info-without-using-interpolation-bsc-11356.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53293
Patch72:       prevent-test_mod_del_repo_multiline_values-to-fail.patch
Patch73:       fix-for-log-checking-in-x509-test.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/190
Patch74:       fixing-streamclosed-issue.patch
Patch75:       fix-batch_async-obsolete-test.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/191
Patch76:       let-salt-ssh-use-platform-python-binary-in-rhel8-191.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/193
Patch77:       xfs-do-not-fails-if-type-is-not-present.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/55245
Patch78:      virt-adding-kernel-boot-parameters-to-libvirt-xml-55.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/200
Patch79:      support-for-btrfs-and-xfs-in-parted-and-mkfs.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56125
Patch80:      add-astra-linux-common-edition-to-the-os-family-list.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/211
Patch81:      apply-patch-from-upstream-to-support-python-3.8.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/217
Patch82:      batch_async-avoid-using-fnmatch-to-match-event-217.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/8a23030d347b7487328c0395f5e30ef29daf1455
Patch83:      batch-async-catch-exceptions-and-safety-unregister-a.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/a38adfa2efe40c2b1508b685af0b5d28a6bbcfc8
Patch84:      fix-unit-tests-for-batch-async-after-refactor.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/b4c401cfe6031b61e27f7795bfa1aca6e8341e52
Patch85:      changed-imports-to-vendored-tornado.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/25b4e3ea983b2606b2fb3d3c0e42f9840208bf84
Patch86:      remove-deprecated-usage-of-no_mock-and-no_mock_reaso.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/a8f0a15e4067ec278c8a2d690e3bf815523286ca
Patch87:      fix-wrong-test_mod_del_repo_multiline_values-test-af.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/55814
Patch88:      opensuse-3000-virt-defined-states-222.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/223
Patch89:      fix-for-temp-folder-definition-in-loader-unit-test.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56392
Patch90:      virt._get_domain-don-t-raise-an-exception-if-there-i.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/226
Patch91:      re-adding-function-to-test-for-root.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/227
Patch92:     loop-fix-variable-names-for-until_no_eval.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/226
Patch93:     make-setup.py-script-to-not-require-setuptools-9.1.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/50453
#                     https://github.com/saltstack/salt/commit/e20362f6f053eaa4144583604e6aac3d62838419
# Can be dropped one pull/50453 is in released version.
Patch94:     reintroducing-reverted-changes.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/b713d0b3031faadc17cd9cf09977ccc19e50bef7
Patch95:     add-new-custom-suse-capability-for-saltutil-state-mo.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56491
Patch96:     sanitize-grains-loaded-from-roster_grains.json.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/228
Patch97:     adds-explicit-type-cast-for-port.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53882
Patch98:     fixed-bug-lvm-has-no-parttion-type.-the-scipt-later-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/4f80e969e31247a4755d98d25f29b5d8b1b916c3
Patch99:     remove-vendored-backports-abc-from-requirements.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57123
Patch100:     prevent-logging-deadlock-on-salt-api-subprocesses-bs.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/235
Patch101:     python3.8-compatibility-pr-s-235.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56419
Patch102:     option-to-en-disable-force-refresh-in-zypper-215.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/229
Patch103:     fix-a-test-and-some-variable-names-229.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56439
Patch104:     add-docker-logout-237.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57392
Patch105:     zypperpkg-filter-patterns-that-start-with-dot-244.patch
# PATCH-FIX_OPENSUSE: hhttps://github.com/openSUSE/salt/commit/da936daeebd701e147707ad814c07bfc259d4be
Patch106:     add-publish_batch-to-clearfuncs-exposed-methods.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57779
Patch107:     info_installed-works-without-status-attr-now.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57491
Patch108:     opensuse-3000.3-spacewalk-runner-parse-command-250.patch
# PATCH-FIX_UPSTREAM: https://github.com/openSUSE/salt/pull/251
Patch109:     opensuse-3000-libvirt-engine-fixes-251.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58013
Patch110:     fix-__mount_device-wrapper-254.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58214
Patch111:     ansiblegate-take-care-of-failed-skipped-and-unreacha.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58301
Patch112:     do-not-raise-streamclosederror-traceback-but-only-lo.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/257
Patch113:     opensuse-3000.2-virt-backports-236-257.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/256
Patch114:     backport-virt-patches-from-3001-256.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/262
Patch115:     fix-the-removed-six.itermitems-and-six.-_type-262.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/263
Patch116:     fix-virt.update-with-cpu-defined-263.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/261
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57571
Patch117:     remove-msgpack-1.0.0-requirement-in-the-installed-me.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/bc20f38d0fa492af70321fef7fe2530937dfc86a
Patch118:     prevent-import-errors-when-running-test_btrfs-unit-t.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58529
Patch119:     invalidate-file-list-cache-when-cache-file-modified-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58400
Patch120:     xen-disk-fixes-264.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58552
Patch121:     zypperpkg-ignore-retcode-104-for-search-bsc-1176697-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58520
Patch122:     support-transactional-systems-microos-271.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/272
Patch123:     backport-a-few-virt-prs-272.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/275
Patch124:     bsc-1176024-fix-file-directory-user-and-group-owners.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/277
Patch125:     fix-grains.test_core-unit-test-277.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/e2c3b1cb72b796fe12f94af64baa2e64cbe5db0b
Patch126:     drop-wrong-mock-from-chroot-unit-test.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/280
Patch127:     ensure-virt.update-stop_on_reboot-is-updated-with-it.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/281
Patch128:     path-replace-functools.wraps-with-six.wraps-bsc-1177.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58560
Patch129:     fix-novendorchange-option-284.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58871
Patch130:     fix-cve-2020-25592-and-add-tests-bsc-1178319.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58520
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/286
Patch131:     grains-master-can-read-grains.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58784
Patch132:     add-migrated-state-and-gpg-key-management-functions-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/292
Patch133:     transactional_update-unify-with-chroot.call.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/295
Patch134:     pkgrepo-support-python-2.7-function-call-295.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/79ae019ac7515614c6fbc620e66575f015bc447
Patch135:     drop-wrong-virt-capabilities-code-after-rebasing-pat.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/5ea2f10b15684dd417bad858642faafc92cd382
#                     (revert https://github.com/saltstack/salt/pull/58655)
Patch136:     revert-fixing-a-use-case-when-multiple-inotify-beaco.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59269
Patch137:     fix-aptpkg.normalize_name-when-package-arch-is-all.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/310
Patch138:     open-suse-3002.2-bigvm-310.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59146
Patch139:     open-suse-3002.2-virt-network-311.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/298
Patch140:     fix-salt.utils.stringutils.to_str-calls-to-make-it-w.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58262
Patch141:     add-pkg.services_need_restart-302.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/301
Patch142:     add-patch-support-for-allow-vendor-change-option-wit.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/304
Patch143:     force-zyppnotify-to-prefer-packages.db-than-packages.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/4028fd6e84d882b6dcee695d409c7e1ed6c83bdc
Patch144:     revert-add-patch-support-for-allow-vendor-change-opt.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/73e357d7eee19a73cade22becb30d9689cae27ba
Patch145:     remove-deprecated-warning-that-breaks-miniion-execut.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59345
Patch146:     fix-onlyif-unless-when-multiple-conditions-bsc-11808.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59354
Patch147:     do-not-crash-when-unexpected-cmd-output-at-listing-p.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59189
Patch148:     virt-uefi-fix-backport-312.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59355
#                     https://github.com/saltstack/salt/pull/59417
Patch149:     3002.2-xen-spicevmc-dns-srv-records-backports-314.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59485
Patch150:     open-suse-3002.2-xen-grub-316.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/320
Patch151:     async-batch-implementation-fix-320.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56173
Patch152:     fixes-56144-to-enable-hotadd-profile-support.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/307
Patch153:     add-sleep-on-exception-handling-on-minion-connection.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/323
Patch154:     implementation-of-suse_ip-execution-module-bsc-10999.patch
# PATCH-FIX_UPSTREAM: no PR to link to yet
Patch155:     fix-for-some-cves-bsc1181550.patch
# PATCH-FIX_UPSTREAM: no PR to link to yet
Patch156:     allow-extra_filerefs-as-sanitized-kwargs-for-ssh-cli.patch
# PATCH-FIX_UPSTREAM: no PR to link to yet
Patch157:     fix-regression-on-cmd.run-when-passing-tuples-as-cmd.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59524
Patch158:     prevent-race-condition-on-sigterm-for-the-minion-bsc.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59746
Patch159:     do-not-monkey-patch-yaml-bsc-1177474.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59536
Patch160:     3002-set-distro-requirement-to-oldest-supported-vers.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59693
Patch161:     virt.network_update-handle-missing-ipv4-netmask-attr.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/313
Patch162:     allow-vendor-change-option-with-zypper-313.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59404
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/341
Patch163:     add-almalinux-and-alibaba-cloud-linux-to-the-os-fami.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/347
Patch164:     notify-beacon-for-debian-ubuntu-systems-347.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/336
Patch165:     update-target-fix-for-salt-ssh-to-process-targets-li.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59687
Patch166:     add-alibaba-cloud-linux-2-by-backporting-upstream-s-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/353
Patch167:     regression-fix-of-salt-ssh-on-processing-targets-353.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60056
Patch168:     improvements-on-ansiblegate-module-354.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  logrotate
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

Requires:       python3-%{name} = %{version}-%{release}

Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd

%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
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
%else
%if 0%{?suse_version}
Requires(pre): %insserv_prereq
%endif
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

%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  yum
%endif

%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in
the world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds or even thousands of individual
servers, handle them quickly and through a simple and manageable interface.

%package -n python3-salt
Summary:        python3 library for salt
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
BuildRequires:  python-rpm-macros
%if 0%{?rhel} == 8
BuildRequires:  platform-python
%else
BuildRequires:  python3
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# requirements/base.txt
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  python3-jinja2
BuildRequires:  python3-markupsafe
BuildRequires:  python3-msgpack > 0.3
BuildRequires:  python3-zmq >= 2.2.0
BuildRequires:  python3-m2crypto
%else
BuildRequires:  python3-Jinja2
BuildRequires:  python3-MarkupSafe
BuildRequires:  python3-msgpack-python > 0.3
BuildRequires:  python3-pyzmq >= 2.2.0
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-M2Crypto
%else
BuildRequires:  python3-pycrypto >= 2.6.1
%endif
%endif
BuildRequires:  python3-PyYAML
BuildRequires:  python3-psutil
BuildRequires:  python3-requests >= 1.0.0
BuildRequires:  python3-distro

# requirements/zeromq.txt
%if %{with test}
BuildRequires:  python3-boto >= 2.32.1
BuildRequires:  python3-mock
BuildRequires:  python3-moto >= 0.3.6
BuildRequires:  python3-pip
BuildRequires:  python3-salt-testing >= 2015.2.16
BuildRequires:  python3-unittest2
BuildRequires:  python3-xml
%endif
%if %{with builddocs}
BuildRequires:  python3-sphinx
%endif
%if 0%{?rhel} == 8
Requires:       platform-python
%else
Requires:       python3
%endif
# requirements/base.txt
%if 0%{?rhel} || 0%{?fedora}
Requires:       python3-jinja2
Requires:       yum
Requires:       python3-markupsafe
Requires:       python3-msgpack > 0.3
Requires:       python3-m2crypto
Requires:       python3-zmq >= 2.2.0

%if 0%{?rhel} == 8 || 0%{?fedora} >= 30
Requires:       dnf
%endif
%if 0%{?rhel} == 6
Requires:       yum-plugin-security
%endif
%else
Requires:       python3-Jinja2
Requires:       python3-MarkupSafe
Requires:       python3-msgpack-python > 0.3
%if 0%{?suse_version} >= 1500
Requires:       python3-M2Crypto
%else
Requires:       python3-pycrypto >= 2.6.1
%endif
Requires:       python3-pyzmq >= 2.2.0
%endif
Requires:       python3-PyYAML
Requires:       python3-psutil
Requires:       python3-requests >= 1.0.0
Requires:       python3-distro
%if 0%{?suse_version}
# required for zypper.py
Requires:       python3-rpm
Requires(pre):  libzypp(plugin:system) >= 0
Requires:       python3-zypp-plugin
# requirements/opt.txt (not all)
# Suggests:     python-MySQL-python  ## Disabled for now, originally Recommended
Suggests:       python3-timelib
Suggests:       python3-gnupg
# requirements/zeromq.txt
%endif
#
%if 0%{?suse_version}
# python-xml is part of python-base in all rhel versions
Requires:       python3-xml
Suggests:       python3-Mako
Recommends:     python3-netaddr
%endif

%description -n python3-salt
Python3 specific files for salt

%package api
Summary:        The api for Salt a parallel remote execution system
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
Requires:       python3-CherryPy >= 3.2.2

%description api
salt-api is a modular interface on top of Salt that can provide a variety of entry points into a running Salt system.

%package cloud
Summary:        Generic cloud provisioning tool for Saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
Requires:       python3-apache-libcloud
%if 0%{?suse_version}
Recommends:     python3-botocore
Recommends:     python3-netaddr
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
Recommends:     python3-pygit2 >= 0.20.3
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
BuildRequires:	systemd
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description master
The Salt master is the central server to which all minions connect.
Enabled commands to remote systems to be called in parallel rather
than serially.

%package minion
Summary:        The client component for Saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}

%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
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
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
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
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
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
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
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
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
Provides:       salt-formulas-configuration
Conflicts:      otherproviders(salt-formulas-configuration)

%description standalone-formulas-configuration
This package adds the standalone configuration for the Salt master in order to make the packaged Salt formulas available on the Salt master


%prep
%setup -q -n salt-%{version}-suse
cp %{S:1} .
cp %{S:5} ./.travis.yml
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1

%build
# Putting /usr/bin at the front of $PATH is needed for RHEL/RES 7. Without this
# change, the RPM will require /bin/python, which is not provided by any package
# on RHEL/RES 7.
%if 0%{?fedora} || 0%{?rhel}
export PATH=/usr/bin:$PATH
%endif
python3 setup.py --with-salt-version=%{version} --salt-transport=both build
cp ./build/lib/salt/_version.py ./salt
mv build _build.python3

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

%install
mv _build.python3 build
python3 setup.py --salt-transport=both install --prefix=%{_prefix} --root=%{buildroot}
mv build _build.python3

DEF_PYPATH=_build.python3/scripts-*/

rm -f %{buildroot}%{_bindir}/*
for script in $DEF_PYPATH/*; do
  install -m 0755 $script %{buildroot}%{_bindir}
done

## create missing directories
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/master.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/minion.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.maps.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.profiles.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.providers.d
install -Dd -m 0750 %{buildroot}%{_localstatedir}/log/salt
install -Dd -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d/
install -Dd -m 0755 %{buildroot}%{_sbindir}
install -Dd -m 0750 %{buildroot}%{_localstatedir}/log/salt
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/minion/extmod
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/jobs
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/proc
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/queues
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/roots
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/syndics
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/tokens
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/cloud
install -Dd -m 0750 %{buildroot}/var/lib/salt
install -Dd -m 0750 %{buildroot}/srv/salt
install -Dd -m 0750 %{buildroot}/srv/pillar
install -Dd -m 0750 %{buildroot}/srv/spm
install -Dd -m 0755 %{buildroot}%{_docdir}/salt
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

# Install salt-support profiles
install -Dpm 0644 salt/cli/support/profiles/* %{buildroot}%{python3_sitelib}/salt/cli/support/profiles


## Install Zypper plugins only on SUSE machines
%if 0%{?suse_version}
install -Dd -m 0750 %{buildroot}%{_prefix}/lib/zypp/plugins/commit
%{__install} scripts/suse/zypper/plugins/commit/zyppnotify %{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!/usr/bin/python3=' %{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif

# Install Yum plugins only on RH machines
%if 0%{?fedora} || 0%{?rhel}
install -Dd %{buildroot}%{_prefix}/share/yum-plugins
install -Dd %{buildroot}/etc/yum/pluginconf.d
%{__install} scripts/suse/yum/plugins/yumnotify.py %{buildroot}%{_prefix}/share/yum-plugins
%{__install} scripts/suse/yum/plugins/yumnotify.conf %{buildroot}/etc/yum/pluginconf.d
%endif

## install init and systemd scripts
%if %{with systemd}
install -Dpm 0644 pkg/suse/salt-master.service %{buildroot}%{_unitdir}/salt-master.service
%if 0%{?suse_version}
install -Dpm 0644 pkg/suse/salt-minion.service %{buildroot}%{_unitdir}/salt-minion.service
%else
install -Dpm 0644 pkg/suse/salt-minion.service.rhel7 %{buildroot}%{_unitdir}/salt-minion.service
%endif
install -Dpm 0644 pkg/salt-syndic.service %{buildroot}%{_unitdir}/salt-syndic.service
install -Dpm 0644 pkg/suse/salt-api.service    %{buildroot}%{_unitdir}/salt-api.service
install -Dpm 0644 pkg/salt-proxy@.service %{buildroot}%{_unitdir}/salt-proxy@.service
ln -s service %{buildroot}%{_sbindir}/rcsalt-master
ln -s service %{buildroot}%{_sbindir}/rcsalt-syndic
ln -s service %{buildroot}%{_sbindir}/rcsalt-minion
ln -s service %{buildroot}%{_sbindir}/rcsalt-api
install -Dpm 644 %{S:2}                   %{buildroot}/usr/lib/tmpfiles.d/salt.conf
%else
mkdir -p %{buildroot}%{_initddir}
## install init scripts
install -Dpm 0755 pkg/suse/salt-master %{buildroot}%{_initddir}/salt-master
install -Dpm 0755 pkg/suse/salt-syndic %{buildroot}%{_initddir}/salt-syndic
install -Dpm 0755 pkg/suse/salt-minion %{buildroot}%{_initddir}/salt-minion
install -Dpm 0755 pkg/suse/salt-api %{buildroot}%{_initddir}/salt-api
ln -sf %{_initddir}/salt-master %{buildroot}%{_sbindir}/rcsalt-master
ln -sf %{_initddir}/salt-syndic %{buildroot}%{_sbindir}/rcsalt-syndic
ln -sf %{_initddir}/salt-minion %{buildroot}%{_sbindir}/rcsalt-minion
ln -sf %{_initddir}/salt-api %{buildroot}%{_sbindir}/rcsalt-api
%endif

## Install sysV salt-minion watchdog for SLES11 and RHEL6
%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
install -Dpm 0755 scripts/suse/watchdog/salt-daemon-watcher %{buildroot}%{_bindir}/salt-daemon-watcher
%endif 

#
## install config files
install -Dpm 0640 conf/minion %{buildroot}%{_sysconfdir}/salt/minion
install -Dpm 0640 /dev/null   %{buildroot}%{_sysconfdir}/salt/minion_id
install -Dpm 0640 conf/master %{buildroot}%{_sysconfdir}/salt/master
install -Dpm 0640 conf/roster %{buildroot}%{_sysconfdir}/salt/roster
install -Dpm 0640 conf/cloud %{buildroot}%{_sysconfdir}/salt/cloud
install -Dpm 0640 conf/cloud.profiles %{buildroot}%{_sysconfdir}/salt/cloud.profiles
install -Dpm 0640 conf/cloud.providers %{buildroot}%{_sysconfdir}/salt/cloud.providers
#
## install logrotate file (for RHEL6 we use without sudo)
%if 0%{?rhel} > 6 || 0%{?suse_version}
install -Dpm 0644  pkg/suse/salt-common.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/salt
%else
install -Dpm 0644  pkg/salt-common.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/salt
%endif
#
%if 0%{?suse_version} <= 1500
## install SuSEfirewall2 rules
install -Dpm 0644  pkg/suse/salt.SuSEfirewall2 %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/salt
%endif
#
## install completion scripts
%if %{with bash_completion}
install -Dpm 0644 pkg/salt.bash %{buildroot}%{_sysconfdir}/bash_completion.d/salt
%endif
%if %{with zsh_completion}
install -Dpm 0644 pkg/zsh_completion.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/salt
%endif

%if %{with fish_completion}
mkdir -p %{buildroot}%{fish_completions_dir}
install -Dpm 0644 pkg/fish-completions/* %{buildroot}%{fish_completions_dir}
%endif

# Standalone Salt formulas configuration
install -Dd -m 0750 %{buildroot}%{_prefix}/share/salt-formulas
install -Dd -m 0750 %{buildroot}%{_prefix}/share/salt-formulas/states
install -Dd -m 0750 %{buildroot}%{_prefix}/share/salt-formulas/metadata
install -Dpm 0640 conf/suse/standalone-formulas-configuration.conf %{buildroot}%{_sysconfdir}/salt/master.d

%if 0%{?suse_version} > 1020
%fdupes %{buildroot}%{_docdir}
%fdupes %{buildroot}%{python3_sitelib}
%endif

%check
%if %{with test}
python3 setup.py test --runtests-opts=-u
%endif

%pre
S_HOME="/var/lib/salt"
S_PHOME="/srv/salt"
getent passwd salt | grep $S_PHOME >/dev/null && usermod -d $S_HOME salt
getent group salt >/dev/null || %{_sbindir}/groupadd -r salt
getent passwd salt >/dev/null || %{_sbindir}/useradd -r -g salt -d $S_HOME -s /bin/false -c "salt-master daemon" salt
if [[ -d "$S_PHOME/.ssh" ]]; then
    mv $S_PHOME/.ssh $S_HOME
fi

%post
%if %{with systemd}
systemd-tmpfiles --create /usr/lib/tmpfiles.d/salt.conf || true
%else
dbus-uuidgen --ensure
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
%fillup_only
%else
%systemd_post salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-proxy@.service
%else
%systemd_postun_with_restart salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-proxy
%endif
%endif

%preun syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-syndic.service
%else
%systemd_preun salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-syndic
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-syndic stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-syndic
  fi
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
%fillup_only
%else
%systemd_post salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-syndic.service
%else
%systemd_postun_with_restart salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-syndic
%endif
%endif

%preun master
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-master.service
%else
%systemd_preun salt-master.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-master
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-master stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-master
  fi
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
%fillup_only
%else
%systemd_post salt-master.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%else
  /sbin/chkconfig --add salt-master
%endif
%endif

%postun master
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-master.service
%else
%systemd_postun_with_restart salt-master.service
%endif
%else
%if 0%{?suse_version}
%restart_on_update salt-master
%insserv_cleanup
%else
  if [ "$1" -ge "1" ] ; then
      /sbin/service salt-master condrestart >/dev/null 2>&1 || :
  fi
%endif
%endif

%preun minion
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-minion.service
%else
%systemd_preun salt-minion.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-minion
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-minion stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-minion
  fi
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
%fillup_only
%else
%systemd_post salt-minion.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%else
  /sbin/chkconfig --add salt-minion
%endif
%endif

%postun minion
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-minion.service
%else
%systemd_postun_with_restart salt-minion.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-minion
%else
  if [ "$1" -ge "1" ] ; then
      /sbin/service salt-minion condrestart >/dev/null 2>&1 || :
  fi
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
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun api
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-api.service
%else
%systemd_postun_with_restart salt-api.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update
%endif
%endif

%posttrans -n python3-salt
# force re-generate a new thin.tgz
rm -f %{_localstatedir}/cache/salt/master/thin/version
rm -f %{_localstatedir}/cache/salt/minion/thin/version

%files api
%defattr(-,root,root)
%{_bindir}/salt-api
%{_sbindir}/rcsalt-api
%if %{with systemd}
%{_unitdir}/salt-api.service
%else
%{_initddir}/salt-api
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
%attr(755,root,root)%{python3_sitelib}/salt/cloud/deploy/bootstrap-salt.sh
%{_mandir}/man1/salt-cloud.1.*

%files ssh
%defattr(-,root,root)
%{_bindir}/salt-ssh
%{_mandir}/man1/salt-ssh.1.gz

%files syndic
%defattr(-,root,root)
%{_bindir}/salt-syndic
%{_mandir}/man1/salt-syndic.1.gz
%{_sbindir}/rcsalt-syndic
%if %{with systemd}
%{_unitdir}/salt-syndic.service
%else
%{_initddir}/salt-syndic
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
%{_sbindir}/rcsalt-minion

# Install plugin only on SUSE machines
%if 0%{?suse_version}
%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif

# Install Yum plugins only on RH machines
%if 0%{?fedora} || 0%{?rhel}
%{_prefix}/share/yum-plugins/
/etc/yum/pluginconf.d/yumnotify.conf
%endif

%if %{with systemd}
%{_unitdir}/salt-minion.service
%else
%config(noreplace) %{_initddir}/salt-minion
%endif

## Install sysV salt-minion watchdog for SLES11 and RHEL6
%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
%{_bindir}/salt-daemon-watcher
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
%{_sbindir}/rcsalt-master
%if %{with systemd}
%{_unitdir}/salt-master.service
%else
%config(noreplace) %{_initddir}/salt-master
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
%{_bindir}/salt-call
%{_bindir}/salt-support
%{_bindir}/salt-unity
%{_mandir}/man1/salt-unity.1.gz
%{_mandir}/man1/salt-call.1.gz
%{_mandir}/man1/spm.1.gz
%config(noreplace) %{_sysconfdir}/logrotate.d/salt
%if 0%{?suse_version} < 1500
%doc LICENSE AUTHORS README.rst HACKING.rst README.SUSE
%else
%license LICENSE
%doc AUTHORS README.rst HACKING.rst README.SUSE
%endif
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

%files -n python3-salt
%defattr(-,root,root,-)
%{python3_sitelib}/*
%exclude %{python3_sitelib}/salt/cloud/deploy/*.sh

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
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/master.d/standalone-formulas-configuration.conf
%dir               %attr(0755, root, salt) %{_prefix}/share/salt-formulas/
%dir               %attr(0755, root, salt) %{_prefix}/share/salt-formulas/states/
%dir               %attr(0755, root, salt) %{_prefix}/share/salt-formulas/metadata/

%changelog


