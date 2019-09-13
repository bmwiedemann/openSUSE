#
# spec file for package dnf-plugins-extras
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.1}
%global dnf_plugins_extra_obsolete 2.0.0

# openSUSE does not have pykickstart
%bcond_with pykickstart

# openSUSE does not have tracer
%bcond_with tracer

# Tests are broken on SUSE for now
%bcond_with tests

Name:           dnf-plugins-extras
Version:        4.0.4
Release:        0
Summary:        Extras Plugins for DNF
Group:          System/Packages
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python3-nose
BuildRequires:  python3-Sphinx

%description
This package contains extra community plugins for use
with the DNF package manager.

%package -n python3-%{name}-common
Summary:        Common files for Extras Plugins for DNF
Group:          System/Packages
Requires:       python3-dnf >= %{dnf_lowest_compatible}
Provides:       %{name}-common = %{version}-%{release}
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      python3-%{name}-common < %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
Obsoletes:      %{name}-common-data < %{version}-%{release}
Conflicts:      python2-%{name}-common < %{version}-%{release}
# Python 2 bindings are no longer available
Obsoletes:      python2-%{name}-common < 4.0.1

%description -n python3-%{name}-common
Common files for Extras Plugins for DNF, Python 3 version.

%if %{with pykickstart}
%package -n python3-dnf-plugin-kickstart
Summary:        Kickstart Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
BuildRequires:  python3-pykickstart
Requires:       python3-pykickstart
Provides:       dnf-command(kickstart)
Provides:       %{name}-kickstart = %{version}-%{release}
Provides:       dnf-plugin-kickstart = %{version}-%{release}
Provides:       python3-%{name}-kickstart = %{version}-%{release}
Conflicts:      python2-dnf-plugin-kickstart < %{version}-%{release}
Obsoletes:      python3-%{name}-kickstart < %{dnf_plugins_extra_obsolete}
# Python 2 version is no longer available
Obsoletes:      python2-dnf-plugin-kickstart < 4.0.1
Obsoletes:      python2-%{name}-kickstart < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-kickstart
Kickstart Plugin for DNF, Python 3 version. Install packages listed in a
Kickstart file.
%endif

%package -n python3-dnf-plugin-rpmconf
Summary:        RpmConf Plugin for DNF
Group:          System/Packages
BuildRequires:  python3-rpmconf
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-rpmconf
Provides:       %{name}-rpmconf = %{version}-%{release}
Provides:       dnf-plugin-rpmconf = %{version}-%{release}
Provides:       python3-%{name}-rpmconf = %{version}-%{release}
Obsoletes:      python3-%{name}-rpmconf < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-rpmconf
RpmConf Plugin for DNF, Python 3 version. Handles .rpmnew, .rpmsave every
transaction.

%package -n python3-dnf-plugin-snapper
Summary:        Snapper Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-dbus-python
Requires:       snapper
Provides:       %{name}-snapper = %{version}-%{release}
Provides:       dnf-plugin-snapper = %{version}-%{release}
Provides:       python3-%{name}-snapper = %{version}-%{release}
Conflicts:      python2-dnf-plugin-snapper < %{version}-%{release}
Obsoletes:      python3-%{name}-snapper < %{dnf_plugins_extra_obsolete}
# Python 2 version is no longer available
Obsoletes:      python2-dnf-plugin-snapper < 4.0.1
Obsoletes:      python2-%{name}-snapper < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-snapper
Snapper Plugin for DNF, Python 3 version. Creates snapshot every transaction.

%package -n python3-dnf-plugin-system-upgrade
Summary:        System Upgrade Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-systemd
Requires:       systemd
Provides:       dnf-command(system-upgrade)
Provides:       %{name}-system-upgrade = %{version}-%{release}
Provides:       system-upgrade = %{version}-%{release}
Provides:       dnf-plugin-system-upgrade = %{version}-%{release}
Provides:       python3-%{name}-system-upgrade = %{version}-%{release}
Obsoletes:      python3-%{name}-system-upgrade < %{dnf_plugins_extra_obsolete}
Obsoletes:      fedup < 0.9.4
Obsoletes:      dnf-plugin-system-upgrade < 0.10
Conflicts:      python2-dnf-plugin-system-upgrade < %{version}-%{release}
# Python 2 version is no longer available
Obsoletes:      python2-dnf-plugin-system-upgrade < 4.0.1
Obsoletes:      python2-%{name}-system-upgrade < 4.0.1
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-systemd
%{?systemd_requires}

