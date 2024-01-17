#
# spec file for package perl-MooseX-AuthorizedMethods
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


%define cpan_name MooseX-AuthorizedMethods
Name:           perl-MooseX-AuthorizedMethods
Version:        0.006
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Syntax sugar for authorized methods
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DRUOSO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Moose) >= 1.21
BuildRequires:  perl(aliased)
Requires:       perl(Moose) >= 1.21
Requires:       perl(aliased)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Sub::Name)
# MANUAL END

%description
This method exports the "authorized" declarator that makes a verification
if the user has the required permissions before the acual invocation. The
default verification method will take the "user" method result and call
"roles" to list the roles given to that user.

%prep
%autosetup  -n %{cpan_name}-%{version}

# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc README

%changelog
