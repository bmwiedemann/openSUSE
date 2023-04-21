#
# spec file for package libunistring
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


%define sover	5
Name:           libunistring
Version:        1.1
Release:        0
Summary:        GNU Unicode string library
License:        GPL-3.0-or-later OR LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/libunistring/
Source0:        http://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz
Source1:        http://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=1871/%{name}.keyring
Source3:        baselibs.conf

%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package devel
Summary:        Development files for the GNU Unicode string library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
Development files for programs using libunistring and documentation
for UniString library.

%package -n %{name}%{sover}
Summary:        GNU Unicode string library
Group:          System/Libraries

%description -n %{name}%{sover}
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%prep
%autosetup -p1

%build
%configure --disable-static --disable-rpath --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
cp AUTHORS NEWS README HACKING DEPENDENCIES THANKS ChangeLog %{buildroot}/%{_docdir}/%{name}
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/libunistring.la

%check
%if ! 0%{?qemu_user_space_build}
# test-malloca seem not to be suitable for ix86 obs worker
# (locally passes, obs worker stucks -- )
%ifarch %{ix86}
sed -i 's:50000:50:g' tests/test-malloca.c
%endif
# do not run tests in parallel, it stucks randomly
%make_build check #
%endif

%files -n %{name}%{sover}
%license COPYING*
%{_libdir}/libunistring.so.%{sover}{,.*}

%files devel
%license COPYING*
%{_docdir}/%{name}
%{_infodir}/libunistring.info%{?ext_info}
%{_libdir}/libunistring.so
%{_includedir}/unistring
%{_includedir}/*.h

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%changelog
