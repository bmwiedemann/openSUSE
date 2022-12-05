#
# spec file for package newt
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


%define         libname lib%{name}
%define         libsoname %{libname}0_52
%{!?python2_sitearch: %global python2_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%bcond_without python2
Name:           newt
Version:        0.52.23
Release:        0
Summary:        A library for text mode user interfaces
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://pagure.io/newt
Source:         https://fedorahosted.org/releases/n/e/newt/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Source10:       %{name}-rpmlintrc
Patch0:         newt-0.52.20-implicit-pointer-decl.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  slang-devel
%if %{with python2}
BuildRequires:  python-devel
%endif

%description
Newt is a programming library for color text-mode, widget-based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
checkboxes, radio buttons, labels, plain text fields, scrollbars, etc.,
to text mode user interfaces.

This package also contains a Dialog replacement called whiptail. Newt
is based on the slang library.

%package -n %{libsoname}
Summary:        Shared libraries for Nifty Erik's Windowing Toolkit
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libsoname}
This package contains the shared libraries needed by programs built
with newt.

Newt is a programming library for color text-mode widget-based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
check boxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces.

%package devel
Summary:        Development files for the Newt windowing toolkit
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       popt-devel
Requires:       python3-devel
Requires:       slang-devel
Recommends:     %{name} = %{version}

%description devel
This package contains the header files and libraries necessary for
developing applications which use newt.

Newt is a development library for text mode user interfaces.

Install newt-devel if you want to develop applications which depend on
newt.

%package static
# Please keep the static package as this is requested by another
# vendor for his tool. It shouldn't be a problem to keep this
# special package. (lrupp)
Summary:        Static libraries of Nifty Erik's Windowing Toolkit
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description static
This package contains the static libraries needed to compile programs
based on newt which don't need the shared libraries. Install it if you
need to link statically with %{libname}.

Newt is a programming library for color text-mode widget-based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
check boxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces.

%package -n python2-%{name}
Summary:        Python bindings for newt
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Provides:       python-%{name} = %{version}
Obsoletes:      python-%{name} < %{version}
Provides:       %{name}-python = %{version}
Obsoletes:      %{name}-python < %{version}

%description -n python2-%{name}
The python-newt package contains the Python bindings for the newt
library providing a python API for creating text mode interfaces.

%package -n python3-%{name}
Summary:        Python 3 bindings for newt
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}

%description -n python3-%{name}
The python3-newt package contains the Python 3 bindings for the newt library
providing a python API for creating text mode interfaces.

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# gpm support seems to smash the stack
# --with-gpm-support
%configure --without-tcl
## make depend
make CPPFLAGS="%{optflags} -fPIC" %{?_smp_mflags} all
chmod 0644 peanuts.py popcorn.py

%install
%if %{with python2}
pyversions="python%{py_ver}"
%else
pyversions=""
%endif
pyversions="$pyversions python%{py3_ver}"
make PYTHONVERS="$pyversions" instroot=%{buildroot} DESTDIR=%{buildroot} install install-sh
# currently we don't support these languages
for lang in ast bal sr@latin wo; do
  rm -rf %{buildroot}%{_datadir}/locale/$lang
done

%find_lang %{name}

%if %{with python2}
%py_compile %{buildroot}/%{python_sitearch}
%py_compile -O %{buildroot}/%{python_sitearch}
%endif
%py3_compile %{buildroot}/%{python3_sitearch}
%py3_compile -O %{buildroot}/%{python3_sitearch}
%fdupes %{buildroot}/%{python3_sitearch}

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%license COPYING
%{_bindir}/whiptail
%{_mandir}/man1/whiptail.1%{?ext_man}

%files -n %{libsoname}
%defattr(-,root,root)
%{_libdir}/%{libname}.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/*.pc

%files static
%defattr(-,root,root)
%{_libdir}/%{libname}.a

%if %{with python2}
%files -n python2-%{name}
%defattr(-,root,root)
%{python2_sitearch}/*
%endif

%files -n python3-%{name}
%defattr(-,root,root)
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py*
%{python3_sitearch}/__pycache__/*.py*

%changelog
