#
# spec file for package libstorage-ng
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


%define libname %{name}1
Name:           libstorage-ng
Version:        4.5.56
Release:        0
Summary:        Library for storage management
License:        GPL-2.0-only
Group:          System/Libraries
URL:            https://github.com/openSUSE/libstorage-ng
Source:         %{name}-%{version}.tar.xz
%if 0%{?suse_version} >= 1330
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_test-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  grep
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(python3)
%if 0%{?suse_version} == 1315
# Using rubygem(test-unit) does not work since ruby2.1-stdlib claims to
# provide rubygem(test-unit). But that is plain wrong. The version in
# ruby2.1-stdlib does not provide the function assert_raise_kind_of.
BuildRequires:  ruby2.1-rubygem-test-unit
%endif
%if 0%{?fedora}
BuildRequires:  rubygem-test-unit
%endif
BuildRequires:  swig >= 3.0.3
BuildRequires:  pkgconfig(libxml-2.0)
%if 0%{?fedora}
BuildRequires:  glibc-langpack-de
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-fr
BuildRequires:  json-c-devel
%else
BuildRequires:  glibc-locale
BuildRequires:  libjson-c-devel
%endif

%description
This package contains libstorage-ng, a library for storage management.

%package lang
Summary:        Languages for package %{name}
Group:          System/Localization
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%package -n %{libname}
Summary:        Library for storage management
Group:          System/Libraries
Recommends:     %{name}-lang
Requires:       coreutils
Suggests:       cryptsetup
Requires:       device-mapper
Suggests:       dmraid
Requires:       lsscsi >= 0.26
Suggests:       lvm2
Suggests:       mdadm >= 3.3
Suggests:       multipath-tools
Requires:       parted >= 3.2
Requires:       pkgconfig
Requires:       util-linux >= 2.16
Requires:       pkgconfig(udev)
Obsoletes:      %{libname} < %{version}
Obsoletes:      libstorage %(echo `seq -s " " -f "libstorage%.f" 9`)
%ifarch s390 s390x
Requires:       s390-tools
%endif
# Old version of libdmraid cannot be used. Upgrading from SLE11 to SLE15
# does not remove old version, so it needs to be marked as conflict.
# For more info, see https://bugzilla.suse.com/show_bug.cgi?id=1088570#c35
Conflicts:      libdmraid.so.1.0.0.rc16(libdmraid.so.1.0.0.rc16)(64bit)

%description -n %{libname}
This package contains libstorage-ng, a library for storage management.

%package devel
Summary:        Header files and documentation for libstorage-ng
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}
Requires:       gcc-c++
Requires:       libstdc++-devel
Requires:       pkgconfig
Requires:       pkgconfig(libxml-2.0)

%description devel
This package contains header files and documentation for developing with
libstorage-ng.

%package python3
Summary:        Python bindings for libstorage-ng
Group:          System/Libraries
Requires:       %{libname} = %{version}
Obsoletes:      libstorage-python

%description python3
This package contains Python bindings for libstorage-ng.

%package ruby
Summary:        Ruby bindings for libstorage-ng
Group:          System/Libraries
Requires:       %{libname} = %{version}
Obsoletes:      libstorage-ruby

%description ruby
This package contains Ruby bindings for libstorage-ng.

%package utils
Summary:        Utils for libstorage-ng
Group:          Development/Tools/Other
Recommends:     ImageMagick
Recommends:     graphviz

%description utils
This package contains utils for libstorage-ng.

%package integration-tests
Summary:        Integration tests for libstorage-ng
Group:          Development/Tools/Other
Requires:       libstorage-ng-python3
BuildArch:      noarch

%description integration-tests
This package contains integration tests for libstorage-ng.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -DNDEBUG"
export CXXFLAGS="%{optflags} -DNDEBUG"

autoreconf -fvi
%configure \
    --docdir="%{_docdir}/%{name}" \
    --disable-static \
    --disable-silent-rules
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check VERBOSE=1 \
    LIBSTORAGE_CONFDIR=%{buildroot}%{_datadir}/libstorage \
    LIBSTORAGE_LOCALEDIR=%{buildroot}%{_datadir}/locale

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.pyc" -delete -print

install -d -m 755 %{buildroot}/run/libstorage-ng
touch %{buildroot}/run/libstorage-ng/lock

%fdupes -s %{buildroot}

%find_lang libstorage-ng

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{name}-lang -f libstorage-ng.lang

%files -n %{libname}
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%license %{_docdir}/%{name}/LICENSE
%{_libdir}/libstorage-ng.so.*
%ghost /run/libstorage-ng
%dir %{_datadir}/libstorage
%{_datadir}/libstorage/udev-filters.json

%files devel
%{_libdir}/libstorage-ng.so
%{_includedir}/storage
%dir %{_docdir}/%{name}/autodocs
%doc %{_docdir}/%{name}/autodocs/*

%files python3
%{python3_sitelib}/storage.py*
%attr(755,root,root) %{python3_sitearch}/_storage.so
# Fedora has brp-python-bytecompile so apparently they want those packaged
%if 0%{?fedora}
%{python3_sitelib}/__pycache__/storage*.pyc
%endif

%files ruby
%if 0%{?fedora}
%{ruby_vendorarchdir}/storage.so
%else
%{rb_vendorarchdir}/storage.so
%endif

%files utils
%dir %{_prefix}/lib/libstorage-ng
%{_prefix}/lib/libstorage-ng/utils

%files integration-tests
%{python3_sitelib}/storageitu.py*
%dir %{_prefix}/lib/libstorage-ng
%{_prefix}/lib/libstorage-ng/integration-tests

%changelog
