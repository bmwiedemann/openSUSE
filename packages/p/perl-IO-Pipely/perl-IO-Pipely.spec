#
# spec file for package perl-IO-Pipely
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-IO-Pipely
Version:        0.005
Release:        0
%define cpan_name IO-Pipely
Summary:        Portably create pipe() or pipe-like handles, one way or another.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-Pipely/
Source:         http://www.cpan.org/authors/id/R/RC/RCAPUTO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.26
BuildRequires:  perl(Exporter) >= 5.68
BuildRequires:  perl(Fcntl) >= 1.06
BuildRequires:  perl(IO::Socket) >= 1.31
BuildRequires:  perl(Scalar::Util) >= 1.29
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(base) >= 2.18
Requires:       perl(Exporter) >= 5.68
Requires:       perl(Fcntl) >= 1.06
Requires:       perl(IO::Socket) >= 1.31
Requires:       perl(base) >= 2.18
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES LICENSE README README.mkdn

%changelog
