#
# spec file for package perl-Role-Identifiable
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Role-Identifiable
Name:           perl-Role-Identifiable
Version:        0.009
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Thing you can identify somehow
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::TypeConstraints)
%{perl_requires}

%description
Role::Identifiable isn't really a module that does anything. It's here to
make things simpler for indexing on CPAN and looking up docs.

You probably want to use either Role::Identifiable::HasIdent, for
identifying things by an identifier string, or Role::Identifiable::HasTags
for identifying things by a list of tags.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
