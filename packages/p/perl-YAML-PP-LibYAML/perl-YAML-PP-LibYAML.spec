#
# spec file for package perl-YAML-PP-LibYAML
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-YAML-PP-LibYAML
Version:        0.005
Release:        0
%define cpan_name YAML-PP-LibYAML
Summary:        Faster parsing for YAML::PP
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(YAML::LibYAML::API) >= 0.011
BuildRequires:  perl(YAML::LibYAML::API::XS)
BuildRequires:  perl(YAML::PP) >= 0.025
BuildRequires:  perl(YAML::PP::Common)
BuildRequires:  perl(YAML::PP::Emitter)
BuildRequires:  perl(YAML::PP::Parser)
BuildRequires:  perl(YAML::PP::Reader)
BuildRequires:  perl(YAML::PP::Writer)
Requires:       perl(YAML::LibYAML::API) >= 0.011
Requires:       perl(YAML::LibYAML::API::XS)
Requires:       perl(YAML::PP) >= 0.025
Requires:       perl(YAML::PP::Emitter)
Requires:       perl(YAML::PP::Parser)
Requires:       perl(YAML::PP::Reader)
Requires:       perl(YAML::PP::Writer)
%{perl_requires}

%description
YAML::PP::LibYAML is a subclass of YAML::PP. Instead of using
YAML::PP::Parser as a the backend parser, it uses YAML::PP::LibYAML::Parser
which calls YAML::LibYAML::API, an XS wrapper around the 'C libyaml'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README README.md
%license LICENSE

%changelog
