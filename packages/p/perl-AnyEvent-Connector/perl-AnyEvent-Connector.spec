#
# spec file for package perl-AnyEvent-Connector
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-AnyEvent-Connector
Version:        0.03
Release:        0
%define cpan_name AnyEvent-Connector
Summary:        Tcp_connect with Transparent Proxy Handling
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/AnyEvent-Connector/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Module::Build::Prereqs::FromCPANfile) >= 0.02
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(URI)
Requires:       perl-base = %{perl_version}
Requires:       perl(AnyEvent::Handle)
Requires:       perl(AnyEvent::Socket)
Requires:       perl(URI)

%{perl_requires}

%description
AnyEvent::Connector object has 'tcp_connect' method compatible with that
from AnyEvent::Socket, and it handles proxy settings transparently.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
