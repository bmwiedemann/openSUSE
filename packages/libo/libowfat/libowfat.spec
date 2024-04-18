#
# spec file for package libowfat
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libowfat
Version:        0.33
Release:        0
Summary:        A reimplementation of libdjb
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
#CVS-checkout:  :pserver:cvs@cvs.fefe.de:/cvs libowfat
URL:            https://www.fefe.de/libowfat/
Source:         https://www.fefe.de/libowfat/%{name}-%{version}.tar.xz
Source98:       https://www.fefe.de/libowfat/%{name}-%{version}.tar.xz.sig
Source99:       https://dl.fefe.de/felix@fefe.de.asc#/%{name}.keyring

%description
libowfat is a library of general purpose APIs extracted from Dan
Bernstein's software, reimplemented and covered by the GNU General
Public License Version 2 (no later versions).

%package devel
Summary:        A reimplementation of libdjb
Group:          Development/Libraries/C and C++

%description devel
libowfat is a library of general purpose APIs extracted from Dan
Bernstein's software, reimplemented and covered by the GNU General
Public License Version 2 (no later versions).

%prep
%setup -q

%build
%make_build headers
%make_build \
    prefix=%{_prefix} \
    INCLUDEDIR=%{_includedir}
    MAN3DIR=%{_mandir}/man3 \
    LIBDIR=%{_libdir} \
    CFLAGS="%{optflags} -I. -ffat-lto-objects -g" \
    CFLAGS_OPT="%{optflags} -I. -O3 -ffat-lto-objects -g"

%install
make %{?_smp_mflags} \
    prefix=%{_prefix} \
    INCLUDEDIR=%{_includedir} \
    MAN3DIR=%{_mandir}/man3 \
    LIBDIR=%{_libdir} \
    DESTDIR="%{?buildroot}" install

%files devel
%license COPYING
%doc README CHANGES
%dir %{_includedir}/libowfat
%{_includedir}/libowfat/*.h
%{_libdir}/libowfat.a
%{_mandir}/man3/*.3%{?ext_man}

%changelog
