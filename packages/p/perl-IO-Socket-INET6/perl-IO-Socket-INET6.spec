#
# spec file for package perl-IO-Socket-INET6
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name IO-Socket-INET6
Name:           perl-IO-Socket-INET6
Version:        2.73
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        [ DEPRECATED!! ] Object interface for AF_INET/AF_INET6 domain sockets
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.360000
BuildRequires:  perl(Socket6) >= 0.12
Requires:       perl(Socket6) >= 0.12
%{perl_requires}

%description
'IO::Socket::INET6' provides an object interface to creating and using
sockets in either AF_INET or AF_INET6 domains. It is built upon the
IO::Socket interface and inherits all the methods defined by IO::Socket.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
# MANUAL no testing (needs network connectivity)
#./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog README
%license LICENSE

%changelog
