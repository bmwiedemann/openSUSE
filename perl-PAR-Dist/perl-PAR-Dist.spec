#
# spec file for package perl-PAR-Dist
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


Name:           perl-PAR-Dist
Version:        0.49
Release:        0
%define cpan_name PAR-Dist
Summary:        Create and manipulate PAR distributions
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/PAR-Dist/
Source:         http://www.cpan.org/authors/id/R/RS/RSCHUPP/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Archive::Unzip::Burst)
#BuildRequires: perl(Archive::Zip)
#BuildRequires: perl(LWP::Simple)
#BuildRequires: perl(Module::Signature)
#BuildRequires: perl(PAR::Dist)
%{perl_requires}

%description
This module creates and manipulates _PAR distributions_. They are
architecture-specific *PAR* files, containing everything under _blib/_ of
CPAN distributions after their 'make' or 'Build' stage, a _META.yml_
describing metadata of the original CPAN distribution, and a _MANIFEST_
detailing all files within it. Digitally signed PAR distributions will also
contain a _SIGNATURE_ file.

The naming convention for such distributions is:

    $NAME-$VERSION-$ARCH-$PERL_VERSION.par

For example, 'PAR-Dist-0.01-i386-freebsd-5.8.0.par' corresponds to the 0.01
release of 'PAR-Dist' on CPAN, built for perl 5.8.0 running on
'i386-freebsd'.

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
%doc Changes README

%changelog
