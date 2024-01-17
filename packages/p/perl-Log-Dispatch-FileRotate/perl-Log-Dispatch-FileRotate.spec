#
# spec file for package perl-Log-Dispatch-FileRotate
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Log-Dispatch-FileRotate
Name:           perl-Log-Dispatch-FileRotate
Version:        1.38
Release:        0
Summary:        Log to Files that Archive/Rotate Themselves
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Log::Dispatch) >= 2.60
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::Output)
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(Path::Tiny) >= 0.018
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(version)
Requires:       perl(Date::Manip)
Requires:       perl(Log::Dispatch) >= 2.60
Requires:       perl(Log::Dispatch::File)
Requires:       perl(Log::Dispatch::Output)
Requires:       perl(version)
%{perl_requires}

%description
This module extends the base class Log::Dispatch::Output to provides a
simple object for logging to files under the Log::Dispatch::* system, and
automatically rotating them according to different constraints. This is
basically a Log::Dispatch::File wrapper with additions.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README
%license LICENSE

%changelog
