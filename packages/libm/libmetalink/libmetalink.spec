#
# spec file for package libmetalink
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname 3
Name:           libmetalink
Version:        0.1.3
Release:        0
Summary:        Metalink Library
License:        MIT
Group:          System/Libraries
Url:            https://launchpad.net/libmetalink
Source:         https://launchpad.net/libmetalink/trunk/libmetalink-%{version}/+download/%{name}-%{version}.tar.xz
Patch0:         libmetalink-autotools.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1310
BuildRequires:  pkgconfig(cunit)
%endif
%if 0%{?suse_version} >= 1310
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libxml-2.0)
%else
BuildRequires:  libexpat-devel
BuildRequires:  libxml2-devel
%endif
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libmetalink is a Metalink library written in C language. It is intended to
provide the programs written in C to add Metalink functionality such as parsing
Metalink XML files.

%package -n libmetalink%{soname}
Summary:        Metalink Library
Group:          System/Libraries

%description -n libmetalink%{soname}
Libmetalink is a Metalink library written in C language. It is intended to
provide the programs written in C to add Metalink functionality such as parsing
Metalink XML files.

%package -n libmetalink-devel
Summary:        Metalink Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libmetalink%{soname} = %{version}

%description -n libmetalink-devel
Libmetalink is a Metalink library written in C language. It is intended to
provide the programs written in C to add Metalink functionality such as parsing
Metalink XML files.

%prep
%setup -q
%patch0

%build
autoreconf -fiv
%configure \
	 --disable-static \
    --with-libexpat

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -rf "%{buildroot}%{_datadir}/doc"
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libmetalink%{soname} -p /sbin/ldconfig

%postun -n libmetalink%{soname} -p /sbin/ldconfig

%check
make %{?_smp_mflags} test

%files -n libmetalink%{soname}
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/libmetalink.so.%{soname}
%{_libdir}/libmetalink.so.%{soname}.*

%files -n libmetalink-devel
%defattr(-,root,root)
%{_includedir}/metalink
%{_libdir}/libmetalink.so
%{_libdir}/pkgconfig/libmetalink.pc
%{_mandir}/man3/metalink*.3*

%changelog
