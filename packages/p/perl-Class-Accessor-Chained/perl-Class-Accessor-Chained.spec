#
# spec file for package perl-Class-Accessor-Chained
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


%define cpan_name Class-Accessor-Chained
Name:           perl-Class-Accessor-Chained
Version:        0.10.0
Release:        0
# 0.01 -> normalize -> 0.10.0
%define cpan_version 0.01
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Make chained accessors
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Module::Build)
Requires:       perl(Class::Accessor)
Provides:       perl(Class::Accessor::Chained) = %{version}
Provides:       perl(Class::Accessor::Chained::Fast)
%undefine       __perllib_provides
%{perl_requires}

%description
A chained accessor is one that always returns the object when called with
parameters (to set), and the value of the field when called with no
arguments.

This module subclasses Class::Accessor in order to provide the same
mk_accessors interface.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
