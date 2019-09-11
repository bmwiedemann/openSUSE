#
# spec file for package perl-Text-Iconv
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

# norootforbuild


Name:           perl-Text-Iconv
%define cpan_name Text-Iconv
Summary:        Perl interface to iconv() codeset conversion function
Version:        1.7
Release:        7
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Iconv
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
The Text::Iconv module provides a Perl interface to the iconv() function as
defined by the Single UNIX Specification.

The convert() method converts the encoding of characters in the input string
from the fromcode codeset to the tocode codeset, and returns the result.

Settings of fromcode and tocode and their permitted combinations are
implementation-dependent. Valid values are specified in the system
documentation; the iconv(1) utility should also provide a -l option that lists
all supported codesets.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
# normally you only need to check for doc files
%defattr(-,root,root,)
%doc Changes README

%changelog
