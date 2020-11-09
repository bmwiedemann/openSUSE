#
# spec file for package nomacs
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


Name:           nomacs
Version:        3.16.224
Release:        0
Summary:        Lightweight image viewer
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://nomacs.org/
Source:         https://github.com/nomacs/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         quazip1_cmake_remove_after_new_version.diff
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  lcov
BuildRequires:  libqt5-linguist-devel >= 5.2
BuildRequires:  opencv-qt5-devel >= 2.4.6
BuildRequires:  pkgconfig
BuildRequires:  quazip-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2
BuildRequires:  pkgconfig(Qt5Svg) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(exiv2) >= 0.26
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libraw) >= 0.17
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang

%description
nomacs is a free image viewer, which is small, fast and able to handle the
most common image formats. Additionally it is possible to synchronise
multiple viewers. A synchronisation of viewers running on the same
computer or via LAN is possible. It allows to compare images and spot the
differences (e.g. schemes of architects to show the progress).

%lang_package

%prep
%setup -q
%patch0 -p1

%build
pushd ImageLounge/
%cmake \
  -DCMAKE_BUILD_TYPE=Release                           \
  -DCMAKE_C_FLAGS='%{optflags} -fno-strict-aliasing'   \
  -DCMAKE_CXX_FLAGS='%{optflags} -fno-strict-aliasing' \
  -DUSE_SYSTEM_QUAZIP=ON                               \
  -DCMAKE_SHARED_LINKER_FLAGS=""                       \
  -DENABLE_TRANSLATIONS=ON
%make_build
popd

%install
pushd ImageLounge/
%cmake_install
popd

rm %{buildroot}%{_libdir}/lib%{name}*.so
%suse_update_desktop_file org.%{name}.ImageLounge
%find_lang %{name} --with-qt
# find_lang doesn't escape paths, but language paths contain "Image Lounge" with space,
# we'll escape the paths manually
sed -i -E 's|(%{_datadir}.*)$|"\1"|' %{name}.lang
%fdupes %{buildroot}%{_datadir}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/%{name}
%{_libdir}/lib%{name}*.so.*
%{_datadir}/%{name}/
%exclude "%{_datadir}/nomacs/Image Lounge/translations/"
%{_datadir}/applications/org.%{name}.ImageLounge.desktop
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/org.%{name}.ImageLounge.svg
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.%{name}.ImageLounge.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang
%dir "%{_datadir}/nomacs/Image Lounge/translations/"

%changelog
