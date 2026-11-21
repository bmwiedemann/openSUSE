#
# spec file for package perl-ExtUtils-Typemaps-Default
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


%define cpan_name ExtUtils-Typemaps-Default
Name:           perl-ExtUtils-Typemaps-Default
Version:        1.70.0
Release:        0
# 1.07 -> normalize -> 1.70.0
%define cpan_version 1.07
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Set of useful typemaps
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Typemaps) >= 3.21
BuildRequires:  perl(Module::Build) >= 0.420
Requires:       perl(ExtUtils::Typemaps) >= 3.21
Provides:       perl(ExtUtils::Typemap::Basic) = %{version}
Provides:       perl(ExtUtils::Typemap::Default) = %{version}
Provides:       perl(ExtUtils::Typemap::ObjectMap) = %{version}
Provides:       perl(ExtUtils::Typemap::STL) = %{version}
Provides:       perl(ExtUtils::Typemap::STL::String) = %{version}
Provides:       perl(ExtUtils::Typemap::STL::Vector) = %{version}
Provides:       perl(ExtUtils::Typemaps::Basic) = %{version}
Provides:       perl(ExtUtils::Typemaps::Default) = %{version}
Provides:       perl(ExtUtils::Typemaps::ObjectMap) = %{version}
Provides:       perl(ExtUtils::Typemaps::STL) = %{version}
Provides:       perl(ExtUtils::Typemaps::STL::List) = %{version}
Provides:       perl(ExtUtils::Typemaps::STL::String) = %{version}
Provides:       perl(ExtUtils::Typemaps::STL::Vector) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'ExtUtils::Typemaps::Default' is an 'ExtUtils::Typemaps' subclass that
provides a set of default mappings (in addition to what perl itself
provides). These default mappings are currently defined as the combination
of the mappings provided by the following typemap classes which are
provided in this distribution:

ExtUtils::Typemaps::ObjectMap, ExtUtils::Typemaps::STL,
ExtUtils::Typemaps::Basic

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
%doc Changes

%changelog
