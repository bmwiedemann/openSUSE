#
# spec file for package python-semanage
#
# Copyright (c) 2024 SUSE LLC
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
%define soversion 2
%define libname libsemanage%{soversion}

%define libsepol_ver     3.6
%define libselinux_ver   3.6

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-semanage
Version:        3.6
Release:        0
Summary:        Python bindings for SELinux's policy management library
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://github.com/SELinuxProject/selinux
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsemanage-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsemanage-%{version}.tar.gz.asc
Source2:        libsemanage.keyring
Source3:        baselibs.conf
# PATCH-FIX-UPSTREAM bsc#1133102 LTO: Update map file to include new symbols and remove wildcards
# For now we need to disable this. This breaks e.g. shadow and also other packages in security:SELinux
# Patch0:         libsemanage-update-map-file.patch
BuildRequires:  %{python_module devel}
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libbz2-devel
BuildRequires:  libselinux-devel >= %{libselinux_ver}
BuildRequires:  libsepol-devel >= %{libsepol_ver}
BuildRequires:  python-rpm-macros
BuildRequires:  swig
# Ensure same version
Requires:       %{libname} = %{version}
%python_subpackages

%description
This package contains the Python bindings for developing
SELinux policy management applications.

%prep
%setup -q -n libsemanage-%{version}
# Replace /usr/libexec with whatever the distro defines as libexecdir - across all files
grep /usr/libexec . -rl | xargs sed -i "s|/usr/libexec|%{_libexecdir}|g"

%build
%make_build clean
%{python_expand # loop over possible pythons
%make_build PYTHON=$python CFLAGS="%{optflags} -fno-semantic-interposition -ffat-lto-objects" swigify
%make_build PYTHON=$python CFLAGS="%{optflags} -fno-semantic-interposition -ffat-lto-objects" \
         LIBDIR="%{_libdir}" \
         LIBEXECDIR="%{_libexecdir}" \
         SHLIBDIR="%{_lib}" \
    pywrap
}

%install
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
%{python_expand # loop over possible pythons
%make_install install-pywrap PYTHON="$python" \
     LIBDIR="%{_libdir}" \
     LIBEXECDIR="%{_libexecdir}" \
     SHLIBDIR="%{_libdir}"
}

# remove files contained in other packages
rm -rf %{buildroot}%{_sysconfdir}
%if "%{_lib}" == "lib64"
rm -rf %{buildroot}%{_libexecdir}
%else
rm -rf %{buildroot}%{_libexecdir}/selinux
%endif
rm -rf %{buildroot}%{_includedir}
rm  -f %{buildroot}%{_libdir}/libsemanage.*
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_mandir}

%files %{python_files}
%{python_sitearch}/*

%changelog
