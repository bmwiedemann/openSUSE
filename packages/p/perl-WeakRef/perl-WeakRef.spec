#
# spec file for package perl-WeakRef
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


Name:           perl-WeakRef
%define cpan_name WeakRef
Version:        0.01
Release:        0
Provides:       perl-Weakref
Obsoletes:      perl-Weakref
Summary:        API for weak references to be created in Perl
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/WeakRef/
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
A patch to Perl 5.005_55 by the author implements a core API for weak
references. This module is a Perl-level interface to that API, allowing
weak references to be created in Perl.

A weak reference is just like an ordinary Perl reference except that it
isn't included in the reference count of the thing referred to. This
means that once all references to a particular piece of data are weak,
the piece of data is freed and all the weak references are set to
undef. This is particularly useful for implementing circular data
structures without memory leaks or caches of objects.



Authors:
--------
    Tuomas J. Lukka      <lukka@iki.fi>

%prep
%setup -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=site
make %{?_smp_mflags}
make test

%install
[ "$RPM_BUILD_ROOT" != "/" -a -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
 [ "$RPM_BUILD_ROOT" != "/" -a -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc %{_mandir}/man?/*
%{perl_vendorarch}/WeakRef.pm
%{perl_vendorarch}/auto/WeakRef

%changelog
