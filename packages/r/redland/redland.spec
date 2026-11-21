#
# spec file for package redland
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname	librdf0
%bcond_with perl
Name:           redland
Version:        1.0.17
Release:        0
Summary:        Libraries that provide support for the Resource Description Framework (RDF)
License:        Apache-2.0 AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.librdf.org
Source0:        https://download.librdf.org/source/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         redland-ocloexec.patch
Patch2:         redland-db6.diff
Patch3:         redland-postgresql.patch
Patch4:         redland-fix-tests.patch
Patch5:         redland-stack-overflow-fix.patch
Patch6:         redland-raptor-stringbuffer-copy.patch
BuildRequires:  autoconf
BuildRequires:  db-devel
BuildRequires:  librasqal-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  sqlite-devel

%description
Redland is a library that provides a high-level interface for RDF
(Resource Description Framework) implemented in an object-based API. It
is modular and supports different RDF parsers, serializers, storage and
query languages.  Redland is designed for developers to provide RDF
support in their applications as well as a core library for RDF
developers to start with.

%package -n libredland-devel
Summary:        Development package for programs that use Redland
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description -n libredland-devel
Files needed to develop with the Redland RDF library.

%package -n %{lname}
Summary:        Libraries that provide support for the Resource Description Framework (RDF)
Group:          System/Libraries
# Added for 13.1 time
Obsoletes:      libredland0 < %{version}-%{release}
Provides:       libredland0 = %{version}-%{release}

%description -n %{lname}
Redland is a library that provides a high-level interface for RDF
(Resource Description Framework) implemented in an object-based API. It
is modular and supports different RDF parsers, serializers, storage and
query languages.  Redland is designed for developers to provide RDF
support in their applications as well as a core library for RDF
developers to start with.

%package -n redland-storage-postgresql
Summary:        Redland storage module for PostgresSQL
Group:          System/Libraries
Requires:       redland

%description -n redland-storage-postgresql
This store provides storage using the PostgreSQL open source database
including contexts.

%prep

%autosetup -p1

%build
autoconf
%global optflags %{optflags} -D_GNU_SOURCE
# only compile bdb backend as it seems to be the recommended one?
%configure --enable-release --with-raptor=system --with-rasqal=system \
  --with-threestore=no --with-sqlite=3 \
  --with-postgresql --with-virtuoso=no \
  --without-mysql \
  --with-pic \
  --disable-static \
  --with-html-dir=%{_docdir}/%{name}-devel/ \
  --includedir=%{_includedir}/%{name}
%make_build

%install
make install DESTDIR=%{buildroot} docdir=%{_docdir}/%{name}-devel/
find %{buildroot} -type f -name "*.la" -delete -print

%check
%if 0%{?suse_version} > 1030
export MALLOC_CHECK_=2
%make_build check
unset MALLOC_CHECK_
%endif

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%{_libdir}/librdf.so.*

%files -n libredland-devel
%{_bindir}/redland-config
%{_libdir}/librdf.so
%{_libdir}/pkgconfig/redland.pc
%dir %{_libdir}/redland
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/Redland.i
%{_includedir}/%{name}/
%{_mandir}/man1/redland-config.1%{?ext_man}
%{_mandir}/man3/redland.3%{?ext_man}
%doc %{_docdir}/%{name}-devel/

%files -n redland-storage-postgresql
%{_libdir}/redland/librdf_storage_postgresql.so

%files
%{_bindir}/rdfproc
%{_bindir}/redland-db-upgrade
%{_libdir}/redland/librdf_storage_sqlite.so
%{_mandir}/man1/redland-db-upgrade.1%{?ext_man}
%{_mandir}/man1/rdfproc.1%{?ext_man}
%license COPYING COPYING.LIB LICENSE.txt LICENSE-2.0.txt
%doc AUTHORS ChangeLog NEWS README NOTICE

%changelog
