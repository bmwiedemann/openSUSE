#
# spec file for package perl-MooseX-ArrayRef
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-ArrayRef
Version:        0.005
Release:        0
%define cpan_name MooseX-ArrayRef
Summary:        blessed arrayrefs with Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-ArrayRef/
Source:         http://www.cpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 2.00
Requires:       perl(Moose) >= 2.00
%{perl_requires}

%description
Objects implemented with arrayrefs rather than hashrefs are often faster
than those implemented with hashrefs. Moose's default object implementation
is hashref based. Can we go faster?

Simply 'use MooseX::ArrayRef' instead of 'use Moose', but note the
limitations in the section below.

The current implementation is mostly a proof of concept, but it does mostly
seem to work.

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
%doc Changes CONTRIBUTING COPYRIGHT CREDITS doap.ttl examples LICENSE README

%changelog
