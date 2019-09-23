#
# spec file for package log4shib
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libvers 2
%define pkgdocdir %{_docdir}/%{name}
Name:           log4shib
Version:        2.0.0
Release:        0
Summary:        Log for C++, Shibboleth Edition
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
Url:            https://wiki.shibboleth.net/confluence/display/OpenSAML/log4shib
Source0:        http://shibboleth.net/downloads/log4shib/%{version}/%{name}-%{version}.tar.gz
Source1:        http://shibboleth.net/downloads/log4shib/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch0:         log4shib-1.0.9-doxygen_timestamp.patch
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Log for C++ is a library of classes for flexible logging to files, syslog,
and other destinations. It is modeled after the Log for Java library and
stays as close to its API as is reasonable.

%package -n liblog4shib%{libvers}
Summary:        Log for C++, Shibboleth Edition
Group:          System/Libraries
Provides:       log4shib = %{version}-%{release}
Obsoletes:      log4shib < %{version}-%{release}

%description -n liblog4shib%{libvers}
Log for C++ is a library of classes for flexible logging to files, syslog,
and other destinations. It is modeled after the Log for Java library and
stays as close to its API as is reasonable.

This package contains just the shared library.

%package -n liblog4shib-devel
Summary:        Development tools for Log for C++
Group:          Development/Libraries/C and C++
Requires:       libboost_thread-devel
Requires:       liblog4shib%{libvers} = %{version}-%{release}
Provides:       log4shib-devel = %{version}-%{release}
Obsoletes:      log4shib-devel < %{version}-%{release}

%description -n liblog4shib-devel
The static libraries and header files needed for development with log4shib.

%prep
%setup -q
%patch0 -p1

%build
%configure \
  --disable-static \
  --enable-doxygen
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} apidir=%{buildroot}%{pkgdocdir}/api install
# If we use %%doc down below to package the README files from the build tree,
# it will blow away the package's docdir folder, and the installed API docs with it.
# Instead, copy the README files manually into the platform's docdir.
config/install-sh -d %{buildroot}%{pkgdocdir}
config/install-sh -m 644 -c AUTHORS COPYING NEWS README THANKS ChangeLog %{buildroot}%{pkgdocdir}

# We don't want to ship these
find %{buildroot} -type f -name "*.la" -delete -print

%post -n liblog4shib%{libvers} -p /sbin/ldconfig

%post -n liblog4shib-devel
if test "x$RPM_INSTALL_PREFIX0" != "x" ; then
    perl -pi -e"s|^prefix=\"[^\"]*\"|prefix=\"$RPM_INSTALL_PREFIX0\"|" $RPM_INSTALL_PREFIX0/bin/log4shib-config
fi

%postun -n liblog4shib%{libvers} -p /sbin/ldconfig

%files -n liblog4shib%{libvers}
%defattr(-,root,root,755)
%{_libdir}/lib*.so.*

%files -n liblog4shib-devel
%defattr(-,root,root,755)
%{_includedir}/*
%{_mandir}/man?/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/pkgconfig/log4shib.pc
%doc %{pkgdocdir}

%changelog
