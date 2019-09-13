#
# spec file for package perl-App-MFILE
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-App-MFILE
Version:        0.182
Release:        0
%define cpan_name App-MFILE
Summary:        MFILE shared modules
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/App-MFILE/
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMITHFARM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::CELL) >= 0.222
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build) >= 0.370000
BuildRequires:  perl(Params::Validate) >= 1.06
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Test::Fatal)
Requires:       perl(App::CELL) >= 0.222
Requires:       perl(HTTP::Request::Common)
Requires:       perl(JSON)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Params::Validate) >= 1.06
%{perl_requires}

%description
This distro consists of general, reusable modules. Currently, there is only
one module, App::MFILE::HTTP, which is used by App::MFILE::WWW,
App::Dochazka::WWW, and App::Dochazka::CLI.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.rst
%license LICENSE

%changelog
