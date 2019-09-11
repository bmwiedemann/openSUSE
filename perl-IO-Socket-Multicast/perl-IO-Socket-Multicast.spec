#
# spec file for package perl-IO-Socket-Multicast
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


Name:           perl-IO-Socket-Multicast
%define cpan_name IO-Socket-Multicast
Summary:        Send and receive multicast messages
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Version:        1.12
Release:        0
Url:            http://search.cpan.org/dist/IO-Socket-Multicast
Source0:        %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Interface) >= 0.94
Requires:       perl(IO::Interface) >= 0.94

%description
The IO::Socket::Multicast module subclasses IO::Socket::INET to enable
you to manipulate multicast groups. With this module (and an operating
system that supports multicasting), you will be able to receive
incoming multicast transmissions and generate your own outgoing
multicast packets.



Authors:
--------
    Lincoln Stein <lstein@cshl.org>

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root)
%doc Changes README

%changelog
