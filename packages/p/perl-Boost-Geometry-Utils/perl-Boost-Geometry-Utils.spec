#
# spec file for package perl-Boost-Geometry-Utils
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


%define cpan_name Boost-Geometry-Utils
Name:           perl-Boost-Geometry-Utils
Version:        0.150.0
Release:        0
# 0.15 -> normalize -> 0.150.0
%define cpan_version 0.15
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Bindings for the Boost Geometry library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AA/AAR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         avextend.diff
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.70
BuildRequires:  perl(ExtUtils::Typemaps::Default) >= 0.50
BuildRequires:  perl(ExtUtils::XSpp) >= 0.160
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Module::Build::WithXSpp) >= 0.100
Provides:       perl(Boost::Geometry::Utils) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-c++
# MANUAL END

%description
Bindings for the Boost Geometry library

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -N

%patch -P0 -p0

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES README
%license LICENSE

%changelog
