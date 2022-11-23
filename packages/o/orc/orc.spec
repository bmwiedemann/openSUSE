#
# spec file for package orc
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands.
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


Name:           orc
Version:        0.4.33
Release:        0
Summary:        The Oil Runtime Compiler
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Other
URL:            https://gitlab.freedesktop.org/gstreamer/orc
Source:         https://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  gtk-doc >= 1.12
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
Provides:       %{name}-devel = %{version}

%description
Orc is a library and set of tools for compiling and executing very simple
programs that operate on arrays of data.  The “language” is a generic
assembly language that represents many of the features available in SIMD
architectures, including saturated addition and subtraction, and many
arithmetic operations.

%package -n liborc-0_4-0
Summary:        The Oil Runtime Compiler Library
Group:          System/Libraries

%description -n liborc-0_4-0
Orc is a library and set of tools for compiling and executing very simple
programs that operate on arrays of data.  The “language” is a generic
assembly language that represents many of the features available in SIMD
architectures, including saturated addition and subtraction, and many
arithmetic operations.

%package doc
Summary:        The Oil Runtime Compiler Library - Documentation
Group:          Documentation/HTML

%description doc
Orc is a library and set of tools for compiling and executing very simple
programs that operate on arrays of data.  The “language” is a generic
assembly language that represents many of the features available in SIMD
architectures, including saturated addition and subtraction, and many
arithmetic operations.

%prep
%autosetup -p1

%build
%meson \
	-Dorc-test=disabled \
	-Dexamples=disabled \
	-Dtests=disabled \
	%{nil}
%meson_build

%install
%meson_install

%post -n liborc-0_4-0 -p /sbin/ldconfig
%postun -n liborc-0_4-0 -p /sbin/ldconfig

%files
%{_bindir}/orcc
%{_includedir}/orc-0.4/
%{_libdir}/*.so
%{_libdir}/pkgconfig/orc-0.4.pc
%{_datadir}/aclocal/orc.m4

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/orc/

%files -n liborc-0_4-0
%{_libdir}/liborc*-0.4.so.*

%changelog
