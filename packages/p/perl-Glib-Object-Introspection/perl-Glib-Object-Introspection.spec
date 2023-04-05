#
# spec file for package perl-Glib-Object-Introspection
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Glib-Object-Introspection
Name:           perl-Glib-Object-Introspection
Version:        0.050
Release:        0
#Upstream:  This library is free software; you can redistribute it and/or modify it under the terms of the Lesser General Public License (LGPL). For more information, see http://www.fsf.org/licenses/lgpl.txt
License:        LGPL-2.1-only
Summary:        Dynamically create Perl language bindings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.3
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1
BuildRequires:  perl(Glib) >= 1.32
Requires:       perl(ExtUtils::Depends) >= 0.3
Requires:       perl(ExtUtils::PkgConfig) >= 1
Requires:       perl(Glib) >= 1.32
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# MANUAL END

%description
Dynamically create Perl language bindings

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
%doc NEWS perl-glib-object-introspection.doap README.md
%license LICENSE

%changelog
