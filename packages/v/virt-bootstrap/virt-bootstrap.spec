#
# spec file for package virt-bootstrap
#
# Copyright (c) 2023 SUSE LLC
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
# python-libguestfs is python3 only
%define pythons python3
Name:           virt-bootstrap
Version:        1.1.1
Release:        0
Summary:        System container rootfs creation tool
License:        GPL-3.0-or-later
URL:            https://github.com/virt-manager/virt-bootstrap
Source:         http://virt-manager.org/download/sources/virt-bootstrap/%{name}-%{version}.tar.gz
Patch0:         7704260f28c111b141e96e4e717a9522b23bc816.patch
Patch1:         c8ce262cf346535713d45b4660cfdc02c99cfd4c.patch
Patch2:         e30315182c5d95e6f5c14b4b743504434f966edd.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module libguestfs}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python3-libguestfs
Requires:       python3-passlib
Requires:       skopeo
Requires:       virt-sandbox
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
ExclusiveArch:  x86_64 ppc64 ppc64le s390x aarch64 powerpc64 powerpc64le
%python_subpackages

%description
Provides a way to create the root file system to use for
libvirt containers.

%prep
%autosetup -p1

%build
sed -i '1 {/env python/ d}' src/virtBootstrap/virt_bootstrap.py
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
