#
# spec file for package giblib
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define libname libgiblib1
Name:           giblib
Version:        1.2.4
Release:        0
Summary:        A simple library which wraps imlib2
License:        MIT
Group:          System/Libraries
Url:            http://freecode.com/projects/giblib
Source0:        %{name}-%{version}.tar.gz
Source90:       giblib-rpmlintrc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(imlib2) >= 1.2.0
Requires:       freetype2
Requires:       imlib2 >= 1.2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Giblib is a utility library. It incorporates doubly linked lists, some string
functions, and a wrapper for imlib2.

%package devel
Summary:        Giblib development files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for the giblib library.

%package -n %{libname}
Summary:        A simple library which wraps imlib2
Group:          System/Libraries

%description -n %{libname}
Giblib is a utility library. It incorporates doubly linked lists, some string
functions, and a wrapper for imlib2.

%prep
%setup -q

%build
%configure \
   --disable-static
make %{?_smp_mflags}

%install
make \
	DESTDIR=%{buildroot} \
	LIBDIR=%{buildroot}%{_libdir} \
	install

find %{buildroot} -type f -name "*.la" -delete -print

rm -rf %{buildroot}%{_prefix}/doc

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-, root, root)
%doc README AUTHORS ChangeLog COPYING
%{_libdir}/libgiblib.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/giblib-config
%{_libdir}/libgiblib.so
%{_libdir}/pkgconfig/giblib.pc
%dir %{_includedir}/giblib
%{_includedir}/giblib/gib*.h

%changelog
