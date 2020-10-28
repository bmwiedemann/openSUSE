#
# spec file for package goxel
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


Name:           goxel
Version:        0.10.6
Release:        0
Summary:        Voxel graphics editor
License:        GPL-3.0-only
URL:            https://github.com/guillaumechereau/goxel
Source0:        https://github.com/guillaumechereau/goxel/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  scons
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(zlib)

%description
Goxel is an open source voxel graphics editor. Voxels are 3D images formed
of cubic elements.

%prep
%autosetup

%build
# Manually set build flag as Leap 15.2 does not support %%{set_build_flags} macro unlike TW.
CFLAGS='-O2 -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto'
export CFLAGS
CXXFLAGS='-O2 -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto'
export CXXFLAGS
FFLAGS='-O2 -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto '
export FFLAGS
FCFLAGS='-O2 -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto '
export FCFLAGS
LDFLAGS=-flto=auto
export LDFLAGS
scons mode=release

%install
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}

install -d %{buildroot}%{_datadir}/icons/hicolor/{48x48,256x256,1024x1024}/apps
install -m644 icon.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
convert icon.png -resize 48x48 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
convert icon.png -resize 256x256 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

# Install desktop icon
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir /usr/share/icons/hicolor/1024x1024
%dir /usr/share/icons/hicolor/1024x1024/apps
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
