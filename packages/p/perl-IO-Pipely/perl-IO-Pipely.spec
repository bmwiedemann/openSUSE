#
# spec file for package perl-IO-Pipely
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


%define cpan_name IO-Pipely
Name:           perl-IO-Pipely
Version:        0.006
Release:        0
Summary:        Portably create pipe() or pipe-like handles, one way or another
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.42
BuildRequires:  perl(Exporter) >= 5.72
BuildRequires:  perl(Fcntl) >= 1.13
BuildRequires:  perl(IO::Socket) >= 1.38
BuildRequires:  perl(Scalar::Util) >= 1.46_02
BuildRequires:  perl(Symbol) >= 1.08
BuildRequires:  perl(Test::More) >= 1.302120
Requires:       perl(Exporter) >= 5.72
Requires:       perl(Fcntl) >= 1.13
Requires:       perl(IO::Socket) >= 1.38
Requires:       perl(Symbol) >= 1.08
%{perl_requires}

%description
Pipes are troublesome beasts because there are a few different,
incompatible ways to create them. Not all platforms support all ways, and
some platforms may have hidden difficulties like incomplete or buggy
support.

IO::Pipely provides a couple functions to portably create one- and two-way
pipes and pipe-like socket pairs. It acknowledges and works around known
platform issues so you don't have to.

On the other hand, it doesn't work around unknown issues, so please report
any problems early and often.

IO::Pipely currently understands pipe(), UNIX-domain socketpair() and
regular IPv4 localhost sockets. This covers every platform tested so far,
but it's hardly complete. Please help support other mechanisms, such as
INET-domain socketpair() and IPv6 localhost sockets.

IO::Pipely will use different kinds of pipes or sockets depending on the
operating system's capabilities and the number of directions requested. The
autodetection may be overridden by specifying a particular pipe type.

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
%doc CHANGES README README.mkdn
%license LICENSE

%changelog
