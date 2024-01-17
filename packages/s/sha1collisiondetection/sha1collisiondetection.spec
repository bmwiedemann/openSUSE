#
# spec file for package sha1collisiondetection
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Andreas Stieger <astieger@suse.com>
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


Name:           sha1collisiondetection
Version:        1.0.3
Release:        0
Summary:        Detection of SHA-1 collisions
License:        MIT
Group:          Productivity/Security
Url:            https://github.com/cr-marcstevens/sha1collisiondetection
Source:         https://github.com/cr-marcstevens/sha1collisiondetection/archive/stable-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         sha1collisiondetection-1.0.3-io-fixes.patch
Patch1:         sha1collisiondetection-endian_detection.patch
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This command line tool was designed as near drop-in replacements for other sha1sum
implementations. It will compute the SHA-1 hash of any given file and additionally
will detect cryptanalytic collision attacks against SHA-1 present in each file.
It is very fast and takes less than twice the amount of time as regular SHA-1.

%package -n libsha1detectcoll1
Summary:        Library that can detect SHA-1 collisions
Group:          System/Libraries

%description -n libsha1detectcoll1
This library was designed as near drop-in replacements for other sha1sum
implementations. It will compute the SHA-1 hash of any given file and additionally
will detect cryptanalytic collision attacks against SHA-1 present in each file.
It is very fast and takes less than twice the amount of time as regular SHA-1.

%package -n libsha1detectcoll-devel
Summary:        Development files for
Group:          Development/Libraries/C and C++
Requires:       libsha1detectcoll1 = %{version}

%description -n libsha1detectcoll-devel
This library was designed as near drop-in replacements for other sha1sum
implementations. It will compute the SHA-1 hash of any given file and additionally
will detect cryptanalytic collision attacks against SHA-1 present in each file.
It is very fast and takes less than twice the amount of time as regular SHA-1.

%prep
%setup -q -n %{name}-stable-v%{version}
%patch0 -p1
%patch1

%build
export TARGETCFLAGS="%{optflags}"
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
%make_install \
	PREFIX=%{buildroot}%{_prefix} \
	LIBDIR=%{buildroot}%{_libdir}
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete -print
chmod -x %{buildroot}%{_includedir}/sha1dc/sha1.h

%check
make %{?_smp_mflags} test

%post   -n libsha1detectcoll1 -p /sbin/ldconfig
%postun -n libsha1detectcoll1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc LICENSE.txt README.md
%{_bindir}/*

%files -n libsha1detectcoll1
%defattr(-,root,root)
%doc LICENSE.txt README.md
%{_libdir}/libsha1detectcoll.so.*

%files -n libsha1detectcoll-devel
%defattr(-,root,root)
%doc LICENSE.txt README.md
%{_includedir}/sha1dc
%{_libdir}/libsha1detectcoll.so

%changelog
