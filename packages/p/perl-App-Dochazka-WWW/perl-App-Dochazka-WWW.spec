#
# spec file for package perl-App-Dochazka-WWW
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-App-Dochazka-WWW
Version: 0.125
Release:        0
%define cpan_name App-Dochazka-WWW
Summary:        Dochazka Attendance & Time Tracking system web client
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/App-Dochazka-WWW/
Source:         App-Dochazka-WWW-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::CELL) >= 0.199
BuildRequires:  perl(App::MFILE::WWW) >= 0.134
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Module::Build) >= 0.37
BuildRequires:  perl(Params::Validate) >= 1.06
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Test::Fatal)
Requires:       perl(App::CELL) >= 0.199
Requires:       perl(App::MFILE::WWW) >= 0.134
Requires:       perl(File::ShareDir) >= 1.00
%{perl_requires}

%description
This is the web client of the Dochazka Attendance & Time Tracking system.
For more information see the App::Dochazka::REST manpage and the
App::MFILE::WWW manpage.

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
%doc Changes ignore.txt README share

%changelog
