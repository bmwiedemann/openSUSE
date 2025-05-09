#
# spec file for package recode
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define         libname lib%{name}3
Name:           recode
Version:        3.7.15
Release:        0
Summary:        Character Set Converter
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Text/Convertors
URL:            https://github.com/rrthomas/recode
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz


# Need python >= 3.8, SLE/Leap15 has 3.6 as default
%if 0%{?suse_version} > 1500
%global pythons %{primary_python}
%else
%global pythons python311
%endif

BuildRequires:  %{pythons}
BuildRequires:  %{pythons}-Cython
BuildRequires:  %{pythons}-setuptools

%description
Recode converts files between various character sets.
It supports conversion to and from HTML entities as well.

%package      devel
Summary:        Character Set Converter
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description  devel
Recode converts files between various character sets.

%package -n %{libname}
Summary:        Recode shared library
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname}
Recode converts files between various character sets.

This package contains librecode shared library for embedding in
other applications.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
rm -f %{buildroot}%{_libdir}/librecode.la
%find_lang %{name}

%ldconfig_scriptlets -n %{libname}

%files -f %{name}.lang
%license COPYING COPYING-LIB
%doc ABOUT-NLS AUTHORS NEWS README THANKS TODO ChangeLog
%{_mandir}/man1/*.1%{?ext_man}
%{_infodir}/recode*
%{_bindir}/recode

%files devel
%license COPYING COPYING-LIB
%{_includedir}/*.h
%{_libdir}/librecode.so

%files -n %{libname}
%license COPYING COPYING-LIB
%{_libdir}/librecode.so.*

%changelog
