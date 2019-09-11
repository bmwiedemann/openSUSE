#
# spec file for package lshw
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           lshw
Version:        B.02.18+git.20190324
Release:        0
Summary:        HardWare LiSter
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://www.ezix.org/project/wiki/HardwareLiSter
Source:         lshw-%{version}.tar.xz
Source1:        lshw.desktop.in
Source2:        lshw.png
# PATCH-FIX-UPSTREAM lswh-logical-name-iface.patch bsc#1133923
Patch0:         lswh-logical-name-iface.patch
# PATCH-FIX-UPSTREAM lshw-display-latest-version.patch lshw-help-man.patch lshw-modified-time.patch bsc##1130818
Patch1:         lshw-display-latest-version.patch
Patch2:         lshw-help-man.patch
Patch3:         lshw-modified-time.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4
Recommends:     %{name}-lang
Recommends:     hwdata
%lang_package

%description
lshw (Hardware Lister) is a small tool to provide detailed informaton on the
hardware configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version and
speed, cache config uration, bus speed, etc. on DMI-capable x86 systems and
on some PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

For detailed information on lshw features and usage, please see the
included documentation or go to the lshw Web page,
http://www.ezix.org/software/lshw.html

%package gui
Summary:        HardWare LiSter (GUI Frontend)
Group:          Hardware/Other
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

%description gui
lshw (Hardware Lister) is a small tool to provide detailed informaton on the
hardware configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version and
speed, cache config uration, bus speed, etc. on DMI-capable x86 systems and
on some PowerPC machines (PowerMac G4 is known to work).

This package provides a graphical user interface to display hardware
information.

For detailed information on lshw features and usage, please see the
included documentation or go to the lshw Web page,
http://www.ezix.org/software/lshw.html

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make \
  SBINDIR="%{_sbindir}" \
  RPM_OPT_FLAGS="%{optflags} -fno-strict-aliasing" \
  STRIP=touch \
  VERSION="%{version}" \
  all gui

%install
%make_install install-gui

install -d "%{buildroot}%{_datadir}/applications"
sed 's,@@EXEC@@,%{_sbindir}/gtk-lshw,g' < "%{SOURCE1}" \
    > "%{buildroot}%{_datadir}/applications/%{name}.desktop"
chmod 0644 "%{buildroot}%{_datadir}/applications/%{name}.desktop"
install -D -p -m 0644 %{SOURCE2} \
  %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file -r "%{name}" System HardwareSettings
# All of following are shipped by other packages as well
rm -f %{buildroot}%{_datadir}/%{name}/pci.ids
rm -f %{buildroot}%{_datadir}/%{name}/usb.ids
rm -f %{buildroot}%{_datadir}/%{name}/pnp.ids
rm -f %{buildroot}%{_datadir}/%{name}/oui.txt
rm -f %{buildroot}%{_datadir}/%{name}/manuf.txt
rm -f %{buildroot}%{_datadir}/%{name}/pnpid.txt

%find_lang lshw

%files
%defattr(-,root,root,0755)
%license COPYING
%doc README.md docs/TODO docs/Changelog docs/lshw.xsd
%attr(0755,root,root) %{_sbindir}/lshw
%dir %{_datadir}/lshw
%{_mandir}/man1/lshw.1%{ext_man}

%files lang -f %{name}.lang
%defattr(-,root,root)

%files gui
%defattr(-,root,root,0755)
%license COPYING
%attr(0755,root,root) %{_sbindir}/gtk-lshw
%{_datadir}/lshw/artwork
%{_datadir}/lshw/ui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
