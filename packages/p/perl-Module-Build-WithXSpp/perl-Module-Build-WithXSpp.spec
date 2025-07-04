#
# spec file for package perl-Module-Build-WithXSpp
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


%define cpan_name Module-Build-WithXSpp
Name:           perl-Module-Build-WithXSpp
Version:        0.140.0
Release:        0
# 0.14 -> normalize -> 0.140.0
%define cpan_version 0.14
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        XS++ enhanced flavour of Module::Build
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.40
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.22
BuildRequires:  perl(ExtUtils::Typemaps) >= 1.00
BuildRequires:  perl(ExtUtils::XSpp) >= 0.110
BuildRequires:  perl(Module::Build) >= 0.26
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(ExtUtils::CppGuess) >= 0.40
Requires:       perl(ExtUtils::ParseXS) >= 2.22
Requires:       perl(ExtUtils::Typemaps) >= 1.00
Requires:       perl(ExtUtils::XSpp) >= 0.110
Requires:       perl(Module::Build) >= 0.26
Provides:       perl(Module::Build::WithXSpp) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This subclass of Module::Build adds some tools and processes to make it
easier to use for wrapping C++ using XS++ (ExtUtils::XSpp).

There are a few minor differences from using 'Module::Build' for an
ordinary XS module and a few conventions that you should be aware of as an
XS++ module author. They are documented in the "FEATURES AND CONVENTIONS"
section below. But if you can't be bothered to read all that, you may
choose skip it and blindly follow the advice in "JUMP START FOR THE
IMPATIENT".

An example of a full distribution based on this build tool can be found in
the ExtUtils::XSpp distribution under _examples/XSpp-Example_. Using that
example as the basis for your 'Module::Build::WithXSpp'-based distribution
is probably a good idea.

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
