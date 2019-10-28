#
# spec file for package ggz
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ggz
Version:        0.0.14.1
Release:        0
Summary:        Makes free online gaming possible
License:        GPL-2.0+ and LGPL-2.1+
Group:          Amusements/Games/Other
Url:            http://www.ggzgamingzone.org/
Source0:        libggz-%{version}.tar.bz2
BuildRequires:  libgcrypt-devel
BuildRequires:  libopenssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The GGZ project makes free online gaming possible.

%package -n libggz2-devel
Summary:        Makes free online gaming possible
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       gnutls-devel
Requires:       libgcrypt-devel
Requires:       libggz2 = %{version}

%description -n libggz2-devel
The GGZ project makes free online gaming possible.

%package -n libggz2
Summary:        Makes free online gaming possible
Group:          Amusements/Games/Other
Provides:       %{name} = %{version}
Obsoletes:      %{name} <= %{version}

%description -n libggz2
The GGZ project makes free online gaming possible.

%prep
%setup -q -n libggz-%{version}

%build
%configure --disable-static --with-pic --enable-anl --with-tls
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_datadir}/ggz

%post   -n libggz2 -p /sbin/ldconfig
%postun -n libggz2 -p /sbin/ldconfig

%files -n libggz2
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README*
%{_libdir}/*.so.*
%dir %{_datadir}/ggz

%files -n libggz2-devel
%defattr(-, root, root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_mandir}/man3/*.gz

%changelog
