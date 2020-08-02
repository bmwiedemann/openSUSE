#
# spec file for package perl-Text-DelimMatch
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Text-DelimMatch
%define module_name DelimMatch
%define module_version 1.06
Summary:        DelimMatch for Locating Delimited Substrings with Proper Nesting
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Version:        1.06
Release:        0
Source0:        %{module_name}-1.06a.tar.gz
Url:            http://search.cpan.org/~nwalsh/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
DelimMatch is a Perl 5 module that provides functions for locating
delimited substrings with proper nesting.

%prep
%setup -q -n %{module_name}-%{module_version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist

%files
%defattr(-, root, root)
%doc  README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/auto/Text
%{perl_vendorlib}/auto/Text
%{perl_vendorlib}/Text

%changelog
