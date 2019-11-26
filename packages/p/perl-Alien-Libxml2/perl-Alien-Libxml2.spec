#
# spec file for package perl-Alien-Libxml2
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           perl-Alien-Libxml2
Version:        0.11
Release:        0
%define cpan_name Alien-Libxml2
Summary:        Install the C libxml2 library on your system
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::Base) >= 0.73
BuildRequires:  perl(Alien::Build) >= 1.60
BuildRequires:  perl(Alien::Build::MM) >= 1.60
BuildRequires:  perl(Alien::Build::Plugin::Build::SearchDep) >= 0.35
BuildRequires:  perl(Alien::Build::Plugin::Prefer::BadVersion) >= 1.05
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(Test::Alien)
Requires:       perl(Alien::Base) >= 0.73
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl-URI
BuildRequires:  perl(Mojo::DOM58)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
# MANUAL END

%description
This module provides libxml2 for other modules to use. There was an already
existing Alien::LibXML, but it uses the older Alien::Build::ModuleBuild and
has not been actively maintained for a while.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -name "*.sh" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc alienfile author.yml Changes README
%license LICENSE

%changelog
