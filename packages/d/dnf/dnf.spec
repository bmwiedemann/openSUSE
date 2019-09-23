#
# spec file for package dnf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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


%global hawkey_version 0.33.0
%global libcomps_version 0.1.8
%global rpm_version 4.14.0
%global min_plugins_core 4.0.6
%global min_plugins_extras 4.0.4

%global confdir %{_sysconfdir}/%{name}

%global pluginconfpath %{confdir}/plugins

%global py3pluginpath %{python3_sitelib}/dnf-plugins

# Tests fail (possibly due to failures in libdnf tests on SUSE)
# Until those are resolved, these will remain disabled
%bcond_with tests

Name:           dnf
Version:        4.2.6
Release:        0
Summary:        Package manager forked from Yum, using libsolv as a dependency resolver
# For a breakdown of the licensing, see PACKAGE-LICENSING
License:        GPL-2.0-or-later AND GPL-2.0-only
Group:          System/Packages
Url:            https://github.com/rpm-software-management/dnf
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  python3-Sphinx
BuildRequires:  python3-bugzilla
BuildRequires:  systemd-rpm-macros
Requires:       python3-dnf = %{version}-%{release}
Recommends:     %{name}-lang >= %{version}
Recommends:     dnf-plugins-core
Recommends:     dnf-yum
Conflicts:      dnf-plugins-core < %{min_plugins_core}
Provides:       dnf-command(autoremove)
Provides:       dnf-command(check-update)
Provides:       dnf-command(clean)
Provides:       dnf-command(distro-sync)
Provides:       dnf-command(downgrade)
Provides:       dnf-command(group)
Provides:       dnf-command(history)
Provides:       dnf-command(info)
Provides:       dnf-command(install)
Provides:       dnf-command(list)
Provides:       dnf-command(makecache)
Provides:       dnf-command(mark)
Provides:       dnf-command(provides)
Provides:       dnf-command(reinstall)
Provides:       dnf-command(remove)
Provides:       dnf-command(repolist)
Provides:       dnf-command(repoquery)
Provides:       dnf-command(repository-packages)
Provides:       dnf-command(search)
Provides:       dnf-command(updateinfo)
Provides:       dnf-command(upgrade)
Provides:       dnf-command(upgrade-to)
BuildArch:      noarch
%{?systemd_requires}

%description
DNF is an package manager for RPM systems that was forked from Yum. Among the
many improvements, it uses libsolv as a dependency resolver.

%package conf
Summary:        Configuration files for DNF
Group:          System/Packages
Recommends:     logrotate

%description conf
This package provides the configuration files for DNF.

%package yum
Summary:        As a Yum CLI compatibility layer, supplies %{_bindir}/yum redirecting to DNF
Group:          System/Packages
Requires:       dnf = %{version}-%{release}
Conflicts:      yum

%description yum
As a Yum CLI compatibility layer, it supplies %{_bindir}/yum redirecting to DNF.

%package -n python3-dnf
Summary:        Python 3 interface to DNF
Group:          System/Packages
BuildRequires:  python3-curses
BuildRequires:  python3-devel
BuildRequires:  python3-gpg
BuildRequires:  python3-hawkey >= %{hawkey_version}
BuildRequires:  python3-libcomps >= %{libcomps_version}
BuildRequires:  python3-nose
BuildRequires:  python3-rpm >= %{rpm_version}
Recommends:     (python3-dbus-python if NetworkManager)
Requires:       deltarpm
Requires:       dnf-conf = %{version}-%{release}
Requires:       python3-curses
Requires:       python3-gpg
Requires:       python3-hawkey >= %{hawkey_version}
Requires:       python3-libcomps >= %{libcomps_version}
Requires:       python3-rpm >= %{rpm_version}
Recommends:     bash-completion
# DNF 2.0 doesn't work with old plugins
Conflicts:      python3-dnf-plugins-core < %{min_plugins_core}
Conflicts:      python3-dnf-plugins-extras-common < %{min_plugins_extras}
# Python 2 subpackage is no longer provided
Obsoletes:      python2-dnf < 4.0.10

%description -n python3-dnf
This package provides the Python 3 interface to DNF.

%lang_package

%package automatic
Summary:        Alternative CLI to "dnf upgrade" suitable for automatic, regular execution
Group:          System/Packages
BuildRequires:  systemd-rpm-macros
Requires:       dnf = %{version}-%{release}
%{?systemd_requires}

%description automatic
Alternative CLI to "dnf upgrade" suitable for automatic, regular execution.

%prep
%autosetup -p1

# Fix sphinx-build run...
sed -e "s/sphinx-build-3/sphinx-build-%{python3_version}/" -i doc/CMakeLists.txt

