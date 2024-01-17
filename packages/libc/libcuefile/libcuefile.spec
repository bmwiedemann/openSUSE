#
# spec file for package libcuefile
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Asterios Dramis <asterios.dramis@gmail.com>.
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


%define so_ver 0

Name:           libcuefile
Version:        r475
Release:        0
Summary:        Library for Working With Cue Sheet (cue) and Table Of Contents (toc) Files
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
Url:            https://www.musepack.net/
Source0:        https://files.musepack.net/source/%{name}_%{version}.tar.gz
# PATCH-FIX-OPENSUSE mathmeaning.patch asterios.dramis@gmail.com -- Fix rpm post build error "Program uses operation a <= b <= c, which is not well defined." (based on patch from openSUSE cuetools)
Patch0:         mathmeaning.patch
BuildRequires:  cmake

%description
libcuefile is a library for working with Cue Sheet (cue) and Table of Contents
(toc) files.

%package devel
Summary:        Development files for libcuefile
Group:          Development/Libraries/C and C++
Requires:       libcuefile%{so_ver} = %{version}

%description devel
This package includes development files for libcuefile.

%package -n libcuefile%{so_ver}
Summary:        Library for Working With Cue Sheet (cue) and Table Of Contents (toc) Files
Group:          System/Libraries

%description -n libcuefile%{so_ver}
libcuefile is a library for working with Cue Sheet (cue) and Table of Contents
(toc) files.

%prep
%setup -q -n %{name}_%{version}
%patch0

# Fix rpmlint error "spurious-executable-perm"
chmod 644 AUTHORS COPYING README
chmod 644 include/cuetools/*.h

%build
%cmake
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_includedir}
cp -a include/cuetools/ %{buildroot}%{_includedir}

rm -f %{buildroot}%{_libdir}/*.a

%post -n libcuefile%{so_ver} -p /sbin/ldconfig

%postun -n libcuefile%{so_ver} -p /sbin/ldconfig

%files devel
%license COPYING
%doc AUTHORS README
%{_includedir}/cuetools/
%{_libdir}/libcuefile.so

%files -n libcuefile%{so_ver}
%{_libdir}/libcuefile.so.%{so_ver}*

%changelog
