#
# spec file for package python-ryu
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
Name:           python-ryu
Version:        4.32
Release:        0
Summary:        Component-based Software-defined Networking Framework
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://osrg.github.io/ryu/
Source:         https://pypi.io/packages/source/r/ryu/ryu-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module FormEncode}
BuildRequires:  %{python_module Routes}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module oslo.config}
BuildRequires:  %{python_module ovs}
BuildRequires:  %{python_module tinyrpc}
# /SECTION
Requires:       python-Routes
Requires:       python-WebOb >= 1.2
Requires:       python-eventlet >= 0.18.2
Requires:       python-msgpack >= 0.3.0
Requires:       python-netaddr
Requires:       python-oslo.config >= 1.15.0
Requires:       python-ovs >= 2.6.0
Requires:       python-ryu-common = %{version}
Requires:       python-six >= 1.4.0
Requires:       python-tinyrpc
BuildArch:      noarch

%python_subpackages

%description
Ryu is a component-based software defined networking framework. Ryu
provides software components with an API for creating network
management and control applications. Ryu supports various protocols
for managing network devices, such as OpenFlow, Netconf, OF-config,
etc. About OpenFlow, Ryu fully supports 1.0, 1.2, 1.3, 1.4, 1.5 and
Nicira Extensions.

%package -n python-ryu-common
Summary:        Configuration files for python-ryu, a SDN framework
Group:          Development/Languages/Python
Provides:       %{python_module ryu-common = %{version}}

%description -n python-ryu-common
Ryu is a component-based software defined networking framework. Ryu
provides software components with an API for creating network
management and control applications. Ryu supports various protocols
for managing network devices, such as OpenFlow, Netconf, OF-config,
etc. About OpenFlow, Ryu fully supports 1.0, 1.2, 1.3, 1.4, 1.5 and
Nicira Extensions.

%prep
%setup -q -n ryu-%{version}

%build
%python_build

%install
%python_install
mkdir -p %{buildroot}%{_sysconfdir}
mv %{buildroot}/usr/%{_sysconfdir}/ryu %{buildroot}%{_sysconfdir}/ryu
%python_clone -a %{buildroot}%{_bindir}/ryu
%python_clone -a %{buildroot}%{_bindir}/ryu-manager

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_requirements.py: not applicable, test_controller.py: test_ssl fails
rm ryu/tests/unit/{test_requirements.py,controller/test_controller.py}
%{python_expand PYTHON=$python sh run_tests.sh -N -P}

%post
%{python_install_alternative ryu ryu-manager}

%postun
%python_uninstall_alternative ryu

%files %python_files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/ryu
%python_alternative %{_bindir}/ryu-manager

%files -n python-ryu-common
%dir %{_sysconfdir}/ryu
%config(noreplace) %{_sysconfdir}/ryu/ryu.conf

%changelog
