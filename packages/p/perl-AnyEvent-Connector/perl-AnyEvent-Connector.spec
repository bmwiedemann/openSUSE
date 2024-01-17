#
# spec file for package perl-AnyEvent-Connector
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name AnyEvent-Connector
Name:           perl-AnyEvent-Connector
Version:        0.40.0
Release:        0
%define cpan_version 0.04
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tcp_connect with transparent proxy handling
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Module::Build::Prereqs::FromCPANfile) >= 0.02
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(URI)
Requires:       perl(AnyEvent::Handle)
Requires:       perl(AnyEvent::Socket)
Requires:       perl(URI)
Provides:       perl(AnyEvent::Connector) = 0.40.0
Provides:       perl(AnyEvent::Connector::Proxy::http)
%define         __perllib_provides /bin/true
%{perl_requires}

%description
AnyEvent::Connector object has 'tcp_connect' method compatible with that
from AnyEvent::Socket, and it handles proxy settings transparently.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
