#
# spec file for package perl-Config-Simple
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


Name:           perl-Config-Simple
%define cpan_name Config-Simple
Summary:        Simple configuration file class
Url:            http://search.cpan.org/perldoc?Config::Simple
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Version:        4.59
Release:        2
Source:         http://search.cpan.org/CPAN/authors/id/S/SH/SHERZODR/%{cpan_name}-%{version}.tar.gz
Requires:       perl(AutoLoader)
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
Reading and writing configuration files is one of the most frequent tasks of
any software design. Config::Simple is the library that helps you with it.

Config::Simple is a class representing configuration file object. It supports
several configuration file syntax and tries to identify the file syntax
automatically. Library supports parsing, updating and creating configuration
files.

%prep
%setup -q -n %{cpan_name}-%{version}
# rpmlint: executable-docs, script-without-shebang
chmod 644 Changes README Simple.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%dir %perl_vendorlib/Config
%perl_vendorlib/Config/Simple.pm
%dir %{perl_vendorlib}/auto/Config
%dir %{perl_vendorlib}/auto/Config/Simple
%{perl_vendorlib}/auto/Config/Simple/*
%dir %{perl_vendorarch}/auto/Config
%dir %{perl_vendorarch}/auto/Config/Simple
%{_mandir}/man3/Config::Simple.3pm.gz

%changelog