%description -n python3-dnf-plugin-system-upgrade
System Upgrade Plugin for DNF, Python 3 version. Enables offline system upgrades
using the "dnf system-upgrade" command.

%if %{with tracer}
%package -n python3-dnf-plugin-tracer
Summary:        Tracer Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-tracer >= 0.6.12
Provides:       dnf-plugin-tracer = %{version}-%{release}
Provides:       %{name}-tracer = %{version}-%{release}
Provides:       python3-%{name}-tracer = %{version}-%{release}
Conflicts:      python2-dnf-plugin-tracer < %{version}-%{release}
Obsoletes:      python3-%{name}-tracer < %{dnf_plugins_extra_obsolete}
# Python 2 version is no longer available
Obsoletes:      python2-dnf-plugin-tracer < 4.0.1
Obsoletes:      python2-%{name}-tracer < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-tracer
Tracer Plugin for DNF, Python 3 version. Finds outdated running applications in
your system every transaction.
%endif

%package -n python3-dnf-plugin-torproxy
Summary:        Tor Proxy Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-pycurl
Provides:       dnf-plugin-torproxy = %{version}-%{release}
Provides:       %{name}-torproxy = %{version}-%{release}
Provides:       python3-%{name}-torproxy = %{version}-%{release}
Obsoletes:      python3-%{name}-torproxy < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-torproxy
Tor proxy plugin forces DNF to use Tor to download packages. It makes sure that
Tor is working and avoids leaking the hostname by using the proper SOCKS5 interface.


%prep
%autosetup -n %{name}-%{version}%{?prerel:-%{prerel}} -p1

# Fix sphinx-build run...
sed -e "s/sphinx-build-3/sphinx-build-%{python3_version}/" -i doc/CMakeLists.txt

%build
%cmake -DPYTHON_DESIRED:FILEPATH=%{__python3}
%make_build
make doc-man

%install
pushd build
  %make_install
popd

mkdir -p %{buildroot}%{_unitdir}/system-update.target.wants/
pushd %{buildroot}%{_unitdir}/system-update.target.wants/
  ln -sr ../dnf-system-upgrade.service
popd

%find_lang %{name}

%if ! %{with pykickstart}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/kickstart.*
rm -rf %{buildroot}%{_mandir}/man8/dnf.plugin.kickstart.*
%endif

%if ! %{with tracer}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/tracer.*
rm -rf %{buildroot}%{_mandir}/man8/dnf.plugin.tracer.*
%endif

%if %{with tests}
%check
%if ! %{with pykickstart}
rm -rf tests/test_kickstart.*
%endif

PYTHONPATH="%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitelib}/dnf-plugins/" nosetests-%{python3_version} -s tests/
%endif

%files -n python3-%{name}-common -f %{name}.lang
%{python3_sitelib}/dnfpluginsextras/
%license COPYING
%doc AUTHORS README.rst

%if %{with pykickstart}
%files -n python3-dnf-plugin-kickstart
%{python3_sitelib}/dnf-plugins/kickstart.*
%{_mandir}/man8/dnf.plugin.kickstart.*
%endif

%files -n python3-dnf-plugin-rpmconf
%config(noreplace) %{_sysconfdir}/dnf/plugins/rpmconf.conf
%{python3_sitelib}/dnf-plugins/rpm_conf.*
%{_mandir}/man8/dnf.plugin.rpmconf.*

%files -n python3-dnf-plugin-snapper
%{python3_sitelib}/dnf-plugins/snapper.*
%{_mandir}/man8/dnf.plugin.snapper.*

%files -n python3-dnf-plugin-system-upgrade
%{_unitdir}/dnf-system-upgrade.service
%{_unitdir}/dnf-system-upgrade-cleanup.service
%dir %{_unitdir}/system-update.target.wants
%{_unitdir}/system-update.target.wants/dnf-system-upgrade.service
%{python3_sitelib}/dnf-plugins/system_upgrade.py
%{_mandir}/man8/dnf.plugin.system-upgrade.*

%if %{with tracer}
%files -n python3-dnf-plugin-tracer
%{python3_sitelib}/dnf-plugins/tracer.*
%{_mandir}/man8/dnf.plugin.tracer.*
%endif

%files -n python3-dnf-plugin-torproxy
%config(noreplace) %{_sysconfdir}/dnf/plugins/torproxy.conf
%{python3_sitelib}/dnf-plugins/torproxy.*
%{_mandir}/man8/dnf.plugin.torproxy.*

%changelog

