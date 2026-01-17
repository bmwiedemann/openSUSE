#
# spec file for package perl-Module-Starter
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


%define cpan_name Module-Starter
Name:           perl-Module-Starter
Version:        1.820.0
Release:        0
# 1.82 -> normalize -> 1.820.0
%define cpan_version 1.82
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple starter kit for any module
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Software::License) >= 0.103.5
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(parent)
BuildRequires:  perl(version) >= 0.77
Requires:       perl(Module::Runtime)
Requires:       perl(Software::License) >= 0.103.5
Requires:       perl(Test::More) >= 0.94
Requires:       perl(parent)
Requires:       perl(version) >= 0.77
Provides:       perl(Module::Starter) = %{version}
Provides:       perl(Module::Starter::App) = %{version}
Provides:       perl(Module::Starter::BuilderSet) = %{version}
Provides:       perl(Module::Starter::Plugin::Template) = %{version}
Provides:       perl(Module::Starter::Simple) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This is the core module for Module::Starter. If you're not looking to
extend or alter the behavior of this module, you probably want to look at
module-starter instead.

Module::Starter is used to create a skeletal CPAN distribution, including
basic builder scripts, tests, documentation, and module code. This is done
through just one method, 'create_distro'.

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
%doc Changes CONTRIBUTING.md getting-started.html README
%license LICENSE

%changelog
