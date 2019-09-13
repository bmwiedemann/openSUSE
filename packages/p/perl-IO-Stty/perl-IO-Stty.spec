#
# spec file for package perl-IO-Stty (Version 0.03)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild

%bcond_with pod

Name:           perl-IO-Stty
%define cpan_name IO-Stty
Summary:        IO::Stty Perl module
Version:        0.03
Release:        2
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-Stty/
Source:         http://www.cpan.org/modules/by-module/IO/IO-Stty-%{version}.tar.gz
#Source:         %{cpan_name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl(Module::Build)
BuildRequires:  perl-macros
%if %{with pod}
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
#

%description
This is the PERL POSIX compliant stty.

Authors:
--------
    Austin Schutz <auschutz@cpan.org>
    Todd Rinaldo <toddr@cpan.org>

%prep
%setup -q -n %{cpan_name}-%{version}
#rpmlint: wrong-script-interpreter
%{__sed} -i -e "s@/usr/local/perl/bin/perl@%{__perl}@" scripts/stty.pl

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes README scripts

%changelog
