#
# spec file for package attractmode
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


Name:           attractmode
Version:        2.6.1
Release:        0
Summary:        A graphical frontend for emulators
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://attractmode.org
Source0:        https://github.com/mickelson/attract/archive/v%{version}/attract-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
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
BuildRequires:  pkgconfig(sfml-all) >= 2.0
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
%make_build EXTRA_CFLAGS="%{optflags}" prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

# Install icon and appdata- and .desktop-file
install -Dm644 util/linux/attract-mode.appdata.xml %{buildroot}%{_datadir}/appdata/attract-mode.appdata.xml
install -Dm644 util/linux/attract-mode.png         %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/attract-mode.png
install -Dm644 util/linux/attract-mode.desktop     %{buildroot}%{_datadir}/applications/attract-mode.desktop

# Hardlinks so users can copy it
%fdupes %{buildroot}%{_datadir}/attract

%files
%doc Readme.md
%license License.txt
%{_bindir}/attract
%{_datadir}/attract
%{_datadir}/icons/hicolor/512x512/apps/attract-mode.png
%{_datadir}/applications/attract-mode.desktop
%{_datadir}/appdata/attract-mode.appdata.xml

%changelog
