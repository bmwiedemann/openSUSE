#
# spec file for package unetbootin
#
# Copyright (c) 2020 SUSE LLC
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


%define rev 681
Name:           unetbootin
Version:        0.0.%{rev}
Release:        0
Summary:        Universal Netboot Installer
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://sourceforge.net/projects/unetbootin/
#Source:         %%{name}-source-%%{rev}.tar.gz
Source:         https://downloads.sourceforge.net/project/unetbootin/UNetbootin/%{rev}/unetbootin-source-%{rev}.tar.gz
Patch0:         0001-rought-Qt5-port.patch
Patch1:         0002-comment-out-all-sources-that-require-FTP-LIST.patch
Patch2:         0003-fix-distrolst.cpp.patch
Patch3:         0004-don-t-wait-until-the-file-is-downloaded-fully-before.patch
Patch4:         %{name}-suse.patch
Patch5:         %{name}-locate-usb-devices.diff
Patch6:         %{name}-desktop.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
Requires:       mtools
Requires:       syslinux
Requires:       udev
Requires:       util-linux
Requires:       xdg-utils
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
# Requires syslinux, and that only exists for the following arches:
ExclusiveArch:  %{ix86} x86_64
# Remove when p7zip-full is in all products
%if 0%{?suse_version} >= 1500
Requires:       p7zip-full
%else
Requires:       p7zip
%endif

%description
UNetbootin allows for the installation of various Linux/BSD distributions
to a partition or USB drive, so it's no different from a standard install,
only it doesn't need a CD. It can create a dual-boot install,
or replace the existing OS entirely.

%prep
%setup -q -c -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6
# rpmlint: wrong-file-end-of-line-encoding
sed -i 's/\r$//' README.TXT

%build
lupdate-qt5 unetbootin.pro
lrelease-qt5 unetbootin.pro
%qmake5 "DEFINES += NOSTATIC" "RESOURCES -= unetbootin.qrc"
%make_build

%install
install -D -m 0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -D -m 0644 unetbootin_*.qm %{buildroot}%{_datadir}/%{name}

for i in 16 22 24 32 48 64 128 192 256 ; do
  install -D -m 0644 unetbootin_"$i".png %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps/%{name}.png;
done

install -D -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%doc README.TXT
%{_sbindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
