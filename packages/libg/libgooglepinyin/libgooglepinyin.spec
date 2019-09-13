#
# spec file for package libgooglepinyin
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define  py_ver  %(python -c "import sys; v=sys.version_info[:2]; print '%%d.%%d'%%v" 2>/dev/null || echo PYTHON-NOT-FOUND)

Name:           libgooglepinyin
Version:        0.1.2
Release:        1
Summary:        A fork from google pinyin on android
Group:		System/I18n/Chinese
Url:            http://code.google.com/p/libgooglepinyin
License:        Apache-2.0
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  cairo-devel
BuildRequires: 	cmake 
BuildRequires:	gcc-c++ 
BuildRequires:	gtk2-devel 
BuildRequires:	intltool 
BuildRequires:	pango-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libgooglepinyin is an input method fork from google pinyin on android

%package -n %{name}0
Summary:	A fork from googlepinyin on android
Group:		System/I18n/Chinese

%description -n %{name}0
libgooglepinyin is an input method fork from google pinyin on android

%package devel
Summary:        Development files for libgooglepinyin
Group:          Development/Libraries/Other
%if 0%{?suse_version}
Requires:       python-base >= %py_ver
%else
Requires:       python-libs >= %py_ver
%endif
Requires:	%{name}0 = %{version}

%description devel
The libgooglepinyin-devel package includes the header files for the googlepinyin package.
  
%prep
%setup -q -n %{name}-%{version}

%build
%{__mkdir} -pv build
pushd build
cmake   -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DLIB_INSTALL_DIR=%{_libdir} \
        ..
make

%install
pushd build
make DESTDIR=%{buildroot} install

# Fix ibus-googlepinyin working in 64bit
%ifarch x86_64
mkdir -p %{buildroot}/%{_prefix}/lib/
cd %{buildroot}/%{_prefix}/lib/
ln -s  ../lib64/googlepinyin googlepinyin
%endif

%{__strip} %{buildroot}%{_libdir}/%{name}.so.0.1.0

%post -n %{name}0 -p /sbin/ldconfig

%postun -n %{name}0 -p /sbin/ldconfig

%files -n %{name}0
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*
%{_libdir}/googlepinyin
%ifarch x86_64
%{_prefix}/lib/googlepinyin
%endif

%files devel
%defattr(-,root,root,-)
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/googlepinyin.pc
%{_includedir}/googlepinyin

%changelog
