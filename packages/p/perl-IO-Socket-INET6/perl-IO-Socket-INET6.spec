#
# spec file for package perl-IO-Socket-INET6
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%bcond_with test

Name:           perl-IO-Socket-INET6
Version:        2.72
Release:        0
%define cpan_name IO-Socket-INET6
Summary:        Object interface for AF_INET/AF_INET6 domain sockets
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-Socket-INET6/
Source:         http://www.cpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}
%if %{with test}
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(Socket6) >= 0.12
Requires:       perl(Socket6) >= 0.12

%description
IO::Socket::INET6 provides an object interface to creating and using
   sockets in either AF_INET or AF_INET6 domains. It is built upon the
   IO::Socket interface and inherits all the methods defined by IO::Socket.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build
#exclude this test as it needs IPv6 network
mv t/io_sock6.t t/io_sock6.tt

%if %{with test}

%check
#disable test suite as it doesn't work at all without being online
#and our build hosts are completly without network interfaces
./Build test
%endif

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,-)
%doc ChangeLog README

%changelog
