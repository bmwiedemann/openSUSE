#
# spec file for package chck
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           chck
Version:        0.0.20161208
Release:        0
Summary:        C utilities collection library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/Cloudef/chck
Source:         %name-%version.tar.xz
BuildRequires:  cmake >= 3.1
BuildRequires:  pkg-config

%description
Collection of C utilities taken and cleaned up from my other projects.

%package -n libchck0
Summary:        C utilities collection library itself
Group:          System/Libraries

%description -n libchck0
C utilities collection library itself.

%package devel
Summary:        Development files for chck
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       libchck0 = %version

%description devel
Development files for Wayland Compositor Library.

%prep
%setup -q

%build
%cmake

make %{?_smp_mflags}

%install
%cmake_install

%post   -n libchck0 -p /sbin/ldconfig
%postun -n libchck0 -p /sbin/ldconfig

%files -n libchck0
%doc LICENSE README.md
%defattr(-,root,root)
%_libdir/libchck*.so.*

%files devel
%defattr(-,root,root)
%_libdir/libchck*.so
%_includedir/chck/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
