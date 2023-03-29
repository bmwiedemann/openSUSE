#
# spec file for package zchunk
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


%global somajor 1
%global libname libzck%{somajor}
%global devname libzck-devel
Name:           zchunk
Version:        1.3.0
Release:        0
Summary:        Compressed file format that allows easy deltas
License:        BSD-2-Clause AND MIT
Group:          Productivity/Archiving/Compression
URL:            https://github.com/zchunk/zchunk
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.44.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
# ABI is unstable between components and ensures that patching doesn't break things
Requires:       %{libname} = %{version}-%{release}
Provides:       bundled(buzhash-urlblock) = 0.1

%description
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

%package -n %{libname}
Summary:        Zchunk library
Group:          System/Libraries

%description -n %{libname}
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the zchunk library, libzck.

%package -n %{devname}
Summary:        Headers for building against zchunk
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the headers necessary for building against the zchunk
library, libzck.

%prep
%autosetup -p1
# Remove bundled sha libraries
rm -rf src/lib/hash/sha*

%build
%meson -Dwith-openssl=enabled -Dwith-zstd=enabled
%meson_build

%install
%meson_install
# Install dictionary generation script
mkdir -p %{buildroot}%{_libexecdir}
install -p contrib/gen_xml_dictionary %{buildroot}%{_libexecdir}/zck_gen_xml_dictionary

%check
%meson_test

%post -n   %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md contrib
%{_bindir}/zck*
%{_bindir}/unzck
%{_libexecdir}/zck_gen_xml_dictionary
%{_mandir}/man1/unzck.1%{?ext_man}
%{_mandir}/man1/zck*.1%{?ext_man}

%files -n %{libname}
%license LICENSE
%{_libdir}/libzck.so.%{somajor}
%{_libdir}/libzck.so.%{version}

%files -n %{devname}
%doc zchunk_format.txt
%{_libdir}/libzck.so
%{_libdir}/pkgconfig/zck.pc
%{_includedir}/zck.h

%changelog
