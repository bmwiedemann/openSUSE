#
# spec file for package libdnf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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

%if (0%{?sle_version} && 0%{?sle_version} < 150200)
    %global libsolv_version 0.7.3
%else
    %global libsolv_version 0.7.4
%endif

%global libmodulemd_version 1.6.1
%global librepo_version 1.9.6
%global swig_version 3.0.12

# Keep tests switched off for now, it bombs out on SUSE
%bcond_with check

# Keep valgrind tests switched off for now
%bcond_with valgrind

%define somajor 2
%define libname %{name}%{somajor}
%define devname %{name}-devel

Name:           libdnf
Version:        0.33.0
Release:        0
Summary:        Library providing C and Python APIs atop libsolv
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/rpm-software-management/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# PATCH-FIX-OPENSUSE: Fix libdnf build with static libsolvext
Patch1000:      libdnf-0.28.1-with-static-libsolvext.patch
# PATCH-FIX-OPENSUSE: Switch default reposdir to /etc/dnf/repos.d
Patch1001:      libdnf-0.28.1-Switch-default-reposdir-to-etc-dnf-repos.d.patch

# PATCH-FIX-SLE: Revert support for module advisories, since that requires libsolv 0.7.4
## Drop when bsc#1133527 is fixed
Patch2001:      libdnf-0.31.0-Revert-support-for-Module-advisories.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gpgme-devel
BuildRequires:  libsolv-devel >= %{libsolv_version}
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(librepo) >= %{librepo_version}
%if %{with valgrind}
BuildRequires:  valgrind
%endif
BuildRequires:  rpm-devel >= 4.11.0
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(modulemd) >= %{libmodulemd_version}
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  pkgconfig(sqlite3)

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
BuildRequires:  python3-nose
BuildArch:      noarch

%description -n hawkey-man
This package provides the man pages for the hawkey Python bindings.

%package -n python3-hawkey
Summary:        Python 3 bindings for the hawkey interface
Group:          Development/Libraries/Python
BuildRequires:  python3-devel
BuildRequires:  python3-nose
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Recommends:     hawkey-man = %{version}-%{release}
# DNF older than 4.0.0 isn't compatible with this
Conflicts:      python3-dnf < 4.0.0
# Python 2 subpackage has been dropped
Obsoletes:      python2-hawkey < 0.24.1

%description -n python3-hawkey
This package provides the Python 3 bindings for %{name} through
the hawkey interface.

%lang_package


%prep
%autosetup -p1

%if (0%{?sle_version} && 0%{?sle_version} > 150100) || 0%{?suse_version} > 1500
# Revert this patch for SLE 15 >SP1 and SUSE Linux >15
%patch2001 -R -p1
%endif

# Fix sphinx-build run...
sed -e "s/sphinx-build-3/sphinx-build-%{python3_version}/" -i docs/hawkey/CMakeLists.txt

%build
%cmake -DPYTHON_DESIRED:FILEPATH=%{__python3} %{!?with_valgrind:-DDISABLE_VALGRIND=1}
%make_build

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
pushd build
  %make_install
popd

%find_lang %{name}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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

%changelog
