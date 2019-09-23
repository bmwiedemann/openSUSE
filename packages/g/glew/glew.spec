#
# spec file for package glew
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


# If you change so_ver, then you have to update baselibs.conf as well.
%define so_ver 2_1
Name:           glew
Version:        2.1.0
Release:        0
Summary:        OpenGL Extension Wrangler Library
License:        BSD-3-Clause AND GPL-2.0 AND MIT
Group:          Development/Libraries/C and C++
Url:            http://glew.sourceforge.net/
Source0:        https://github.com/nigels-com/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tgz
Source1:        baselibs.conf
Source2:        %{name}.rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%package -n libGLEW%{so_ver}
Summary:        OpenGL Extension Wrangler Library
Group:          System/Libraries

%description -n libGLEW%{so_ver}
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%package devel
Summary:        Development files for glew
Group:          Development/Libraries/C and C++
Requires:       libGLEW%{so_ver} = %{version}
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)
# Don't require GLU, because there is GLEW_NO_GLU option
Recommends:     pkgconfig(glu)

%description devel
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%prep
%setup -q

%build
make %{?_smp_mflags} POPT="%{optflags}" GLEW_DEST=%{_prefix} LIBDIR=%{_libdir} LDFLAGS.EXTRA= STRIP=

%install
make DESTDIR=%{buildroot} GLEW_DEST=%{_prefix} LIBDIR=%{_libdir} PKGDIR=%{_libdir}/pkgconfig install.all
chmod +x %{buildroot}%{_libdir}/*.so.*
rm %{buildroot}%{_libdir}/*.a

%post -n libGLEW%{so_ver} -p /sbin/ldconfig
%postun -n libGLEW%{so_ver} -p /sbin/ldconfig

%files
%doc doc/*
%{_bindir}/*info

%files -n libGLEW%{so_ver}
%{_libdir}/*.so.*

%files devel
%{_includedir}/GL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/glew.pc

%changelog
