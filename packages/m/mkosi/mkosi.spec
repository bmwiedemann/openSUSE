#
# spec file for package mkosi
#
# Copyright (c) 2022 SUSE LLC
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


Name:           mkosi
Version:        14
Release:        0
Summary:        Build Legacy-Free OS Images
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://github.com/systemd/mkosi
Source:         https://github.com/systemd/mkosi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(python3) >= 3.7
Requires:       python3 >= 3.7
Requires:       squashfs
Requires:       tar
Requires:       xz
Recommends:     arch-install-scripts
Recommends:     btrfsprogs
Recommends:     debootstrap >= 1.0.117
Recommends:     dnf >= 4.8.0
Recommends:     dosfstools
Recommends:     dpkg
Recommends:     edk2-ovmf
Recommends:     gnupg
Recommends:     pacman >= 6.0.1
Recommends:     veritysetup
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
%setup -q
sed -i '1s/^#!\/usr\/bin\/env /#!\/usr\/bin\//' bin/mkosi

%build
%py3_build

%install
%py3_install

%check
%{buildroot}%{_bindir}/mkosi -h >/dev/null

%files
%doc mkosi.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/mkosi.1%{?ext_man}
%{python3_sitelib}/mkosi/
%{python3_sitelib}/mkosi-%{version}-py*.egg-info/

%changelog
