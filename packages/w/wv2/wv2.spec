#
# spec file for package wv2
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wv2
Version:        0.4.2
Release:        0
Summary:        Library for Importing Microsoft Word (tm) Documents
License:        LGPL-2.1+
Group:          Productivity/Publishing/Word
Url:            http://sourceforge.net/projects/wvware
Source0:        http://sourceforge.net/projects/wvware/files/%{name}-%{version}.tar.bz2
Source1:        http://sourceforge.net/projects/wvware/files/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Patch0:         glib_include.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libgsf-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The wv2 library is used to import Microsoft Word documents in koffice
for example.

%package -n libwv2-4
Summary:        Library for Importing Microsoft Word (tm) Documents
Group:          System/Libraries

%description -n libwv2-4
The wv2 library is used to import Microsoft Word documents in koffice
for example.

%package devel
Summary:        Library for Importing Microsoft Word(tm) Documents - development files
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-4 = %{version}
Requires:       libgsf-devel
Requires:       libstdc++-devel

%description devel
The wv2 library is used to import Microsoft Word documents in koffice
for example.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%optflags -fvisibility-inlines-hidden"
# build fails with %%cmake macro
cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
	%endif

make VERBOSE=1 %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
  mkdir -p %{buildroot}%{_defaultdocdir}/wv2/
  cp -a doc AUTHORS README TODO COPYING.LIB \
        %{buildroot}%{_defaultdocdir}/wv2/
  rm -rf %{buildroot}%{_defaultdocdir}/wv2/doc/escher/CVS
  rm -rf %{buildroot}%{_defaultdocdir}/wv2/doc/CVS
  rm -rf %{buildroot}%{_defaultdocdir}/wv2/doc/.cvsignore

%post -n libwv2-4 -p /sbin/ldconfig

%postun -n libwv2-4 -p /sbin/ldconfig

%files -n libwv2-4
%defattr(-, root, root)
%dir %{_defaultdocdir}/wv2
%{_defaultdocdir}/wv2/AUTHORS
%{_defaultdocdir}/wv2/COPYING.LIB
/%{_libdir}/libwv2.so.*

%files devel
%defattr(-, root, root)
%dir %{_defaultdocdir}/wv2
%{_defaultdocdir}/wv2/doc
%{_defaultdocdir}/wv2/README
%{_defaultdocdir}/wv2/TODO
%{_bindir}/wv2-config
%{_includedir}/wv2
%{_libdir}/libwv2.so
%{_libdir}/wvWare

%changelog
