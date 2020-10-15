#
# spec file for package talloc-man
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


%{!?py3_soflags:  %global py3_soflags cpython-%{python3_version_nodots}m}
%{!?py3_soflags_dash:   %global py3_soflags_dash %(echo %{py3_soflags} | sed "s/_/-/g")}
%{!?py3_incdir:  %global py3_incdir %(%{__python3} -c "import sysconfig as s; print(s.get_path('include'))")}
%define build_man 0

%if %{build_man}
Name:           talloc-man
BuildRequires:  doxygen
%else
Name:           talloc
BuildRequires:  autoconf
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  python3-devel
#!BuildIgnore:  python
%endif # build_man
URL:            http://talloc.samba.org/
Version:        2.3.1
Release:        0
Summary:        Samba talloc Library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Source:         https://download.samba.org/pub/talloc/talloc-%{version}.tar.gz
Source1:        https://download.samba.org/pub/talloc/talloc-%{version}.tar.asc
Source4:        baselibs.conf
Patch0:         talloc-python3.5-fix-soabi_name.patch
Source50:       talloc.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Talloc is a hierarchical, reference counted memory pool system with
destructors.

It is the core memory allocator used in Samba.

%if ! %{build_man}

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
# Man pages are built in a 2nd spec file in order to break a build cycle with doxygen->cmake->krb5->libtalloc
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} > 1030
Recommends:     %{name}-man
%endif
Requires:       libtalloc2 = %{version}
Requires:       pkg-config

%description -n libtalloc-devel
Talloc is a hierarchical, reference counted memory pool system with
destructors.

It is the core memory allocator used in Samba.

Libraries and Header Files to Develop Programs with talloc2 Support.


%package -n python3-talloc
Summary:        Python3 bindings for the Talloc library
Group:          Development/Libraries/Python
Requires:       libtalloc2 = %{version}
Obsoletes:      python-talloc

%description -n python3-talloc
This package contains the Python3 bindings for the Talloc library.

%package -n python3-talloc-devel
Summary:        Developer tools for the Talloc library
Group:          Development/Libraries/Python
Requires:       pkg-config
Requires:       python3-talloc = %{version}
Obsoletes:      python-talloc-devel

%description -n python3-talloc-devel
Libraries and Header Files to Develop Programs with python3-talloc Support

%endif # ! build_man

%prep
%setup -n talloc-%{version} -q
%autopatch -p1

%build
%if ! %{build_man}
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
./configure ${CONFIGURE_OPTIONS}
make %{?_smp_mflags} \
	all

%else

doxygen doxy.config

%endif # ! build_man

%if ! %{build_man}
%check
%if 0%{?suse_version} != 1110 || "%{_build_arch}" == "x86_64"
%if "%{qemu_user_space_build}" == "1"
echo "skipping test on qemu userspace build due to AT_RANDOM not changing"
%else # qemu_user_space_build == 1
mkdir lib/talloc
ln test_magic_differs* lib/talloc/
LD_LIBRARY_PATH=bin/shared make test
%endif # qemu_user_space_build == 1
%endif # suse_version != 1110; fails for i586 and ppc64
%endif # ! build_man

%install
%if ! %{build_man}
%make_install
rm -r "%{buildroot}/%{_mandir}"
mkdir -p %{buildroot}/%{py3_incdir}
mv %{buildroot}/%{_includedir}/pytalloc.h %{buildroot}/%{py3_incdir}/pytalloc.h
sed -i 's;${prefix}/include;%{py3_incdir};g' %{buildroot}/%{_libdir}/pkgconfig/pytalloc-util.%{py3_soflags}.pc
sed -i 's;-lpytalloc-util.%{py3_soflags_dash};-lpytalloc-util.%{py3_soflags};g' %{buildroot}/%{_libdir}/pkgconfig/pytalloc-util.%{py3_soflags}.pc
%else

# Install API documentation
mkdir -p "%{buildroot}/%{_mandir}"
cp -a doc/man/* "%{buildroot}/%{_mandir}/"

%endif  # ! build_man

%if ! %{build_man}
%post -n libtalloc2 -p /sbin/ldconfig

%postun -n libtalloc2 -p /sbin/ldconfig

%post -n python3-talloc -p /sbin/ldconfig

%postun -n python3-talloc -p /sbin/ldconfig

%files -n libtalloc2
%defattr(-,root,root)
%{_libdir}/libtalloc.so.*

%files -n libtalloc-devel
%defattr(-,root,root)
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc

%files -n python3-talloc
%defattr(-,root,root)
%{_libdir}/libpytalloc-util.%{py3_soflags}.so.*
%{python3_sitearch}/talloc.%{py3_soflags}.so

%files -n python3-talloc-devel
%defattr(-,root,root)
%{py3_incdir}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.%{py3_soflags}.pc
%{_libdir}/libpytalloc-util.%{py3_soflags}.so

%else

%files
%defattr(-,root,root)
%{_mandir}/man3/libtalloc*.3.*
%{_mandir}/man3/talloc*.3.*

%endif # ! build_man

%changelog
