#
# spec file for package perl-Cairo
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


%define cpan_name Cairo
Name:           perl-Cairo
Version:        1.109
Release:        0
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
Summary:        Perl interface to the cairo 2d vector graphics library
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1
Requires:       perl(ExtUtils::Depends) >= 0.2
Requires:       perl(ExtUtils::PkgConfig) >= 1
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig(cairo)
# MANUAL END

%description
Perl interface to the cairo 2d vector graphics library

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc ChangeLog.pre-git examples NEWS README TODO
%license LICENSE

%changelog
