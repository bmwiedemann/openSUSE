#
# spec file for package libotf
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


Name:           libotf
Version:        0.9.13
Release:        0
Summary:        Library for Handling OpenType Fonts
License:        LGPL-2.1+
Group:          System/I18n/Japanese
Url:            http://www.m17n.org/libotf/
Source0:        http://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
Source1:        http://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz.sig
Source99:       baselibs.conf
Patch0:         libotf-warning-fixes.diff
# patch not sent upstream, because m17n.org is currently down
Patch1:         libotf-automake-1.13.diff
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)

%description
Library for handling OpenType fonts,especially those needed for CJK and other non-Latin
languages.

%package -n libotf0
Summary:        Shared library for libotf
Group:          System/I18n/Japanese

%description -n libotf0
Library for handling OpenType fonts,especially those needed for CJK and other non-Latin
languages.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fvi
%configure \
  --disable-static \
  --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libotf0 -p /sbin/ldconfig
%postun -n libotf0 -p /sbin/ldconfig

%files
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/*

%files -n libotf0
%{_libdir}/libotf.so.*

%files devel
%{_includedir}/*
%{_libdir}/libotf.so
%{_libdir}/pkgconfig/libotf.pc

%changelog
