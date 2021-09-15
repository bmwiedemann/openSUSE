#
# spec file for package perl-Regexp-Trie
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Regexp-Trie
Name:           perl-Regexp-Trie
Version:        0.02
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Builds trie-ized regexp
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module is a faster but simpler version of Regexp::Assemble or
Regexp::Optimizer. It builds a trie-ized regexp as above.

This module is faster than Regexp::Assemble but you can only add literals.
'a+b' is treated as 'a\+b', not "more than one a's followed by b".

I wrote this module because I needed something faster than Regexp::Assemble
and Regexp::Optimizer. If you need more minute control, use those instead.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
