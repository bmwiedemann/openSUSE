#
# spec file for package python-semanage
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-semanage
Version:        2.9
Release:        0
Summary:        Python bindings for SELinux's policy management library
License:        LGPL-2.1-only
Group:          Development/Languages/Python
Url:            https://github.com/SELinuxProject/selinux
Source:         https://github.com/SELinuxProject/selinux/releases/download/20190315/libsemanage-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         suse_path.patch
BuildRequires:  %{python_module devel}
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libbz2-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  libustr-devel
BuildRequires:  python-rpm-macros
BuildRequires:  swig
# Ensure same version
Requires:       libsemanage1 = %{version}
%python_subpackages

%description
This package contains the Python bindings for developing
SELinux policy management applications.

%prep
%setup -q -n libsemanage-%{version}
%patch0

%build
%define _lto_cflags %{nil}
make %{?_smp_mflags} clean
%{python_expand # loop over possible pythons
make -j1 PYTHON=$python CFLAGS="%{optflags}" swigify
make -j1 PYTHON=$python CFLAGS="%{optflags}" \
         LIBDIR="%{_libdir}" \
         LIBEXECDIR="%{_libexecdir}" \
         SHLIBDIR="%{_lib}" \
    all pywrap
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
