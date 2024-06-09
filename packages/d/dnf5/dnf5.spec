#
# spec file for package dnf5
#
# Copyright (c) 2023 Red Hat, Inc.
# Copyright (c) 2024 Neal Gompa.
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

%bcond_with    as_microdnf
%bcond_with    as_dnf
%bcond_with    as_yum

%bcond_without dnf5daemon_client
%bcond_without dnf5daemon_server
%bcond_without libdnf_cli
%bcond_without dnf5
%bcond_without dnf5_plugins
%bcond_without plugin_actions
%bcond_without python_plugins_loader

%bcond_without comps
%bcond_without modulemd
%bcond_without zchunk

%bcond_with    html
%bcond_without man

# openSUSE requires this
%bcond_without static_libsolv

# TODO Go bindings fail to build, disable for now
%bcond_with    go
%bcond_without perl5
%bcond_without python3
%bcond_without ruby

%bcond_without tests
%bcond_with    sanitizers
%bcond_with    performance_tests
%bcond_with    dnf5daemon_tests

# ========== versions of dependencies ==========

%global libmodulemd_version 2.5.0
%global librepo_version 1.15.0
%global libsolv_version 0.7.25
%global sqlite_version 3.35.0
%global swig_version 4
%global zchunk_version 0.9.11
%global libcurl_version 7.62.0

# ====== versioned library package names ======

%global libprefix libdnf5
%global libcliprefix libdnf5-cli
%global libsoversion 2
%global libclisoversion 2

%global libname %{libprefix}_%{libsoversion}
%global libcliname %{libcliprefix}%{libclisoversion}
%global devname %{libprefix}-devel
%global devcliname %{libcliprefix}-devel

Name:           dnf5
Version:        5.2.3.0
Release:        0
Summary:        Next generation RPM package manager
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/dnf5
Source0:        %{url}/archive/%{version}/dnf5-%{version}.tar.gz

# Backports from upstream

# Proposed upstream

# openSUSE specific fixes
## Fix libdnf build with static libsolvext
Patch1001:      dnf5-with-static-libsolvext.patch
## Migrate DNF persistent state directory to /usr/lib/sysimage
Patch1002:      dnf5-Use-usr-lib-sysimage-for-the-persistent-state-dir.patch
## Switch default reposdir to /etc/dnf/repos.d
Patch1003:      dnf5-Switch-default-reposdir-to-etc-dnf-repos.d.patch
## Disable Werror to fix bindings builds
Patch1004:      dnf5-disable-Werror.patch

Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
Requires:       dnf-data
Recommends:     bash-completion

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
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(librepo) >= %{librepo_version}
BuildRequires:  pkgconfig(libsolv) >= %{libsolv_version}
BuildRequires:  pkgconfig(libsolvext) >= %{libsolv_version}
BuildRequires:  pkgconfig(rpm) >= 4.17.0
BuildRequires:  pkgconfig(sqlite3) >= %{sqlite_version}
BuildRequires:  pkgconfig(systemd)
BuildRequires:  toml11-devel

%if %{with tests}
BuildRequires:  createrepo_c
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  rpm-build
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
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
%endif

%if %{with html} || %{with man}
#BuildRequires:  python3dist(breathe)
BuildRequires:  python3-breathe
#BuildRequires:  python3dist(sphinx) >= 4.1.2
BuildRequires:  python3-Sphinx >= 4.1.2
#BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-sphinx_rtd_theme
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
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Exception)
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

%files -f dnf5.lang
%{_bindir}/dnf5
%if %{with as_microdnf}
%{_bindir}/microdnf
%endif
%if %{with as_dnf}
%{_bindir}/dnf
%{_mandir}/man?/dnf-*
%endif
%if %{with as_yum}
%{_bindir}/yum
%endif

