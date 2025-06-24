#
# spec file for package perl-Test-Deep-JSON
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


%define cpan_name Test-Deep-JSON
Name:           perl-Test-Deep-JSON
Version:        0.50.0
Release:        0
# 0.05 -> normalize -> 0.50.0
%define cpan_version 0.05
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Compare JSON with Test::Deep
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MOTEMEN/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Lite)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Tester)
Requires:       perl(Exporter::Lite)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(Test::Deep)
Provides:       perl(Test::Deep::JSON) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Test::Deep::JSON provides the 'json($expected)' function to expect that
target can be parsed as a JSON string and matches (by 'cmp_deeply') with
_$expected_.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
