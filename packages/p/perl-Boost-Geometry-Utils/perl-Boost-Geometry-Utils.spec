#
# spec file for package perl-Boost-Geometry-Utils
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Boost-Geometry-Utils
Version:        0.15
Release:        0
%define cpan_name Boost-Geometry-Utils
Summary:        Bindings for the Boost Geometry library
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Boost-Geometry-Utils/
Source:         http://www.cpan.org/authors/id/A/AA/AAR/%{cpan_name}-%{version}.tar.gz
Patch:          avextend.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.07
BuildRequires:  perl(ExtUtils::Typemaps::Default) >= 0.05
BuildRequires:  perl(ExtUtils::XSpp) >= 0.16
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Module::Build::WithXSpp) >= 0.10
%{perl_requires}
# MANUAL
BuildRequires:  gcc-c++

%description
Bindings for the Boost Geometry library

%prep
%setup -q -n %{cpan_name}-%{version}
%patch

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES LICENSE README src xsp

%changelog
