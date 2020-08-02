#
# spec file for package perl-Log-Dispatch-Config
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-Log-Dispatch-Config
Version:        1.04
Release:        0
%define cpan_name Log-Dispatch-Config
Summary:        Log4j for Perl
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Log-Dispatch-Config/
Source:         http://www.cpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AppConfig) >= 1.52
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp) >= 0.12
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Log::Dispatch) >= 2
BuildRequires:  perl(Test::More) >= 0.32
Requires:       perl(AppConfig) >= 1.52
Requires:       perl(File::Temp) >= 0.12
Requires:       perl(IO::Scalar)
Requires:       perl(Log::Dispatch) >= 2
Requires:       perl(Test::More) >= 0.32
%{perl_requires}

%description
Log::Dispatch::Config is a subclass of Log::Dispatch and provides a way to
configure Log::Dispatch object with configulation file (default, in
AppConfig format). I mean, this is log4j for Perl, not with all API
compatibility though.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
