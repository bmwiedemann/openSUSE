#
# spec file for package libzio
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


Name:           libzio
%define lname   libzio1
Version:        1.08
Release:        0
Summary:        A Library for Accessing Compressed Text Files
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            http://libzio.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  libbz2-devel
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zstd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libzio provides a wrapper function for reading or writing gzip or bzip2
files with FILE streams.

%package -n %lname
Summary:        A Library for Accessing Compressed Text Files
Group:          System/Libraries
Provides:       libzio = 1.06
Obsoletes:      libzio <= 1.00

%description -n %lname
Libzio provides a wrapper function for reading or writing gzip or bzip2
files with FILE streams.

%package        devel
Summary:        Libzio development files
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}
# bug437293

%description    devel
Libzio development files including zio.h, the manual page fzopen(3),
and static library.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
make %{?_smp_mflags} noweak

%check
make testt tests testx
for comp in gzip bzip2 lzma xz zstd
do
    case $comp in
    gzip) x=g ;;
    bzip2) x=b ;;
    lzma) x=l ;;
    xz) x=x ;;
    zstd) x=s ;;
    esac
    $comp -c < fzopen.3.in > fzopen.test
    ./testt fzopen.test | cmp fzopen.3.in -
    cat fzopen.test | ./tests $x | cmp fzopen.3.in -
    ./testx $x < fzopen.3.in | ./tests $x | cmp fzopen.3.in -
done

%install
make DESTDIR=$RPM_BUILD_ROOT install libdir=%{_libdir} mandir=%{_mandir}

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%license COPYING
%{_libdir}/libzio.so.1
%{_libdir}/libzio.so.%{version}

%files devel
%defattr(-,root,root)
%doc README
%{_libdir}/libzio.a
%{_libdir}/libzio.so
%{_mandir}/man3/fzopen.3*
%{_includedir}/zio.h

%changelog
