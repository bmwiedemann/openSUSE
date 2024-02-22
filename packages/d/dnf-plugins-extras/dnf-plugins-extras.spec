#
# spec file for package dnf-plugins-extras
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.4.3}
%global dnf_plugins_extra_obsolete 2.0.0

# YUM v3 has been removed from openSUSE Tumbleweed as of 20191119
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%bcond_with as_yum
%else
%bcond_without as_yum
%endif

# openSUSE does not have tracer
%bcond_with tracer
%bcond_without tests

Name:           dnf-plugins-extras
Version:        4.1.2
Release:        0
Summary:        Extras Plugins for DNF
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/rpm-software-management/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Backports from upstream

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python3-pytest
BuildArch:      noarch

%description
This package contains extra community plugins for use
with the DNF package manager.

%package -n python3-%{name}-common
Summary:        Common files for Extras Plugins for DNF
Group:          System/Packages
Requires:       python3-dnf >= %{dnf_lowest_compatible}
Conflicts:      python2-%{name}-common < %{version}-%{release}
Provides:       %{name}-common = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-common-data < %{version}-%{release}
Obsoletes:      python3-%{name}-common < %{version}-%{release}
# Python 2 bindings are no longer available
Obsoletes:      python2-%{name}-common < 4.0.1

%description -n python3-%{name}-common
Common files for Extras Plugins for DNF, Python 3 version.

%package -n python3-dnf-plugin-kickstart
Summary:        Kickstart Plugin for DNF
Group:          System/Packages
BuildRequires:  python3-pykickstart
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-pykickstart
Conflicts:      python2-dnf-plugin-kickstart < %{version}-%{release}
Provides:       %{name}-kickstart = %{version}-%{release}
Provides:       dnf-plugin-kickstart = %{version}-%{release}
Provides:       python3-%{name}-kickstart = %{version}-%{release}
Provides:       dnf-command(kickstart)
Obsoletes:      python3-%{name}-kickstart < %{dnf_plugins_extra_obsolete}
# Python 2 version is no longer available
Obsoletes:      python2-%{name}-kickstart < %{dnf_plugins_extra_obsolete}
Obsoletes:      python2-dnf-plugin-kickstart < 4.0.1

%description -n python3-dnf-plugin-kickstart
Kickstart Plugin for DNF, Python 3 version. Install packages listed in a
Kickstart file.

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
%if %{with as_yum}
# SUSE-specific yum-utils subpackage obsoletion
Obsoletes:      yum-merge-conf < 4.0.0
Provides:       yum-merge-conf = %{version}-%{release}
%endif

%description -n python3-dnf-plugin-rpmconf
RpmConf Plugin for DNF, Python 3 version. Handles .rpmnew, .rpmsave every
transaction.

%package -n python3-dnf-plugin-snapper
Summary:        Snapper Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-dbus-python
Requires:       snapper
Supplements:    (dnf and snapper)
Conflicts:      python2-dnf-plugin-snapper < %{version}-%{release}
Provides:       %{name}-snapper = %{version}-%{release}
Provides:       dnf-plugin-snapper = %{version}-%{release}
Provides:       python3-%{name}-snapper = %{version}-%{release}
Obsoletes:      python3-%{name}-snapper < %{dnf_plugins_extra_obsolete}
# Python 2 version is no longer available
Obsoletes:      python2-%{name}-snapper < %{dnf_plugins_extra_obsolete}
Obsoletes:      python2-dnf-plugin-snapper < 4.0.1

%description -n python3-dnf-plugin-snapper
Snapper Plugin for DNF, Python 3 version. Creates snapshot every transaction.

%if %{with tracer}
%package -n python3-dnf-plugin-tracer
Summary:        Tracer Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-tracer >= 0.6.12
Conflicts:      python2-dnf-plugin-tracer < %{version}-%{release}
Provides:       %{name}-tracer = %{version}-%{release}
Provides:       dnf-plugin-tracer = %{version}-%{release}
Provides:       python3-%{name}-tracer = %{version}-%{release}
Obsoletes:      python3-%{name}-tracer < %{dnf_plugins_extra_obsolete}
# Python 2 version is no longer available
Obsoletes:      python2-%{name}-tracer < %{dnf_plugins_extra_obsolete}
Obsoletes:      python2-dnf-plugin-tracer < 4.0.1

