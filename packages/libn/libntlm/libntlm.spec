#
# spec file for package libntlm
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


Name:           libntlm
%define lname	libntlm0
Version:        1.7
Release:        0
Summary:        Implementation of Microsoft's NTLMv1 authentication
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://gitlab.com/gsasl/libntlm/
#Git-Clone:	https://gitlab.com/gsasl/libntlm.git
#DL-URL:	https://download.savannah.nongnu.org/releases/libntlm/
Source:         https://download.savannah.nongnu.org/releases/libntlm/%name-%version.tar.gz
Source2:        https://download.savannah.nongnu.org/releases/libntlm/%name-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  pkg-config

%description
Libntlm provides routines to manipulate the structures used for the
client end of Microsoft NTLMv1 authentication.

%package -n %lname
Summary:        Implementation of Microsoft's NTLMv1 authentication
Group:          System/Libraries

%description -n %lname
Libntlm provides routines to manipulate the structures used for the
client end of Microsoft NTLMv1 authentication.

%package devel
Summary:        Development files for libntlm, an NTLMv1 authentication library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Libntlm provides routines to manipulate the structures used for the
client end of Microsoft NTLMv1 authentication.

This subpackage contains libraries and header files for developing
applications that want to make use of libntlm.

%prep
%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
make check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%_libdir/libntlm.so.0*

%files devel
%doc ChangeLog NEWS README
%_includedir/ntlm.h
%_libdir/libntlm.so
%_libdir/pkgconfig/libntlm.pc

%changelog
