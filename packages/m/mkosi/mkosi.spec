#
# spec file for package mkosi
#
# Copyright (c) 2024 SUSE LLC
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

Name:           mkosi
Version:        22
Release:        0
Summary:        Build Legacy-Free OS Images
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://github.com/systemd/mkosi
Source:         https://github.com/systemd/mkosi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/systemd/mkosi/pull/2606
Patch0:         opensuse-dont-install-distribution-release-by-default.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  pandoc
BuildRequires:  python-rpm-macros
Requires:       bubblewrap
Requires:       python3 >= 3.9
Requires:       systemd-experimental
Requires:       zypper
Recommends:     btrfsprogs
Recommends:     dnf >= 4.8.0
Recommends:     dosfstools
Recommends:     dpkg
Recommends:     edk2-ovmf
Recommends:     gnupg
Recommends:     squashfs
Recommends:     tar
Recommends:     xz
Recommends:     zstd
BuildArch:      noarch
ExclusiveArch:  x86_64 aarch64

%description
A fancy wrapper around dnf --installroot, debootstrap, pacstrap and zypper that
may generate disk images with a number of bells and whistles.

Generated images are "legacy-free". This means only GPT disk labels
(and no MBR disk labels) are supported, and only systemd based images
may be generated. Moreover, for bootable images only EFI systems are
supported (not plain MBR/BIOS).

%prep
%autosetup -p1

%build
tools/make-man-page.sh
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/mkosi

mkdir -p %{buildroot}%{_mandir}/man1
cp %{buildroot}%{python3_sitelib}/mkosi/resources/mkosi.1* %{buildroot}%{_mandir}/man1/

%check
%pytest

%files
%doc mkosi.md README.md
%license LICENSE
%{_bindir}/mkosi
%{_mandir}/man1/mkosi.1*
%{python3_sitelib}/mkosi
%{python3_sitelib}/mkosi-%{version}.dist-info

%changelog
