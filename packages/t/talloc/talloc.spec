#
# spec file for package talloc
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "man"
%define psuffix -man
%bcond_without man
%else
%define psuffix %{nil}
%bcond_with man
%endif # build_man
Name:           talloc%{?psuffix}
Version:        2.5.0
Release:        0
%if %{with man}
Summary:        Man pages for the talloc library
%else
Summary:        Samba core memory allocator
%endif
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://talloc.samba.org/
Source:         https://download.samba.org/pub/talloc/talloc-%{version}.tar.gz
Source1:        https://download.samba.org/pub/talloc/talloc-%{version}.tar.asc
Source50:       talloc.keyring
%if %{without man}
Source4:        baselibs.conf
%endif
Patch0:         talloc-python3.5-fix-soabi_name.patch
%if %{with man}
BuildRequires:  doxygen
%else
%{?suse_build_hwcaps_libs}
BuildRequires:  autoconf
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  python3-devel
#!BuildIgnore:  python
%endif # with man

%description
Talloc is a hierarchical, reference counted memory pool system with
destructors.

It is the core memory allocator used in Samba.

%if %{with man}
This package contains the manual pages for the talloc API.
%endif

%if %{without man}
%package -n libtalloc2
Summary:        Samba talloc library
Group:          System/Libraries
Provides:       bundled(libreplace)

%description -n libtalloc2
Talloc is a hierarchical, reference counted memory pool system with
destructors.

It is the core memory allocator used in Samba.

This package includes the talloc2 library.

%package -n libtalloc-devel
Summary:        Libraries and Header Files to Develop Programs with talloc2 Support
# Build man pages in the separate "man" flavor to break the
# doxygen->cmake->krb5->libtalloc build cycle.
Group:          Development/Libraries/C and C++
Requires:       libtalloc2 = %{version}
Requires:       pkgconfig
Recommends:     %{name}-man

%description -n libtalloc-devel
Talloc is a hierarchical, reference counted memory pool system with
destructors.

It is the core memory allocator used in Samba.

Libraries and Header Files to Develop Programs with talloc2 Support.

%package -n python3-talloc
Summary:        Python3 bindings for the Talloc library
Group:          Development/Libraries/Python
Requires:       libtalloc2 = %{version}
Provides:       python-talloc = %{version}-%{release}
Obsoletes:      python-talloc < %{version}-%{release}

%description -n python3-talloc
This package contains the Python3 bindings for the Talloc library.

%package -n python3-talloc-devel
Summary:        Developer tools for the Talloc library
Group:          Development/Libraries/Python
Requires:       pkgconfig
Requires:       python3-talloc = %{version}
Provides:       python-talloc-devel = %{version}-%{release}
Obsoletes:      python-talloc-devel < %{version}-%{release}

%description -n python3-talloc-devel
Libraries and Header Files to Develop Programs with python3-talloc Support

%endif # without man

%prep
%autosetup -p1 -n talloc-%{version}

%build
%if %{with man}
doxygen doxy.config

%install
# Install API documentation
mkdir -p "%{buildroot}/%{_mandir}"
cp -a doc/man/* "%{buildroot}/%{_mandir}/"

%files
%{_mandir}/man3/libtalloc*.3%{?ext_man}
%{_mandir}/man3/talloc*.3%{?ext_man}

%else
export CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -DIDMAP_RID_SUPPORT_TRUSTED_DOMAINS"
CONFIGURE_OPTIONS="\
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-rpath \
	--disable-rpath-install \
	--disable-silent-rules \
	--bundled-libraries=NONE \
	--builtin-libraries=replace \
"
# The waf based build system does not understand the %%configure macro
PYTHONARCHDIR=%{python3_sitearch} ./configure ${CONFIGURE_OPTIONS}
%make_build all

%check
%if "%{qemu_user_space_build}" == "1"
echo "skipping test on qemu userspace build due to AT_RANDOM not changing"
%else # qemu_user_space_build == 1
mkdir lib/talloc
ln test_magic_differs* lib/talloc/
LD_LIBRARY_PATH=bin/shared make test
%endif # qemu_user_space_build == 1

%install
%make_install
rm -r "%{buildroot}/%{_mandir}"
mkdir -p %{buildroot}/%{python3_sysconfig_path include}
mv %{buildroot}/%{_includedir}/pytalloc.h %{buildroot}/%{python3_sysconfig_path include}/pytalloc.h
sed -i 's;${prefix}/include;%{python3_sysconfig_path include};g' %{buildroot}/%{_libdir}/pkgconfig/pytalloc-util.%{python3_sysconfig_var SOABI}.pc

%post -n libtalloc2 -p /sbin/ldconfig
%postun -n libtalloc2 -p /sbin/ldconfig
%post -n python3-talloc -p /sbin/ldconfig
%postun -n python3-talloc -p /sbin/ldconfig

%files -n libtalloc2
%{_libdir}/libtalloc.so.*

%files -n libtalloc-devel
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc

%files -n python3-talloc
%{_libdir}/libpytalloc-util.%{python3_sysconfig_var SOABI}.so.*
%{python3_sitearch}/talloc.%{python3_sysconfig_var SOABI}.so

%files -n python3-talloc-devel
%{python3_sysconfig_path include}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.%{python3_sysconfig_var SOABI}.pc
%{_libdir}/libpytalloc-util.%{python3_sysconfig_var SOABI}.so

%endif # with man

%changelog
