#
# spec file for package mytop
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mytop
Version:        1.6
Release:        0
Summary:        A top Clone for MySQL
License:        GPL-2.0+
Group:          Productivity/Databases/Tools
Url:            http://jeremy.zawodny.com/mysql/mytop/
Source:         http://jeremy.zawodny.com/mysql/mytop/mytop-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mytop_five_o.patch -- makes it work with mysql 5.0
Patch1:         http://ebergen.net/patches/mytop_five_o.patch
# PATCH-FIX-UPSTREAM mytop_option-and-doc.patch [bnc#716439] cwh@suse.de -- fixed starting failure and documentation
Patch2:         mytop_option-and-doc.patch
Requires:       perl = %{perl_version}
Requires:       perl-DBD-mysql
Requires:       perl-DBI
Requires:       perl-TermReadKey
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if %{undefined suse_version}
BuildRequires:  perl-macros
%endif

%description
mytop is a console-based (non-GUI) tool for monitoring the threads and
overall performance of MySQL 3.22.x, 3.23.x, and 4.x servers.

- With Term::ANSIColor installed you even get color.

- If you install Time::HiRes, get good real-time queries/second stats.

%prep
%setup -q -n mytop-%{version}
%patch1
%patch2 -p1

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%files
%defattr(-,root,root,-)
%doc Changes
%{_mandir}/man?/mytop.1.gz
%{_bindir}/mytop
%if 0%{?suse_version} < 1140
%{perl_vendorarch}/auto/mytop
%{_localstatedir}/adm/perl-modules/%{name}
%endif

%changelog
