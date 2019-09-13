#
# spec file for package perl-Set-Crontab
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-Set-Crontab
Version:        1.03
Release:        3
AutoReqProv:    on
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Url:            http://cpan.org/modules/by-module/Set
Summary:        Expand crontab(5)-style integer lists
Source0:        http://cpan.org/modules/by-module/Set/Set-Crontab-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Set::Crontab parses crontab-style lists of integers and defines some
utility functions to make it easier to deal with them.



Authors:
--------
    Abhijit Menon-Sen <ams@wiw.org>

%prep
%setup -q -n Set-Crontab-%{version}

%build
# replace rest of /usr/local/bin/perl with /usr/bin/perl
for f in `find . -type f -exec grep -l /usr/local/bin/perl \{\} \;` ; do
    rm -f tmp
    sed -e "s:^#!.*/usr/local/bin/perl:#!/usr/bin/perl:g" $f > tmp
    mv -f tmp $f
done
perl Makefile.PL
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Set
%{perl_vendorarch}/auto/Set

%changelog
