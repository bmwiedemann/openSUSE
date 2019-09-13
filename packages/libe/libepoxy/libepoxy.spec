#
# spec file for package libepoxy
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libepoxy
%define sonum   0
Version:        1.5.3
Release:        0
Summary:        OpenGL function pointer management library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/anholt/libepoxy
Source0:        https://github.com/anholt/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf

BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)

%description
Epoxy is a library for handling OpenGL function pointer management for you.

It hides the complexity of dlopen(), dlsym(), glXGetProcAddress(),
eglGetProcAddress(), etc. from the app developer, with very little knowledge
needed on their part. They get to read GL specs and write code using undecorated
function names like glCompileShader().

%package -n %{name}%{sonum}
Summary:        OpenGL function pointer management library
Group:          Development/Libraries/C and C++

%description -n %{name}%{sonum}
Epoxy is a library for handling OpenGL function pointer management for you.

It hides the complexity of dlopen(), dlsym(), glXGetProcAddress(),
eglGetProcAddress(), etc. from the app developer, with very little knowledge
needed on their part. They get to read GL specs and write code using undecorated
function names like glCompileShader().

%package devel
Summary:        Development files for libepoxy
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sonum} = %{version}
Requires:       pkgconfig(x11)
Requires:       pkgconfig(egl)
Requires:       glibc-devel

%description devel
Epoxy is a library for handling OpenGL function pointer management for you.

It hides the complexity of dlopen(), dlsym(), glXGetProcAddress(),
eglGetProcAddress(), etc. from the app developer, with very little knowledge
needed on their part. They get to read GL specs and write code using undecorated
function names like glCompileShader().

Development files.

%prep
%autosetup

%build
%meson \
	-D docs=false \
	-D glx=yes \
	-D egl=yes \
	-D x11=true \
	-D tests=false \
	%{nil}
%meson_build

%install
%meson_install

%post   -n %{name}%{sonum} -p /sbin/ldconfig
%postun -n %{name}%{sonum} -p /sbin/ldconfig

%files -n %{name}%{sonum}
%license COPYING
%{_libdir}/libepoxy.so.*

%files devel
%doc README.md
%{_libdir}/libepoxy.so
%{_libdir}/pkgconfig/epoxy.pc
%{_includedir}/epoxy/

%changelog
