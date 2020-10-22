#
# spec file for package perl-Glib-Object-Introspection
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Glib-Object-Introspection
Version:        0.049
Release:        0
#Upstream:  This library is free software; you can redistribute it and/or modify it under the terms of the Lesser General Public License (LGPL). For more information, see http://www.fsf.org/licenses/lgpl.txt
%define cpan_name Glib-Object-Introspection
Summary:        Dynamically create Perl language bindings
License:        LGPL-2.1-only
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc NEWS perl-Glib-Object-Introspection.doap README
%license LICENSE

%changelog
