#
# spec file for package libkdumpfile
#
# Copyright (c) 2020 SUSE LLC
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


# Begin compatibility cruft
#

%{!?make_install:%define make_install make install DESTDIR=%{?buildroot}}

%if 0%{!?have_snappy:1}
%if 0%{?suse_version} >= 1310
%define have_snappy 1
%else
%define have_snappy 0
%endif
%endif

# There was no Python single-spec before SLE15
%if %{defined python_subpackages}
%define new_python_macros 1
%else
%define new_python_macros 0
%define python_module() python-%{**} python3-%{**}
%define ifpython2 %if 0
%define python_build python setup.py build
%define python_install python setup.py install --skip-build --root %{?buildroot}
%define python3_build python3 setup.py build
%define python3_install python3 setup.py install --skip-build --root %{?buildroot}
%endif

#
# End compatibility cruft

%define oldpython python

Name:           libkdumpfile
Version:        0.4.0
Release:        0
%if "%name" == "libkdumpfile"
Summary:        Kernel dump file access library
License:        LGPL-3.0-or-later OR GPL-2.0-or-later
Group:          Development/Languages/Python
%else
Summary:        Python interface for libkdumpfile
License:        LGPL-3.0-or-later OR GPL-2.0-or-later
Group:          Development/Languages/Python
%endif
URL:            https://github.com/ptesarik/libkdumpfile
Source:         https://github.com/ptesarik/libkdumpfile/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Patch1:         %{name}-use-python-distutils.patch
Patch2:         %{name}-uninstall-using-distutils.patch
Patch3:         %{name}-honour-DESTDIR.patch
Patch4:         %{name}-move-python-setup-command-options.patch
Patch5:         %{name}-python-includedir.patch
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} < 1030
BuildRequires:  binutils
%else
BuildRequires:  binutils-devel
%endif
BuildRequires:  %{python_module devel}
%if %{have_snappy}
BuildRequires:  snappy-devel
%endif
%ifpython2
Provides:       %{oldpython}-libaddrxlat = %{version}-%{release}
Obsoletes:      %{oldpython}-libaddrxlat < %{version}-%{release}
%endif

%if %new_python_macros
%python_subpackages
%endif

%description
%if "%name" == "libkdumpfile"
A library that provides an abstraction layer for reading kernel dump
core files.  It supports different kernel dump core formats, virtual
to physical translation, Xen mappings and more.
%else
This package contains all necessary python modules to use libkdumpfile via
the Python interpreter.
%endif

%if !%new_python_macros

%package -n python2-libkdumpfile
Summary:        Python interface for libkdumpfile
Group:          Development/Languages/Python
Provides:       python-libkdumpfile = %{version}-%{release}
Obsoletes:      python-libkdumpfile < %{version}-%{release}
Provides:       python-libaddrxlat = %{version}-%{release}
Obsoletes:      python-libaddrxlat < %{version}-%{release}

%description -n python2-libkdumpfile
This package contains all necessary python modules to use libkdumpfile via
the Python interpreter.

%package -n python3-libkdumpfile
Summary:        Python interface for libkdumpfile
Group:          Development/Languages/Python

%description -n python3-libkdumpfile
This package contains all necessary python modules to use libkdumpfile via
the Python interpreter.

%endif

%package -n %{name}-devel
Summary:        Include files and libraries for libkdumpfile development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libkdumpfile8 = %{version}

%description -n %{name}-devel
This package contains all necessary include files and libraries needed
to develop applications that require libkdumpfile.

%package -n libkdumpfile8
Summary:        Kernel dump file access library
Group:          System/Libraries

%description -n libkdumpfile8
A library that provides an abstraction layer for reading kernel dump
core files.  It supports different kernel dump core formats, virtual
to physical translation, Xen mappings and more.

This package contains the libkdumpfile library.

%package -n libaddrxlat1
Summary:        Address translation library used primarily by libkdumpfile
Group:          System/Libraries

%description -n libaddrxlat1
A library that provides an abstraction layer for translating addresses
between address spaces (i.e. physical vs virtual).

This package contains the libaddrxlat library.

%package -n libaddrxlat-devel
Summary:        Include files and libraries for libaddrxlat development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libaddrxlat1 = %{version}

%description -n libaddrxlat-devel
This package contains all necessary include files and libraries needed
to develop applications that require libaddrxlat.

# Compatibility cruft
# there is no %%license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %{_defaultdocdir}
%endif
%endif
# End of compatibility cruft

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Avoid autotools recheck after patching config*
touch aclocal.m4 Makefile.in config.h.in configure

%build
%configure --disable-static --without-python
make %{?_smp_mflags}
cd python
%if %new_python_macros
%{python_expand # Build for each Python version
rm -f setup.cfg
make setup.cfg DESTDIR=%{?buildroot} pyexecdir=%{$python_sitearch}
%$python_build
}
%else
make setup.cfg DESTDIR=%{?buildroot} pyexecdir=%{python_sitearch}
%python_build
rm -f setup.cfg
make setup.cfg DESTDIR=%{?buildroot} pyexecdir=%{python3_sitearch}
%python3_build
%endif

%install
%make_install
cd python
%python_install
%if !%new_python_macros
%python3_install
%endif

# Do not install example code
rm -v %{?buildroot}%{_bindir}/dumpattr
rm -v %{?buildroot}%{_bindir}/listxendoms
rm -v %{?buildroot}%{_bindir}/showxlat
# Remove Libtool files
rm -v %{?buildroot}%{_libdir}/libkdumpfile.la
rm -v %{?buildroot}%{_libdir}/libaddrxlat.la
%if %new_python_macros
%{python_expand # Libtool files for extension modules
rm -v %{?buildroot}%{$python_sitearch}/_kdumpfile*.la
rm -v %{?buildroot}%{$python_sitearch}/_addrxlat*.la
}
%else
rm -v %{?buildroot}%{python_sitearch}/_kdumpfile*.la
rm -v %{?buildroot}%{python_sitearch}/_addrxlat*.la
rm -v %{?buildroot}%{python3_sitearch}/_kdumpfile*.la
rm -v %{?buildroot}%{python3_sitearch}/_addrxlat*.la
%endif

%post -n libkdumpfile8 -p /sbin/ldconfig

%post -n libaddrxlat1 -p /sbin/ldconfig

%postun -n libkdumpfile8 -p /sbin/ldconfig

%postun -n libaddrxlat1 -p /sbin/ldconfig

%files -n libkdumpfile8
%defattr(-,root,root)
%{_libdir}/libkdumpfile.so.*
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc README.md NEWS

%files -n libkdumpfile-devel
%defattr(-,root,root)
%{_includedir}/libkdumpfile/kdumpfile.h
%{_libdir}/libkdumpfile.so
%{_libdir}/pkgconfig/libkdumpfile.pc

%files -n libaddrxlat1
%defattr(-,root,root)
%{_libdir}/libaddrxlat.so.*
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc README.md NEWS

%files -n libaddrxlat-devel
%defattr(-,root,root)
%dir %{_includedir}/libkdumpfile
%{_includedir}/libkdumpfile/addrxlat.h
%{_libdir}/libaddrxlat.so
%{_libdir}/pkgconfig/libaddrxlat.pc

%if %new_python_macros

%files %{python_files}
%defattr(-,root,root)
%{python_sitearch}/*

%else

%files -n python2-libkdumpfile
%defattr(-,root,root)
%{python_sitearch}/*

%files -n python3-libkdumpfile
%defattr(-,root,root)
%{python3_sitearch}/*

%endif

%changelog
