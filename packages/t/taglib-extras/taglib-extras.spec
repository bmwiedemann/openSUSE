#
# spec file for package taglib-extras
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


Name:           taglib-extras
Version:        1.0.1
Release:        0
Summary:        Extra plugins for TagLib
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://amarok.kde.org
Source0:        taglib-extras-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM taglib-extras-fix-findtaglib-1_10.patch mlin@suse.com -- fix wrong string comparison of version number
Patch0:         taglib-extras-fix-findtaglib-1_10.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  taglib-devel >= 1.6
Obsoletes:      taglib-extras < %{version}
Provides:       taglib-extras = %{version}

%description
Unofficial TagLib file type plugins maintained by the Amarok project

%package devel
Summary:        Extra plugins for TagLib
Group:          Development/Libraries/C and C++
Requires:       libstdc++-devel
Requires:       libtag-extras1 = %{version}

%description devel
Unofficial TagLib file type plugins maintained by the Amarok project

%package -n libtag-extras1
Summary:        Extra plugins for TagLib
Group:          System/GUI/KDE

%description -n libtag-extras1
Unofficial TagLib file type plugins maintained by the Amarok project

%prep
%setup -q
%patch0 -p1

%build
%cmake ..
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%post -n libtag-extras1 -p /sbin/ldconfig
%postun -n libtag-extras1 -p /sbin/ldconfig

%files -n libtag-extras1
%license COPYING.LGPL
%doc AUTHORS ChangeLog
%{_libdir}/libtag-extras*.so.*

%files -n taglib-extras-devel
%license COPYING.LGPL
%doc AUTHORS ChangeLog
%{_bindir}/taglib-extras-config
%{_includedir}/taglib-extras
%{_libdir}/libtag-extras*.so
%{_libdir}/pkgconfig/*.pc

%changelog
