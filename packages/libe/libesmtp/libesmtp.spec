#
# spec file for package libesmtp
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libesmtp
%define lname	libesmtp6
Version:        1.0.6
Release:        0
Summary:        A Library for Posting Electronic Mail
License:        GPL-2.0+ and LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.stafford.uklinux.net/libesmtp/
Source0:        %{name}-%{version}.tar.bz2
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/Packaging/Patches
Patch0:         libesmtp-removedecls.diff
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/Packaging/Patches
Patch1:         libesmtp-1.0.4-bloat.patch
# PATCH-FIX-UPSTREAM libesmtp-tlsv12.patch crrodriguez@opensuse.org -- All TLS clients must support and use the highest TLS version available
Patch2:         libesmtp-tlsv12.patch
Patch3:         libesmtp-openssl11.patch
BuildRequires:  openssl-devel
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA). It may
be used as part of a Mail User Agent (MUA) or another program that
must be able to post electronic mail but where mail functionality is
not that program's primary purpose.

%package -n %lname
Summary:        A Library for Posting Electronic Mail
Group:          System/Libraries

%description -n %lname
libESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA). It may
be used as part of a Mail User Agent (MUA) or another program that
must be able to post electronic mail but where mail functionality is
not that program's primary purpose.

%package devel
Summary:        A Library for Posting Electronic Mail
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA).

This subpackage contains the API definition files.

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fiv
%configure --with-openssl=yes --disable-static --enable-ntlm --enable-etrn \
	--disable-isoc --with-auth-plugin-dir="%_libdir/%lname-plugins"
make %{?_smp_mflags}

%install
%make_install
# library uses dlsym not ltdl
find "%buildroot" -type f -name "*.la" -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%license COPYING
%_libdir/%lname-plugins/
%{_libdir}/libesmtp.*so.*

%files devel
%defattr(-,root,root)
%{_bindir}/libesmtp-config
%{_includedir}/*.h
%{_libdir}/libesmtp.*so

%changelog
