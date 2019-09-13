#
# spec file for package perl-Algorithm-Annotate
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



Name:           perl-Algorithm-Annotate
Version:        0.10
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Algorithm-Annotate
Summary:        represent a series of changes in annotate form
Url:            http://search.cpan.org/dist/Algorithm-Annotate/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/C/CL/CLKAO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::Diff) >= 1.15
Requires:       perl(Algorithm::Diff) >= 1.15
%{perl_requires}

%description
Algorithm::Annotate generates a list that is useful for generating output
simliar to 'cvs annotate'.

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

%files -f %{name}.files
%defattr(-,root,root,755)

%changelog
