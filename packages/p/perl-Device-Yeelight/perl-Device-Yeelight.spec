#
# spec file for package perl-Device-Yeelight
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Device-Yeelight
Name:           perl-Device-Yeelight
Version:        0.13
Release:        0
Summary:        Controller for Yeelight smart devices
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JB/JBAIER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO) >= 1.38
BuildRequires:  perl(IO::Socket::Multicast) >= 1.12
BuildRequires:  perl(JSON) >= 2.97
Requires:       perl(IO) >= 1.38
Requires:       perl(IO::Socket::Multicast) >= 1.12
Requires:       perl(JSON) >= 2.97
%{perl_requires}

%description
Controller for Yeelight smart devices

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes examples README

%changelog
