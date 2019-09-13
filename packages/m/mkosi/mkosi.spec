#
# spec file for package mkosi
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mkosi
Version:        4
Release:        0
Summary:        Build Legacy-Free OS Images
License:        LGPL-2.1+
Group:          System/Management
Url:            https://github.com/systemd/mkosi
Source:         https://github.com/systemd/mkosi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-setuptools
Requires:       python3 >= 3.5
Requires:       squashfs
Recommends:     btrfs-progs
Recommends:     dosfstools
Recommends:     edk2-ovmf
Recommends:     gnupg
Recommends:     tar
Recommends:     veritysetup
Recommends:     xz
# To build other distros:
Recommends:     debootstrap >= 1.0.83
Recommends:     dnf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64
BuildArch:      noarch

%description
A fancy wrapper around dnf --installroot, debootstrap, pacstrap and zypper that
may generate disk images with a number of bells and whistles.

Generated images are "legacy-free". This means only GPT disk labels
(and no MBR disk labels) are supported, and only systemd based images
may be generated. Moreover, for bootable images only EFI systems are
supported (not plain MBR/BIOS).

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
%{buildroot}%{_bindir}/mkosi -h

%files
%defattr(-,root,root)
%doc README.md
%if 0%{?leap_version} >= 420200 || 0%{?suse_version} > 1320
%license LICENSE
%else
%doc LICENSE
%endif
%{_bindir}/%{name}
%doc mkosi.default
%{python3_sitelib}/

%changelog