%description -n python3-dnf-plugin-tracer
Tracer Plugin for DNF, Python 3 version. Finds outdated running applications in
your system every transaction.
%endif

%package -n python3-dnf-plugin-torproxy
Summary:        Tor Proxy Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
Requires:       python3-pycurl
Provides:       %{name}-torproxy = %{version}-%{release}
Provides:       dnf-plugin-torproxy = %{version}-%{release}
Provides:       python3-%{name}-torproxy = %{version}-%{release}
Obsoletes:      python3-%{name}-torproxy < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-torproxy
Tor proxy plugin forces DNF to use Tor to download packages. It makes sure that
Tor is working and avoids leaking the hostname by using the proper SOCKS5 interface.

%package -n python3-dnf-plugin-showvars
Summary:        showvars Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name}-common = %{version}-%{release}
Provides:       dnf-plugin-showvars = %{version}-%{release}
Provides:       python3-%{name}-showvars = %{version}-%{release}

%description -n python3-dnf-plugin-showvars
This plugin dumps the current value of any defined DNF variables. For example
$releasever and $basearch.

%prep
%autosetup -n %{name}-%{version}%{?prerel:-%{prerel}} -p1

# Fix sphinx-build run...
sed -e "s/sphinx-build-3/sphinx-build-%{python3_version}/" -i doc/CMakeLists.txt

%build
%cmake -DPYTHON_DESIRED:FILEPATH=%{_bindir}/python3
%make_build
%make_build doc-man

%install
pushd build
  %make_install
popd

%find_lang %{name}

%if ! %{with tracer}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/tracer.*
rm -rf %{buildroot}%{_mandir}/man8/dnf-tracer.*
%endif

%python_compileall
%fdupes %{buildroot}%{python3_sitelib}

%if %{with tests}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitelib}/dnf-plugins/"
pytest-%{python3_version} -v -s tests/
%endif

%files -n python3-%{name}-common -f %{name}.lang
%{python3_sitelib}/dnfpluginsextras/
%license COPYING
%doc AUTHORS README.rst

%files -n python3-dnf-plugin-kickstart
%{python3_sitelib}/dnf-plugins/kickstart.*
%dir %{python3_sitelib}/dnf-plugins/__pycache__
%{python3_sitelib}/dnf-plugins/__pycache__/kickstart.*
%{_mandir}/man8/dnf-kickstart.*

%files -n python3-dnf-plugin-rpmconf
%config(noreplace) %{_sysconfdir}/dnf/plugins/rpmconf.conf
%{python3_sitelib}/dnf-plugins/rpm_conf.*
%dir %{python3_sitelib}/dnf-plugins/__pycache__
%{python3_sitelib}/dnf-plugins/__pycache__/rpm_conf.*
%{_mandir}/man8/dnf-rpmconf.*

%files -n python3-dnf-plugin-snapper
%config(noreplace) %{_sysconfdir}/dnf/plugins/snapper.conf
%{python3_sitelib}/dnf-plugins/snapper.*
%dir %{python3_sitelib}/dnf-plugins/__pycache__
%{python3_sitelib}/dnf-plugins/__pycache__/snapper.*
%{_mandir}/man8/dnf-snapper.*

%if %{with tracer}
%files -n python3-dnf-plugin-tracer
%{python3_sitelib}/dnf-plugins/tracer.*
%dir %{python3_sitelib}/dnf-plugins/__pycache__
%{python3_sitelib}/dnf-plugins/__pycache__/tracer.*
%{_mandir}/man8/dnf-tracer.*
%endif

%files -n python3-dnf-plugin-torproxy
%config(noreplace) %{_sysconfdir}/dnf/plugins/torproxy.conf
%{python3_sitelib}/dnf-plugins/torproxy.*
%dir %{python3_sitelib}/dnf-plugins/__pycache__
%{python3_sitelib}/dnf-plugins/__pycache__/torproxy.*
%{_mandir}/man8/dnf-torproxy.*

%files -n python3-dnf-plugin-showvars
%{python3_sitelib}/dnf-plugins/showvars.*
%dir %{python3_sitelib}/dnf-plugins/__pycache__
%{python3_sitelib}/dnf-plugins/__pycache__/showvars.*
%{_mandir}/man8/dnf-showvars.*

%changelog
