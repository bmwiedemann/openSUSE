#
# spec file for package perl-AnyEvent-I3
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name AnyEvent-I3
Name:           perl-AnyEvent-I3
Version:        0.190.0
Release:        0
# 0.19 -> normalize -> 0.190.0
%define cpan_version 0.19
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Communicate with the i3 window manager
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTPLBG/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Test::More) >= 0.8
Requires:       perl(AnyEvent)
Requires:       perl(AnyEvent::Handle)
Requires:       perl(AnyEvent::Socket)
Requires:       perl(JSON::XS)
Provides:       perl(AnyEvent::I3) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
communicate with the i3 window manager

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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

%changelog