%build
%cmake -DPYTHON_DESIRED:FILEPATH=%{__python3}
%make_build
make doc-man

%install
pushd ./build
%make_install
popd

%find_lang %{name}

mkdir -p %{buildroot}%{confdir}/repos.d
mkdir -p %{buildroot}%{confdir}/vars
mkdir -p %{buildroot}%{pluginconfpath}
mkdir -p %{buildroot}%{py3pluginpath}
mkdir -p %{buildroot}%{_sharedstatedir}/dnf
mkdir -p %{buildroot}%{_localstatedir}/log
mkdir -p %{buildroot}%{_var}/cache/dnf
touch %{buildroot}%{_localstatedir}/log/%{name}.log

ln -sr %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/dnf
mv %{buildroot}%{_bindir}/dnf-automatic-3 %{buildroot}%{_bindir}/dnf-automatic
ln -sr %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/yum

# We don't want this just yet...
rm -f %{buildroot}%{confdir}/protected.d/yum.conf

# We don't have ABRT/libreport in openSUSE
rm -rf %{buildroot}%{_sysconfdir}/libreport

%if %{with tests}
%check
pushd ./build
make ARGS="-V" test
popd
%endif

%files
%license COPYING PACKAGE-LICENSING
%doc AUTHORS README.rst
%{_bindir}/dnf
%{_mandir}/man8/dnf.8.*
%{_mandir}/man8/yum2dnf.8.*
%dir %{_var}/cache/dnf
%{_unitdir}/dnf-makecache.service
%{_unitdir}/dnf-makecache.timer

%files lang -f %{name}.lang

%files conf
%license COPYING PACKAGE-LICENSING
%doc AUTHORS README.rst
%dir %{confdir}
%dir %{pluginconfpath}
%dir %{confdir}/aliases.d
%dir %{confdir}/protected.d
%dir %{confdir}/repos.d
%dir %{confdir}/vars
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/aliases.d/zypper.conf
%config(noreplace) %{confdir}/protected.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %{_localstatedir}/log/hawkey.log
%ghost %{_localstatedir}/log/%{name}.log
%ghost %{_localstatedir}/log/%{name}.librepo.log
%ghost %{_localstatedir}/log/%{name}.rpm.log
%ghost %{_localstatedir}/log/%{name}.plugin.log
%dir %{_sharedstatedir}/%{name}
%ghost %{_sharedstatedir}/%{name}/groups.json
%ghost %{_sharedstatedir}/%{name}/yumdb
%ghost %{_sharedstatedir}/%{name}/history
%{_datadir}/bash-completion/completions/dnf
%{_mandir}/man5/dnf.conf.5.*
%{_tmpfilesdir}/dnf.conf

%files yum
%license COPYING PACKAGE-LICENSING
%doc AUTHORS README.rst
%{_bindir}/yum
%{_mandir}/man8/yum.8.*
%{_mandir}/man8/yum-shell.8*
%{_mandir}/man5/yum.conf.5*
%{_mandir}/man1/yum-aliases.1*

%files -n python3-dnf
%license COPYING PACKAGE-LICENSING
%doc AUTHORS README.rst
%{_bindir}/dnf-3
%exclude %{python3_sitelib}/dnf/automatic
%{python3_sitelib}/dnf/
%dir %{py3pluginpath}

%files automatic
%license COPYING PACKAGE-LICENSING
%doc AUTHORS
%{_bindir}/%{name}-automatic
%config(noreplace) %{confdir}/automatic.conf
%{_mandir}/man8/%{name}-automatic.8.*
%{_unitdir}/%{name}-automatic.service
%{_unitdir}/%{name}-automatic.timer
%{_unitdir}/%{name}-automatic-notifyonly.service
%{_unitdir}/%{name}-automatic-notifyonly.timer
%{_unitdir}/%{name}-automatic-download.service
%{_unitdir}/%{name}-automatic-download.timer
%{_unitdir}/%{name}-automatic-install.service
%{_unitdir}/%{name}-automatic-install.timer
%{python3_sitelib}/%{name}/automatic

%post
%systemd_post %{name}-makecache.timer

%preun
%systemd_preun %{name}-makecache.timer

%postun
%systemd_postun_with_restart %{name}-makecache.timer

%post automatic
%systemd_post %{name}-automatic.timer %{name}-automatic-notifyonly.timer %{name}-automatic-download.timer %{name}-automatic-install.timer

%preun automatic
%systemd_preun %{name}-automatic.timer %{name}-automatic-notifyonly.timer %{name}-automatic-download.timer %{name}-automatic-install.timer

%postun automatic
%systemd_postun_with_restart %{name}-automatic.timer %{name}-automatic-notifyonly.timer %{name}-automatic-download.timer %{name}-automatic-install.timer


%changelog
