#
# spec file for package ldapcpplib
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


Name:           ldapcpplib
Url:            http://www.openldap.org
Summary:        C++ API for LDAPv3
License:        OLDAP-2.8
Group:          Development/Libraries/C and C++
Version:        0.3.1
Release:        0

Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  openldap2-devel

%description
C++ API for LDAPv3.

Documentation is in /usr/share/doc/packages/ldapcpplib/srcdoc.



Authors:
--------
    Ralf Haferkamp <rhafer@suse.de>

%package -n libldapcpp1
Summary:        C++ API for LDAPv3
Group:          Development/Libraries/C and C++
Provides:       ldapcpplib = %{version}-%{release}
Obsoletes:      ldapcpplib <= 0.0.5

%description -n libldapcpp1
This package provides a C++ library for accessing LDAP (Version 3)
Servers



Authors:
--------
    Ralf Haferkamp <rhafer@suse.de>

%package -n libldapcpp-devel
Summary:        Files for Developing libldapcpp Applications
Group:          Development/Libraries/C and C++
Provides:       ldapcpplib-devel = %{version}
Obsoletes:      ldapcpplib-devel <= 0.0.5
Requires:       libldapcpp1 = %{version}
Requires:       libstdc++-devel
Requires:       openldap2-devel

%description -n libldapcpp-devel
This package contains files needed for development with the LDAP C++
library.



Authors:
--------
    Ralf Haferkamp <rhafer@suse.de>

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
%{?suse_update_config:%{suse_update_config -l -f build}}
autoreconf -fiv
%configure 	--disable-static --with-pic \
		  	--enable-shared --with-libldap=%{_libdir} \
			--with-ldap-includes=/usr/include 
make CXXFLAGS="$RPM_OPT_FLAGS" %{?jobs:-j%jobs}
rm -rf srcdoc/CVS
doxygen doxygen.rc

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/html
install -m644 srcdoc/html/* $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/html/
install -m644 LICENSE $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/LICENSE
install -m644 README $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/README
install -m644 COPYRIGHT $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/COPYRIGHT
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -n libldapcpp1 -p /sbin/ldconfig

%postun -n libldapcpp1 -p /sbin/ldconfig

%files -n libldapcpp1
%defattr(-,root,root)
%{_libdir}/libldapcpp.so.*

%files -n libldapcpp-devel
%defattr(-,root,root)
/usr/include/Ldif*.h
/usr/include/LDAP*.h
/usr/include/Sasl*.h
/usr/include/StringList.h
/usr/include/TlsOptions.h
%{_libdir}/libldapcpp.so
%{_defaultdocdir}/%{name}/html
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/LICENSE
%{_defaultdocdir}/%{name}/README
%{_defaultdocdir}/%{name}/COPYRIGHT

%changelog
