#
# spec file for package perl-IO-String
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-IO-String
%define cpan_name IO-String
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/~gaas/
AutoReqProv:    on
Summary:        Perl IO/String interface
Version:        1.08
Release:        152
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
IO::String is an IO::File (and IO::Handle) compatible class that reads
or writes data from in-core strings.



Authors:
--------
    Gisle Aas.  <gisle@aas.no>

%prep
%setup -n %{cpan_name}-%{version}
# ---------------------------------------------------------------------------

%build
perl Makefile.PL
make %{?_smp_mflags}
# ---------------------------------------------------------------------------

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%{perl_vendorlib}/IO
%{perl_vendorarch}/auto/IO
%{perl_vendorarch}/auto/IO/String
%doc %{_mandir}/man3/*.gz
%doc MANIFEST Changes README*

%changelog
