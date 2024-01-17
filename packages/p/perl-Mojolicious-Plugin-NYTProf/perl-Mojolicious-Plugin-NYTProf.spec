#
# spec file for package perl-Mojolicious-Plugin-NYTProf
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


Name:           perl-Mojolicious-Plugin-NYTProf
Version:        0.23
Release:        0
%define cpan_name Mojolicious-Plugin-NYTProf
Summary:        Auto handling of Devel::NYTProf in your Mojolicious app
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEEJO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::Combinatorics) >= 0.27
BuildRequires:  perl(Devel::NYTProf) >= 6.06
BuildRequires:  perl(File::Spec::Functions) >= 3.30
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(File::Which) >= 1.09
BuildRequires:  perl(Mojolicious) >= 8.00
BuildRequires:  perl(Test::Exception) >= 0.320000
BuildRequires:  perl(Time::HiRes) >= 1.9719
Requires:       perl(Devel::NYTProf) >= 6.06
Requires:       perl(File::Spec::Functions) >= 3.30
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(File::Which) >= 1.09
Requires:       perl(Mojolicious) >= 8.00
Requires:       perl(Time::HiRes) >= 1.9719
%{perl_requires}

%description
This plugin enables Mojolicious to automatically generate Devel::NYTProf
profiles and routes for your app, it has been inspired by
Dancer::Plugin::NYTProf

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
%doc Changes README.md

%changelog
