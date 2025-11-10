#
# spec file for package python-virtualbmc
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global pythons %{primary_python}
Name:           python-virtualbmc
Version:        3.2.0
Release:        0
Summary:        Python module to create virtual BMCs for controlling virtual instances via IPMI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/virtualbmc
Source0:        https://files.pythonhosted.org/packages/source/v/virtualbmc/virtualbmc-%{version}.tar.gz
Source1:        virtualbmc.service
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  openstack-macros
BuildRequires:  systemd-rpm-macros
Requires:       python-cliff
Requires:       python-libvirt-python
Requires:       python-pyghmi
Requires:       python-pyzmq
BuildArch:      noarch
%{?systemd_requires}
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-virtualbmc < %{version}
%endif
%python_subpackages

%description
A virtual BMC for controlling virtual machines using IPMI commands.

%prep
%autosetup -p1 -n virtualbmc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# directories
install -d -m 755 %{buildroot}%{_datadir}/virtualbmc
install -d -m 755 %{buildroot}%{_sharedstatedir}/virtualbmc
install -d -m 750 %{buildroot}%{_localstatedir}/lib/virtualbmc

# systemd
install -p -D -m 444 %{SOURCE1} %{buildroot}%{_unitdir}/virtualbmc.service

%pre
%service_add_pre virtualbmc.service

%post
%service_add_post virtualbmc.service

%preun
%service_del_preun virtualbmc.service

%postun
%service_del_postun virtualbmc.service

%files %{python_files}
%license LICENSE
%{python_sitelib}/virtualbmc
%{python_sitelib}/virtualbmc-%{version}.dist-info
%{_bindir}/vbmc
%{_bindir}/vbmcd
%{_unitdir}/virtualbmc.service

%changelog
