#
# spec file for package perl-MooX-StrictConstructor
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name MooX-StrictConstructor
Name:           perl-MooX-StrictConstructor
Version:        0.13.0
Release:        0
# 0.013 -> normalize -> 0.13.0
%define cpan_version 0.013
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Make your Moo-based object constructors blow up on unknown attributes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moo) >= 2.004000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Moo) >= 2.004000
Requires:       perl(Moo::Role)
Provides:       perl(MooX::StrictConstructor) = %{version}
Provides:       perl(MooX::StrictConstructor::Role::BuildAll) = %{version}
Provides:       perl(MooX::StrictConstructor::Role::Constructor) = %{version}
Provides:       perl(MooX::StrictConstructor::Role::Constructor::Base) = %{version}
Provides:       perl(MooX::StrictConstructor::Role::Constructor::Late) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Simply loading this module makes your constructors "strict". If your
constructor is called with an attribute init argument that your class does
not declare, then it dies. This is a great way to catch small typos.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
