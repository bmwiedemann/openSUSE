#
# spec file for package perl-List-MoreUtils
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-List-MoreUtils
Version:        0.430
Release:        0
%define cpan_name List-MoreUtils
Summary:        Provide the stuff missing in List::Util
License:        Apache-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Tiny) >= 0.038
BuildRequires:  perl(List::MoreUtils::XS) >= 0.430
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Exporter::Tiny) >= 0.038
Requires:       perl(List::MoreUtils::XS) >= 0.430
%{perl_requires}

%description
*List::MoreUtils* provides some trivial but commonly needed functionality
on lists which is not going to go into List::Util.

All of the below functions are implementable in only a couple of lines of
Perl code. Using the functions from this module however should give
slightly better performance as everything is implemented in C. The
pure-Perl implementation of these functions only serves as a fallback in
case the C portions of this module couldn't be compiled on this machine.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes GPL-1 README.md
%license ARTISTIC-1.0 LICENSE

%changelog
