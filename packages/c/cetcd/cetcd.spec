#
# spec file for package cetcd
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


Name:           cetcd
Version:        0.0.5_b79a7a2
Release:        0
Summary:        C client library for etcd
License:        Apache-2.0 and BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            http://github.com/shafreeck/cetcd
Source:         cetcd-master.zip
Patch0:         cetcd-SUSE.diff
BuildRequires:  libcurl-devel
BuildRequires:  libyajl-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cetcd is a C client library for etcd.

%package -n libcetcd0
Summary:        C client library for etcd
Group:          System/Libraries

%description -n libcetcd0
Cetcd is a C client library for etcd.
This package contains the runtime library.

%package devel
Summary:        Development package for cetcd
Group:          Development/Libraries/C and C++
Requires:       curl-devel
Requires:       libcetcd0 = %{version}

%description devel
Cetcd is a C client library for etcd.
This package contains all files to develop and link against libcetcd.

%prep
%setup -q -n cetcd-master
%patch0 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"

%install
make install prefix=%{buildroot}/%{_prefix}
%if "%{_lib}" == "lib64"
mkdir -p %{buildroot}/%{_libdir}
mv -v %{buildroot}/%{_prefix}/lib/libcetcd.* %{buildroot}/%{_libdir}
%endif
# Fix .so symlink
ln -sf libcetcd.so.0 %{buildroot}/%{_libdir}/libcetcd.so

%post -n libcetcd0 -p /sbin/ldconfig
%postun -n libcetcd0 -p /sbin/ldconfig

%files -n libcetcd0
%defattr(-,root,root)
%{_libdir}/libcetcd.so.0

%files devel
%defattr(-,root,root)
%doc LICENSE README.md
%{_libdir}/libcetcd.so
%{_includedir}/cetcd.h
%{_includedir}/cetcd_array.h

%changelog
