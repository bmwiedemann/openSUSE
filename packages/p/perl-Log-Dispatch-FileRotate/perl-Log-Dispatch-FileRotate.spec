#
# spec file for package perl-Log-Dispatch-FileRotate
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Log-Dispatch-FileRotate
Version:        1.36
Release:        0
%define cpan_name Log-Dispatch-FileRotate
Summary:        Log to Files that Archive/Rotate Themselves
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Log-Dispatch-FileRotate/
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::Output)
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(Path::Tiny) >= 0.018
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(version)
Requires:       perl(Date::Manip)
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
