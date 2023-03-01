#
# spec file for package libdnf
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 Neal Gompa <ngompa13@gmail.com>.
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


%global libsolv_version 0.7.20
%global libmodulemd_version 2.13.0
%global librepo_version 1.13.1
%global dnf_conflict 4.11.0
%global swig_version 3.0.12

# Keep tests switched off for now, it bombs out on SUSE
%bcond_with check

# Keep valgrind tests switched off for now
%bcond_with valgrind

%define somajor 2
%define libname %{name}%{somajor}
%define devname %{name}-devel

Name:           libdnf
Version:        0.70.0
Release:        0
Summary:        Library providing C and Python APIs atop libsolv
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/rpm-software-management/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Backports from upstream

# Fixes proposed upstream

# openSUSE specific fixes
## Fix libdnf build with static libsolvext
Patch1000:      libdnf-0.48.0-with-static-libsolvext.patch
## Switch default reposdir to /etc/dnf/repos.d
Patch1001:      libdnf-0.54.2-Switch-default-reposdir-to-etc-dnf-repos.d.patch
## Switch allow_vendor_change off by default
Patch1002:      libdnf-0.55.0-Switch-allow_vendor_change-off.patch
## Migrate DNF persistent state directory to /usr/lib/sysimage
Patch1003:      libdnf-0.58.0-Use-usr-lib-sysimage-for-the-persistent-state-dir.patch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gpgme-devel
BuildRequires:  libsolv-devel >= %{libsolv_version}
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(librepo) >= %{librepo_version}
%if %{with valgrind}
BuildRequires:  valgrind
%endif
BuildRequires:  rpm-devel >= 4.15.0
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(modulemd-2.0) >= %{libmodulemd_version}
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zck) >= 0.9.11

# libsolv specific BRs
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

%description
This library provides a high level RPM package manager that can be integrated
into applications to manage software. It is currently used by DNF, RPM-OSTree,
and PackageKit.

%package -n %{libname}
Summary:        Library providing an interface atop libsolv
Group:          System/Libraries
Recommends:     %{name}-lang = %{version}-%{release}
# gobject-introspection is no longer used
Obsoletes:      typelib-1_0-Dnf-1_0 < 0.24.1
# To avoid API issues with librepo and incomprehensible crashes
Requires:       librepo0%{?_isa} >= %{librepo_version}
# To avoid API issues with libmodulemd
Requires:       libmodulemd2%{?_isa} >= %{libmodulemd_version}

%description -n %{libname}
This library provides an interface atop libsolv, and a high-level
RPM package manager library interface.

%package -n python3-%{name}
Summary:        Python 3 bindings for the libdnf library
Group:          Development/Libraries/Python
Requires:       %{libname}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  swig >= %{swig_version}
Conflicts:      python3-dnf < %{dnf_conflict}

%description -n python3-%{name}
This package provides the Python 3 bindings for the libdnf library.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{devname}
This package provides the headers and libraries for developing applications
that use %{name}.

%package -n hawkey-man
Summary:        Documentation for the hawkey Python bindings
Group:          Documentation/Man
BuildRequires:  python3-Sphinx
BuildArch:      noarch

%description -n hawkey-man
This package provides the man pages for the hawkey Python bindings.

%package -n python3-hawkey
Summary:        Python 3 bindings for the hawkey interface
Group:          Development/Libraries/Python
BuildRequires:  python3-devel
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Recommends:     hawkey-man = %{version}-%{release}
Conflicts:      python3-dnf < %{dnf_conflict}
# Python 2 subpackage has been dropped
Obsoletes:      python2-hawkey < 0.24.1

%description -n python3-hawkey
This package provides the Python 3 bindings for %{name} through
the hawkey interface.

%package repo-config-zypp
Summary:        Enables Zypper repository configuration for DNF
Group:          System/Packages
# We're compatible with any SUSE Linux distribution
Requires:       (product(SUSE_SLE) or suse-release)
# Only one instance of this package may be installed at a time...
Provides:       rpm-repos-openSUSE
Conflicts:      rpm-repos-openSUSE

%description repo-config-zypp
This package allows libdnf and all consumers to be able to reuse
repository configuration files set for Zypper.


%lang_package

%prep
%autosetup -p1

# Fix sphinx-build run...
sed -e "s/sphinx-build-3/sphinx-build-%{python3_version}/" -i docs/hawkey/CMakeLists.txt

%build
%cmake -DPYTHON_DESIRED:FILEPATH=%{__python3} %{!?with_valgrind:-DDISABLE_VALGRIND=1}
%cmake_build

%if %{with check}
%check
# The test suite doesn't automatically know to look at the "built"
# library, so we force it by creating an LD_LIBRARY_PATH
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

if [ "$(id -u)" == "0" ] ; then
        cat <<ERROR 1>&2
Package tests cannot be run under superuser account.
Please build the package as non-root user.
ERROR
        exit 1
fi
pushd build
  make ARGS="-V" test
popd

%endif

%install
%cmake_install

%find_lang %{name}

# For repo-config-zypp subpackage
mkdir -p %{buildroot}%{_sysconfdir}/zypp/repos.d
ln -sr %{buildroot}%{_sysconfdir}/zypp/repos.d %{buildroot}%{_sysconfdir}/distro.repos.d

%python_compileall
%fdupes %{buildroot}%{python3_sitearch}

%ldconfig_scriptlets -n %{libname}

%files -n %{libname} -f %{name}.lang
%license COPYING
%doc README.md AUTHORS
%{_libdir}/%{name}.so.%{somajor}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/README

%files -n python3-%{name}
%{python3_sitearch}/%{name}/

%files -n %{devname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
%{_datadir}/gtk-doc/html/%{name}/

%files -n hawkey-man
%{_mandir}/man3/hawkey.3*

%files -n python3-hawkey
%{python3_sitearch}/hawkey/

%files repo-config-zypp
# Co-own the zypp repos dir
%dir %{_sysconfdir}/zypp
%dir %{_sysconfdir}/zypp/repos.d
%{_sysconfdir}/distro.repos.d

%changelog
