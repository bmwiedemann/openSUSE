#
# spec file for package createrepo_c
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2022 Neal Gompa <ngompa13@gmail.com>.
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


%if 0%{?suse_version} >= 1330
# Enable Python bindings on openSUSE
%bcond_without python3
%bcond_without tests
%else
%bcond_with python3
%bcond_with tests
%endif

%if 0%{?sle_version} >= 160000 || 0%{?suse_version} >= 1550
# Enable enhanced DeltaRPM support
%bcond_without drpm
%else
%bcond_with drpm
%endif

%if 0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550
%bcond_without zchunk
%bcond_without libmodulemd
%else
%bcond_with zchunk
%bcond_with libmodulemd
%endif

%if 0%{?sle_version} && 0%{?sle_version} < 160000
%bcond_with as_createrepo
%else
%bcond_without as_createrepo
%endif

%{!?make_build: %global make_build %{__make} %{?_smp_mflags}}

%define major 0
%define libname lib%{name}%{major}
%define devname lib%{name}-devel

Name:           createrepo_c
Version:        0.20.1
Release:        0
Summary:        RPM repository metadata generation utility
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/rpm-software-management/createrepo_c
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#rpm-software-management/createrepo_c!316
Patch1:         0001-Add-optional-filelists_ext-metadata.patch
# PATCH-FIX-UPSTREAM gh#rpm-software-management/createrepo_c!348
Patch2:         0002-Rename-filelists_ext-to-filelists-ext-to-be-consiste.patch
Patch3:         0003-Rename-filelists_ext.xml-metadata-to-filelists-ext.x.patch
Patch4:         0004-Add-missing-ext-to-filelists-ext-repomd-record.patch
# PATCH-FIX-UPSTREAM gh#rpm-software-management/createrepo_c!349
Patch5:         0005-Complete-renaming-to-filelists-ext.patch

%if %{with python3}
BuildRequires:  python3-devel
%endif
%if 0%{?suse_version} >= 1330
BuildRequires:  python-rpm-macros
%endif
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  git-core
BuildRequires:  glib2-devel >= 2.22.0
BuildRequires:  libbz2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  lzma-devel
BuildRequires:  openssl-devel
BuildRequires:  rpm-devel >= 4.9.0
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel
%if %{with zchunk}
BuildRequires:  zchunk
BuildRequires:  zchunk-devel >= 0.9.11
%endif
%if %{with libmodulemd}
BuildRequires:  libmodulemd-devel >= 2.3.0
%endif
Requires:       %{libname}%{?_isa} = %{version}-%{release}
%if %{with tests}
BuildRequires:  python3
BuildRequires:  python3-setuptools
%endif
%if 0%{?suse_version} >= 1330
BuildRequires:  bash-completion-devel
%endif
%if %{with drpm}
BuildRequires:  drpm-devel >= 0.4.0
%endif

Requires:       %{libname} = %{version}-%{release}

%if %{with as_createrepo}
# Fully replaces createrepo
Requires(pre):  update-alternatives
Obsoletes:      createrepo < 0.11.0
Provides:       createrepo = %{version}-%{release}
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif

Provides:       createrepo-implementation

# prevent provides from nonstandard paths:
%global __provides_exclude ^(%{python3_sitearch}/.*\\.so)$

%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package -n %{libname}
Summary:        Library for repodata manipulation
Group:          System/Libraries

%description -n %{libname}
Libraries for applications using the createrepo_c library
for easy manipulation with a repodata.

%package -n %{devname}
Summary:        Library for repodata manipulation
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the createrepo_c C library and header files.
These development files are for easy manipulation with a repodata.

%package -n python3-%{name}
Summary:        Python 3 bindings for the createrepo_c library
Group:          Development/Libraries/Python
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# Python 2 subpackage is fully dropped
Obsoletes:      python2-%{name} < 0.12.0

%description -n python3-%{name}
The Python 3 bindings for the createrepo_c library.

%prep
%autosetup -S git_am

# do not hardcode date in the docs
sed -i -e '/HTML_TIMESTAMP/d' doc/Doxyfile.in.in

%build
%define __builddir build
%cmake \
    %{!?with_zchunk:-DWITH_ZCHUNK=OFF} \
    %{!?with_libmodulemd:-DWITH_LIBMODULEMD=OFF} \
    %{!?with_drpm:-DENABLE_DRPM=OFF} \
    %{!?with_python3:-DENABLE_PYTHON=OFF} \
    -DPYTHON_DESIRED:str=3

%make_build
%make_build doc-c

