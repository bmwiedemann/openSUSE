#
# spec file for package recode
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


%define          libname lib%{name}3
Name:           recode
Version:        3.7.6
Release:        0
Summary:        Character Set Converter
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Text/Convertors
URL:            https://github.com/rrthomas/recode
Source:         https://github.com/rrthomas/recode/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  flex
BuildRequires:  python3
BuildRequires:  python3-Cython
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
Recode converts files between various character sets.
It supports conversion to and from HTML entities as well.

%package      devel
Summary:        Character Set Converter
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

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
#autoreconf -fiv
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
rm -f %{buildroot}%{_libdir}/librecode.la
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING COPYING-LIB
%doc ABOUT-NLS AUTHORS NEWS README THANKS TODO ChangeLog
%{_mandir}/man1/*
%{_infodir}/recode*
%{_bindir}/recode

%files devel
%{_includedir}/*.h
%{_libdir}/librecode.so

%files -n %{libname}
%{_libdir}/librecode.so.*

%changelog
