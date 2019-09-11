#
# spec file for package perl-Regexp-Common
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Regexp-Common
Version:        2017060201
Release:        0
#Upstream: SUSE-Public-Domain
%define cpan_name Regexp-Common
Summary:        Provide commonly requested regular expressions
License:        Artistic-1.0 or Artistic-2.0 or BSD-3-Clause or MIT
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Regexp-Common/
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
By default, this module exports a single hash ('%RE') that stores or
generates commonly needed regular expressions (see "List of available
patterns").

There is an alternative, subroutine-based syntax described in
"Subroutine-based interface".

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes COPYRIGHT COPYRIGHT.AL COPYRIGHT.AL2 COPYRIGHT.BSD COPYRIGHT.MIT README TODO
%license LICENSE

%changelog
