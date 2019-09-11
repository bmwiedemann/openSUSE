#
# spec file for package infiniband-diags
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


%define ibnetdisc_major 5
%define mad_major 5
%define git_ver .0.b48b4a630f54

Name:           infiniband-diags
Summary:        OpenFabrics Alliance InfiniBand Diagnostic Tools
License:        GPL-2.0-only OR BSD-2-Clause
Group:          Productivity/Networking/Diagnostic
Version:        2.2.0
Release:        0
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Source1:        baselibs.conf
Patch2:         infiniband-diags-help_for_ibnodes.patch
Url:            http://www.openfabrics.org
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  opensm-devel
BuildRequires:  pkg-config
BuildRequires:  rdma-core-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libudev)
Requires:       perl = %{perl_version}

%description
diags provides IB diagnostic programs and scripts needed to diagnose an
IB subnet.

%package    -n libibnetdisc%{ibnetdisc_major}
Summary:        Infiniband Net Discovery runtime library
Group:          System/Libraries

%description -n libibnetdisc%{ibnetdisc_major}
This package contains the Infiniband Net Discovery runtime library needed
mainly by infiniband-diags.


%package        devel
Summary:        OpenIB InfiniBand Diagnostic Tools SDK
Group:          Development/Libraries/C and C++
BuildRequires:  opensm-devel
BuildRequires:  rdma-core-devel
Requires:       %{name} = %{version}
Requires:       libibmad%{mad_major} = %version
Requires:       libibnetdisc%{ibnetdisc_major} = %version
Provides:       infiniband-diags:%{_libdir}/libibnetdisc.so
Provides:       libibmad-devel = %{version}-%{release}
Obsoletes:      libibmad-devel < %{version}

%description    devel
diags provides IB diagnostic programs and scripts needed to diagnose an
IB subnet. This package contains all files needed for development.

%package -n     libibmad%{mad_major}
Summary:        Libibamd runtime library
Group:          System/Libraries
BuildRequires:  rdma-core-devel

%description -n libibmad%{mad_major}
Libibmad provides low layer IB functions for use by the IB diagnostic
and management programs. These include MAD, SA, SMP, and other basic IB
functions. This package contains the runtime library.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
# rename to silence automake
%patch2

# Avoid unnecessary rebuilds of the package
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/ibdiag_common.c

%build
autoreconf -fi
export CFLAGS="%{optflags}"
%configure --with-perl-installdir=%{perl_vendorarch} --disable-static
make %{?_smp_mflags} V=1

%install
make DESTDIR=%buildroot install
rm -f %{buildroot}%{_libdir}/*.la

%check
make check

%post -n libibnetdisc%{ibnetdisc_major} -p /sbin/ldconfig
%postun -n libibnetdisc%{ibnetdisc_major} -p /sbin/ldconfig

%post -n libibmad%{mad_major} -p /sbin/ldconfig
%postun -n libibmad%{mad_major} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%license COPYING ChangeLog
%doc README
%config %{_sysconfdir}/infiniband-diags/error_thresholds
%dir %{_sysconfdir}/infiniband-diags
%config(noreplace) %{_sysconfdir}/infiniband-diags/*
%_sbindir/*
%_mandir/man8/*
%_mandir/man3/*
%{perl_vendorarch}/IBswcountlimits.pm

%files -n libibnetdisc%{ibnetdisc_major}
%defattr(-, root, root)
%license COPYING
%{_libdir}/libibnetdisc.so.*

%files -n libibmad%{mad_major}
%defattr(-, root, root)
%license COPYING
%_libdir/libibmad.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/infiniband/*.h
%{_libdir}/*.so

%changelog
