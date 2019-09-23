#
# spec file for package perl-Parse-Method-Signatures
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


Name:           perl-Parse-Method-Signatures
Version:        1.003019
Release:        0
%define cpan_name Parse-Method-Signatures
Summary:        Perl6 like method signature parser
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Parse-Method-Signatures/
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load) >= 0.19
BuildRequires:  perl(List::MoreUtils) >= 0.20
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Traits) >= 0.06
BuildRequires:  perl(MooseX::Types) >= 0.17
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(PPI) >= 1.203
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(aliased)
BuildRequires:  perl(namespace::clean) >= 0.10
Requires:       perl(Class::Load) >= 0.19
Requires:       perl(List::MoreUtils) >= 0.20
Requires:       perl(Moose)
Requires:       perl(MooseX::Traits) >= 0.06
Requires:       perl(MooseX::Types) >= 0.17
Requires:       perl(MooseX::Types::Moose)
Requires:       perl(MooseX::Types::Structured)
Requires:       perl(PPI) >= 1.203
Requires:       perl(namespace::clean) >= 0.10
%{perl_requires}

%description
Inspired by Perl6::Signature but streamlined to just support the subset
deemed useful for TryCatch and MooseX::Method::Signatures.

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
%doc Changes

%changelog
