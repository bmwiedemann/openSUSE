#
# spec file for package python-virtualbmc
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-virtualbmc
Version:        1.4.0
Release:        0
Summary:        Python module to create virtual BMCs for controlling virtual instances via IPMI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/v/virtualbmc/virtualbmc-1.4.0.tar.gz
Source1:        virtualbmc.service
BuildRequires:  fdupes
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
Requires:       python-PrettyTable
Requires:       python-libvirt-python >= 3.5.0
Requires:       python-pbr >= 2.0.0
Requires:       python-pyghmi >= 1.0.22
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%else
BuildRequires:  systemd
Requires(post): systemd
Requires(postun): systemd
Requires(preun): systemd
%endif
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
A virtual BMC for controlling virtual machines using IPMI commands.

%prep
%autosetup -p1 -n virtualbmc-1.4.0
%py_req_cleanup
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/vbmc
%python_clone -a %{buildroot}%{_bindir}/vbmcd

# directories
install -d -m 755 %{buildroot}%{_datadir}/virtualbmc
install -d -m 755 %{buildroot}%{_sharedstatedir}/virtualbmc
install -d -m 750 %{buildroot}%{_localstatedir}/lib/virtualbmc

# systemd
install -p -D -m 444 %{SOURCE1} %{buildroot}%{_unitdir}/virtualbmc.service

%post
%python_install_alternative vbmc
%python_install_alternative vbmcd
%systemd_post virtualbmc.service

%postun
%systemd_postun virtualbmc.service
%python_uninstall_alternative vbmc
%python_uninstall_alternative vbmcd

%files %{python_files}
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/vbmc
%python_alternative %{_bindir}/vbmcd
%if 0%{?suse_version}
%python3_only %{_unitdir}/virtualbmc.service
%else
%{_unitdir}/virtualbmc.service
%endif

%changelog
