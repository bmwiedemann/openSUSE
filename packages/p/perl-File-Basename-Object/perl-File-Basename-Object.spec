#
# spec file for package perl-File-Basename-Object
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


Name:           perl-File-Basename-Object
Url:            http://cpan.org/modules/by-module/File/
License:        Artistic-1.0
Group:          Development/Libraries/Perl
AutoReqProv:    on
Summary:        Object-oriented syntax sugar for File::Basename
Version:        0.01
Release:        47
Source:         File-Basename-Object-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
File::Basename::Object is an object-oriented wrapper around
File::Basename. The goal is to allow pathnames to be presented and
manipulated easily.



Authors:
--------
    Tyler "Crackerjack" MacDonald <japh@crackerjack.net>

%prep
%setup -n File-Basename-Object-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make test

%install
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Basename
%{perl_vendorlib}/File/Basename/Object.pm
%dir %{perl_vendorarch}/auto/File
%dir %{perl_vendorarch}/auto/File/Basename/
%dir %{perl_vendorarch}/auto/File/Basename/Object
%{_mandir}/man3/*

%changelog
