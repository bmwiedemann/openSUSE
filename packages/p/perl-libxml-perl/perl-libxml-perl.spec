#
# spec file for package perl-libxml-perl
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


Name:           perl-libxml-perl
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-macros
Version:        0.08
Release:        0
Requires:       perl-XML-Parser
Url:            http://cpan.org/modules/by-module/XML/
Summary:        Collection of Perl modules for working with XML
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Source:         libxml-perl-%{version}.tar.bz2
Patch:          libxml-perl-%{version}-test.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
perl-libxml-perl is a collection of Perl modules for working with XML.



Authors:
--------
    Ken MacLeod <ken@bitsko.slc.ut.us>

%prep
%setup -n libxml-perl-%{version}
%patch

%build
perl Makefile.PL
make %{?_smp_mflags}
make test

%install
%perl_make_install
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes ChangeLog README examples doc/*
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Data
%{perl_vendorlib}/XML
%{perl_vendorarch}/auto/libxml-perl

%changelog
