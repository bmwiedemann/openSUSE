#
# spec file for package libselinux-bindings
#
# Copyright (c) 2023 SUSE LLC
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


%{?sle15_python_module_pythons}
%if 0%{?suse_version} < 1699
# Leap15, SLES15
# have some safe defaults
%define python_subpackage_name python3-selinux
%define python_base_requirement python3
%if "%pythons" == "python36"
%define python_subpackage_name python36-selinux
%define python_base_requirement python36
%endif
%if "%pythons" == "python310"
%define python_subpackage_name python310-selinux
%define python_base_requirement python310
%endif
%if "%pythons" == "python311"
%define python_subpackage_name python311-selinux
%define python_base_requirement python311
%endif
%else
# Tumbleweed
%define python_subpackage_name python3-selinux
%define python_base_requirement python3
%endif

%define libsepol_ver 3.5
Name:           libselinux-bindings
Version:        3.5
Release:        0
Summary:        SELinux runtime library and simple utilities
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/libselinux-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/libselinux-%{version}.tar.gz.asc
Source2:        libselinux.keyring
Source3:        selinux-ready
Source4:        baselibs.conf
# PATCH-FIX-UPSTREAM Include <sys/uio.h> for readv prototype
Patch4:         readv-proto.patch
# PATCH-FIX-UPSTREAM python3.8-compat.patch mcepl@suse.com
# Make linking working even when default pkg-config doesn’t provide -lpython<ver>
Patch5:         python3.8-compat.patch
Patch6:         swig4_moduleimport.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  libsepol-devel-static >= %{libsepol_ver}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  ruby-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(libpcre2-8)

%description
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

%package -n %{python_subpackage_name}
%define oldpython python
Summary:        Python bindings for the SELinux runtime library
Group:          Development/Libraries/Python
Requires:       %{python_base_requirement}
Requires:       libselinux1 = %{version}
%ifpython2
Obsoletes:      %{oldpython}-selinux < %{version}
Provides:       %{oldpython}-selinux = %{version}
%endif

%description -n %{python_subpackage_name}
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
make %{?_smp_mflags} LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" swigify V=1 USE_PCRE2=y
make %{?_smp_mflags} LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" pywrap V=1 USE_PCRE2=y
make %{?_smp_mflags} LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" rubywrap V=1 USE_PCRE2=y

%install
make DESTDIR=%{buildroot} LIBDIR="%{_libdir}" SHLIBDIR="/%{_lib}" LIBSEPOLA=%{_libdir}/libsepol.a install-pywrap V=1
make DESTDIR=%{buildroot} LIBDIR="%{_libdir}" SHLIBDIR="/%{_lib}" LIBSEPOLA=%{_libdir}/libsepol.a install-rubywrap V=1
rm -rf %{buildroot}/%{_lib} %{buildroot}%{_libdir}/libselinux.* %{buildroot}%{_libdir}/pkgconfig

%files -n %{python_subpackage_name}
%{python3_sitearch}/*selinux*

%files -n ruby-selinux
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/selinux.so

%changelog
