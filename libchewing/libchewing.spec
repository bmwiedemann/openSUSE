#
# spec file for package libchewing
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


%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define with_utils 1
%if %{with_utils}
%define utilver 0.4.0+git20150602.81299e5
%endif

Name:           libchewing
%define soname	3
Version:        0.5.1+git20171114.3df07c9
Release:        0
Summary:        Intelligent Phonetic Input Method Library for Traditional Chinese
License:        LGPL-2.1+
Group:          System/I18n/Chinese
Url:            https://github.com/chewing
Source:         %{name}-%{version}.tar.xz
Source1:        chewing-utils-%{utilver}.tar.gz
#PATCH-FIX-UPSTREAM yuyichao@gmail.com fix a lot of errors in the code
Source2:        chewing-utils-abuild.patch
#PATCH-FIX-UPSTREAM marguerite@opensuse.org remove rpath from simple-select
Patch:          libchewing-0.4.0-simple-select-rpath.patch
Source99:       baselibs.conf
BuildRequires:  autoconf >= 2.67
%if %{with_utils}
BuildRequires:  gtk2-devel
%endif
BuildRequires:  libtool
%if 0%{?suse_version} >= 1230
BuildRequires:  makeinfo
%else
BuildRequires:  texinfo
%endif
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  sqlite3-devel
Requires(post):	info
Requires(postun):	info
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Intelligent phonetic input method library for traditional Chinese.

%package devel
Summary:        Development package for chewing
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}
Requires:       python-chewing = %{version}

%description devel
Development package for chewing (An Intelligent phonetic input method library for traditional Chinese)

%package -n %{name}%{soname}
Summary:        Chewing libraries
Group:          System/Libraries
Requires:       chewing-data
Recommends:     chewing-utils = %{version}

%description -n %{name}%{soname}
This package contains libraries for Chewing, an intelligent phonetic
input method library for traditional Chinese.

%package -n chewing-data
Summary:        Chewing Data for %{name}
Group:          System/I18n/Chinese

%description -n chewing-data
This package contains data files for chewing, an intelligent phonetic
input method library for traditional Chinese.

%package -n chewing-utils
Summary:        Hash editor for %{name}
Group:          System/I18n/Chinese

%description -n chewing-utils
This package contains a hash editor for chewing, an intelligent phonetic
input method library for tranditional Chinese.

It's used to add, modify and remove entries in the chewing user database
(usually located at ~/.chewing/uhash.dat).

%package -n python-chewing
Summary:        Python 2 bindings for %{name}
Group:          Development/Libraries/Python
%py_requires

%description -n python-chewing
This package contains python bindings for chewing, an intelligent phonetic
input method library for traditional Chinese.

Only input method framework written in python (like very old versions of ibus)
or developers will need it.


%prep
%setup -q
%patch -p1

%build
# build libchewing main
./autogen.sh
NCURSESW6_CFLAGS=`ncursesw6-config --cflags`
NCURSESW6_LIBS=`ncursesw6-config --libs`
CFLAGS="$NCURSESW6_CFLAGS %{optflags} -fno-strict-aliasing" \
LIBS="$NCURSES_LIBS" \
%configure --disable-static --with-pic --with-ncurses

make %{?_smp_mflags}

# build contrib
pushd contrib
make -f Makefile %{?_smp_mflags}
popd

# build utils
cp -r %{SOURCE1} ./
tar -xf chewing-utils-%{utilver}.tar.gz
rm -rf chewing-utils-%{utilver}.tar.gz
pushd chewing-utils-%{utilver}/hash-editor
pushd ..
patch -p1 < %{SOURCE2}
popd
make %{?_smp_mflags}
popd

%install
# install main
make DESTDIR=%{buildroot} install %{?_smp_mflags}

# remove .la file
find %{buildroot}%{_libdir} -name "*.la" -delete

# install simple-select
mkdir -p %{buildroot}%{_bindir}
cp -r contrib/simple-select %{buildroot}%{_bindir}

# install python 2 bindings
mkdir -p %{buildroot}%{python_sitearch}/chewing/
cp -r contrib/python/chewing.py %{buildroot}%{python_sitearch}/chewing/
pushd %{buildroot}%{python_sitearch}/chewing/
%py_compile -O .
popd

# install chewing-utils
mkdir -p %{buildroot}%{_docdir}/chewing-utils
pushd chewing-utils-%{utilver}
cp -r AUTHORS %{buildroot}%{_docdir}/chewing-utils/
cp -r COPYING %{buildroot}%{_docdir}/chewing-utils/
cp -r hash-editor/ChangeLog.old %{buildroot}%{_docdir}/chewing-utils/ChangeLog
cp -r hash-editor/src/che %{buildroot}%{_bindir}
cp -r hash-editor/src/zhuindict_compile %{buildroot}%{_bindir}
popd

%post -n %{name}%{soname}
/sbin/ldconfig
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n %{name}%{soname} -p /sbin/ldconfig

%preun -n %{name}%{soname}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n chewing-utils -p /sbin/ldconfig

%postun -n chewing-utils -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README.md TODO
%{_bindir}/simple-select
%{_libdir}/libchewing.so.3
%{_libdir}/libchewing.so.3.3.1
%{_infodir}/*.gz

%files -n chewing-data
%defattr(-, root, root)
%{_datadir}/%{name}/

%files -n python-chewing
%defattr(-, root, root)
%{python_sitearch}/chewing

%files -n chewing-utils
%defattr(-, root, root)
%{_bindir}/che
%{_bindir}/zhuindict_compile
%doc %{_docdir}/chewing-utils

%files devel
%defattr(-, root, root)
%{_includedir}/chewing/
%{_libdir}/libchewing.so
%{_libdir}/pkgconfig/chewing.pc

%changelog
