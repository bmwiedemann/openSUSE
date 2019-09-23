#
# spec file for package perl-UNIVERSAL-isa
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-UNIVERSAL-isa
Version:        1.20171012
Release:        0
%define cpan_name UNIVERSAL-isa
Summary:        Attempt to recover from people calling UNIVERSAL::isa as a function
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/UNIVERSAL-isa/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Whenever you use UNIVERSAL/isa as a function, a kitten using
Test::MockObject dies. Normally, the kittens would be helpless, but if they
use UNIVERSAL::isa (the module whose docs you are reading), the kittens can
live long and prosper.

This module replaces 'UNIVERSAL::isa' with a version that makes sure that,
when called as a function on objects which override 'isa', 'isa' will call
the appropriate method on those objects

In all other cases, the real 'UNIVERSAL::isa' gets called directly.

*NOTE:* You should use this module only for debugging purposes. It does not
belong as a dependency in running code.

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
%doc Changes CONTRIBUTING LICENCE README

%changelog
