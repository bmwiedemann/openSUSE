#
# spec file for package perl-XS-Parse-Sublike
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name XS-Parse-Sublike
Name:           perl-XS-Parse-Sublike
Version:        0.360.0
Release:        0
# 0.36 -> normalize -> 0.360.0
%define cpan_version 0.36
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        XS functions to assist in parsing sub-like syntax
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{cpan_version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test2::V0)
Requires:       perl(File::ShareDir) >= 1.00
Provides:       perl(Sublike::Extended) = %{version}
Provides:       perl(XS::Parse::Sublike) = %{version}
Provides:       perl(XS::Parse::Sublike::Builder) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides some XS functions to assist in writing parsers for
'sub'-like syntax, primarily for authors of keyword plugins using the
'PL_keyword_plugin' hook mechanism. It is unlikely to be of much use to
anyone else; and highly unlikely to be any use when writing perl code using
these. Unless you are writing a keyword plugin using XS, this module is not
for you.

This module is also currently experimental, and the design is still
evolving and subject to change. Later versions may break ABI compatibility,
requiring changes or at least a rebuild of any module that depends on it.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
