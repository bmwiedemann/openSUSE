#
# spec file for package libselinux-bindings
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define libsepol_ver 3.1
Name:           libselinux-bindings
Version:        3.1
Release:        0
Summary:        SELinux runtime library and simple utilities
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
# embedded is the MD5
Source:         libselinux-%{version}.tar.gz
Source1:        selinux-ready
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM Include <sys/uio.h> for readv prototype
Patch4:         readv-proto.patch
# PATCH-FIX-UPSTREAM python3.8-compat.patch mcepl@suse.com
# Make linking working even when default pkg-config doesn’t provide -lpython<ver>
Patch5:         python3.8-compat.patch
Patch6:         swig4_moduleimport.patch
BuildRequires:  libsepol-devel-static >= %{libsepol_ver}
BuildRequires:  pcre-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  ruby-devel
BuildRequires:  swig

%description
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

%package -n python3-selinux
%define oldpython python
Summary:        Python bindings for the SELinux runtime library
Group:          Development/Libraries/Python
Requires:       libselinux1 = %{version}
Requires:       python3
%ifpython2
Obsoletes:      %{oldpython}-selinux < %{version}
Provides:       %{oldpython}-selinux = %{version}
%endif

%description -n python3-selinux
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

This subpackage contains Python extensions to use SELinux from that
language.

%package -n ruby-selinux
Summary:        Ruby bindings for the SELinux runtime library
Group:          Development/Languages/Ruby
Requires:       libselinux1 = %{version}
Requires:       ruby

%description -n ruby-selinux
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

This subpackage contains Ruby extensions to use SELinux from that
language.

%prep
%setup -q -n libselinux-%{version}
%autopatch -p1

%build
%define _lto_cflags %{nil}
make %{?_smp_mflags} LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" -C src V=1
make %{?_smp_mflags} LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" -C src swigify V=1
make %{?_smp_mflags} LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" -C src pywrap V=1
make %{?_smp_mflags} LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" -C src rubywrap V=1

%install
make DESTDIR=%{buildroot} LIBDIR="%{_libdir}" SHLIBDIR="/%{_lib}" LIBSEPOLA=%{_libdir}/libsepol.a -C src install V=1
make DESTDIR=%{buildroot} LIBDIR="%{_libdir}" SHLIBDIR="/%{_lib}" LIBSEPOLA=%{_libdir}/libsepol.a -C src install-pywrap V=1
make DESTDIR=%{buildroot} LIBDIR="%{_libdir}" SHLIBDIR="/%{_lib}" LIBSEPOLA=%{_libdir}/libsepol.a -C src install-rubywrap V=1
rm -rf %{buildroot}/%{_lib} %{buildroot}%{_libdir}/libselinux.* %{buildroot}%{_libdir}/pkgconfig

%files -n python3-selinux
%{python3_sitearch}/*selinux*

%files -n ruby-selinux
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/selinux.so

%changelog
