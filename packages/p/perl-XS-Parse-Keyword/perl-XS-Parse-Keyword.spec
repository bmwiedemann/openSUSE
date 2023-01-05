#
# spec file for package perl-XS-Parse-Keyword
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name XS-Parse-Keyword
Name:           perl-XS-Parse-Keyword
Version:        0.31
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        XS functions to assist in parsing keyword syntax
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CChecker) >= 0.11
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.16
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
This module provides some XS functions to assist in writing syntax modules
that provide new perl-visible syntax, primarily for authors of keyword
plugins using the 'PL_keyword_plugin' hook mechanism. It is unlikely to be
of much use to anyone else; and highly unlikely to be any use when writing
perl code using these. Unless you are writing a keyword plugin using XS,
this module is not for you.

This module is also currently experimental, and the design is still
evolving and subject to change. Later versions may break ABI compatibility,
requiring changes or at least a rebuild of any module that depends on it.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
