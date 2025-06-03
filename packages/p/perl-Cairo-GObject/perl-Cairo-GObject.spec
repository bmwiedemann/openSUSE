#
# spec file for package perl-Cairo-GObject
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


%define cpan_name Cairo-GObject
Name:           perl-Cairo-GObject
Version:        1.5.0
Release:        0
# 1.005 -> normalize -> 1.5.0
%define cpan_version 1.005
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        LGPL-2.1-or-later
Summary:        Integrate Cairo into the Glib type system
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cairo) >= 1.80
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.0
BuildRequires:  perl(Glib) >= 1.224
Requires:       perl(Cairo) >= 1.80
Requires:       perl(ExtUtils::Depends) >= 0.2
Requires:       perl(ExtUtils::PkgConfig) >= 1.0
Requires:       perl(Glib) >= 1.224
Provides:       perl(Cairo::GObject) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig(cairo-gobject)
# MANUAL END

%description
Integrate Cairo into the Glib type system

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc examples NEWS perl-Cairo-GObject.doap README
%license LICENSE

%changelog
