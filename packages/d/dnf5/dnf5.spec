#
# spec file for package dnf5
#
# Copyright (c) 2023 Red Hat, Inc.
# Copyright (c) 2026 Neal Gompa.
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


# ========== build options ==========

# As of openSUSE Tumbleweed 20260122, DNF5 replaces all legacy implementations
%bcond_without as_microdnf
%bcond_without as_dnf
%bcond_without as_yum

%bcond_without dnf5daemon_client
%bcond_without dnf5daemon_server
%bcond_without libdnf_cli
%bcond_without dnf5
%bcond_without dnf5_plugins
%bcond_without plugin_actions
%bcond_without plugin_appstream
%bcond_without plugin_expired_pgp_keys
%bcond_without plugin_manifest
%bcond_without python_plugins_loader
%bcond_without plugin_local

%bcond_without comps
%bcond_without modulemd
%bcond_without zchunk

%bcond_with    html
%bcond_without man

# TODO Go bindings fail to build, disable for now
%bcond_with    go
%bcond_without perl5
%bcond_without python3
%bcond_without ruby

# Tests are currently broken: https://github.com/rpm-software-management/dnf5/issues/1893
%bcond_without tests
%bcond_with    sanitizers
%bcond_with    performance_tests
%bcond_with    dnf5daemon_tests

# ========== versions of dependencies ==========

%global libmodulemd_version 2.5.0
%global librepo_version 1.20.0
%global libsolv_version 0.7.35
%global sqlite_version 3.35.0
%global swig_version 4
%global zchunk_version 0.9.11
%global libcurl_version 7.62.0

# ====== versioned library package names ======

%global libprefix libdnf5
%global libcliprefix libdnf5-cli
%global libsoversion 2
%global libclisoversion 3

%global libname %{libprefix}_%{libsoversion}
%global libcliname %{libcliprefix}%{libclisoversion}
%global devname %{libprefix}-devel
%global devcliname %{libcliprefix}-devel

Name:           dnf5
Version:        5.4.0.0
Release:        0
Summary:        Next generation RPM package manager
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/dnf5
Source0:        %{url}/archive/%{version}/dnf5-%{version}.tar.gz

# Backports from upstream

# Proposed upstream

# openSUSE specific fixes
## Migrate DNF persistent state directory to /usr/lib/sysimage
Patch1001:      dnf5-Use-usr-lib-sysimage-for-the-persistent-state-dir.patch
## Switch default reposdir to /etc/dnf/repos.d
Patch1002:      dnf5-Switch-default-reposdir-to-etc-dnf-repos.d.patch
## Disable Werror to fix bindings builds
Patch1003:      dnf5-disable-Werror.patch

Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       dnf-data
Recommends:     bash-completion

%if %{with plugin_expired_pgp_keys}
Recommends:     (libdnf5-plugin-expired-pgp-keys if gpg2)
%endif

%if %{with as_microdnf}
# We want to replace Micro DNF
Obsoletes:      microdnf < 4
Provides:       microdnf = %{version}-%{release}
%endif

%if %{with as_dnf}
# We want to replace DNF
Obsoletes:      dnf < 5
Provides:       dnf = %{version}-%{release}
%endif

%if %{with as_yum}
# We want to replace YUM
Obsoletes:      yum < 5
Provides:       yum = %{version}-%{release}
%endif

Provides:       dnf5-command(advisory)
Provides:       dnf5-command(autoremove)
Provides:       dnf5-command(check)
Provides:       dnf5-command(check-upgrade)
Provides:       dnf5-command(clean)
Provides:       dnf5-command(distro-sync)
Provides:       dnf5-command(downgrade)
Provides:       dnf5-command(download)
Provides:       dnf5-command(environment)
Provides:       dnf5-command(group)
Provides:       dnf5-command(history)
Provides:       dnf5-command(info)
Provides:       dnf5-command(install)
Provides:       dnf5-command(leaves)
Provides:       dnf5-command(list)
Provides:       dnf5-command(makecache)
Provides:       dnf5-command(mark)
Provides:       dnf5-command(module)
Provides:       dnf5-command(offline)
Provides:       dnf5-command(provides)
Provides:       dnf5-command(reinstall)
Provides:       dnf5-command(remove)
Provides:       dnf5-command(repo)
Provides:       dnf5-command(repoquery)
Provides:       dnf5-command(search)
Provides:       dnf5-command(swap)
Provides:       dnf5-command(system-upgrade)
Provides:       dnf5-command(upgrade)
Provides:       dnf5-command(versionlock)

