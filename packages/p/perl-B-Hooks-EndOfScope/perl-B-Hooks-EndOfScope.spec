#
# spec file for package perl-B-Hooks-EndOfScope
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-B-Hooks-EndOfScope
Version:        0.24
Release:        0
%define cpan_name B-Hooks-EndOfScope
Summary:        Execute code after a scope finished compilation
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/B-Hooks-EndOfScope/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Module::Implementation) >= 0.05
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001006
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Variable::Magic) >= 0.48
Requires:       perl(Hash::Util::FieldHash)
Requires:       perl(Module::Implementation) >= 0.05
Requires:       perl(Sub::Exporter::Progressive) >= 0.001006
Requires:       perl(Variable::Magic) >= 0.48
%{perl_requires}

%description
This module allows you to execute code when perl finished compiling the
surrounding scope.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTING LICENCE README

%changelog
