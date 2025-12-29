#
# spec file for package nomacs
#
# Copyright (c) 2025 mantarimay
# Copyright (c) 2024 SUSE LLC
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
Version:        3.22.0
Release:        0
Summary:        Lightweight image viewer
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://nomacs.org/
Source0:        https://github.com/nomacs/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
%if 0%{?suse_version} < 1600
BuildRequires:  clang
%else
BuildRequires:  gcc-c++ >= 8
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(QuaZip-Qt6)
BuildRequires:  pkgconfig(exiv2) >= 0.26
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libraw) >= 0.17
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
Requires:       kf6-kimageformats
Recommends:     %{name}-lang
Recommends:     %{name}-plugins

%description
nomacs is a free image viewer, which is small, fast and able to handle the
most common image formats. Additionally it is possible to synchronise
multiple viewers. A synchronisation of viewers running on the same
computer or via LAN is possible. It allows to compare images and spot the
differences (e.g. schemes of architects to show the progress).

%package plugins	
Summary:        Plugins for nomacs image viewer
Requires:       %{name} = %{version}

%description plugins	
Some usefull plugins for nomacs:
- Affine transformations
- RGB image from greyscales
- Fake miniature filter
- Page extractions
- Painting

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
%endif
pushd ImageLounge/
%cmake \
  -DCMAKE_BUILD_TYPE=Release                           \
  -DCMAKE_C_FLAGS='%{optflags} -fno-strict-aliasing'   \
  -DCMAKE_CXX_FLAGS='%{optflags} -fno-strict-aliasing' \
  -DQT_VERSION_MAJOR=6                                 \
  -DENABLE_QUAZIP=ON                                   \
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

# fix zero-length
rm %{buildroot}%{_datadir}/nomacs/Image\ Lounge/themes/System.css

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
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

%files plugins
%doc ImageLounge/plugins/README.md
%dir %{_libdir}/nomacs-plugins
%{_libdir}/nomacs-plugins/*.so.*
# should be in devel but unneeded to include in or make new the package
%exclude %{_libdir}/nomacs-plugins/*.so

%files lang -f %{name}.lang
%dir "%{_datadir}/nomacs/Image Lounge/translations/"

%changelog
