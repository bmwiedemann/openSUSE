#
# spec file for package salt
#
# Copyright (c) 2021 SUSE LLC
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
Version:        3005.1
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
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61189
Patch44:        state.apply-don-t-check-for-cached-pillar-errors.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/482
Patch45:        drop-serial-from-event.unpack-in-cli.batch_async.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/61093
Patch46:        state.orchestrate_single-does-not-pass-pillar-none-4.patch

### SALT-SSH WITH SALT BUNDLE ###
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61715 (ssh_pre_flight_args)
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/493
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/497
Patch47:        add-salt-ssh-support-with-venv-salt-minion-3004-493.patch
Patch48:        prevent-shell-injection-via-pre_flight_script_args-4.patch
###############

# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/501
Patch49:        fix-salt-ssh-opts-poisoning-bsc-1197637-3004-501.patch

# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/505
Patch50:        prevent-affection-of-ssh.opts-with-lazyloader-bsc-11.patch

# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/506
Patch51:        fix-regression-with-depending-client.ssh-on-psutil-b.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61895
Patch52:        make-sure-saltcacheloader-use-correct-fileclient-519.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61827
Patch53:        ignore-erros-on-reading-license-files-with-dpkg_lowp.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62109
Patch54:        use-salt-bundle-in-dockermod.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61984
Patch55:        save-log-to-logfile-with-docker.build.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62029
Patch56:        normalize-package-names-once-with-pkg.installed-remo.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62089
Patch57:        set-default-target-for-pip-from-venv_pip_target-envi.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/534
Patch58:        fix-ownership-of-salt-thin-directory-when-using-the-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62033
Patch59:        add-support-for-name-pkgs-and-diff_attr-parameters-t.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62067
Patch60:        fix-salt.states.file.managed-for-follow_symlinks-tru.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62209
Patch61:        add-support-for-gpgautoimport-539.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/2b486d0484c51509e9972e581d97655f4f87852e
Patch62:        fix-test_ipc-unit-tests.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62204
Patch63:        retry-if-rpm-lock-is-temporarily-unavailable-547.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62519
Patch64:        change-the-delimeters-to-prevent-possible-tracebacks.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61847
Patch65:        fix-state.apply-in-test-mode-with-file-state-module-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62539
Patch66:        add-amazon-ec2-detection-for-virtual-grains-bsc-1195.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62633
Patch67:       ignore-non-utf8-characters-while-reading-files-with-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62817
Patch68:       fopen-workaround-bad-buffering-for-binary-mode-563.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62120
Patch69:       make-pass-renderer-configurable-other-fixes-532.patch
### ENHANCE ZYPPERPKG ERROR MESSAGES ###
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62750
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62346
Patch70:       include-stdout-in-error-message-for-zypperpkg-559.patch
###############
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57426
Patch71:       clarify-pkg.installed-pkg_verify-documentation.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62862
Patch72:       ignore-extend-declarations-from-excluded-sls-files.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61772
Patch73:       detect-module.run-syntax.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62539
Patch74:       align-amazon-ec2-nitro-grains-with-upstream-pr-bsc-1.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62898
Patch75:       pass-the-context-to-pillar-ext-modules.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/c6be36eeea49ee0d0641da272087305f79c32c99 (not yet upstream)
# Fix problem caused by: https://github.com/openSUSE/salt/pull/493 (Patch47) affecting only 3005.1.
Patch76:       use-rlock-to-avoid-deadlocks-in-salt-ssh.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/61064
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/5e3ff4d662321c237ddd5b2c5c83f35a84af594c (not PR to master yet)
Patch77:       fixes-for-python-3.10-502.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/62854
Patch78:       allow-entrypoint-compatibility-for-importlib-metadat.patch

### IMPORTANT: The line below is used as a snippet marker. Do not touch it.
### SALT PATCHES LIST END

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  logrotate
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

Requires:       python3-%{name} = %{version}-%{release}
Obsoletes:      python2-%{name}

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
Requires:       python3-contextvars
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
Recommends:     python3-pyinotify
%endif

Provides:       bundled(python3-tornado) = 4.5.3

%description -n python3-salt
Python3 specific files for salt

%package api
Summary:        The api for Salt a parallel remote execution system
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if 0%{?suse_version}
Requires:       python3-CherryPy >= 3.2.2
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
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
Requires:       (%{name}-transactional-update = %{version}-%{release} if read-only-root-fs)
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

