#
# spec file for package perl-Module-Starter
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


Name:           perl-Module-Starter
Version:        1.77
Release:        0
%define cpan_name Module-Starter
Summary:        Simple starter kit for any module
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Software::License) >= 0.103005
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(parent)
BuildRequires:  perl(version) >= 0.77
Requires:       perl(Module::Runtime)
Requires:       perl(Software::License) >= 0.103005
Requires:       perl(Test::More) >= 0.94
Requires:       perl(parent)
Requires:       perl(version) >= 0.77
%{perl_requires}

%description
This is the core module for Module::Starter. If you're not looking to
extend or alter the behavior of this module, you probably want to look at
module-starter instead.

Module::Starter is used to create a skeletal CPAN distribution, including
basic builder scripts, tests, documentation, and module code. This is done
through just one method, 'create_distro'.

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
%doc Changes CONTRIBUTING.md getting-started.html prereqs.yml README
%license LICENSE

%changelog
