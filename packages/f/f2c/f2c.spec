#
# spec file for package f2c
#
# Copyright (c) 2022 SUSE LLC
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


%define libname libf2c0
%global sover 0.23
Name:           f2c
#
Version:        20210928
Release:        0
Summary:        A Fortran-77 to C Translator
License:        MIT
Group:          Development/Languages/Fortran
URL:            https://www.netlib.org/f2c/
Source0:        https://www.netlib.org/f2c/src.tgz
Source1:        https://www.netlib.org/f2c/libf2c.zip
Source2:        https://www.netlib.org/f2c/f2c.pdf
Source3:        https://www.netlib.org/f2c/f2c.ps
Source4:        https://www.netlib.org/f2c/fc
Patch0:         f2c-20110801.patch
Patch1:         libf2c-20110801-format-security.patch
Patch2:         f2c-20180821.patch
BuildRequires:  tcsh
BuildRequires:  unzip

%description
This package uses an 'f77' script that hides the C translation process from the user.

%package -n %{libname}
Summary:        A Fortran-77 to C Translator
Group:          System/Libraries

%description -n %{libname}
This package uses an 'f77' script that hides the C translation process from the user.

%package devel
Summary:        Files for Developing with f2c
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package uses an 'f77' script that hides the C translation process from the user.

%prep

%setup -q -c %{name}-%{version}

mkdir libf2c
unzip -qq %{SOURCE1} -d libf2c
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Set library soversion
sed -i "s/@SOVER@/%{sover}/" libf2c/makefile.u

# PDF and PS documentation
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
%make_build -C src -f makefile.u CFLAGS="%{optflags} -fno-strict-aliasing" f2c
%make_build -C libf2c -f makefile.u CFLAGS="%{optflags} -fPIC -fno-strict-aliasing"

%install
install -D -p -m 644 src/f2c.h  %{buildroot}%{_includedir}/f2c.h
install -D -p -m 755 src/f2c    %{buildroot}%{_bindir}/f2c
install -D -p -m 644 src/f2c.1t %{buildroot}%{_mandir}/man1/f2c.1
install -D -p -m 755 libf2c/libf2c.so.%{sover} %{buildroot}%{_libdir}/libf2c.so.%{sover}
ln -sr %{buildroot}%{_libdir}/libf2c.so.%{sover} %{buildroot}%{_libdir}/libf2c.so.0
ln -sr %{buildroot}%{_libdir}/libf2c.so.%{sover} %{buildroot}%{_libdir}/libf2c.so

# Setup f77 script
sed -i "s/@lib@/%{_lib}/" fc
install -Dpm 0755 fc %{buildroot}%{_bindir}/f77

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/f2c*

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/f2c
%{_bindir}/f77
%{_mandir}/man1/f2c.1%{?ext_man}

%changelog
