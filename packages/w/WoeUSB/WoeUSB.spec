#
# spec file for package WoeUSB
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


Name:           WoeUSB
Version:        5.2.4
Release:        0
Summary:        Windows USB installation media creator
License:        GPL-3.0-or-later
URL:            https://github.com/WoeUSB/WoeUSB
Source:         https://github.com/WoeUSB/WoeUSB/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  libtool
Requires:       bash >= 4.3
Requires:       dosfstools
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       grub2
Requires:       ntfsprogs
Requires:       parted
Requires:       util-linux
Requires:       wget
Requires:       wimtools
Recommends:     p7zip
BuildArch:      noarch

%description
WoeUSB is a utility for creating a bootable Windows installation
USB storage device from an existing Windows installation disc or disk image.

%prep
%setup -q
%autosetup
find . -type f -exec sed -i "s/@@WOEUSB_VERSION@@/%{version}/" {} \+
sed -i '1 s/env //' sbin/woeusb

%build

%install
install -Dm 755 sbin/woeusb %{buildroot}%{_sbindir}/woeusb
install -Dm 644 share/man/man1/woeusb.1 %{buildroot}%{_mandir}/man1/woeusb.1
install -Dm 644 share/woeusb/woeusb.svg %{buildroot}%{_datadir}/woeusb/woeusb.svg
%fdupes %{buildroot}

%files
%doc README.md
%license LICENSES/
%{_sbindir}/woeusb
%{_mandir}/man1/woeusb.1%{?ext_man}
%dir %{_datadir}/woeusb
%{_datadir}/woeusb/woeusb.svg

%changelog
