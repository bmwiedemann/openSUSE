#
# spec file for package perl-PkgConfig
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


%define cpan_name PkgConfig
Name:           perl-PkgConfig
Version:        0.26026
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Pure-Perl Core-Only replacement for pkg-config
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.56
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Test::More) >= 0.94
%{perl_requires}

%description
'PkgConfig' provides a pure-perl, core-only replacement for the
'pkg-config' utility.

This is not a description of the uses of 'pkg-config' but rather a
description of the differences between the C version and the Perl one.

While 'pkg-config' is a compiled binary linked with glib, the pure-perl
version has no such requirement, and will run wherever Perl ( >= 5.6 )
does.

The main supported options are the common '--libs', '--cflags', '--static',
'--exists' and '--modversion'.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes ignore.txt PkgConfig.kpf README README.win32
%license LICENSE

%changelog
