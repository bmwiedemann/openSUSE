#
# spec file for package perl-Perl-Critic-Pulp
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Perl-Critic-Pulp
Name:           perl-Perl-Critic-Pulp
Version:        99
Release:        0
#Upstream: GPL-1.0-or-later
Summary:        Some add-on perlcritic policies
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         avoid-wrong-provides.diff
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::String) >= 1.02
BuildRequires:  perl(List::MoreUtils) >= 0.24
BuildRequires:  perl(PPI) >= 1.220
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Perl::Critic) >= 1.084
BuildRequires:  perl(Perl::Critic::Policy) >= 1.084
BuildRequires:  perl(Perl::Critic::Utils) >= 1.100
BuildRequires:  perl(Perl::Critic::Utils::PPI)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::MinimumVersion) >= 50
BuildRequires:  perl(version)
Requires:       perl(IO::String) >= 1.02
Requires:       perl(List::MoreUtils) >= 0.24
Requires:       perl(PPI) >= 1.220
Requires:       perl(PPI::Document)
Requires:       perl(PPI::Dumper)
Requires:       perl(Perl::Critic) >= 1.084
Requires:       perl(Perl::Critic::Policy) >= 1.084
Requires:       perl(Perl::Critic::Utils) >= 1.100
Requires:       perl(Perl::Critic::Utils::PPI)
Requires:       perl(Perl::Critic::Violation)
Requires:       perl(Pod::Escapes)
Requires:       perl(Pod::MinimumVersion) >= 50
Requires:       perl(version)
%{perl_requires}

%description
This is a collection of add-on policies for 'Perl::Critic'. They're under a
"pulp" theme plus other themes according to their purpose (see
Perl::Critic/POLICY THEMES).

%prep
%autosetup  -n %{cpan_name}-%{version} -p1
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license COPYING

%changelog
