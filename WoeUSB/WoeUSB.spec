#
# spec file for package WoeUSB
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.3.0
Release:        0
Summary:        Windows USB installation media creator
License:        GPL-3.0-or-later
Group:          System/Management
Url:            https://github.com/slacka/WoeUSB
Source:         https://github.com/slacka/WoeUSB/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel
Requires:       dosfstools
Requires:       grub2
Requires:       ntfsprogs
Requires:       parted
Requires:       util-linux

%description
WoeUSB is a utility for creating a bootable Windows installation
USB storage device from an existing Windows installation disc or disk image.

%prep
%setup -q
%autosetup

%build
find . -type f -exec sed -i "s/@@WOEUSB_VERSION@@/%{version}/" {} \+
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
sed -i '1!b;s@/usr/bin/env bash@/bin/bash@' %{buildroot}%{_bindir}/woeusb %{buildroot}%{_datadir}/woeusb/data/listDvdDrive %{buildroot}%{_datadir}/woeusb/data/listUsb
rm %{buildroot}%{_datadir}/applications/woeusbgui.desktop
cp src/linux-menu/woeusbgui.desktop .
%suse_update_desktop_file -i -G "WoeUSB" -r woeusbgui System HardwareSettings
%fdupes %buildroot%{_datadir}

%files
%doc ChangeLog README.md README.upstream
%license COPYING
%{_bindir}/woeusb
%{_mandir}/man1/woeusb.1%{?ext_man}
%{_mandir}/man1/woeusbgui.1%{?ext_man}
%{_bindir}/woeusbgui
%{_datadir}/applications/woeusbgui.desktop
%{_datadir}/pixmaps/woeusbgui-icon.png
%dir %{_datadir}/woeusb
%dir %{_datadir}/woeusb/data
%{_datadir}/woeusb/data/c501-logo.png
%{_datadir}/woeusb/data/icon.png
%{_datadir}/woeusb/data/listDvdDrive
%{_datadir}/woeusb/data/listUsb
%{_datadir}/woeusb/data/woeusb-logo.png
%dir %{_datadir}/woeusb/locale
%dir %{_datadir}/woeusb/locale/fr
%dir %{_datadir}/woeusb/locale/fr/LC_MESSAGES
%dir %{_datadir}/woeusb/locale/zh_TW
%dir %{_datadir}/woeusb/locale/zh_TW/LC_MESSAGES
%lang(fr) %{_datadir}/woeusb/locale/fr/LC_MESSAGES/woeusb.mo
%lang(fr) %{_datadir}/woeusb/locale/fr/LC_MESSAGES/wxstd.mo
%lang(zh) %{_datadir}/woeusb/locale/zh_TW/LC_MESSAGES/woeusb.mo

%changelog
