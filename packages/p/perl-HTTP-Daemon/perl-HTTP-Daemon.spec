#
# spec file for package perl-HTTP-Daemon
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


%define cpan_name HTTP-Daemon
Name:           perl-HTTP-Daemon
Version:        6.16
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple http server class
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Response) >= 6
BuildRequires:  perl(HTTP::Status) >= 6
BuildRequires:  perl(IO::Socket::IP) >= 0.32
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Needs)
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Response) >= 6
Requires:       perl(HTTP::Status) >= 6
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(LWP::MediaTypes) >= 6
%{perl_requires}

%description
Instances of the 'HTTP::Daemon' class are HTTP/1.1 servers that listen on a
socket for incoming requests. The 'HTTP::Daemon' is a subclass of
'IO::Socket::IP', so you can perform socket operations directly on it too.

Please note that 'HTTP::Daemon' used to be a subclass of
'IO::Socket::INET'. To support IPv6, it switched the parent class to
'IO::Socket::IP' at version 6.05. See IPv6 SUPPORT for details.

The accept() method will return when a connection from a client is
available. The returned value will be an 'HTTP::Daemon::ClientConn' object
which is another 'IO::Socket::IP' subclass. Calling the get_request()
method on this object will read data from the client and return an
'HTTP::Request' object. The ClientConn object also provide methods to send
back various responses.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
