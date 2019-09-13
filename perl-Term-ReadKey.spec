#
# spec file for package perl-Term-ReadKey
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Term-ReadKey
Version:        2.38
Release:        0
Summary:        Module for Simple Terminal Control
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/pod/Term::ReadKey
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.58
Requires:       /bin/stty
Provides:       perl-TermReadKey = %{version}
Obsoletes:      perl-TermReadKey <= 2.30
%{perl_requires}

%description
This module, ReadKey, provides ioctl control for terminals and Win32 consoles
so the input modes can be changed (thus allowing reads of a single character at
a time), and also provides non-blocking reads of stdin, as well as several
other terminal related features, including retrieval/modification of the screen
size, and retrieval/modification of the control characters.

%prep
%setup -q -n "TermReadKey-%{version}"
sed -i '/^auto_install/d' Makefile.PL

%build
perl Makefile.PL PREFIX="%{_prefix}"
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist

%check
# s390/s390x don't have /dev/tty
%ifnarch s390 s390x
make %{?_smp_mflags} test
%endif

%files
%doc README
%dir %{perl_vendorarch}/Term
%{perl_vendorarch}/Term/ReadKey.pm
%dir %{perl_vendorarch}/auto/Term
%{perl_vendorarch}/auto/Term/ReadKey
%doc %{perl_man3dir}/Term::ReadKey.%{perl_man3ext}%{ext_man}

%changelog
