#
# spec file for package tre
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


Name:           tre
Version:        0.8.0_git201402282055
Release:        0
Summary:        POSIX compatible regexp library with approximate matching
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://laurikari.net/tre/
# This source comes from https://github.com/laurikari/tre/, revision
# c2f5d130c91b1696385a6ae0b5bcfd5214bcc9ca. The previously released
# version 0.8.0 is old (2009) and no new released have been made by
# the author, so I'm terming this 0.8.0_git201402282055.
Source0:        tre-%{version}.tar.bz2
Patch0:         %{name}.diff
# Update the python build to fix wrong include and lib paths.
# See https://github.com/laurikari/tre/pull/19.
Patch1:         %{name}-chicken.patch
Patch2:         CVE-2016-8859.patch
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
TRE is a lightweight, robust, and efficient POSIX compatible regexp
matching library with some exciting features such as approximate
matching.

%package -n libtre5
Summary:        POSIX compatible regexp library with approximate matching
Group:          System/Libraries
Requires:       %{name} = %{version}
Obsoletes:      libtre
Provides:       libtre
Recommends:     %{name}-lang = %{version}

%description -n libtre5
TRE is a lightweight, robust, and efficient POSIX compatible regexp
matching library with some exciting features such as approximate
matching.

%post -n libtre5 -p /sbin/ldconfig

%postun -n libtre5 -p /sbin/ldconfig

%package devel
Summary:        POSIX compatible regexp library with approximate matching
Group:          Development/Libraries/C and C++
Requires:       libtre5 = %{version}
Obsoletes:      libtre-devel
Provides:       libtre-devel

%description devel
TRE is a lightweight, robust, and efficient POSIX compatible regexp
matching library with some exciting features such as approximate
matching.

%package -n agrep
Summary:        Another powerful grep with interesting features
Group:          Productivity/Text/Utilities

%description -n agrep
agrep is another powerful grep which has the  ability to search for
approximate patterns as well as block oriented search.

%package -n python-%{name}
Summary:        Python bindings for the tre library
Group:          System/Libraries

%description -n python-%{name}
This package contains the python bindings for the TRE library.

%lang_package


%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .chicken
%patch2 -p1
./utils/autogen.sh

%build
%configure --disable-static --enable-shared
make %{?_smp_mflags}
pushd python
python setup.py build
popd

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
pushd python
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} || echo -n >> %{name}.lang

%files
%defattr (-, root, root)
%doc ABOUT-NLS AUTHORS LICENSE NEWS README THANKS TODO

%files -n libtre5
%defattr (-, root, root)
%{_libdir}/libtre.so.*

%files devel
%defattr (-, root, root)
%doc doc/default.css doc/tre-api.html doc/tre-syntax.html
%{_includedir}/*
%{_libdir}/libtre.so
%{_libdir}/pkgconfig/*

%files -n agrep
%defattr (-, root, root)
%{_bindir}/agrep
%{_mandir}/man1/agrep.1.gz

%files -n python-%{name}
%defattr (-, root, root)
%{python_sitearch}/tre.so
%{python_sitearch}/*.egg-info

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%check
make check %{?_smp_mflags}

%changelog
