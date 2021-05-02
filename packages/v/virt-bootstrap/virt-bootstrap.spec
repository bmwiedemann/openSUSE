#
# spec file for package virt-bootstrap
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python3-%{**}}
%if 0%{suse_version} >= 1550
# python-libguestfs is python3 only
%define pythons python3
%endif
Name:           virt-bootstrap
Version:        1.1.1
Release:        0
Summary:        System container rootfs creation tool
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://github.com/virt-manager/virt-bootstrap
Source:         http://virt-manager.org/download/sources/virt-bootstrap/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module libguestfs}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-libguestfs
Requires:       python-passlib
Requires:       skopeo
Requires:       virt-sandbox
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
ExclusiveArch:  x86_64 ppc64 ppc64le s390x aarch64 powerpc64le
%python_subpackages

%description
Provides a way to create the root file system to use for
libvirt containers.

%prep
%setup -q
sed -i '1 {/env python/ d}' src/virtBootstrap/virt_bootstrap.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/virt-bootstrap
%python_clone -a %{buildroot}%{_mandir}/man1/virt-bootstrap.1
%fdupes %{buildroot}%{_prefix}

%check
%pyunittest -v

%post
%python_install_alternative virt-bootstrap virt-bootstrap.1

%postun
%python_uninstall_alternative virt-bootstrap virt-bootstrap.1

%files %{python_files}
%license LICENSE
%doc README.md ChangeLog AUTHORS
%python_alternative %{_bindir}/virt-bootstrap
%{python_sitelib}/virtBootstrap
%{python_sitelib}/virt_bootstrap-*.egg-info
%python_alternative %{_mandir}/man1/virt-bootstrap.1%{ext_man}

%changelog
