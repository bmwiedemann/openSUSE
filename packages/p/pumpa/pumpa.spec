#
# spec file for package pumpa
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pumpa
Version:        0.9.3
Release:        0
Summary:        A pump.io client written in C++/Qt
License:        GPL-3.0+
Group:          System/GUI/Other
Url:            https://pumpa.branchable.com/
Source:         https://sjoberg.fi/software/downloads/%{name}/%{name}-%{version}.tar.xz
Source1:        https://sjoberg.fi/software/downloads/%{name}/%{name}-%{version}.tar.xz.sign
Source2:        %{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtidy-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
Pumpa is a pump.io client written in C++ and Qt.

%prep
%setup -q

%build
%qmake5 \
  QMAKE_CXXFLAGS="%{optflags}" \
  QMAKE_CFLAGS="%{optflags}"   \
  PREFIX=%{_prefix}
make %{?_smp_mflags} V=1

%install
%qmake5_install

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}*

%changelog
