#
# spec file for package virt-firmware
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define pythons python3

Name:           virt-firmware
Version:        25.12
Release:        0
Summary:        Tools for virtual machine firmware volumes
License:        GPL-2.0-only
URL:            https://gitlab.com/kraxel/virt-firmware
Source:         https://gitlab.com/kraxel/virt-firmware/-/archive/v%{version}/virt-firmware-v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pefile}
# /SECTION
BuildRequires:  fdupes
Requires:       python3-cryptography
Requires:       python3-pefile
Requires:       python3-setuptools
BuildArch:      noarch
%python_subpackages

%description
Tools for virtual machine firmware volumes.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m0644 man/*.1 %{buildroot}%{_mandir}/man1/

%check
# Fake systemd-detect-virt to avoid a BuildRequires on systemd.
echo "#!/bin/true" | install -D -m 0755 /dev/stdin tmpbin/systemd-detect-virt
export PATH="%{buildroot}%{_bindir}:$PATH:$PWD/tmpbin" PYTHONPATH="%{buildroot}%{python_sitelib}" PYTHONDONTWRITEBYTECODE=1
virt-fw-vars --help
# The other tests are Fedora-specific and not that useful.
make test-unittest

%files
%doc README.md
%license LICENSE
%{_bindir}/host-efi-vars
%{_bindir}/virt-fw-vars
%{_bindir}/virt-fw-dump
%{_bindir}/virt-fw-sigdb
%{_bindir}/virt-fw-measure
%{_bindir}/migrate-vars
%{_bindir}/kernel-bootcfg
%{_bindir}/uefi-boot-menu
%{_bindir}/pe-dumpinfo
%{_bindir}/pe-listsigs
%{_bindir}/pe-inspect
%{_bindir}/pe-addsigs
%{_bindir}/uki-addons
%dir %{python_sitelib}/virt/
%{python_sitelib}/virt/firmware/
%{python_sitelib}/virt/peutils/
%{python_sitelib}/virt_firmware-%{version}.dist-info/
%{_mandir}/man1/*.1%{?ext_man}

%changelog
