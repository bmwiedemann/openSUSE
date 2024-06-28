#
# spec file for package perl-GD
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name GD
Name:           perl-GD
Version:        2.830.0
Release:        0
# 2.83 -> normalize -> 2.830.0
%define cpan_version 2.83
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to the libgd graphics library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         GD-cflags.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Constant) >= 0.22
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Test::Fork) >= 0.02
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings) >= 1.00
Provides:       perl(GD) = %{version}
Provides:       perl(GD::Group) = 1.00
Provides:       perl(GD::Image) = %{version}
Provides:       perl(GD::Polygon)
Provides:       perl(GD::Polyline) = 0.2
Provides:       perl(GD::Simple)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gd-devel >= 2.0.28
Requires:       gd
# MANUAL END

%description
*GD.pm* is a Perl interface to Thomas Boutell's gd graphics library
(version 2.01 or higher; see below). GD allows you to create color drawings
using a large number of graphics primitives, and emit the drawings as PNG
files.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc ChangeLog const-c.inc const-xs.inc README README.QUICKDRAW
%license LICENSE

%changelog
