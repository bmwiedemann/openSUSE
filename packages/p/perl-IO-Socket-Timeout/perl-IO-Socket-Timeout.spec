#
# spec file for package perl-IO-Socket-Timeout
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-IO-Socket-Timeout
Version:        0.32
Release:        0
%define cpan_name IO-Socket-Timeout
Summary:        IO::Socket with read/write timeout
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-Socket-Timeout/
Source0:        http://www.cpan.org/authors/id/D/DA/DAMS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(PerlIO::via::Timeout) >= 0.32
BuildRequires:  perl(Test::TCP)
Requires:       perl(PerlIO::via::Timeout) >= 0.32
%{perl_requires}

%description
'IO::Socket' provides a way to set a timeout on the socket, but the timeout
will be used only for connection, not for reading / writing operations.

This module provides a way to set a timeout on read / write operations on
an 'IO::Socket' instance, or any 'IO::Socket::*' modules, like
'IO::Socket::INET'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
