#
# spec file for package perl-X11-Protocol
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-X11-Protocol
Version:        0.56
Release:        0
# MANUAL
%define cpan_name X11-Protocol
Summary:        Perl module for the X Window System Protocol, version 11
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/X11-Protocol/
Source:         http://www.cpan.org/authors/id/S/SM/SMCCAM/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildArch:      noarch
%{perl_requires}
Patch0:         xauthlocalhostname-localhost.diff

%description
X11::Protocol is a client-side interface to the X11 Protocol (see X(1) for
information about X11), allowing perl programs to display windows and
graphics on X11 servers.

A full description of the protocol is beyond the scope of this
documentation; for complete information, see the _X Window System Protocol,
X Version 11_, available as Postscript or *roff source from
'ftp://ftp.x.org', or _Volume 0: X Protocol Reference Manual_ of O'Reilly &
Associates's series of books about X (ISBN 1-56592-083-X,
'http://www.oreilly.com'), which contains most of the same information.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
# MANUAL
# too complex %{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README Todo

%changelog
