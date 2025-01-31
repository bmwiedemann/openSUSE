#
# spec file for package perl-Object-Pad
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


%define cpan_name Object-Pad
Name:           perl-Object-Pad
Version:        0.819.0
Release:        0
# 0.819 -> normalize -> 0.819.0
%define cpan_version 0.819
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple syntax for lexical field-based objects
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Test2::V0) >= 0.000148
BuildRequires:  perl(XS::Parse::Keyword) >= 0.470
BuildRequires:  perl(XS::Parse::Keyword::Builder) >= 0.480
BuildRequires:  perl(XS::Parse::Sublike) >= 0.350
BuildRequires:  perl(XS::Parse::Sublike::Builder) >= 0.350
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(XS::Parse::Keyword) >= 0.470
Requires:       perl(XS::Parse::Sublike) >= 0.350
Provides:       perl(Object::Pad) = %{version}
Provides:       perl(Object::Pad::ExtensionBuilder) = %{version}
Provides:       perl(Object::Pad::MOP::Class) = %{version}
Provides:       perl(Object::Pad::MOP::Field) = %{version}
Provides:       perl(Object::Pad::MOP::FieldAttr) = %{version}
Provides:       perl(Object::Pad::MOP::Method) = %{version}
Provides:       perl(Object::Pad::MetaFunctions) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
%if 0%{?suse_version} <= 1600
BuildRequires:  perl(indirect)
Requires:       perl(indirect)
%endif
# MANUAL END

%description
This module provides a simple syntax for creating object classes, which
uses private variables that look like lexicals as object member fields.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
