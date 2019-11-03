#
# spec file for package twolame
#
# Copyright (c) 2019 SUSE LLC
# Copyright (c) 2006-2008 oc2pus
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


%define sonum   0
Name:           twolame
Version:        0.4.0
Release:        0
Summary:        An optimised MPEG Audio Layer 2 (MP2) encoder
License:        LGPL-2.1-only
URL:            http://www.twolame.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sndfile) >= 1.0.0

%description
TwoLAME is an optimised MPEG Audio Layer 2 (MP2) encoder based on
tooLAME by Mike Cheng, which in turn is based upon the ISO dist10
code and portions of LAME. TwoLAME includes libtwolame, a fully
thread-safe shared library with an API very similar to LAME's.

%package -n lib%{name}%{sonum}
Summary:        Shared libraries for TwoLame

%description -n lib%{name}%{sonum}
TwoLAME is an optimised MPEG Audio Layer 2 (MP2) encoder based on
tooLAME by Mike Cheng, which in turn is based upon the ISO dist10
code and portions of LAME. TwoLAME includes libtwolame, a fully
thread-safe shared library with an API very similar to LAME's.

This package contains the shared libraries for TwoLame.

%package -n lib%{name}-devel
Summary:        Include Files and Libraries mandatory for Development
Requires:       lib%{name}%{sonum} = %{version}
Provides:       %{name}-devel = 0.3.10
Obsoletes:      %{name}-devel < 0.3.10

%description -n lib%{name}-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

install -dm 755 %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} \
    %{buildroot}%{_docdir}/lib%{name}-devel
rm %{buildroot}%{_docdir}/lib%{name}-devel/COPYING

find %{buildroot} -type f -name "*.la" -delete -print

%post   -n lib%{name}%{sonum} -p /sbin/ldconfig
%postun -n lib%{name}%{sonum} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n lib%{name}%{sonum}
%{_libdir}/lib%{name}.so.%{sonum}*
%{_libdir}/lib%{name}.so.%{sonum}

%files -n lib%{name}-devel
%doc ChangeLog
%doc %{_docdir}/lib%{name}-devel
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
