#
# spec file for package perl-ExtUtils-PkgConfig
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-ExtUtils-PkgConfig
Version:        1.160000
Release:        0
%define cpan_version 1.16
Provides:       perl(ExtUtils::PkgConfig) = 1.160000
%define cpan_name ExtUtils-PkgConfig
Summary:        Simplistic Interface to Pkg-Config
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/ExtUtils-PkgConfig/
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig
Requires:       pkgconfig
# MANUAL END

%description
The pkg-config program retrieves information about installed libraries,
usually for the purposes of compiling against and linking to them.

ExtUtils::PkgConfig is a very simplistic interface to this utility,
intended for use in the Makefile.PL of perl extensions which bind libraries
that pkg-config knows. It is really just boilerplate code that you would've
written yourself.

%prep
%setup -q -n %{cpan_name}-%{cpan_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes perl-ExtUtils-PkgConfig.doap README

%changelog
