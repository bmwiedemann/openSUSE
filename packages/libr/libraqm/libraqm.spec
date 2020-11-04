#
# spec file for package libraqm
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 0
Name:           libraqm
Version:        0.7.0
Release:        0
Summary:        Complex Textlayout Library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/HOST-Oman/libraqm
Source:         https://github.com/HOST-Oman/libraqm/releases/download/v%{version}/raqm-%{version}.tar.gz
# PATCH-FIX-OPENSUSE disable some tests for old SuSE Versions
Patch0:         libraqm-test.patch
BuildRequires:  freetype2-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  harfbuzz-devel

%description
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package -n %{name}%{sover}
Summary:        Complex Textlayout Library
Group:          System/Libraries

%description -n %{name}%{sover}
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package doc
Summary:        Libraqm documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains documentation files for raqm.

%package devel
Summary:        Complex Textlayout Library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%prep
%setup -q -n raqm-%{version}
%if 0%{?suse_version} <= 1510
%patch0 -p1
%endif
%if 0%{?suse_version} >= 1500
sed s:python:%{__python3}:g -i tests/Makefile.in #Fixed in next release on upstream
%endif
%configure --enable-gtk-doc

%build
make %{?_smp_mflags}

%check
export LC_ALL=C.utf8
make %{?_smp_mflags} check

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.{la,a}

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig
%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%{_libdir}/libraqm.so.*

%files devel
%{_includedir}/raqm.h
%{_includedir}/raqm-version.h
%{_libdir}/libraqm.so
%{_libdir}/pkgconfig/raqm.pc

%files doc
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/gtk-doc/html/raqm

%changelog
