#
# spec file for package perl-String-Print
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name String-Print
Name:           perl-String-Print
Version:        1.20.0
Release:        0
# 1.02 -> normalize -> 1.20.0
%define cpan_version 1.02
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Printf extensions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Parse) >= 2.300
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1
BuildRequires:  perl(Unicode::GCString)
Requires:       perl(Date::Parse) >= 2.300
Requires:       perl(HTML::Entities)
Requires:       perl(Test::More) >= 0.86
Requires:       perl(Unicode::GCString)
Provides:       perl(String::Print) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module inserts values into (format) strings. It provides 'printf()'
and 'sprintf()' alternatives via both an object oriented and a functional
interface.

Read in the DETAILS chapter below, why this module provides a better
alternative for 'printf()'. Also, some extended *examples* can be found
down there. Take a look at them first, when you start using this module!

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog README.md

%changelog
