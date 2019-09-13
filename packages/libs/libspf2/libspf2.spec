#
# spec file for package libspf2
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


Name:           libspf2
%define lname	libspf2-2
Version:        1.2.10
Release:        0
Summary:        Implementation of the Sender Policy Framework
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.libspf2.org/
Source:         http://www.libspf2.org/spf/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Implementation of the Sender Policy Framework, a part of the SPF/SRS protocol
pair.

%package -n %lname
Summary:        Development Package for libspf2
Group:          System/Libraries

%description -n %lname
Implementation of the Sender Policy Framework, a part of the SPF/SRS protocol
pair. libspf2 is a library which allows email systems such as Sendmail,
Postfix, Exim, Zmailer and MS Exchange to check SPF records and make sure that
the email is authorized by the domain name that it is coming from. This
prevents email forgery, commonly used by spammers, scammers and email
viruses/worms.

%package devel
Summary:        Development files for libspf
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Implementation of the Sender Policy Framework, a part of the SPF/SRS protocol
pair. libspf2 is a library which allows email systems such as Sendmail,
Postfix, Exim, Zmailer and MS Exchange to check SPF records and make sure that
the email is authorized by the domain name that it is coming from. This
prevents email forgery, commonly used by spammers, scammers and email
viruses/worms.

This is the development package.

%package tools
Summary:        Tools to work with libspf2
Group:          Applications/System
Obsoletes:      spf2 < %version-%release
Provides:       spf2 = %version-%release

%description tools
Implementation of the Sender Policy Framework, a part of the SPF/SRS protocol
pair. libspf2 is a library which allows email systems such as Sendmail,
Postfix, Exim, Zmailer and MS Exchange to check SPF records and make sure that
the email is authorized by the domain name that it is coming from. This
prevents email forgery, commonly used by spammers, scammers and email
viruses/worms.

This is the package with the binaries.


%prep
%setup -q

%build
export CFLAGS="%optflags -std=gnu89"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}%{_libdir}/*.{a,la}
rm %{buildroot}%{_bindir}/*_static
mv %{buildroot}%{_bindir}/spfquery %{buildroot}%{_bindir}/spf_query

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc LICENSES
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*

%files tools
%defattr(-,root,root)
%doc README
%{_bindir}/*

%changelog
