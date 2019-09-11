#
# spec file for package perl-Unicode-Stringprep
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Unicode-Stringprep
Version:        1.105
Release:        0
%define cpan_name Unicode-Stringprep
Summary:        Preparation of Internationalized Strings (S<RFC 3454>)
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Unicode-Stringprep/
Source:         http://www.cpan.org/authors/id/C/CF/CFAERBER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Unicode::Normalize) >= 1
Requires:       perl(Unicode::Normalize) >= 1
%{perl_requires}

%description
This module implements the _stringprep_ framework for preparing Unicode
text strings in order to increase the likelihood that string input and
string comparison work in ways that make sense for typical users throughout
the world. The _stringprep_ protocol is useful for protocol identifier
values, company and personal names, internationalized domain names, and
other text strings.

The _stringprep_ framework does not specify how protocols should prepare
text strings. Protocols must create profiles of stringprep in order to
fully specify the processing options.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
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
