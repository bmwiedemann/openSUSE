#
# spec file for package perl-Geo-Coordinates-UTM
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Geo-Coordinates-UTM
%define cpan_name Geo-Coordinates-UTM
Summary:        Perl extension for Latitude Longitude conversions
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Version:        0.11
Release:        0
Url:            http://search.cpan.org/dist/Geo-Coordinates-UTM/
Source:         http://www.cpan.org/authors/id/G/GR/GRAHAMC/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
This module will translate latitude longitude coordinates to Universal
Transverse Mercator(UTM) coordinates and vice versa.

%prep
%setup -q -n %{cpan_name}-%{version}
### rpmlint:
# spurious-executable-perm
%{__chmod} 0644 README Changes
# script-without-shebang
%{__chmod} 0644 UTM.pm 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes README

%changelog
