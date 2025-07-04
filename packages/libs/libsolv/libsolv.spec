#
# spec file for package libsolv
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


%define libname libsolv1

%if 0%{?sle_version} >= 120300 || 0%{?suse_version} >= 1330 || !0%{?suse_version}
%bcond_without bz2
%bcond_without xz
%else
%bcond_with bz2
%bcond_with xz
%endif
%if 0%{?sle_version} >= 150000 || 0%{?suse_version} >= 1500
%bcond_without zstd
%else
%bcond_with zstd
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7 || 0%{?mageia} >= 6 || 0%{?suse_version} >= 1330
%bcond_without richdeps
%else
%bcond_with richdeps
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%bcond_without python_singlespec
%{?sle15allpythons}
%endif
# we need at least swig 1.3.40 for the bindings ($typemap support)
%if 0%{?suse_version} != 1110
%if %{with python_singlespec}
%bcond_with python
%bcond_with python3
%else
%bcond_without python3
%if 0%{?suse_version} < 1550
%bcond_without python
%else
%bcond_with python
%endif
%endif
%bcond_without ruby
%bcond_without perl
%else
%bcond_with python3
%bcond_with python
%bcond_with ruby
%bcond_with perl
%endif

%if 0%{?suse_version} >= 1600
%bcond_without static
%bcond_without shared
%else
%bcond_without static
%bcond_with shared
%endif

%bcond_with zypp

Name:           libsolv
Version:        0.7.33
Release:        0
Summary:        Package dependency solver using a satisfiability algorithm
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/openSUSE/libsolv
Source:         libsolv-%{version}.tar.bz2
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  rpm-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?mageia}
BuildRequires:  db-devel
%endif

%if %{with perl}
BuildRequires:  perl
%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?mageia}
BuildRequires:  perl-devel
%endif
BuildRequires:  swig
%endif

%if %{with ruby}
%global ruby_vendorarch %(ruby  -r rbconfig -e "puts RbConfig::CONFIG['vendorarchdir'].nil? ? RbConfig::CONFIG['sitearchdir'] : RbConfig::CONFIG['vendorarchdir']")
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  swig
%endif

%if %{with python}
%global python_sitearch %(python -c "from sysconfig import get_path; print(get_path('platlib'))")
BuildRequires:  python-devel
BuildRequires:  swig
%endif

%if %{with python3}
%global python3_sitearch %(python3 -c "from sysconfig import get_path; print(get_path('platlib'))")
BuildRequires:  python3-devel
BuildRequires:  swig
%endif

%if %{with python_singlespec}
BuildRequires:  %{python_module devel}
BuildRequires:  swig
%endif

%if %{with bz2}
%if 0%{?suse_version}
BuildRequires:  libbz2-devel
%else
BuildRequires:  bzip2-devel
%endif
%endif

%if %{with xz}
BuildRequires:  xz-devel
%endif

%if %{with zstd}
BuildRequires:  libzstd-devel
%endif

%if %{with python_singlespec}
%define python_subpackage_only 1
%python_subpackages
%endif

%description
libsolv is a library for solving packages and reading repositories.
The solver uses a satisfiability algorithm.

%if %{with shared}
%package -n %{libname}
Summary:        Package dependency solver using a satisfiability algorithm
Group:          System/Libraries

%description -n %{libname}
libsolv is a library for solving packages and reading repositories.
It consists of two central blocks: Using a dictionary approach to
store and retrieve package and dependency information, and, using a
so-called satisfiability algorithm for resolving package
dependencies.

%endif

%package devel
Summary:        Development files for libsolv, a package solver
Group:          Development/Libraries/C and C++
%if %{with shared}
Requires:       %{libname} = %version
%endif
Requires:       rpm-devel
Conflicts:      libsatsolver-devel

%description devel
Development files for libsolv, a library for solving packages and
reading repositories.

%package devel-static
Summary:        Development files for libsolv, a package solver
Group:          Development/Libraries/C and C++
Requires:       libsolv-devel = %version

%description devel-static
Development files for libsolv, a library for solving packages and
reading repositories.

%package tools-base
Summary:        Utilities used by libzypp to manage .solv files
Group:          System/Management
Provides:       libsolv-tools:%{_bindir}/repo2solv
Conflicts:      libsolv-tools < %{version}

%description tools-base
This subpackage contains utilities used by libzypp to manage solv files.

%package tools
Summary:        Utilities to work with .solv files
Group:          System/Management
Conflicts:      satsolver-tools-obsolete
Obsoletes:      satsolver-tools < 0.18
Provides:       satsolver-tools = 0.18
Requires:       libsolv-tools-base = %{version}

%description tools
libsolv is a library for solving packages and reading repositories.

This subpackage contains utilities to create and work with the .solv
files used by libsolv.

%package demo
Summary:        Applications demoing the libsolv library
Group:          System/Management
Requires:       curl
Conflicts:      libsatsolver-demo
%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?mageia}
Requires:       gnupg2
%endif
%if 0%{?suse_version}
Requires:       gpg2
%endif

%description demo
Applications demoing the libsolv library.

%package -n ruby-solv
Summary:        Ruby bindings for the libsolv library
Group:          Development/Languages/Ruby
%if 0%{?suse_version}
Provides:       ruby-solv-ruby-%{rb_ver}
%endif

%description -n ruby-solv
Ruby bindings for libsolv.

%package -n python-solv
%if 0%{?py_requires:1} && %{with python}
%py_requires
%endif
Summary:        Python bindings for the libsolv library
Group:          Development/Languages/Python

%description -n python-solv
Python bindings for libsolv.

