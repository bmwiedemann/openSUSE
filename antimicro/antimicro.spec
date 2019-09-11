#
# spec file for package antimicro
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


Name:           antimicro
Version:        2.23
Release:        0
Summary:        Graphical program used to map keyboard keys and mouse controls to a game-pad
License:        GPL-3.0-or-later
Group:          Hardware/Joystick
URL:            https://github.com/AntiMicro/%{name}
Source0:        %{name}-%{version}.tar.gz
Patch0:         remove_datetime_aboutdialog.patch
Patch1:         remove_qt5_wrap_cpp.patch
Patch2:         rpmlint.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  libqt5-qttools-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

%description
AntiMicro is a graphical program that can be used to map keyboard
keys and mouse controls to a game-pad. This functionality is useful
for playing games with no built-in or poor game-pad support.

%prep
%setup -q
%autopatch -p1

%build
%cmake -LA
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt
%fdupes %{buildroot}%{_datadir}
%suse_update_desktop_file -r %{name} System HardwareSettings
mv gpl.txt LICENSE

%post
%desktop_database_post
%mime_database_post

%postun
%desktop_database_postun
%mime_database_postun

%files
%defattr(0644,root,root,-)
%license LICENSE
%doc Changelog README.md
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
