#
# spec file for package perl-Font-AFM
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


Name:           perl-Font-AFM
Summary:        Interface to Adobe Font Metrics Files
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Version:        1.20
Release:        0
Source:         Font-AFM-%{version}.tar.gz
Url:            http://cpan.org/authors/id/G/GA/GAAS
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
This module implements the Font::AFM class. Objects of this class are
initialized from an AFM file and allow you to obtain information about
the font and the metrics of the various glyphs in the font.



Authors:
--------
    Gisle Aas <gisle@aas.no>

%prep
%setup -n Font-AFM-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}
make test

%install
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%dir %{perl_vendorlib}/Font
%{perl_vendorlib}/Font/*
%{perl_vendorarch}/auto/*
%doc %{_mandir}/man?/*
%doc README Changes

%changelog
