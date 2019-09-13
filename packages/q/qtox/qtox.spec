#
# spec file for package qtox
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           qtox
Version:        1.16.3
Release:        0
Summary:        Qt based Tox client
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
Url:            https://qtox.github.io/
Source0:        https://github.com/qTox/qTox/releases/download/v%{version}/v%{version}.tar.gz
Source1:        https://github.com/qTox/qTox/releases/download/v%{version}/v%{version}.tar.gz.asc
Source2:        qtox.keyring
# PATCH-FEATURE-UPSTREAM
Patch:          5041.patch
BuildRequires:  c-toxcore-devel
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(xscrnsaver)

%description
qTox is a chat, voice, video, and file transfer IM client using the
encrypted peer-to-peer Tox protocol.

%prep
%setup -q -c -n qTox-%{version}

%patch -p1

# W: file-contains-date-and-time
BUILD_TIME=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{H}:%{M}')
BUILD_DATE=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{b} %{d} %{Y}')
sed -i "s/__TIME__/\"$BUILD_TIME\"/" $(grep -rl '__TIME__')
sed -i "s/__DATE__/\"$BUILD_DATE\"/" $(grep -rl '__DATE__')

%build
CFLAGS="%{optflags} -Wno-error=parentheses"
mkdir build
pushd build
cmake -DCMAKE_C_FLAGS="$CFLAGS" -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags} PREFIX=%{_prefix}
popd

%install
make install -C build PREFIX=%{_prefix} DESTDIR=%buildroot
# remove non-standard dimensions
rm -rf %{buildroot}%{_datadir}/icons/hicolor/14x14
# decompress svgz to svg
cd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
gzip -d < %{name}.svgz > %{name}.svg
rm %{name}.svgz
# fix desktop-file-name
mv %{buildroot}%{_datadir}/applications/io.github.qtox.qTox.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/metainfo
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