%dir %{_sysconfdir}/dnf
%dir %{_sysconfdir}/dnf/dnf5-aliases.d
%doc %{_sysconfdir}/dnf/dnf5-aliases.d/README
%dir %{_sysconfdir}/dnf/dnf5-plugins
%dir %{_datadir}/dnf5
%dir %{_datadir}/dnf5/aliases.d
%config %{_datadir}/dnf5/aliases.d/compatibility.conf
%dir %{_datadir}/dnf5/dnf5-plugins
%dir %{_libdir}/dnf5
%dir %{_libdir}/dnf5/plugins
%doc %{_libdir}/dnf5/plugins/README
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/dnf5
%if %{with as_dnf}
%{_datadir}/bash-completion/completions/dnf
%endif
%dir %{_prefix}/lib/sysimage/dnf
%verify(not md5 size mtime) %ghost %{_prefix}/lib/sysimage/dnf/*
%license COPYING.md
%license gpl-2.0.txt
%{_mandir}/man8/dnf5.8.*
%{_mandir}/man8/dnf5-advisory.8.*
%{_mandir}/man8/dnf5-autoremove.8.*
%{_mandir}/man8/dnf5-check.8.*
%{_mandir}/man8/dnf5-check-upgrade.8.*
%{_mandir}/man8/dnf5-clean.8.*
%{_mandir}/man8/dnf5-distro-sync.8.*
%{_mandir}/man8/dnf5-downgrade.8.*
%{_mandir}/man8/dnf5-download.8.*
%{_mandir}/man8/dnf5-environment.8.*
%{_mandir}/man8/dnf5-group.8.*
# TODO(jkolarik): history is not ready yet
# %%{_mandir}/man8/dnf5-history.8.*
%{_mandir}/man8/dnf5-info.8.*
%{_mandir}/man8/dnf5-install.8.*
%{_mandir}/man8/dnf5-leaves.8.*
%{_mandir}/man8/dnf5-list.8.*
%{_mandir}/man8/dnf5-makecache.8.*
%{_mandir}/man8/dnf5-mark.8.*
%{_mandir}/man8/dnf5-module.8.*
%{_mandir}/man8/dnf5-offline.8.*
%{_mandir}/man8/dnf5-provides.8.*
%{_mandir}/man8/dnf5-reinstall.8.*
%{_mandir}/man8/dnf5-remove.8.*
%{_mandir}/man8/dnf5-repo.8.*
%{_mandir}/man8/dnf5-repoquery.8.*
%{_mandir}/man8/dnf5-search.8.*
%{_mandir}/man8/dnf5-swap.8.*
%{_mandir}/man8/dnf5-system-upgrade.8.*
%{_mandir}/man8/dnf5-upgrade.8.*
%{_mandir}/man8/dnf5-versionlock.8.*
%{_mandir}/man7/dnf5-aliases.7.*
%{_mandir}/man7/dnf5-caching.7.*
%{_mandir}/man7/dnf5-comps.7.*
# TODO(jkolarik): filtering is not ready yet
# %%{_mandir}/man7/dnf5-filtering.7.*
%{_mandir}/man7/dnf5-forcearch.7.*
%{_mandir}/man7/dnf5-installroot.7.*
# TODO(jkolarik): modularity is not ready yet
# %%{_mandir}/man7/dnf5-modularity.7.*
%{_mandir}/man7/dnf5-specs.7.*
%{_mandir}/man5/dnf5.conf.5.*
%{_mandir}/man5/dnf5.conf-todo.5.*
%{_mandir}/man5/dnf5.conf-deprecated.5.*

%{_unitdir}/dnf5-offline-transaction.service
%{_unitdir}/dnf5-offline-transaction-cleanup.service
%dir %{_unitdir}/system-update.target.wants
%{_unitdir}/system-update.target.wants/dnf5-offline-transaction.service

# ========== libdnf5 ==========
%package -n %{libname}
Summary:        Package management library
License:        LGPL-2.1-or-later
Requires:       libmodulemd2%{?_isa} >= %{libmodulemd_version}
#Requires:       libsolv%{?_isa} >= %{libsolv_version}
Requires:       librepo0%{?_isa} >= %{librepo_version}
Requires:       libsqlite3-0%{?_isa} >= %{sqlite_version}

%description -n %{libname}
Package management library.

%ldconfig_scriptlets -n %{libname}

%files -n %{libname} -f libdnf5.lang
%dir %{_libdir}/libdnf5
%{_libdir}/libdnf5.so.%{libsoversion}
%license lgpl-2.1.txt
%{_var}/cache/libdnf5/
%dir %{_datadir}/dnf5/libdnf.conf.d
%dir %{_sysconfdir}/dnf/libdnf5.conf.d
%dir %{_datadir}/dnf5/repos.override.d
%dir %{_sysconfdir}/dnf/repos.override.d
%dir %{_sysconfdir}/dnf/libdnf5-plugins
%dir %{_libdir}/libdnf5/plugins
%dir %{_datadir}/dnf5/repos.d
%dir %{_datadir}/dnf5/vars.d

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
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       %{devname}%{?_isa} = %{version}-%{release}
Requires:       %{devcliname}%{?_isa} = %{version}-%{release}

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
Conflicts:      libdnf-devel < 5

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
%dir %{python3_sitelib}/libdnf_plugins/
%doc %{python3_sitelib}/libdnf_plugins/README
%endif


# ========== dnf5daemon-client ==========

%if %{with dnf5daemon_client}
%package -n dnf5daemon-client
Summary:        Command-line interface for dnf5daemon-server
License:        GPL-2.0-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
Requires:       dnf5daemon-server

%description -n dnf5daemon-client
Command-line interface for dnf5daemon-server.

%files -n dnf5daemon-client -f dnf5daemon-client.lang
%{_bindir}/dnf5daemon-client
%license COPYING.md
%license gpl-2.0.txt
%{_mandir}/man8/dnf5daemon-client.8.*
%endif


# ========== dnf5daemon-server ==========

%if %{with dnf5daemon_server}
%package -n dnf5daemon-server
Summary:        Package management service with a DBus interface
License:        GPL-2.0-or-later
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
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
%{_mandir}/man8/dnf5daemon-server.8.*
%{_mandir}/man8/dnf5daemon-dbus-api.8.*
%endif


# ========== dnf5-plugins ==========

%if %{with dnf5_plugins}
%package -n dnf5-plugins
Summary:        Plugins for dnf5
License:        LGPL-2.1-or-later
Requires:       libcurl4%{?_isa} >= %{libcurl_version}
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       %{libcliname}%{?_isa} = %{version}-%{release}
Provides:       dnf5-command(builddep)
Provides:       dnf5-command(changelog)
Provides:       dnf5-command(config-manager)
Provides:       dnf5-command(copr)
Provides:       dnf5-command(needs-restarting)
Provides:       dnf5-command(repoclosure)

%description -n dnf5-plugins
Core DNF5 plugins that enhance dnf5 with builddep, changelog,
config-manager, copr, and repoclosure commands.

%files -n dnf5-plugins -f dnf5-plugin-builddep.lang -f dnf5-plugin-changelog.lang -f dnf5-plugin-config-manager.lang -f dnf5-plugin-copr.lang -f dnf5-plugin-needs-restarting.lang -f dnf5-plugin-repoclosure.lang
%{_libdir}/dnf5/plugins/builddep_cmd_plugin.so
%{_libdir}/dnf5/plugins/changelog_cmd_plugin.so
%{_libdir}/dnf5/plugins/config-manager_cmd_plugin.so
%{_libdir}/dnf5/plugins/copr_cmd_plugin.so
%{_libdir}/dnf5/plugins/needs_restarting_cmd_plugin.so
%{_libdir}/dnf5/plugins/repoclosure_cmd_plugin.so
%{_mandir}/man8/dnf5-builddep.8.*
%{_mandir}/man8/dnf5-changelog.8.*
%{_mandir}/man8/dnf5-config-manager.8.*
%{_mandir}/man8/dnf5-copr.8.*
%{_mandir}/man8/dnf5-needs-restarting.8.*
%{_mandir}/man8/dnf5-repoclosure.8.*

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
%{_mandir}/man8/dnf5-automatic.8.*
%{_unitdir}/dnf5-automatic.service
%{_unitdir}/dnf5-automatic.timer
%{_unitdir}/dnf-automatic.service
%{_unitdir}/dnf-automatic.timer
%if %{with as_dnf}
%{_bindir}/dnf-automatic
%endif

%endif


# ========== unpack, build, check & install ==========

%prep
%autosetup -S git_am -n dnf5-%{version}


%build
%cmake \
    -DPERL_INSTALLDIRS=vendor \
    \
    -DWITH_SYSTEMD=ON \
    -DWITH_DNF5DAEMON_CLIENT=%{?with_dnf5daemon_client:ON}%{!?with_dnf5daemon_client:OFF} \
    -DWITH_DNF5DAEMON_SERVER=%{?with_dnf5daemon_server:ON}%{!?with_dnf5daemon_server:OFF} \
    -DWITH_LIBDNF5_CLI=%{?with_libdnf_cli:ON}%{!?with_libdnf_cli:OFF} \
    -DWITH_DNF5=%{?with_dnf5:ON}%{!?with_dnf5:OFF} \
    -DWITH_PLUGIN_ACTIONS=%{?with_plugin_actions:ON}%{!?with_plugin_actions:OFF} \
    -DWITH_PYTHON_PLUGINS_LOADER=%{?with_python_plugins_loader:ON}%{!?with_python_plugins_loader:OFF} \
    \
    -DWITH_COMPS=%{?with_comps:ON}%{!?with_comps:OFF} \
    -DWITH_MODULEMD=%{?with_modulemd:ON}%{!?with_modulemd:OFF} \
    -DWITH_ZCHUNK=%{?with_zchunk:ON}%{!?with_zchunk:OFF} \
    \
    -DWITH_STATIC_LIBSOLV=%{?with_static_libsolv:ON}%{!?with_static_libsolv:OFF} \
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
%cmake_build
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
    transaction_history.sqlite-wal userinstalled.toml
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
%find_lang dnf5daemon-client
%find_lang dnf5daemon-server
%find_lang libdnf5
%find_lang libdnf5-cli
%find_lang libdnf5-plugin-actions

# Let's not replace what dnf-data offers just yet..
rm %{buildroot}%{_sysconfdir}/dnf/dnf.conf

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
%else
rm %{buildroot}%{_bindir}/dnf-automatic
%endif
%if %{with as_yum}
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/yum
%endif


%changelog
