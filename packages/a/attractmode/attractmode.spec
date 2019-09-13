#
# spec file for package attractmode
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           attractmode
Version:        2.5.0
Release:        0
Summary:        A graphical frontend for emulators
License:        GPL-3.0-only
Group:          System/Emulators/Other
Url:            https://attractmode.org
Source0:        https://github.com/mickelson/attract/archive/v%{version}/attract-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg8-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(openal)
%if 0%{?suse_version} <= 1315
BuildRequires:  pkgconfig(sfml-audio)
BuildRequires:  pkgconfig(sfml-graphics)
BuildRequires:  pkgconfig(sfml-system)
%else
BuildRequires:  sfml2-devel
%endif
BuildRequires:  pkgconfig(xcb-xinerama)
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Attract-Mode is a graphical frontend for command line emulators such as MAME,
MESS and Nestopia. It hides the underlying operating system and is intended to
be controlled with a joystick, gamepad or spinner, making it ideal for use
in arcade cabinets.

%prep
%setup -q -n attract-%{version}

%build
make %{?_smp_mflags} EXTRA_CFLAGS="%{optflags}" prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

# Install icon and appdata- and .desktop-file
install -Dm644 util/linux/attract-mode.appdata.xml %{buildroot}%{_datadir}/appdata/attract-mode.appdata.xml
install -Dm644 util/linux/attract-mode.png         %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/attract-mode.png
install -Dm644 util/linux/attract-mode.desktop     %{buildroot}%{_datadir}/applications/attract-mode.desktop

# Hardlinks so users can copy it
%fdupes %{buildroot}%{_datadir}/attract

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc Readme.md
%if ( 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100 ) || ! 0%{?is_opensuse}
# Fix for Leap 42.1 and SLE (TODO: Remove when 42.1 is out of maintenance)
%dir %{_datadir}/appdata
%doc License.txt
%else
%license License.txt
%endif
%{_bindir}/attract
%{_datadir}/attract
%dir /usr/share/icons/hicolor
%dir /usr/share/icons/hicolor/512x512
%dir /usr/share/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/512x512/apps/attract-mode.png
%{_datadir}/applications/attract-mode.desktop
%{_datadir}/appdata/attract-mode.appdata.xml

%changelog