%package tests
Summary:        Unit and integration tests for Salt
Requires:       %{name} = %{version}-%{release}

%description tests
Collections of unit and integration tests for Salt

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


%prep
%setup -q -n salt-%{version}-suse
cp %{S:1} .
cp %{S:5} ./.travis.yml
cp %{S:6} .
%autopatch -p1

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
install -Dd -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d/

# Install salt-support profiles
install -Dpm 0644 salt/cli/support/profiles/* %{buildroot}%{python3_sitelib}/salt/cli/support/profiles

# Install Salt tests
install -Dd -m 0750 %{buildroot}%{_datadir}/salt
install -Dd -m 0750 %{buildroot}%{_datadir}/salt/tests
cp -a tests/* %{buildroot}%{_datadir}/salt/tests/
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!/usr/bin/python3=' %{buildroot}%{_datadir}/salt/tests/runtests.py

## Install Zypper plugins only on SUSE machines
%if 0%{?suse_version}
install -Dd -m 0750 %{buildroot}%{_prefix}/lib/zypp/plugins/commit
%{__install} scripts/suse/zypper/plugins/commit/zyppnotify %{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!/usr/bin/python3=' %{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif

# Install Yum plugins only on RH machines
%if 0%{?fedora} || 0%{?rhel}
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 8
install -Dd %{buildroot}%{python3_sitelib}/dnf-plugins
install -Dd %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__
install -Dd %{buildroot}%{_sysconfdir}/dnf/plugins
%{__install} scripts/suse/dnf/plugins/dnfnotify.py %{buildroot}%{python3_sitelib}/dnf-plugins
%{__install} scripts/suse/dnf/plugins/dnfnotify.conf %{buildroot}%{_sysconfdir}/dnf/plugins
%{__python3} -m compileall -d %{python3_sitelib}/dnf-plugins %{buildroot}%{python3_sitelib}/dnf-plugins/dnfnotify.py
%{__python3} -O -m compileall -d %{python3_sitelib}/dnf-plugins %{buildroot}%{python3_sitelib}/dnf-plugins/dnfnotify.py
%else
install -Dd %{buildroot}%{_prefix}/share/yum-plugins
install -Dd %{buildroot}%{_sysconfdir}/yum/pluginconf.d
%{__install} scripts/suse/yum/plugins/yumnotify.py %{buildroot}%{_prefix}/share/yum-plugins
%{__install} scripts/suse/yum/plugins/yumnotify.conf %{buildroot}%{_sysconfdir}/yum/pluginconf.d
%{__python} -m compileall -d %{_prefix}/share/yum-plugins %{buildroot}%{_prefix}/share/yum-plugins/yumnotify.py
%{__python} -O -m compileall -d %{_prefix}/share/yum-plugins %{buildroot}%{_prefix}/share/yum-plugins/yumnotify.py
%endif
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
install -Dpm 0640 transactional_update.conf %{buildroot}%{_sysconfdir}/salt/minion.d/transactional_update.conf
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
install -Dpm 0644 pkg/salt.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/salt
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
install -Dpm 0640 conf/suse/standalone-formulas-configuration.conf %{buildroot}%{_sysconfdir}/salt/minion.d

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
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 8
%{python3_sitelib}/dnf-plugins/dnfnotify.py
%{python3_sitelib}/dnf-plugins/__pycache__/dnfnotify.*
%{_sysconfdir}/dnf/plugins/dnfnotify.conf
%else
%{_prefix}/share/yum-plugins/yumnotify.*
%{_sysconfdir}/yum/pluginconf.d/yumnotify.conf
%endif
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
%{_mandir}/man1/salt-call.1.gz
%{_mandir}/man1/spm.1.gz
%config(noreplace) %{_sysconfdir}/logrotate.d/salt
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

%files -n python3-salt
%defattr(-,root,root,-)
%{python3_sitelib}/*
%exclude %{python3_sitelib}/salt/cloud/deploy/*.sh

%if %{with docs}
%files doc
%defattr(-,root,root)
%doc doc/_build/html
%endif

%files tests
%dir %{_datadir}/salt/
%dir %{_datadir}/salt/tests/
%{_datadir}/salt/tests/*

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


%changelog


