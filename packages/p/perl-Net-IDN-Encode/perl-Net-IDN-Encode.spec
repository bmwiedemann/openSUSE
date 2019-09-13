#
# spec file for package perl-Net-IDN-Encode
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


Name:           perl-Net-IDN-Encode
Version:        2.300
Release:        0
%define cpan_name Net-IDN-Encode
Summary:        Internationalizing Domain Names in Applications (IDNA)
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-IDN-Encode/
Source0:        http://www.cpan.org/authors/id/C/CF/CFAERBER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         encodeoffbyone.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Test::NoWarnings)
%{perl_requires}

%description
This module provides an easy-to-use interface for encoding and decoding
Internationalized Domain Names (IDNs).

IDNs use characters drawn from a large repertoire (Unicode), but IDNA
allows the non-ASCII characters to be represented using only the ASCII
characters already allowed in so-called host names today
(letter-digit-hypen, '/[A-Z0-9-]/i').

Use this module if you just want to convert domain names (or email
addresses), using whatever IDNA standard is the best choice at the moment.

You should be familiar with Unicode support in perl, as this module expects
correctly encoded input. See the perlunitut manpage, the perluniintro
manpage and the perlunicode manpage for details.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644
%patch0 

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes eg LICENSE README

%changelog
