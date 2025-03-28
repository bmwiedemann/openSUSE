#
# spec file for package libselinux-bindings
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15allpythons}
%define python_subpackage_only 1
%define libsepol_ver 3.8.1
%define upname libselinux
Name:           libselinux-bindings
Version:        3.8.1
Release:        0
Summary:        SELinux runtime library and utilities
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{upname}-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{upname}-%{version}.tar.gz.asc
Source2:        libselinux.keyring
Source3:        selinux-ready
Source4:        baselibs.conf
# PATCH-FIX-UPSTREAM Include <sys/uio.h> for readv prototype
Patch4:         readv-proto.patch
Patch5:         skip_cycles.patch
# PATCH-FIX-UPSTREAM python3.8-compat.patch mcepl@suse.com
# Make linking working even when default pkg-config doesn’t provide -lpython<ver>
Patch6:         python3.8-compat.patch
Patch7:         swig4_moduleimport.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libselinux-devel = %{version}
BuildRequires:  libsepol-devel >= %{libsepol_ver}
BuildRequires:  libsepol-devel-static >= %{libsepol_ver}
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  ruby-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(libpcre2-8)
%python_subpackages

%description
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

%package -n python-selinux
%define oldpython python
Summary:        Python bindings for the SELinux runtime library
Group:          Development/Libraries/Python
Requires:       libselinux1 = %{version}
Obsoletes:      python-selinux < %{version}
Provides:       python-selinux = %{version}
%ifpython2
Obsoletes:      %{oldpython}-selinux < %{version}
Provides:       %{oldpython}-selinux = %{version}
%endif

%description -n python-selinux
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
%autosetup -p1 -n %{upname}-%{version}

%build
%{python_expand :
%make_build LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" swigify USE_PCRE2=y PYTHON=$python
%make_build LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" pywrap USE_PCRE2=y PYTHON=$python
%make_build LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fno-semantic-interposition" rubywrap USE_PCRE2=y PYTHON=$python
}

%install
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_sbindir}
%{python_expand :
make DESTDIR=%{buildroot} LIBDIR="%{_libdir}" SHLIBDIR="/%{_lib}" PYTHON=$python LIBSEPOLA=%{_libdir}/libsepol.a install-pywrap V=1
make DESTDIR=%{buildroot} LIBDIR="%{_libdir}" SHLIBDIR="/%{_lib}" PYTHON=$python LIBSEPOLA=%{_libdir}/libsepol.a install-rubywrap V=1
}

# Remove duplicate files
%fdupes -s %{buildroot}%{_mandir}

%files %{python_files selinux}
%{python_sitearch}/selinux
%{python_sitearch}/selinux-%{version}.dist-info
%{python_sitearch}/_selinux*

%files -n ruby-selinux
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/selinux.so

%changelog