# ========== build requires ==========

BuildRequires:  bash-completion-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  toml11-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(librepo) >= %{librepo_version}
BuildRequires:  pkgconfig(libsolv) >= %{libsolv_version}
BuildRequires:  pkgconfig(libsolvext) >= %{libsolv_version}
BuildRequires:  pkgconfig(rpm) >= 4.19.0
BuildRequires:  pkgconfig(sqlite3) >= %{sqlite_version}
BuildRequires:  pkgconfig(systemd)

%if %{with tests}
BuildRequires:  createrepo_c
BuildRequires:  rpm-build
BuildRequires:  pkgconfig(cppunit)
%endif

%if %{with comps}
BuildRequires:  pkgconfig(libcomps)
%endif

%if %{with modulemd}
BuildRequires:  pkgconfig(modulemd-2.0) >= %{libmodulemd_version}
%endif

%if %{with zchunk}
BuildRequires:  pkgconfig(zck) >= %{zchunk_version}
%endif

%if %{with static_libsolv}
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
%endif

%if %{with html} || %{with man}
#BuildRequires:  python3dist(breathe)
BuildRequires:  python3-breathe
#BuildRequires:  python3dist(sphinx) >= 4.1.2
BuildRequires:  python3-Sphinx >= 4.1.2
#BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-sphinx_rtd_theme
# requests requires ca-certs to work properly
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
%endif

%if %{with sanitizers}
BuildRequires:  libasan
BuildRequires:  liblsan
BuildRequires:  libubsan
%endif

%if %{with libdnf_cli}
# required for libdnf5-cli
BuildRequires:  pkgconfig(smartcols)
%endif

%if %{with dnf5_plugins}
# required for config-manager
BuildRequires:  libcurl-devel >= %{libcurl_version}
%if %{with plugin_manifest}
BuildRequires:  pkgconfig(libpkgmanifest)
%endif
%endif

%if %{with dnf5daemon_server}
# required for dnf5daemon-server
BuildRequires:  pkgconfig(sdbus-c++) >= 0.9.0
BuildRequires:  systemd-rpm-macros
%if %{with dnf5daemon_tests}
BuildRequires:  dbus-1-daemon
BuildRequires:  polkit
BuildRequires:  python3-devel
#BuildRequires:  python3dist(dbus-python)
BuildRequires:  python3-dbus-python
%endif
%endif

# ========== language bindings section ==========

%if %{with perl5} || %{with ruby} || %{with python3}
BuildRequires:  swig >= %{swig_version}
%endif

%if %{with perl5}
# required for perl-libdnf5 and perl-libdnf5-cli
BuildRequires:  perl
%if %{with tests}
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%endif
%endif

%if %{with ruby}
# required for ruby-libdnf5 and ruby-libdnf5-cli
BuildRequires:  ruby-devel
BuildRequires:  ruby-macros
%if %{with tests}
BuildRequires:  rubygem(test-unit)
%endif
%endif

%if %{with python3}
# required for python3-libdnf5 and python3-libdnf5-cli
BuildRequires:  python3-devel
%endif

%description
DNF5 is a command-line package manager that automates the process of installing,
upgrading, configuring, and removing computer programs in a consistent manner.
It supports RPM packages, modulemd modules, and comps groups & environments.

%post
%systemd_post dnf5-makecache.timer

%preun
%systemd_preun dnf5-makecache.timer

%postun
%systemd_postun_with_restart dnf5-makecache.timer

%files -f dnf5.lang
%{_bindir}/dnf5
%if %{with as_microdnf}
%{_bindir}/microdnf
%endif
%if %{with as_dnf}
%{_bindir}/dnf
%{_unitdir}/dnf-makecache.service
%{_unitdir}/dnf-makecache.timer
%endif
%if %{with as_yum}
%{_bindir}/yum
%endif

%{_unitdir}/dnf5-makecache.service
%{_unitdir}/dnf5-makecache.timer

