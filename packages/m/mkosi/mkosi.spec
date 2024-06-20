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
Version:        23.1
Release:        0
Summary:        Build bespoke OS Images
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://github.com/systemd/mkosi
Source:         https://github.com/systemd/mkosi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  pandoc
BuildRequires:  python-rpm-macros
Requires:       bubblewrap
Requires:       python3 >= 3.9
Requires:       zypper
Recommends:     btrfsprogs
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
A fancy wrapper around "dnf --installroot", "apt", "pacman", and "zypper" that
generates disk images with a number of bells and whistles.

Generated images are tailored to the purpose: GPT partitions,
systemd-boot or grub2, images for containers, VMs, initrd, and extensions.

mkosi can boot an image via QEMU or systemd-nspawn, or simply start a shell in
chroot, burn the image to a device, connect to a running VM via ssh, extract
logs and coredumps, and also serve an image over HTTP.

See https://mkosi.systemd.io/ for documentation.

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
