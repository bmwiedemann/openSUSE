#
# spec file for package perl-App-Dochazka-Common
#
# Copyright (c) 2022 SUSE LLC
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


Name:           perl-App-Dochazka-Common
Version:        0.210
Release:        0
%define cpan_name App-Dochazka-Common
Summary:        Dochazka Attendance and Time Tracking System shared modules
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/App-Dochazka-Common/
Source0:        App-Dochazka-Common-0.210.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.370000
BuildRequires:  perl(Params::Validate) >= 1.06
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Test::Deep::NoTest)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Seconds)
Requires:       perl(Params::Validate) >= 1.06
Requires:       perl(Test::Deep::NoTest)
Requires:       perl(Time::Piece)
Requires:       perl(Time::Seconds)
%{perl_requires}

%description
This distro contains modules that are used by both the server the
App::Dochazka::REST manpage and the command-line client the
App::Dochazka::CLI manpage.

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
%doc Changes LICENSE README.rst

%changelog