%dir %{_sysconfdir}/dnf
%dir %{_sysconfdir}/dnf/dnf5-aliases.d
%doc %{_sysconfdir}/dnf/dnf5-aliases.d/README
%dir %{_sysconfdir}/dnf/dnf5-plugins
%ghost %attr(0644, root, root) %{_sysconfdir}/dnf/versionlock.toml
%dir %{_datadir}/dnf5
%dir %{_datadir}/dnf5/aliases.d
%config %{_datadir}/dnf5/aliases.d/compatibility.conf
%dir %{_datadir}/dnf5/dnf5-plugins
%dir %{_libdir}/dnf5
%dir %{_libdir}/dnf5/plugins
%doc %{_libdir}/dnf5/plugins/README
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/dnf*
%dir %{_prefix}/lib/sysimage/dnf
%verify(not md5 size mtime) %ghost %{_prefix}/lib/sysimage/dnf/*
%license COPYING.md
%license gpl-2.0.txt
%if %{with as_dnf}
%{_mandir}/man8/dnf.8.*
%endif
%{_mandir}/man8/dnf5.8.*
%{_mandir}/man8/dnf*-advisory.8.*
%{_mandir}/man8/dnf*-autoremove.8.*
%{_mandir}/man8/dnf*-check.8.*
%{_mandir}/man8/dnf*-check-upgrade.8.*
%{_mandir}/man8/dnf*-clean.8.*
%{_mandir}/man8/dnf*-distro-sync.8.*
%{_mandir}/man8/dnf*-do.8.*
%{_mandir}/man8/dnf*-downgrade.8.*
%{_mandir}/man8/dnf*-download.8.*
%{_mandir}/man8/dnf*-environment.8.*
%{_mandir}/man8/dnf*-group.8.*
%{_mandir}/man8/dnf*-history.8.*
%{_mandir}/man8/dnf*-info.8.*
%{_mandir}/man8/dnf*-install.8.*
%{_mandir}/man8/dnf*-leaves.8.*
%{_mandir}/man8/dnf*-list.8.*
%{_mandir}/man8/dnf*-makecache.8.*
%{_mandir}/man8/dnf*-mark.8.*
%{_mandir}/man8/dnf*-module.8.*
%{_mandir}/man8/dnf*-offline.8.*
%{_mandir}/man8/dnf*-provides.8.*
%{_mandir}/man8/dnf*-reinstall.8.*
%{_mandir}/man8/dnf*-remove.8.*
%{_mandir}/man8/dnf*-replay.8.*
%{_mandir}/man8/dnf*-repo.8.*
%{_mandir}/man8/dnf*-repoquery.8.*
%{_mandir}/man8/dnf*-search.8.*
%{_mandir}/man8/dnf*-swap.8.*
%{_mandir}/man8/dnf*-system-upgrade.8.*
%{_mandir}/man8/dnf*-upgrade.8.*
%{_mandir}/man8/dnf*-versionlock.8.*
%{_mandir}/man7/dnf*-aliases.7.*
%{_mandir}/man7/dnf*-caching.7.*
%{_mandir}/man7/dnf*-changes-from-dnf4.7.*
%{_mandir}/man7/dnf*-comps.7.*
%{_mandir}/man7/dnf*-filtering.7.*
%{_mandir}/man7/dnf*-forcearch.7.*
%{_mandir}/man7/dnf*-installroot.7.*
%{_mandir}/man7/dnf*-modularity.7.*
%{_mandir}/man7/dnf*-specs.7.*
%{_mandir}/man7/dnf*-system-state.7.*
%{_mandir}/man5/dnf*.conf.5.*
%{_mandir}/man5/dnf*.conf-vendorpolicy*.5.*
%{_mandir}/man5/dnf*.conf-todo.5.*
%{_mandir}/man5/dnf*.conf-deprecated.5.*

%{_unitdir}/dnf5-offline-transaction.service
%{_unitdir}/dnf5-offline-transaction-cleanup.service
%dir %{_unitdir}/system-update.target.wants
%{_unitdir}/system-update.target.wants/dnf5-offline-transaction.service

# ========== libdnf5 ==========
%package -n %{libname}
Summary:        Package management library
License:        LGPL-2.1-or-later
Requires:       libmodulemd2%{?_isa} >= %{libmodulemd_version}
Requires:       librepo0%{?_isa} >= %{librepo_version}
Requires:       libsolv1%{?_isa} >= %{libsolv_version}
Requires:       libsqlite3-0%{?_isa} >= %{sqlite_version}
%if %{with as_dnf}
# So OBS can detect this
Provides:       %{_sysconfdir}/dnf/dnf.conf
%endif

%description -n %{libname}
Package management library.

%ldconfig_scriptlets -n %{libname}

%files -n %{libname} -f libdnf5.lang
%dir %{_libdir}/libdnf5
%{_libdir}/libdnf5.so.%{libsoversion}
%license lgpl-2.1.txt
%ghost %attr(0755, root, root) %dir %{_var}/cache/libdnf5
%if %{with as_dnf}
%config(noreplace) %{_sysconfdir}/dnf/dnf.conf
%endif
%dir %{_prefix}/lib/sysimage/libdnf5
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/comps_groups
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/comps_groups/environments
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/comps_groups/groups
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/environments.toml
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/groups.toml
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/modules.toml
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/nevras.toml
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/offline
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/offline/offline-transaction-state.toml
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/offline/packages
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/offline/transaction.json
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/packages.toml
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/system.toml
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/transaction_history.sqlite{,-shm,-wal}
%verify(not md5 size mtime) %attr(0664, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/system-repo.lock
%dir %{_datadir}/dnf5/libdnf.conf.d
%dir %{_sysconfdir}/dnf/libdnf5.conf.d
%dir %{_datadir}/dnf5/repos.override.d
%dir %{_sysconfdir}/dnf/repos.override.d
%dir %{_sysconfdir}/dnf/libdnf5-plugins
%dir %{_libdir}/libdnf5/plugins
%dir %{_datadir}/dnf5/repos.d
%dir %{_datadir}/dnf5/vars.d
%dir %{_datadir}/dnf5/vendors.d
%dir %{_datadir}/dnf5/libdnf.plugins.conf.d
%dir %{_sysconfdir}/dnf/vendors.d


# ========== libdnf5-cli ==========

%if %{with libdnf_cli}
%package -n %{libcliname}
Summary:        Library for working with a terminal in a command-line package manager
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libcliname}
Library for working with a terminal in a command-line package manager.

%ldconfig_scriptlets -n %{libcliname}

%files -n %{libcliname} -f libdnf5-cli.lang
%{_libdir}/libdnf5-cli.so.%{libclisoversion}
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== dnf5-devel ==========

%package -n dnf5-devel
Summary:        Development files for dnf5
License:        LGPL-2.1-or-later
Requires:       %{devcliname}%{?_isa} = %{version}-%{release}
Requires:       %{devname}%{?_isa} = %{version}-%{release}
Requires:       dnf5%{?_isa} = %{version}-%{release}

%description -n dnf5-devel
Develpment files for dnf5.

%files -n dnf5-devel
%{_includedir}/dnf5/
%license COPYING.md
%license lgpl-2.1.txt

# ========== libdnf5-devel ==========

%package -n %{devname}
Summary:        Development files for libdnf
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       libsolv-devel%{?_isa} >= %{libsolv_version}
# Do not conflict with libdnf-devel yet, packagekit needs both devel packages for now.
#Conflicts:      libdnf-devel < 5

%description -n %{devname}
Development files for libdnf.

%files -n %{devname}
%{_includedir}/libdnf5/
%dir %{_libdir}/libdnf5
%{_libdir}/libdnf5.so
%{_libdir}/pkgconfig/libdnf5.pc
%license COPYING.md
%license lgpl-2.1.txt

# ========== libdnf5-cli-devel ==========

%package -n %{devcliname}
Summary:        Development files for libdnf5-cli
License:        LGPL-2.1-or-later
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}

%description -n %{devcliname}
Development files for libdnf5-cli.

%files -n %{devcliname}
%{_includedir}/libdnf5-cli/
%{_libdir}/libdnf5-cli.so
%{_libdir}/pkgconfig/libdnf5-cli.pc
%license COPYING.md
%license lgpl-2.1.txt

# ========== perl-libdnf5 ==========

%if %{with perl5}
%package -n perl-libdnf5
Summary:        Perl 5 bindings for the libdnf library
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n perl-libdnf5
Perl 5 bindings for the libdnf library.

%files -n perl-libdnf5
%{perl_vendorarch}/libdnf5
%{perl_vendorarch}/auto/libdnf5
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== perl-libdnf5-cli ==========

%if %{with perl5} && %{with libdnf_cli}
%package -n perl-libdnf5-cli
Summary:        Perl 5 bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}

%description -n perl-libdnf5-cli
Perl 5 bindings for the libdnf5-cli library.

%files -n perl-libdnf5-cli
%{perl_vendorarch}/libdnf5_cli
%{perl_vendorarch}/auto/libdnf5_cli
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== python3-libdnf5 ==========

%if %{with python3}
%package -n python3-libdnf5
%{?python_provide:%python_provide python3-libdnf}
Summary:        Python 3 bindings for the libdnf library
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5
Python 3 bindings for the libdnf library.

%files -n python3-libdnf5
%{python3_sitearch}/libdnf5
%{python3_sitearch}/libdnf5-*.dist-info
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== python3-libdnf5-cli ==========

%if %{with python3} && %{with libdnf_cli}
%package -n python3-libdnf5-cli
%{?python_provide:%python_provide python3-libdnf5-cli}
Summary:        Python 3 bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5-cli
Python 3 bindings for the libdnf5-cli library.

%files -n python3-libdnf5-cli
%{python3_sitearch}/libdnf5_cli
%{python3_sitearch}/libdnf5_cli-*.dist-info
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== ruby-libdnf5 ==========

%if %{with ruby}
%package -n ruby-libdnf5
Summary:        Ruby bindings for the libdnf library
License:        LGPL-2.1-or-later
Provides:       ruby(libdnf) = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n ruby-libdnf5
Ruby bindings for the libdnf library.

%files -n ruby-libdnf5
%{rb_vendorarchdir}/libdnf5
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== ruby-libdnf5-cli ==========

%if %{with ruby} && %{with libdnf_cli}
%package -n ruby-libdnf5-cli
Summary:        Ruby bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Provides:       ruby(libdnf_cli) = %{version}-%{release}
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}

%description -n ruby-libdnf5-cli
Ruby bindings for the libdnf5-cli library.

%files -n ruby-libdnf5-cli
%{rb_vendorarchdir}/libdnf5_cli
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== libdnf5-plugin-actions ==========

%if %{with plugin_actions}
%package -n libdnf5-plugin-actions
Summary:        Libdnf plugin that allows to run actions (external executables) on hooks
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n libdnf5-plugin-actions
Libdnf plugin that allows to run actions (external executables) on hooks.

%files -n libdnf5-plugin-actions -f libdnf5-plugin-actions.lang
%{_libdir}/libdnf5/plugins/actions.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/actions.conf
%dir %{_sysconfdir}/dnf/libdnf5-plugins/actions.d
%{_mandir}/man8/libdnf5-actions.8.*
%endif

# ========== libdnf5-plugin-appstream ==========

%if %{with plugin_appstream}
%package -n libdnf5-plugin-appstream
Summary:        Libdnf5 plugin to install repo AppStream data
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}
BuildRequires:  pkgconfig(appstream) >= 0.16

%description -n libdnf5-plugin-appstream
Libdnf5 plugin that installs repository's AppStream data, for repositories which provide them.

%files -n libdnf5-plugin-appstream
%{_libdir}/libdnf5/plugins/appstream.so
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/appstream.conf
%endif

# ========== libdnf5-plugin-expired-pgp-keys ==========

%if %{with plugin_expired_pgp_keys}
%package -n libdnf5-plugin-expired-pgp-keys
Summary:        Libdnf5 plugin for detecting and removing expired PGP keys
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       gpg2

%description -n libdnf5-plugin-expired-pgp-keys
Libdnf5 plugin for detecting and removing expired PGP keys.

%files -n libdnf5-plugin-expired-pgp-keys -f libdnf5-plugin-expired-pgp-keys.lang
%{_libdir}/libdnf5/plugins/expired-pgp-keys.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/expired-pgp-keys.conf
%{_mandir}/man8/libdnf5-expired-pgp-keys.8.*
%endif

# ========== python3-libdnf5-plugins-loader ==========

%if %{with python_plugins_loader}
%package -n python3-libdnf5-python-plugins-loader
Summary:        Libdnf plugin that allows loading Python plugins
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       python3-libdnf5%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5-python-plugins-loader
Libdnf plugin that allows loading Python plugins.

%files -n python3-libdnf5-python-plugins-loader
%{_libdir}/libdnf5/plugins/python_plugins_loader.*
%config %{_sysconfdir}/dnf/libdnf5-plugins/python_plugins_loader.conf
%dir %{_sysconfdir}/dnf/libdnf5-plugins/python_plugins_loader.d
%dir %{python3_sitelib}/libdnf_plugins/
%doc %{python3_sitelib}/libdnf_plugins/README
%endif

# ========== libdnf5-plugin-local ==========

%if %{with plugin_local}
%package -n libdnf5-plugin-local
Summary:        Libdnf5 plugin that downloads all packages to a local repository
License:        LGPL-2.1-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       createrepo_c

%description -n libdnf5-plugin-local
Libdnf5 plugin that automatically copies all downloaded packages to
a repository on the local filesystem and generates repo metadata.

%files -n libdnf5-plugin-local
%{_libdir}/libdnf5/plugins/local.*
%config %{_sysconfdir}/dnf/libdnf5-plugins/local.conf
%if %{with man}
%{_mandir}/man8/libdnf5-local.8.*
%endif
%endif

# ========== dnf5daemon-client ==========

%if %{with dnf5daemon_client}
%package -n dnf5daemon-client
Summary:        Command-line interface for dnf5daemon-server
License:        GPL-2.0-or-later
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       dnf5daemon-server = %{version}-%{release}

%description -n dnf5daemon-client
Command-line interface for dnf5daemon-server.

%files -n dnf5daemon-client -f dnf5daemon-client.lang
%{_bindir}/dnf5daemon-client
%license COPYING.md
%license gpl-2.0.txt
%{_mandir}/man8/dnf*daemon-client.8.*
%endif

# ========== dnf5daemon-server ==========

%if %{with dnf5daemon_server}
%package -n dnf5daemon-server
Summary:        Package management service with a DBus interface
License:        GPL-2.0-or-later
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       dbus-1-common
Requires:       dnf-data
Requires:       polkit

%description -n dnf5daemon-server
Package management service with a DBus interface.

%post -n dnf5daemon-server
%systemd_post dnf5daemon-server.service

%preun -n dnf5daemon-server
%systemd_preun dnf5daemon-server.service

%postun -n dnf5daemon-server
%systemd_postun_with_restart dnf5daemon-server.service

%files -n dnf5daemon-server -f dnf5daemon-server.lang
%config(noreplace) %{_sysconfdir}/dnf/dnf5daemon-server.conf
%{_sbindir}/dnf5daemon-server
%{_unitdir}/dnf5daemon-server.service
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d
%dir %{_datadir}/dbus-1/system-services
%dir %{_datadir}/dbus-1/interfaces
%{_datadir}/dbus-1/system.d/org.rpm.dnf.v0.conf
%{_datadir}/dbus-1/system-services/org.rpm.dnf.v0.service
%{_datadir}/dbus-1/interfaces/org.rpm.dnf.v0.*.xml
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.rpm.dnf.v0.policy
%license COPYING.md
%license gpl-2.0.txt
%{_mandir}/man8/dnf*daemon-server.8.*
%{_mandir}/man8/dnf*daemon-dbus-api.8.*
%endif

# ========== dnf5-plugins ==========

%if %{with dnf5_plugins}
%package -n dnf5-plugins
Summary:        Plugins for dnf5
License:        LGPL-2.1-or-later
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libcurl4%{?_isa} >= %{libcurl_version}
Provides:       dnf5-command(builddep)
Provides:       dnf5-command(changelog)
Provides:       dnf5-command(config-manager)
Provides:       dnf5-command(copr)
Provides:       dnf5-command(needs-restarting)
Provides:       dnf5-command(repoclosure)
Provides:       dnf5-command(reposync)
Provides:       dnf5-command(repomanage)

%description -n dnf5-plugins
Core DNF5 plugins that enhance dnf5 with builddep, changelog, config-manager,
copr, needs-restarting, repoclosure, repomanage, and reposync commands.


%files -n dnf5-plugins -f dnf5-plugin-builddep.lang -f dnf5-plugin-changelog.lang -f dnf5-plugin-config-manager.lang -f dnf5-plugin-copr.lang -f dnf5-plugin-needs-restarting.lang -f dnf5-plugin-repoclosure.lang -f dnf5-plugin-reposync.lang
%{_libdir}/dnf5/plugins/builddep_cmd_plugin.so
%{_libdir}/dnf5/plugins/changelog_cmd_plugin.so
%{_libdir}/dnf5/plugins/config-manager_cmd_plugin.so
%{_libdir}/dnf5/plugins/copr_cmd_plugin.so
%{_libdir}/dnf5/plugins/needs_restarting_cmd_plugin.so
%{_libdir}/dnf5/plugins/repoclosure_cmd_plugin.so
%{_libdir}/dnf5/plugins/reposync_cmd_plugin.so
%{_libdir}/dnf5/plugins/repomanage_cmd_plugin.so
%{_mandir}/man8/dnf*-builddep.8.*
%{_mandir}/man8/dnf*-changelog.8.*
%{_mandir}/man8/dnf*-config-manager.8.*
%{_mandir}/man8/dnf*-copr.8.*
%{_mandir}/man8/dnf*-needs-restarting.8.*
%{_mandir}/man8/dnf*-repoclosure.8.*
%{_mandir}/man8/dnf*-reposync.8.*
%{_mandir}/man8/dnf*-repomanage.8.*
%{_datadir}/dnf5/aliases.d/compatibility-plugins.conf
%{_datadir}/dnf5/aliases.d/compatibility-reposync.conf

# ========== dnf5-automatic plugin ==========

%package plugin-automatic
Summary:        Package manager - automated upgrades
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libcurl4%{?_isa} >= %{libcurl_version}
Provides:       dnf5-command(automatic)
%if %{with as_dnf}
Provides:       dnf-automatic = %{version}-%{release}
Obsoletes:      dnf-automatic < 5
%else
Conflicts:      dnf-automatic < 5
%endif

%description plugin-automatic
Alternative command-line interface "dnf upgrade" suitable to be executed
automatically and regularly from systemd timers, cron jobs or similar.

%files plugin-automatic -f dnf5-plugin-automatic.lang
%ghost %{_sysconfdir}/motd.d/dnf5-automatic
%{_libdir}/dnf5/plugins/automatic_cmd_plugin.so
%{_datadir}/dnf5/dnf5-plugins/automatic.conf
%ghost %config(noreplace) %{_sysconfdir}/dnf/automatic.conf
%ghost %config(noreplace) %{_sysconfdir}/dnf/dnf5-plugins/automatic.conf
%{_mandir}/man8/dnf*-automatic.8.*
%{_unitdir}/dnf5-automatic.service
%{_unitdir}/dnf5-automatic.timer
%{_unitdir}/dnf-automatic.service
%{_unitdir}/dnf-automatic.timer
%if %{with as_dnf}
%{_bindir}/dnf-automatic
%endif

# ========== dnf5-manifest plugin ==========

%if %{with plugin_manifest}
%package plugin-manifest
Summary:        DNF5 plugin for working with RPM package manifest files
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
Provides:       dnf5-command(manifest)

%description plugin-manifest
DNF5 plugin for working with RPM package manifest files.

%files plugin-manifest
%{_libdir}/dnf5/plugins/manifest_cmd_plugin.so
%if %{with man}
%{_mandir}/man8/dnf*-manifest.8.*
%endif
%endif
%endif

# ========== unpack, build, check & install ==========

%prep
%autosetup -S git_am -n dnf5-%{version}

%build
%cmake \
    -DPERL_INSTALLDIRS=vendor \
    \
    -DENABLE_SOLV_FOCUSNEW=ON \
    -DWITH_SYSTEMD=ON \
    -DWITH_DNF5DAEMON_CLIENT=%{?with_dnf5daemon_client:ON}%{!?with_dnf5daemon_client:OFF} \
    -DWITH_DNF5DAEMON_SERVER=%{?with_dnf5daemon_server:ON}%{!?with_dnf5daemon_server:OFF} \
    -DWITH_LIBDNF5_CLI=%{?with_libdnf_cli:ON}%{!?with_libdnf_cli:OFF} \
    -DWITH_DNF5=%{?with_dnf5:ON}%{!?with_dnf5:OFF} \
    -DWITH_DNF5_OBSOLETES_DNF=OFF \
    -DWITH_PLUGIN_ACTIONS=%{?with_plugin_actions:ON}%{!?with_plugin_actions:OFF} \
    -DWITH_PLUGIN_APPSTREAM=%{?with_plugin_appstream:ON}%{!?with_plugin_appstream:OFF} \
    -DWITH_PLUGIN_EXPIRED_PGP_KEYS=%{?with_plugin_expired_pgp_keys:ON}%{!?with_plugin_expired_pgp_keys:OFF} \
    -DWITH_PLUGIN_MANIFEST=%{?with_plugin_manifest:ON}%{!?with_plugin_manifest:OFF} \
    -DWITH_PYTHON_PLUGINS_LOADER=%{?with_python_plugins_loader:ON}%{!?with_python_plugins_loader:OFF} \
    \
    -DWITH_ACL=ON \
    -DWITH_COMPS=%{?with_comps:ON}%{!?with_comps:OFF} \
    -DWITH_MODULEMD=%{?with_modulemd:ON}%{!?with_modulemd:OFF} \
    -DWITH_ZCHUNK=%{?with_zchunk:ON}%{!?with_zchunk:OFF} \
    \
    -DWITH_HTML=%{?with_html:ON}%{!?with_html:OFF} \
    -DWITH_MAN=%{?with_man:ON}%{!?with_man:OFF} \
    \
    -DWITH_GO=%{?with_go:ON}%{!?with_go:OFF} \
    -DWITH_PERL5=%{?with_perl5:ON}%{!?with_perl5:OFF} \
    -DWITH_PYTHON3=%{?with_python3:ON}%{!?with_python3:OFF} \
    -DWITH_RUBY=%{?with_ruby:ON}%{!?with_ruby:OFF} \
    \
    -DWITH_SANITIZERS=%{?with_sanitizers:ON}%{!?with_sanitizers:OFF} \
    -DWITH_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
    -DWITH_PERFORMANCE_TESTS=%{?with_performance_tests:ON}%{!?with_performance_tests:OFF} \
    -DWITH_DNF5DAEMON_TESTS=%{?with_dnf5daemon_tests:ON}%{!?with_dnf5daemon_tests:OFF}
%cmake_build -O
%if %{with man}
    %cmake_build doc-man
%endif

%check
%if %{with tests}
    %ctest
%endif

%install
%cmake_install

# own dirs and files that dnf5 creates on runtime
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/dnf
for files in \
    groups.toml modules.toml nevras.toml packages.toml \
    system.toml transaction_history.sqlite \
    transaction_history.sqlite-shm \
    transaction_history.sqlite-wal userinstalled.toml \
    system-repo.lock
do
    touch %{buildroot}%{_prefix}/lib/sysimage/dnf/$files
done

# own the offline transaction target
mkdir -p %{buildroot}%{_unitdir}/system-update.target.wants/
pushd %{buildroot}%{_unitdir}/system-update.target.wants/
  ln -sr ../dnf5-offline-transaction.service
popd

%find_lang dnf5
%find_lang dnf5-plugin-automatic
%find_lang dnf5-plugin-builddep
%find_lang dnf5-plugin-changelog
%find_lang dnf5-plugin-config-manager
%find_lang dnf5-plugin-copr
%find_lang dnf5-plugin-needs-restarting
%find_lang dnf5-plugin-repoclosure
%find_lang dnf5-plugin-reposync
%find_lang dnf5daemon-client
%find_lang dnf5daemon-server
%find_lang libdnf5
%find_lang libdnf5-cli
%find_lang libdnf5-plugin-actions
%find_lang libdnf5-plugin-expired-pgp-keys

%if %{with as_microdnf}
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/microdnf
%endif
%if %{with as_dnf}
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/dnf
ln -sr %{buildroot}%{_datadir}/bash-completion/completions/dnf5 %{buildroot}%{_datadir}/bash-completion/completions/dnf
for file in %{buildroot}%{_mandir}/man[578]/dnf5[-.]*; do
    dir=$(dirname $file)
    filename=$(basename $file)
    ln -sr $file $dir/${filename/dnf5/dnf}
done
ln -sr %{buildroot}%{_unitdir}/dnf5-makecache.service %{buildroot}%{_unitdir}/dnf-makecache.service
ln -sr %{buildroot}%{_unitdir}/dnf5-makecache.timer %{buildroot}%{_unitdir}/dnf-makecache.timer
%else
# Let's not replace what dnf-data offers just yet..
rm %{buildroot}%{_sysconfdir}/dnf/dnf.conf
rm %{buildroot}%{_bindir}/dnf-automatic
%endif

# own dirs and files that dnf5 creates on runtime
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5
for file in \
    environments.toml groups.toml modules.toml nevras.toml packages.toml \
    system.toml \
    transaction_history.sqlite transaction_history.sqlite-shm \
    transaction_history.sqlite-wal
do
    touch %{buildroot}%{_prefix}/lib/sysimage/libdnf5/$file
done
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5/comps_groups

mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5/offline
touch %{buildroot}%{_sysconfdir}/dnf/versionlock.toml

%if %{with as_yum}
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/yum
%endif

# Do not deliver polkit rule allowing privileged actions for wheel (bsc#1245451)
rm -rf %{buildroot}%{_datadir}/polkit-1/rules.d

%changelog
