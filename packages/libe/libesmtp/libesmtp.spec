#
# spec file for package libesmtp
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


%define so_ver 6.2.0
%define lname libesmtp6_2_0
Name:           libesmtp
Version:        1.1.0
Release:        0
Summary:        A Library for Posting Electronic Mail
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://libesmtp.github.io/
Source0:        https://github.com/libesmtp/libESMTP/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         add_ntlm.patch
BuildRequires:  libtool
BuildRequires:  meson >= 0.50.0
BuildRequires:  openssl-devel >= 1.1.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libntlm)

%description
libESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA). It may
be used as part of a Mail User Agent (MUA) or another program that
must be able to post electronic mail but where mail functionality is
not that program's primary purpose.

%package -n %{lname}
Summary:        A Library for Posting Electronic Mail
Group:          System/Libraries

%description -n %{lname}
libESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA). It may
be used as part of a Mail User Agent (MUA) or another program that
must be able to post electronic mail but where mail functionality is
not that program's primary purpose.

%package devel
Summary:        A Library for Posting Electronic Mail
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA).

This subpackage contains the API definition files.

%prep
%autosetup -p1 -n libESMTP-%{version}

%build
%meson \
  -Dntlm=enabled
%meson_build

%install
%meson_install

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%doc README.md docs/*
%{_libdir}/esmtp-plugins-%{so_ver}
%{_libdir}/libesmtp.so.%{so_ver}

%files devel
%{_includedir}/*.h
%{_libdir}/libesmtp.so
%{_libdir}/pkgconfig/libesmtp-1.0.pc

%changelog
