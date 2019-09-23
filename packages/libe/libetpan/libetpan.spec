#
# spec file for package libetpan
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


%define sover 20

Name:           libetpan
Version:        1.9.1
Release:        0
Summary:        Mail Handling Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.etpan.org/libetpan.html
Source0:        https://github.com/dinhviethoa/libetpan/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
# Stupid dependency. Compiles with gcc but tries to link with g++.
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libEtPan is a mail purpose library. It will be used for low-level mail
handling: network protocols (IMAP/NNTP/POP3/SMTP over TCP/IP and
SSL/TCP/IP, already implemented), local storage (mbox/MH/maildir) and
and message / MIME parsing.

%package -n libetpan%{sover}
Summary:        Mail handling library
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libetpan%{sover}
libEtPan is a mail purpose library. It will be used for low-level mail
handling: network protocols (IMAP/NNTP/POP3/SMTP over TCP/IP and
SSL/TCP/IP, already implemented), local storage (mbox/MH/maildir)
and message / MIME parsing.

%package -n libetpan-devel
Summary:        Development files for libetpan, a mail handling library
Group:          Development/Libraries/C and C++
Requires:       cyrus-sasl-devel
Requires:       db-devel
Requires:       libetpan%{sover} = %{version}
Requires:       openssl-devel

%description -n libetpan-devel
libEtPan is a mail purpose library. It will be used for low-level mail
handling: network protocols (IMAP/NNTP/POP3/SMTP over TCP/IP and
SSL/TCP/IP, already implemented), local storage (mbox/MH/maildir)
and message / MIME parsing.

%prep
%setup -q

%build
touch README INSTALL COPYING 
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
# remove unneeded *.la files
rm %{buildroot}%{_libdir}/libetpan.la

%post   -n libetpan%{sover} -p /sbin/ldconfig
%postun -n libetpan%{sover} -p /sbin/ldconfig

%files -n libetpan%{sover}
%defattr(-, root, root)
%doc ChangeLog NEWS doc/README*
%{_libdir}/libetpan.so.%{sover}*

%files -n libetpan-devel
%defattr(-, root, root)
%doc doc/API* doc/DOCUMENTATION
%{_bindir}/libetpan-config
%{_includedir}/libetpan/
%{_includedir}/libetpan.h
%{_libdir}/libetpan.so

%changelog
