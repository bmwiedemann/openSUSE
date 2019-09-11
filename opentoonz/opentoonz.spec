#
# spec file for package opentoonz
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


%global __requires_exclude ^(libcolorfx|libimage|libsound|libtif).*
%global __provides_exclude ^(libcolorfx|libimage|libsound|libtif).*
Name:           opentoonz
Version:        1.1.2
Release:        0
Summary:        2D animation software
# need to review license as site indicates: "modified BSD license"
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
Url:            https://opentoonz.github.io/e/
Source0:        %{name}-v%{version}.tar.xz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}-rpmlintrc
Patch1:         p_handle-no-return-in-nonvoid-function.patch
Patch2:         p_add-zlo-to-cmake-include-path-suffixes.patch
Patch10:        https://github.com/opentoonz/opentoonz/commit/fb7729aaaf5c36f059c389b103126c2b039280b6.patch
Patch11:        https://github.com/opentoonz/opentoonz/commit/3ebaf33693caa2d9faf3cfad864f84c638e2cabe.patch
BuildRequires:  boost-devel >= 1.55
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5OpenGL-devel
BuildRequires:  libSDL2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng16-compat-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel >= 5.5
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  libqt5-qtscript-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libusb-devel
BuildRequires:  lzo-devel
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig
BuildRequires:  superlu-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(liblz4)
# freetype2-devel
BuildRequires:  pkgconfig(freetype2)
# needed to setup startup script paths
BuildRequires:  sed
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  i586 x86_64

%description
2D animation software previously known as Toonz.

%prep
%setup -q -n %{name}-v%{version}
%patch1 -p1
%patch2 -p1
%patch10 -p1
%patch11 -p1

# Remove all thirdparty except tiff which is patched.
find thirdparty/* -maxdepth 0 ! -name "tiff-*" ! -name "lzo" -type d -exec rm -r "{}" \;
# Keep thirdparty/lzo/driver, but remove library.
rm -r thirdparty/lzo/2.*

%build
# TODO upstream planning to replace custom thirdparty libs with system versions
cd thirdparty/tiff-*
export CFLAGS="%optflags -fPIC"
%configure
%make_build
cd -

cd toonz
%define __sourcedir sources
%cmake \
  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--no-as-needed" \
  -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--no-as-needed" \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--no-as-needed"

%make_jobs

%install
cd toonz
%cmake_install

# fix lib dir since install puts 64bit libs in /usr/lib/
%ifarch x86_64
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}/usr/lib/%{name}/* %{buildroot}%{_libdir}/%{name}
rm -r %{buildroot}/usr/lib/%{name}

# fix launch script that references lib/ instead of lib64/.
sed -i 's|/lib/|/lib64/|' %{buildroot}%{_bindir}/%{name}
%endif

# install desktop file and icon
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/OpenToonz_*
%{_bindir}/tcleanup
%{_bindir}/tcomposer
%{_bindir}/tconverter
%{_bindir}/tfarmcontroller
%{_bindir}/tfarmserver
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}

%changelog
