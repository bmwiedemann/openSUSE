#
# spec file for package python-avocado-plugins-vt
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define pkgname avocado-vt
Name:           python-avocado-plugins-vt
Version:        69.0
Release:        0
Summary:        Avocado Virt Test Plugin
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://avocado-framework.readthedocs.org/
Source0:        https://github.com/avocado-framework/avocado-vt/archive/%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{pkgname}-common
Requires:       attr
Requires:       bridge-utils
# Requires:     autotest-framework
Requires:       gcc
Requires:       git-core
Requires:       glibc-devel
Requires:       iproute
Requires:       iputils
Requires:       make
Requires:       netcat-openbsd
Requires:       openvswitch
Requires:       python-aexpect > 1.5.0
Requires:       python-avocado >= 51.0
Requires:       python-netaddr >= 0.7.18
Requires:       python-netifaces >= 0.10.5
Requires:       python-simplejson >= 3.5.3
Requires:       qemu-kvm
Requires:       systemtap
Requires:       tcpdump
Requires:       xz
Recommends:     libvirt
Recommends:     policycoreutils-python
BuildArch:      noarch
%ifpython2
Requires:       python-devel
%else
Requires:       python3-dbm
Requires:       python3-devel
%endif
%python_subpackages

%description
Avocado Virt Test is a plugin that executes virt-tests with all the avocado
features, such as HTML report and Xunit output, among others.

%package  -n    %{pkgname}-common
Summary:        Avocado Test Framework
Group:          Development/Tools/Other

%description   -n  %{pkgname}-common
Avocado Virt Test is a plugin that executes virt-tests with all the avocado
features, such as HTML report and Xunit output, among others.

This package contains common infrastructure files

%prep
%setup -q -n %{pkgname}-%{version}

%build
%python_build

%install
%python_install

# Reduce duplicities
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes -s %{buildroot}%{_datadir}/avocado-plugins-vt

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/avocado_vt*
%{python_sitelib}/avocado_plugins_vt*
%{python_sitelib}/virttest*

%files -n %{pkgname}-common
%dir %{_sysconfdir}/avocado
%dir %{_sysconfdir}/avocado/conf.d
%config(noreplace)%{_sysconfdir}/avocado/conf.d/vt.conf
%{_datadir}/avocado-plugins-vt
%{_datadir}/avocado-plugins-vt/backends
%{_datadir}/avocado-plugins-vt/shared
%{_datadir}/avocado-plugins-vt/test-providers.d

%changelog
