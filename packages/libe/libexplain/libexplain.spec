#
# spec file for package libexplain
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


%define lib_name %{name}51
Name:           libexplain
Version:        1.4
Release:        0
Summary:        Library functions to explain system call errors
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://libexplain.sourceforge.net
Source:         http://downloads.sf.net/libexplain/%{name}-%{version}.tar.gz
Patch0:         libexplain-1.4-largefile.patch
Patch1:         libexplain-1.4-syscall.patch
# PATCH-FIX-UPSTREAM libexplain-1.4-missing-defines.patch mpluskal@suse.com
Patch2:         libexplain-1.4-missing-defines.patch
BuildRequires:  bison
BuildRequires:  ghostscript
BuildRequires:  groff-full
BuildRequires:  kernel-devel
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  lsof
BuildRequires:  pkgconfig

%description
The libexplain project provides a library which may be used to explain
Unix and Linux system call errors. This will make an application's
error messages much more informative to users. The library is
not quite a drop-in replacement for strerror, but it comes close. Each
system call has a dedicated libexplain function.

The coverage for system calls is being improved all the time. Coverage
includes 159 system calls and 444 ioctl requests.

%package -n %{lib_name}
Summary:        Library functions to explain system call errors
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lib_name}
The libexplain project provides a library which may be used to explain
Unix and Linux system call errors. This will make an application's
error messages much more informative to users. The library is
not quite a drop-in replacement for strerror, but it comes close. Each
system call has a dedicated libexplain function.

The coverage for system calls is being improved all the time. Coverage
includes 159 system calls and 444 ioctl requests.

%package -n explain
Summary:        Tool to explain system call error reports
License:        GPL-3.0-or-later
Group:          Development/Tools/Other

%description -n explain
The explain command is used to decode an error return read from an
strace(1) listing, or similar.  Because this is being deciphered in a
different process than the original one, the results will be less accurate
than if the program itself were to use libexplain(3).

%package devel
Summary:        Development files for libexplain
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description devel
Development files for the libexplain library.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# --disable-static for configure has no effect
rm %{buildroot}%{_libdir}/%{name}.{a,la}

%find_lang %{name}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name} -f %{name}.lang
%license LICENSE
%doc README
%{_libdir}/%{name}.so.*

%files -n explain
%{_bindir}/explain
%{_mandir}/man1/explain.1%{?ext_man}
%{_mandir}/man1/explain_lca2010.1%{?ext_man}
%{_mandir}/man1/explain_license.1%{?ext_man}

%files devel
%{_datadir}/doc/%{name}
%{_mandir}/man3/*.3%{?ext_man}
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
