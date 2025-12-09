#
# spec file for package dabstar
#
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


Name:           dabstar
Version:        4.5.0
Release:        0
Summary:        A DAB receiver with a technical focus
License:        GPL-2.0-only
URL:            https://github.com/tomneda/DABstar
Source:         https://github.com/tomneda/DABstar/archive/refs/tags/V%{version}.tar.gz#/DABstar-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libfdk-aac-devel
BuildRequires:  pkgconfig
BuildRequires:  qwt6-qt6-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(sndfile)

%description
A DAB receiver with a technical focus.

%prep
%autosetup -p1 -n DABstar-%{version}

%build
%cmake \
  -DRTLSDR_LINUX=ON \
  -DRTL_TCP=ON
%make_jobs

%install
install -Dpm 0755 build/dabstar %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 appimage_creator/dabstar.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 res/logo/dabstar.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files
%license COPYING LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
