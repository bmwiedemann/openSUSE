#
# spec file for package perl-Module-Build-Using-PkgConfig
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


Name:           perl-Module-Build-Using-PkgConfig
Version:        0.03
Release:        0
%define cpan_name Module-Build-Using-PkgConfig
Summary:        Extend Module::Build to more easily use platform libraries provided by pkg-config
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(ExtUtils::PkgConfig)
Requires:       perl(Module::Build)
%{perl_requires}

%description
This subclass of Module::Build provides some handy methods to assist the
_Build.PL_ script of XS-based module distributions that make use of
platform libraries managed by _pkg-config_.

As well as supporting libraries installed on a platform-wide basis and thus
visible to _pkg-config_ itself, this subclass also assists with
'Alien::'-based wrappers of these system libraries, allowing them to be
dynamically installed at build time if the platform does not provide them.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