%if %{with tests}
%check
%define __builddir build
%ctest
%endif

%install
%define __builddir build
%cmake_install

%if %{with as_createrepo}
for i in createrepo mergerepo modifyrepo sqliterepo;do
  ln -s %{_bindir}/$i\_c %{buildroot}%{_bindir}/$i
  echo ".so man8/$i\_c.8" > %{buildroot}%{_mandir}/man8/$i\.8
done
%else
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for i in createrepo mergerepo modifyrepo sqliterepo;do
  ln -s %{_bindir}/$i\_c %{buildroot}%{_sysconfdir}/alternatives/$i
  ln -s %{_sysconfdir}/alternatives/$i %{buildroot}%{_bindir}/$i
  ln -s %{_mandir}/man8/$i\_c.8.gz %{buildroot}%{_sysconfdir}/alternatives/$i\.8.gz
  ln -s %{_sysconfdir}/alternatives/$i\.8.gz %{buildroot}%{_mandir}/man8/$i\.8.gz
done
%endif

%fdupes %{buildroot}%{_prefix}
%fdupes build/doc/html

%if %{with python3}
%python_compileall
%fdupes %{buildroot}%{python3_sitearch}
%endif

%if %{with as_createrepo}
%pre
if [ -e %{_sysconfdir}/alternatives/createrepo ]; then
  update-alternatives --remove createrepo %{_bindir}/createrepo_c
fi
%else

%post
update-alternatives --install \
  %{_bindir}/createrepo createrepo %{_bindir}/createrepo_c  20 \
  --slave %{_bindir}/mergerepo mergerepo %{_bindir}/mergerepo_c \
  --slave %{_bindir}/modifyrepo modifyrepo %{_bindir}/modifyrepo_c \
  --slave %{_bindir}/sqliterepo sqliterepo %{_bindir}/sqliterepo_c \
  --slave %{_mandir}/man8/createrepo.8.gz createrepo.8.gz %{_mandir}/man8/createrepo_c.8.gz \
  --slave %{_mandir}/man8/mergerepo.8.gz mergerepo.8.gz %{_mandir}/man8/mergerepo_c.8.gz \
  --slave %{_mandir}/man8/modifyrepo.8.gz modifyrepo.8.gz %{_mandir}/man8/modifyrepo_c.8.gz \
  --slave %{_mandir}/man8/sqliterepo.8.gz sqliterepo.8.gz %{_mandir}/man8/sqliterepo_c.8.gz

%postun
if [ ! -f %{_bindir}/createrepo_c ]; then
  update-alternatives --remove createrepo %{_bindir}/createrepo_c
fi
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc README.md
%license COPYING
%{_mandir}/man8/createrepo_c.8*
%{_mandir}/man8/mergerepo_c.8*
%{_mandir}/man8/modifyrepo_c.8*
%{_mandir}/man8/sqliterepo_c.8*
%{_mandir}/man8/createrepo.8*
%{_mandir}/man8/mergerepo.8*
%{_mandir}/man8/modifyrepo.8*
%{_mandir}/man8/sqliterepo.8*
%{_datadir}/bash-completion/completions/
%{_bindir}/createrepo_c
%{_bindir}/mergerepo_c
%{_bindir}/modifyrepo_c
%{_bindir}/sqliterepo_c
%{_bindir}/createrepo
%{_bindir}/mergerepo
%{_bindir}/modifyrepo
%{_bindir}/sqliterepo
%if ! %{with as_createrepo}
%ghost %_sysconfdir/alternatives/createrepo
%ghost %_sysconfdir/alternatives/mergerepo
%ghost %_sysconfdir/alternatives/modifyrepo
%ghost %_sysconfdir/alternatives/sqliterepo
%ghost %_sysconfdir/alternatives/createrepo.8.gz
%ghost %_sysconfdir/alternatives/mergerepo.8.gz
%ghost %_sysconfdir/alternatives/modifyrepo.8.gz
%ghost %_sysconfdir/alternatives/sqliterepo.8.gz
%endif

%files -n %{libname}
%license COPYING
%{_libdir}/libcreaterepo_c.so.%{major}
%{_libdir}/libcreaterepo_c.so.%{major}.*

%files -n %{devname}
%doc build/doc/html
%license COPYING
%{_libdir}/libcreaterepo_c.so
%{_libdir}/pkgconfig/createrepo_c.pc
%{_includedir}/createrepo_c/

%if %{with python3}
%files -n python3-%{name}
%license COPYING
%{python3_sitearch}/createrepo_c/
%{python3_sitearch}/*egg-info
%endif

%changelog
