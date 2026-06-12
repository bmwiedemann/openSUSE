#
# spec file for package perl-Config-IniFiles
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Config-IniFiles
Name:           perl-Config-IniFiles
Version:        3.001000
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Module for reading .ini-style configuration files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Build) >= 0.280
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(autodie)
BuildRequires:  perl(parent)
Requires:       perl(IO::Scalar)
Requires:       perl(List::Util) >= 1.33
%{perl_requires}

%description
Config::IniFiles provides a way to have readable configuration files
outside your Perl script. Configurations can be imported (inherited,
stacked,...), sections can be grouped, and settings can be accessed from a
tied hash.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes OLD-Changes.txt README
%license LICENSE

%changelog
