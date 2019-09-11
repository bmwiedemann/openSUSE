#
# spec file for package pg_comparator
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Aldemir Akpinar <aldemir.akpinar@gmail.com>
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


#
%define pglibdir %{expand:%%(/usr/bin/pg_config --pkglibdir)}
%define pgdocdir %{expand:%%(/usr/bin/pg_config --docdir)}

Name:           pg_comparator
Version:        2.2.5
Release:        1%{?dist}
Summary:        A tool to compare and sync tables in different locations
License:        BSD-3-Clause
Group:          Development/Libraries

Url:            http://pgfoundry.org/projects/pg-comparator/
Source:         http://pgfoundry.org/frs/download.php/3661/pg_comparator-%{version}.tgz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  postgresql-devel
%if 0%{?suse_version} > 1500
BuildRequires:  postgresql-server-devel
%endif
Requires:       perl
Requires:       perl-DBD-Pg
Requires:       perl-DBD-mysql
Requires:       postgresql

%description
PgComparator is a tool to compare possibly very big tables in different locations and report differences, with a network and time-efficient approach.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
#%makeinstall
install -d %{buildroot}/%{pglibdir}/%{_lib}
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{pgdocdir}
install -d %{buildroot}/%{pgdocdir}/contrib
install pgc_casts.so %{buildroot}/%{pglibdir}/%{_lib}/pgc_casts.so
install pgc_checksum.so %{buildroot}/%{pglibdir}/%{_lib}/pgc_checksum.so
install pg_comparator %{buildroot}/%{_bindir}/pg_comparator
install LICENSE %{buildroot}/%{pgdocdir}/LICENSE
install README.pgc_checksum %{buildroot}/%{pgdocdir}/README.pgc_checksum
install README.pgc_casts %{buildroot}/%{pgdocdir}/README.pgc_casts
install README.pg_comparator %{buildroot}/%{pgdocdir}/README.pg_comparator
install README.xor_aggregate %{buildroot}/%{pgdocdir}/README.xor_aggregate
install pgc_casts.sql %{buildroot}/%{pgdocdir}/contrib/pgc_casts.sql
install pgc_checksum.sql %{buildroot}/%{pgdocdir}/contrib/pgc_checksum.sql
install xor_aggregate.sql %{buildroot}/%{pgdocdir}/contrib/xor_aggregate.sql

%files
%defattr(-, root, root, -)
%{_bindir}/pg_comparator
%dir %{pglibdir}
%dir %{pglibdir}/%{_lib}
%{pglibdir}/%{_lib}/pgc_casts.so
%{pglibdir}/%{_lib}/pgc_checksum.so
%defattr(644, root, root, 755)
%dir %{pgdocdir}
%dir %{pgdocdir}/contrib
%doc %{pgdocdir}/LICENSE
%doc %{pgdocdir}/README.pgc_checksum
%doc %{pgdocdir}/README.pgc_casts
%doc %{pgdocdir}/README.pg_comparator
%doc %{pgdocdir}/README.xor_aggregate

%{pgdocdir}/contrib/pgc_casts.sql
%{pgdocdir}/contrib/pgc_checksum.sql
%{pgdocdir}/contrib/xor_aggregate.sql

%changelog
