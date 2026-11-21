#
# spec file for package perl-Math-Clipper
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Math-Clipper
Name:           perl-Math-Clipper
Version:        1.300.0
Release:        0
# 1.30 -> normalize -> 1.300.0
%define cpan_version 1.30
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Polygon clipping in 2D
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.270
BuildRequires:  perl(ExtUtils::Typemaps::Default) >= 1.60
BuildRequires:  perl(ExtUtils::XSpp) >= 0.180
BuildRequires:  perl(Module::Build) >= 0.380
BuildRequires:  perl(Module::Build::WithXSpp) >= 0.140
BuildRequires:  perl(Test::Deep)
Provides:       perl(Math::Clipper) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'Clipper' is a C++ (and Delphi) library that implements polygon clipping.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
