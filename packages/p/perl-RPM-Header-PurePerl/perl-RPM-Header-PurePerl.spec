#
# spec file for package perl-RPM-Header-PurePerl
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-RPM-Header-PurePerl
BuildRequires:  perl-HTML-Tagset
BuildRequires:  perl-macros
Version:        1.0.2
Release:        0
Url:            http://search.cpan.org/~tlbdk/RPM-Header-PurePerl/lib/RPM/Header/PurePerl.pm
Summary:        A Perl only implementation of a RPM header reader
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Source:         RPM-Header-PurePerl-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
RPM::Header::PurePerl is a clone of RPM::Header written in only Perl, so it
provides a way to read an rpm package on systems where rpm is not installed. 
RPM::Header::PurePerl can be used as a drop in replacement for RPM::Header,
if needed also the other way round.

%prep
%setup -q -n RPM-Header-PurePerl-%{version}

%build
perl Makefile.PL OPTIMIZE="%optflags -Wall"
make

%check
make test

%install
%perl_make_install
%perl_process_packlist

%files
%defattr(-,root,root)
%doc README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/RPM
%{perl_vendorarch}/auto/RPM

%changelog
