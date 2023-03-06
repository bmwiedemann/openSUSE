#
# spec file for package waffle
#
# Copyright (c) 2023 SUSE LLC
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


%define _majorVersion 1
%define _minorVersion 0
%define libname lib%{name}-%{_majorVersion}-%{_minorVersion}
Name:           waffle
Version:        1.7.2
Release:        0
Summary:        C library defering selection of GL API and window system until runtime
License:        BSD-2-Clause
Group:          Development/Libraries/X11
URL:            https://people.freedesktop.org/~chadversary/waffle/index.html
Source0:        https://gitlab.freedesktop.org/mesa/waffle/-/raw/website/files/release/%{name}-%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client) >= 1.10
BuildRequires:  pkgconfig(wayland-egl) >= 9.1
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

%description
Waffle is a C library that allows deferring the selection of GL API
and window system until runtime. For example, on Linux, Waffle enables
an application to select X11/EGL with an OpenGL 3.3 core profile, Wayland
with OpenGL ES2, and other window system / API combinations.

Waffle's immediate goal is to enable Piglit, Mesa's OpenGL test suite, to test
multiple GL flavors.

%package -n %{libname}
Summary:        C library defering selection of GL API and window system until runtime
Group:          System/Libraries
Requires:       %{name}

%description -n %{libname}
Waffle is a C library that allows deferring the selection of GL API
and window system until runtime. For example, on Linux, Waffle enables
an application to select X11/EGL with an OpenGL 3.3 core profile, Wayland
with OpenGL ES2, and other window system / API combinations.

Waffle's immediate goal is to enable Piglit, Mesa's OpenGL test suite, to test
multiple GL flavors.

%package devel
Summary:        Libraries, includes and more to develop Waffle applications
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}

%description devel
Devel files for the waffle C library. Libraries, includes and more to
develop Waffle applications.

%prep
%autosetup -p1

%build
%cmake \
  -Dwaffle_has_glx=1 \
  -Dwaffle_has_gbm=1 \
  -Dwaffle_has_x11_egl=1 \
  -Dwaffle_build_tests=1 \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/waffle-%{_majorVersion}
%cmake_build

%install
%cmake_install

%check
%ctest

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%dir %{_docdir}/waffle-%{_majorVersion}
%{_docdir}/waffle-%{_majorVersion}/*.txt
%{_docdir}/waffle-%{_majorVersion}/README.md
%dir %{_docdir}/waffle-%{_majorVersion}/release-notes
%{_docdir}/waffle-%{_majorVersion}/release-notes/*.txt
%{_docdir}/waffle-%{_majorVersion}/release-notes/waffle-1.6.*.md
%{_docdir}/waffle-%{_majorVersion}/release-notes/waffle-1.7.*.md
%{_bindir}/wflinfo
%{_datadir}/bash-completion/completions/wflinfo

%files -n %{libname}
%{_libdir}/libwaffle-1.so.*

%files devel
%{_libdir}/libwaffle-1.so
%dir %{_docdir}/waffle-%{_majorVersion}/examples
%{_docdir}/waffle-%{_majorVersion}/examples/*
%dir %{_includedir}/waffle-%{_majorVersion}
%{_includedir}/waffle-%{_majorVersion}/*.h
%{_libdir}/pkgconfig/waffle-%{_majorVersion}.pc
%{_libdir}/cmake/Waffle

%changelog
