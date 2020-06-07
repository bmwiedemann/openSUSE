#
# spec file for package ibutils
#
# Copyright (c) 2020 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%flavor" == "ui"
%define pname_suff -ui
%endif

%define ibdm_major 1
%define upstream_ver 1.5.7
%define tar_rel 0.2

Name:           ibutils%{?pname_suff}
Summary:        OpenIB Mellanox InfiniBand Diagnostic Tools
License:        BSD-3-Clause OR GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
Version:        %upstream_ver.%tar_rel
Release:        0
Source0:        https://www.openfabrics.org/downloads/ibutils/ibutils-%upstream_ver-%tar_rel.gbd7e502.tar.gz
Source1:        ibutils-rpmlintrc
#PATCH-FIX-UPSTREAM Fix non-void functions returning no value
Patch1:         ibutils-1.2-retval.patch
#PATCH-FIX-UPSTREAM Extend the check to include tk 8.6
Patch2:         ibutils-tk-8.6.patch
#PATCH-FIX-UPSTREAM Prepare for autoreconf run
Patch4:         ibutils-autotools.patch
#PATCH-FIX-UPSTREAM Do not link ibdmsh statically and remove rpath
Patch5:         ibutils-no_special_ldflags_for_ibdmsh.patch
# Add --disable-ibdiagui option to allow for split builds
Patch6:         ibutils-diagui.patch
Patch7:         ibutils-fix-build-dependency.patch
Patch8:         ibis-drop-multiple-definition-of-IbisObj.patch
URL:            http://www.openfabrics.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  libibverbs-devel
BuildRequires:  libtool
BuildRequires:  opensm-devel
%if "%flavor" == "ui"
BuildRequires:  graphviz-tcl
BuildRequires:  swig
BuildRequires:  tk-devel
Requires:       graphviz-tcl
Requires:       ibutils = %version
%else
BuildRequires:  tcl-devel
%endif

%if "%flavor" == ""
%description
The ibutils package provides a set of diagnostic tools that check the health
of an InfiniBand fabric.

Package components:
ibis:     IB interface - A TCL shell that provides interface for sending various
          MADs on the IB fabric. This is the component that actually accesses
          the IB Hardware.

ibdm:     IB Data Model - A library that provides IB fabric analysis.

ibmgtsim: An IB fabric simulator. Useful for developing IB tools.

ibdiag:   This package provides two tools which provide the user interface
          to activate the above functionality:
            - ibdiagnet:  Performs various quality and health checks on the IB
                          fabric.
            - ibdiagpath: Performs various fabric quality and health checks on
                          the given links and nodes in a specific path.
%else
%description
The ibutils-ui package provides a set of graphical UI tools that check the health
of an InfiniBand fabric.

Package components:
ibdiag:   This package provides one tool which provide the user interface
          to activate the above functionality:
            - ibdiagui:   A GUI wrapper for ibdiagnet and ibdiagpath.
%endif

%package        devel
Summary:        SDK for OpenIB Mellanox InfiniBand Diagnostic Tools
Group:          Development/Libraries/C and C++
Requires:       %name = %version
Requires:       libibdm%ibdm_major = %version

%description    devel
ibutils provides IB network and path diagnostics.

%package     -n libibdm%ibdm_major
Summary:        Shared libraries for ibutils
Group:          System/Libraries

%description -n libibdm%ibdm_major
This package contains shared libraries for the IB utils.

%prep
%setup -q -n ibutils-%upstream_ver
%patch1
%patch2
%patch4
%patch5
%patch6
%patch7
%patch8

%build
autoreconf -fi
./autogen.sh
%if "%flavor" == ""
%configure --with-graphviz-lib=%_libdir --disable-static --disable-ibdiagui
make %{?_smp_mflags}
%else
%configure --with-graphviz-lib=%_libdir --disable-static
make %{?_smp_mflags} -Cibdiag
%endif

%install
export NO_BRP_TCL_INDEX_CHECK=true
%if "%flavor" == ""
%makeinstall 
%else
%makeinstall -Cibdiag/
rm -f %buildroot%_bindir/git_version.tcl %buildroot%_bindir/ibdiagnet %buildroot%_bindir/ibdiagpath
rm -Rf %buildroot%_libdir/ibdiagnet*  %buildroot%_libdir/ibdiagpath*
rm -f %buildroot%_mandir/man1/ibdiagnet.1* %buildroot%_mandir/man1/ibdiagpath.1*
%endif
%fdupes -s %buildroot%_libdir
rm -f %buildroot%_libdir/*.la %buildroot%_libdir/*.a

%post -n libibdm%ibdm_major -p /sbin/ldconfig
%postun -n libibdm%ibdm_major -p /sbin/ldconfig

%if "%flavor" == ""

%files
%defattr(-, root, root)
%license COPYING
%_bindir/*
%_libdir/ibdiagnet%upstream_ver
%_libdir/ibdiagpath%upstream_ver

%files -n libibdm%ibdm_major
%defattr(-, root, root)
%_libdir/libibdm.so.*
%_libdir/libibdmcom.so.*
%_libdir/libibsysapi.so.*
%_libdir/ibdm%upstream_ver
%_libdir/ibis%upstream_ver

%files devel
%defattr(-, root, root)
%_includedir/ibdm
%_libdir/libibdm.so
%_libdir/libibdmcom.so
%_libdir/libibsysapi.so
%_mandir/man1/*

%else

%files
%defattr(-, root, root)
%license COPYING
%_bindir/ibdiagui
%_libdir/ibdiagui%upstream_ver
%_mandir/man1/ibdiagui*
%endif

%changelog
