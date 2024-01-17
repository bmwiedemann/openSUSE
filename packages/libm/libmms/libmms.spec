#
# spec file for package libmms
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname 0

Name:           libmms
Version:        0.6.4
Release:        0
# NOTE: there are files from the xine project with GPL headers in the source,
# but these were re-licensed to LGPLv2+ with the explicit permission of all
# contributors.
# Please see the README.LICENSE file and the xine mailing list discussions in
# libmms-relicensing-1.txt and libmms-relicensing-2.txt 

Summary:        MMS stream protocol library
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://www.sf.net/projects/%{name}
Source0:        %{name}-%{version}.tar.gz
Source1:        libmms-relicensing-1.txt
Source2:        libmms-relicensing-2.txt
Source3:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glib-2.0)
Patch0:         libmms-pkgconfig.patch
Patch1:         libmms-nognetexport.patch

%description
LibMMS is a common library for parsing mms:// and mmsh:// type network streams.
These are commonly used to stream Windows Media Video content over the web.
LibMMS itself is only for receiving MMS stream, it doesn't handle sending at
all.

%package -n %{name}%{soname}
Summary:        MMS stream protocol library
Group:          System/Libraries

%description -n %{name}%{soname}
LibMMS is a common library for parsing mms:// and mmsh:// type network streams.
These are commonly used to stream Windows Media Video content over the web.
LibMMS itself is only for receiving MMS stream, it doesn't handle sending at
all.

%package -n %{name}-devel
Summary:        Libmms development files
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}
Requires:       glibc-devel

%description -n %{name}-devel
Headers and libraries to program against %{name}

%prep
%setup -q
%patch0
%patch1

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%make_install
%{__rm} -f '%{buildroot}%{_libdir}/%{name}.la'
install -d -m 755 %{buildroot}%{_docdir}/%{name}%{soname}
install -m 644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}%{soname}
install -m 644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}%{soname}

%post   -n %{name}%{soname} -p /sbin/ldconfig 
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(0644, root, root, 0755)
%doc AUTHORS ChangeLog COPYING.LIB README README.LICENSE
%doc %{_docdir}/%{name}%{soname}
%{_libdir}/%{name}.so.%{soname}*

%files -n %{name}-devel
%defattr(0644, root, root, 0755)
%{_libdir}/%{name}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
