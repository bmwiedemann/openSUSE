#
# spec file for package tdb
#
# Copyright (c) 2023 SUSE LLC
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


%{!?python_sitearch:  %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?py3_soflags:  %global py3_soflags cpython-%{python3_version_nodots}m}
Name:           tdb
Version:        1.4.8
Release:        0
Summary:        Samba Trivial Database
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://tdb.samba.org/
Source:         https://download.samba.org/pub/tdb/tdb-%{version}.tar.gz
Source1:        https://download.samba.org/pub/tdb/tdb-%{version}.tar.asc
Source2:        tdb.keyring
Source4:        baselibs.conf
Patch0:         build_pie.patch
BuildRequires:  autoconf
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  python3-devel

%description
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB,
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other.

%package -n libtdb1
Summary:        Samba Trivial Database
Group:          System/Libraries

%description -n libtdb1
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB,
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other.

This package contains the tdb1 library.

%package -n libtdb-devel
Summary:        Libraries and Header Files to Develop Programs with tdb1 Support
Group:          Development/Libraries/C and C++
Requires:       libtdb1 = %{version}
Requires:       pkgconfig

%description -n libtdb-devel
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB,
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other.

This package contains libraries and header files need for development.

%package -n tdb-tools
Summary:        Tools to manipulate tdb files
Group:          Development/Libraries/C and C++

%description -n tdb-tools
TDB is a Trivial Database. In concept, it is very much like GDBM, and BSD's DB,
except that it allows multiple simultaneous writers and uses locking
internally to keep writers from trampling on each other.

This package contains tools to manage Tdb files.

%package -n python3-tdb
Summary:        Python3 bindings for the Tdb library
Group:          Development/Libraries/Python
Requires:       libtdb1 = %{version}
Obsoletes:      python-tdb

%description -n python3-tdb
This package contains the Python3 bindings for the Tdb library.

%prep
%setup -q -n tdb-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -DIDMAP_RID_SUPPORT_TRUSTED_DOMAINS"
./configure --prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-rpath \
	--disable-rpath-install \
	--disable-silent-rules \
	--bundled-libraries=NONE

%make_build all
doxygen doxy.config

%check
%if 0%{!?qemu_user_space_build:1}
%make_build test
%endif

%install
%make_install
# Install API documentation
mkdir -p %{buildroot}/%{_mandir}/man3/
cp -a docs/man/man3/tdb.3 %{buildroot}/%{_mandir}/man3/

%post -n libtdb1 -p /sbin/ldconfig
%postun -n libtdb1 -p /sbin/ldconfig

%files -n libtdb1
%{_libdir}/libtdb.so.*

%files -n libtdb-devel
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc
%{_mandir}/man3/tdb.3%{?ext_man}

%files -n tdb-tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbrestore
%{_bindir}/tdbtool
%{_mandir}/man8/tdbbackup.8%{?ext_man}
%{_mandir}/man8/tdbdump.8%{?ext_man}
%{_mandir}/man8/tdbrestore.8%{?ext_man}
%{_mandir}/man8/tdbtool.8%{?ext_man}

%files -n python3-tdb
%{python3_sitearch}/tdb.%{py3_soflags}.so
%{python3_sitearch}/_tdb_text.py
%if 0%{?centos_version} > 599 || 0%{?fedora_version} > 11 || 0%{?rhel_version} > 599
%{python3_sitearch}/__pycache__/_tdb_text.cpython-*.py[co]
%endif

%changelog