%if %{with python3}
%package -n python3-solv
Summary:        Python3 bindings for the libsolv library
Group:          Development/Languages/Python

%description -n python3-solv
Python3 bindings for libsolv.
%endif

%package -n perl-solv
Summary:        Perl bindings for the libsolv library
Group:          Development/Languages/Perl
Requires:       perl = %{perl_version}

%description -n perl-solv
Perl bindings for libsolv.

%prep
%setup -q

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"

CMAKE_FLAGS=
%if 0%{?fedora} || 0%{?rhel} >= 6
CMAKE_FLAGS="-DFEDORA=1"
%endif
%if 0%{?mageia}
CMAKE_FLAGS="-DMAGEIA=1"
%endif
%if 0%{?suse_version}
CMAKE_FLAGS="-DSUSE=1"
%endif

cmake . $CMAKE_FLAGS \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB=%{_lib} \
	-DCMAKE_VERBOSE_MAKEFILE=TRUE \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DWITH_LIBXML2=1 \
	-DENABLE_APPDATA=1 \
	-DENABLE_COMPS=1 \
	-DMULTI_SEMANTICS=1 \
	%{?with_static:-DENABLE_STATIC=1 -DENABLE_STATIC_TOOLS=1 -DENABLE_STATIC_BINDINGS=1} \
	%{!?with_shared:-DDISABLE_SHARED=1} \
	%{?with_perl:-DENABLE_PERL=1} \
	%{?with_python:-DENABLE_PYTHON=1} \
	%{?with_python3:-DENABLE_PYTHON3=1} \
	%{?with_ruby:-DENABLE_RUBY=1} \
	%{?with_bz2:-DENABLE_BZIP2_COMPRESSION=1} \
	%{?with_xz:-DENABLE_LZMA_COMPRESSION=1} \
	%{?with_zstd:-DENABLE_ZSTD_COMPRESSION=1} \
	%{?with_zstd:-DENABLE_ZCHUNK_COMPRESSION=1} \
	%{?with_richdeps:-DENABLE_COMPLEX_DEPS=1} \
	%{?with_zypp:-DENABLE_SUSEREPO=1 -DENABLE_HELIXREPO=1} \
	-DUSE_VENDORDIRS=1 \
	-DCMAKE_SKIP_RPATH=1
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
ln -s repo2solv %{buildroot}/%{_bindir}/repo2solv.sh

%if 0%{?suse_version}
%if %{with python}
%py_compile -O %{buildroot}/%{python_sitearch}
%endif
%if %{with python3}
%py3_compile %{buildroot}/%{python3_sitearch}
%endif
%endif
%if %{with python_singlespec}
%{python_expand #
pyver=%{$python_version}
cmake . -U '*PYTHON*' -DENABLE_PYTHON=1 -DPYTHON_VERSION_MAJOR=${pyver%%.*} -DPYTHON_VERSION_MINOR=${pyver#*.}
make DESTDIR=%{buildroot} -C bindings/python clean
make DESTDIR=%{buildroot} -C bindings/python install
}
%python_compileall
%endif

%check
make ARGS=--output-on-failure test

%if %{with shared}
%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%license LICENSE*
%{_libdir}/libsolv.so.*
%{_libdir}/libsolvext.so.*
%endif

%files tools-base
%defattr(-,root,root)
%{_bindir}/repo2solv
%{_bindir}/rpmdb2solv
%{_mandir}/man1/repo2solv.1*
%{_mandir}/man1/rpmdb2solv.1*

%files tools
%defattr(-,root,root)
%if 0%{?suse_version}
%exclude %{_bindir}/helix2solv
%exclude %{_mandir}/man1/helix2solv*
%endif
%exclude %{_mandir}/man1/solv.1*
%exclude %{_mandir}/man1/repo2solv.1*
%exclude %{_mandir}/man1/rpmdb2solv.1*
%exclude %{_bindir}/solv
%exclude %{_bindir}/repo2solv
%exclude %{_bindir}/rpmdb2solv
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%if %{with static} && !%{with shared}
%{_libdir}/libsolv.a
%{_libdir}/libsolvext.a
%endif
%if %{with shared}
%{_libdir}/libsolv.so
%{_libdir}/libsolvext.so
%endif
%{_includedir}/solv
%if 0%{?suse_version}
%{_bindir}/helix2solv
%{_mandir}/man1/helix2solv*
%endif
%{_datadir}/cmake/Modules/*
%{_libdir}/pkgconfig/libsolv*.pc
%{_mandir}/man3/*

%if %{with static} && %{with shared}
%files devel-static
%defattr(-,root,root)
%{_libdir}/libsolv.a
%{_libdir}/libsolvext.a
%endif

%files demo
%defattr(-,root,root)
%{_bindir}/solv
%{_mandir}/man1/solv.1*

%if %{with perl}
%files -n perl-solv
%defattr(-,root,root)
%{perl_vendorarch}/*
%endif

%if %{with ruby}
%files -n ruby-solv
%defattr(-,root,root)
%{ruby_vendorarch}/*
%endif

%if %{with python}
%files -n python-solv
%defattr(-,root,root)
%{python_sitearch}/*
%endif

%if %{with python3}
%files -n python3-solv
%defattr(-,root,root)
%{python3_sitearch}/*solv*
%if 0%{?suse_version}
%{python3_sitearch}/*/*solv*
%endif
%endif

%if %{with python_singlespec}
%files %{python_files solv}
%defattr(-,root,root)
%{python_sitearch}/*
%if 0%{?suse_version}
%{python_sitearch}/*/*solv*
%endif
%endif

%changelog
