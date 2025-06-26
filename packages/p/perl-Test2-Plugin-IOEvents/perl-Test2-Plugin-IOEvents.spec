#
# spec file for package perl-Test2-Plugin-IOEvents
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


%define cpan_name Test2-Plugin-IOEvents
Name:           perl-Test2-Plugin-IOEvents
Version:        0.1.1
Release:        0
# 0.001001 -> normalize -> 0.1.1
%define cpan_version 0.001001
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Turn STDOUT and STDERR into Test2 events
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test2::API) >= 1.302165
BuildRequires:  perl(Test2::V0) >= 0.000124
Requires:       perl(Test2::API) >= 1.302165
Provides:       perl(Test2::Plugin::IOEvents) = %{version}
Provides:       perl(Test2::Plugin::IOEvents::Tie) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This plugin turns prints to STDOUT and STDERR (including warnings) into
proper Test2 events.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README README.md
%license LICENSE

%changelog
