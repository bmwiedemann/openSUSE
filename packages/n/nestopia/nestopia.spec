#
# spec file for package nestopia
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2018-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           nestopia
Version:        1.52.0
Release:        0
Summary:        Nintendo Entertainment System/Famicom emulator
License:        GPL-2.0-or-later
Group:          System/Emulators/Other
URL:            https://github.com/0ldsk00l/nestopia
#Git-Clone:     https://github.com/0ldsk00l/nestopia.git
Source:         https://github.com/0ldsk00l/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)

%description
Nestopia is a cycle-accurate NES/Famicom emulator. It has a high compatibility
rate and support for many peripherals and input devices.

%prep
%setup -q
sed -i 's/\r$//' ChangeLog

%build
autoreconf -fiv
%configure \
  --docdir=%{_docdir}/%{name} \
  --enable-gui \
  --enable-doc

make %{?_smp_mflags}

%install
%make_install

%if 0%{?suse_version} < 1330
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%doc ChangeLog readme.html README.md
%license COPYING
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/nespad.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
