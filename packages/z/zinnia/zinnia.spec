#
# spec file for package zinnia
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%if 0%{?sle_version} > 0 && 0%{?sle_version} < 150400
%define with_python 1
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%else
%define with_python 0
%endif

Name:           zinnia
Version:        0.07
Release:        0
Summary:        Online hand recognition system with machine learning
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://taku910.github.io/zinnia
Source0:        https://github.com/silverhikari/zinnia/releases/download/%{version}/zinnia-%{version}.tar.gz
Patch0:         optflags-fixes.diff
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
%if %{with_python}
BuildRequires:  python-devel
%endif
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
Requires:       libzinnia0 = %{version}

%description    devel
The zinnia-devel package contains libraries and header files for
developing applications that use zinnia.

%if %{with_python}
%package -n python-zinnia
Summary:        Python bindings for zinnia
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python-zinnia
This package contains python bindings for zinnia.
%endif

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%if %{with_python}
cd python
CFLAGS="%{optflags} -I../" LDFLAGS="-L../.libs" \
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif

%post -n libzinnia0 -p /sbin/ldconfig
%postun -n libzinnia0 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README AUTHORS
%doc doc
%{_bindir}/zinnia
%{_bindir}/zinnia_learn
%{_bindir}/zinnia_convert

%files -n libzinnia0
%license COPYING
%{_libdir}/libzinnia.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/zinnia.h
%{_includedir}/zinnia
%{_libdir}/libzinnia.so
%{_libdir}/pkgconfig/zinnia.pc

%if %{with_python}
%files -n python-zinnia
%defattr (-,root,root)
%{python_sitearch}/*
%endif

%changelog
