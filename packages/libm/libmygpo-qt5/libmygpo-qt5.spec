#
# spec file for package libmygpo-qt5
#
# Copyright (c) 2025 SUSE LLC
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


Name:           libmygpo-qt5
Version:        1.1.0
Release:        0
Summary:        Qt Library that wraps the gpodder.net Web API
License:        LGPL-2.1-or-later
URL:            http://wiki.gpodder.org/wiki/Libmygpo-qt
Source0:        http://stefan.derkits.at/files/libmygpo-qt/libmygpo-qt.%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- fix-build-with-qt-5_11.patch
Patch0:         fix-build-with-qt-5_11.patch
# PATCH-FIX-UPSTREAM
Patch1:         libmygpo-cmake4.patch
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)

%description
libmygpo-qt5 is a Qt Library that wraps the gpodder.net Web API (http://wiki.gpodder.org/wiki/Web_Services/API_2)

v1.0 wraps nearly every Request from the gpodder.net API except:
- Simple API Calls Downloading subscription Lists & Uploading subscription Lists
- Retrieving Subscription Changes (you should use "Retrieving Updates for a given Device" instead)

%package -n libmygpo-qt5-1
Summary:        Qt Library that wraps the gpodder.net Web API

%description -n libmygpo-qt5-1
libmygpo-qt5 is a Qt Library that wraps the gpodder.net Web API (http://wiki.gpodder.org/wiki/Web_Services/API_2)

v1.0 wraps nearly every Request from the gpodder.net API except:
- Simple API Calls Downloading subscription Lists & Uploading subscription Lists
- Retrieving Subscription Changes (you should use "Retrieving Updates for a given Device" instead)

%package devel
Summary:        Qt Library that wraps the gpodder.net Web API
Requires:       libmygpo-qt5-1 = %{version}

%description devel
libmygpo-qt5 is a Qt Library that wraps the gpodder.net Web API (http://wiki.gpodder.org/wiki/Web_Services/API_2)

v1.0 wraps nearly every Request from the gpodder.net API except:
- Simple API Calls Downloading subscription Lists & Uploading subscription Lists
- Retrieving Subscription Changes (you should use "Retrieving Updates for a given Device" instead)

%prep
%autosetup -p1 -n libmygpo-qt.%{version}

%build
%cmake -DMYGPO_BUILD_TESTS=OFF -DINCLUDE_INSTALL_DIR=%{_includedir}/mygpo-qt5/

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libmygpo-qt5-1

%files devel
%license LICENSE
%{_includedir}/mygpo-qt5/
%{_libdir}/cmake/mygpo-qt5/
%{_libdir}/libmygpo-qt5.so
%{_libdir}/pkgconfig/libmygpo-qt5.pc

%files -n libmygpo-qt5-1
%license LICENSE
%{_libdir}/libmygpo-qt5.so.*

%changelog
