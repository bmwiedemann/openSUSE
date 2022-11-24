#
# spec file for package deepin-image-editor
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Hillwood Yang <hillwood@opensuse.org>
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

%define    _name    image-editor
%define    sover    0_1

Name:           deepin-image-editor
Version:        1.0.19
Release:        0
Summary:        Libraries of Deepin Image editor
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://github.com/linuxdeepin/image-editor
Source0:        https://github.com/linuxdeepin/image-editor/archive/%{version}/%{_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM recompile-with-fPIC.patch hillwood@opensuse.org - Fix build on 64bit arch
Patch0:         recompile-with-fPIC.patch
%if 0%{?suse_version} <= 1500
# PATCH-FIX-OPENSUSE fix-library-link.patch hillwood@opensuse.org - Neet link dl for Leap 15.x
Patch1:         fix-library-link.patch
%endif
BuildRequires:  deepin-gettext-tools
BuildRequires:  dtkcore >= 5.0.0
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libmediainfo)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libraries of Deepin Image editor

%package -n libimagevisualresult-data
Summary:        Data files for libimagevisualresult
Group:          System/Libraries

%description -n libimagevisualresult-data
The package provides date for Deepin Image editor.

%package -n libimageviewer%{sover}
Summary:        The library of Deepin Image editor
Group:          System/Libraries
Recommends:     %{name}-lang

%description -n libimageviewer%{sover}
This package contains the libraries for Deepin Image editor.

%package -n libimagevisualresult%{sover}
Summary:        The library of Deepin Image editor
Group:          System/Libraries
Requires:       libimagevisualresult-data = %{version}

%description -n libimagevisualresult%{sover}
This package contains the libraries for Deepin Image editor.

%package -n libimageviewer-devel
Summary:        The library of Deepin Image editor
Group:          Development/Libraries/X11
Requires:       libimageviewer%{sover}
Provides:       pkgconfig(libimageviewer) = 0.1.0
AutoReqProv:    Off

%description -n libimageviewer-devel
The libimageviewer-devel package contains the header files and developer docs
for Deepin Image editor.

%package -n libimagevisualresult-devel
Summary:        The library of Deepin Image editor
Group:          Development/Libraries/X11
Requires:       libimagevisualresult%{sover}

%description -n libimagevisualresult-devel
The libimagevisualresult-devel package contains the header files and developer
docs for Deepin Image editor.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%find_lang libimageviewer --with-qt
%fdupes %{buildroot}

%post -n libimageviewer%{sover} -p /sbin/ldconfig
%postun -n libimageviewer%{sover} -p /sbin/ldconfig

%post -n libimagevisualresult%{sover} -p /sbin/ldconfig
%postun -n libimagevisualresult%{sover} -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE

%files -n libimagevisualresult-data
%doc README.md
%license LICENSE
%dir %{_datadir}/libimagevisualresult
%dir %{_datadir}/libimagevisualresult/filter_cube
%{_datadir}/libimagevisualresult/filter_cube/*.CUBE
%{_datadir}/libimagevisualresult/filter_cube/*.dat

%files -n libimageviewer%{sover}
%{_libdir}/libimageviewer.so.*

%files -n libimagevisualresult%{sover}
%{_libdir}/libimagevisualresult.so.*

%files -n libimageviewer-devel
%doc README.md
%license LICENSE
%{_includedir}/libimageviewer
%{_libdir}/libimageviewer.so
%{_libdir}/pkgconfig/libimageviewer.pc

%files -n libimagevisualresult-devel
%doc README.md
%license LICENSE
%{_includedir}/libimagevisualresult
%{_libdir}/libimagevisualresult.so
%{_libdir}/pkgconfig/libimagevisualresult.pc

%files lang -f libimageviewer.lang
%dir %{_datadir}/libimageviewer
%dir %{_datadir}/libimageviewer/translations
%{_datadir}/libimageviewer/translations/libimageviewer.qm

%changelog
