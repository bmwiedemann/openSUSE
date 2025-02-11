#
# spec file for package perl-Alien-Build-Plugin-Download-GitLab
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


%define cpan_name Alien-Build-Plugin-Download-GitLab
Name:           perl-Alien-Build-Plugin-Download-GitLab
Version:        0.10.0
Release:        0
# 0.01 -> normalize -> 0.10.0
%define cpan_version 0.01
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Alien::Build plugin to download from GitLab
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::Build::Plugin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
Requires:       perl(Alien::Build::Plugin)
Requires:       perl(JSON::PP)
Requires:       perl(Path::Tiny)
Requires:       perl(URI)
Requires:       perl(URI::Escape)
Provides:       perl(Alien::Build::Plugin::Download::GitLab) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This plugin is designed for downloading assets from a GitLab instance.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
