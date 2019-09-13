#
# spec file for package libtasn1
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define somajor 6
Name:           libtasn1
Version:        4.14
Release:        0
Summary:        ASN.1 parsing library
License:        LGPL-2.1-or-later AND GPL-3.0-only
Group:          Productivity/Networking/Security
URL:            https://www.gnu.org/software/libtasn1/
Source0:        http://ftp.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz.sig
# http://josefsson.org/key.txt
Source2:        %{name}.keyring
Source99:       baselibs.conf
BuildRequires:  info
BuildRequires:  pkgconfig
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
This is the ASN.1 library used by GNUTLS. More up to date information
can be found at http://www.gnu.org/software/gnutls and
http://www.gnutls.org

%package -n libtasn1-%{somajor}
Summary:        ASN.1 parsing library
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libtasn1-%{somajor}
This is the ASN.1 library used by GNUTLS. More up to date information
can be found at http://www.gnu.org/software/gnutls and
http://www.gnutls.org

%package devel
Summary:        Development files for the ASN.1 parsing library
Group:          Development/Libraries/C and C++
Requires:       libtasn1-%{somajor} = %{version}

%description devel
This is the ASN.1 library used by GNUTLS. More up to date information
can be found at http://www.gnu.org/software/gnutls and
http://www.gnutls.org

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n libtasn1-%{somajor} -p /sbin/ldconfig
%postun -n libtasn1-%{somajor} -p /sbin/ldconfig

%files
%license doc/COPYING*
%doc NEWS README.md THANKS
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}
%{_infodir}/*.info%{?ext_info}

%files -n libtasn1-%{somajor}
%license doc/COPYING*
%{_libdir}/*.so.%{somajor}*

%files devel
%license doc/COPYING*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libtasn1.pc
%{_mandir}/man3/*.3%{?ext_man}

%changelog
