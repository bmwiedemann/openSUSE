#
# spec file for package perl-Text-Roman
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Text-Roman
Version:        3.5
Release:        0
%define cpan_name Text-Roman
Summary:        Allows conversion between Roman and Arabic algarisms.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Roman/
Source:         http://www.cpan.org/authors/id/S/SY/SYP/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Text::Roman)
%{perl_requires}

%description
This package supports both conventional Roman algarisms (which range from
_1_ to _3999_) and Milhar Romans, a variation which uses a bar across the
algarism to indicate multiplication by _1_000_. For the purposes of this
module, acceptable syntax consists of an underscore suffixed to the
algarism e.g. IV_V = _4_005_. The term Milhar apparently derives from the
Portuguese word for "thousands" and the range of this notation extends the
range of Roman numbers to _3999 * 1000 + 3999 = 4_002_999_.

Note: the functions in this package treat Roman algarisms in a
case-insensitive manner such that "VI" == "vI" == "Vi" == "vi".

The following functions may be imported into the caller package by name:

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
%doc Changes LICENSE perlcritic.rc README weaver.ini

%changelog
