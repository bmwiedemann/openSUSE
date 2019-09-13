#
# spec file for package zinnia
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
Name:           zinnia
Version:        0.06
Release:        0
Summary:        Online hand recognition system with machine learning
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://taku910.github.io/zinnia
Source0:        %{name}-%{version}.tar.gz
Patch0:         optflags-fixes.diff
Patch1:         zinnia-automake-1.13.patch
# PATCH-FIX-UPSTREAM fix compile with gcc 6.0
Patch2:         zinnia-gcc6.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Zinnia is a simple, customizable and portable online hand recognition system based on Support Vector Machines. Zinnia simply receives user pen strokes as a sequence of coordinate data and outputs n-best characters sorted by SVM confidence. To keep portability, Zinnia doesn\'t have any rendering functionality. In addition to recognition, Zinnia provides training module that allows us to create any hand-written recognition systems with low-cost.

%package -n libzinnia0
Summary:        Shared library for zinnia
Group:          System/Libraries

%description -n libzinnia0
This package contains shared libraries used by zinnia.

%package        devel
Summary:        Development files for zinnia
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description    devel
The zinnia-devel package contains libraries and header files for
developing applications that use zinnia.

%package -n python-zinnia
Summary:        Python bindings for zinnia
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python-zinnia
This package contains python bindings for zinnia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

cd python
CFLAGS="%{optflags} -I../" LDFLAGS="-L../.libs" \
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%post -n libzinnia0 -p /sbin/ldconfig
%postun -n libzinnia0 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README COPYING AUTHORS
%doc doc
%{_bindir}/zinnia
%{_bindir}/zinnia_learn
%{_bindir}/zinnia_convert

%files -n libzinnia0
%defattr(-,root,root)
%{_libdir}/libzinnia.so.0
%{_libdir}/libzinnia.so.0.0.0

%files devel
%defattr(-,root,root)
%{_includedir}/zinnia.h
%{_includedir}/zinnia
%{_libdir}/libzinnia.so
%{_libdir}/pkgconfig/zinnia.pc

%files -n python-zinnia
%defattr (-,root,root)
%{python_sitearch}/*

%changelog
