#
# spec file for package vid_stab
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname 1_1

Name:           vid_stab
Version:        1.1.0
Release:        0
Summary:        Video stabilizer
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://public.hronopik.de/vid.stab/
Source0:        https://github.com/georgmartius/vid.stab/archive/v1.1.0.tar.gz
Source99:       baselibs.conf
Patch0:         vid_stab-fix-license.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
A library to deshake videos, designed to stabilize even strongly jiggled clips.

%package -n libvidstab%{soname}
Summary:        A library to deshake video
Group:          System/Libraries

%description -n libvidstab%{soname}
A library to deshake videos, designed to stabilize even strongly jiggled clips.

%package -n libvidstab-devel
Summary:        Development files for libvidstab%{soname}
Group:          Development/Libraries/C and C++
Requires:       libvidstab%{soname} = %{version}

%description -n libvidstab-devel
Development (headers and libraries) files for libvidstab%{soname}.

%prep
%setup -q -n vid.stab-%{version}
%patch0 -p1

%build
%cmake \
%ifarch %ix86 x86_64
	-DSSE2_FOUND=TRUE \
%else
	-DSSE2_FOUND=FALSE \
%endif
	-DSSE3_FOUND=FALSE \
	-DSSSE3_FOUND=FALSE \
	-DSSE4_1_FOUND=FALSE \
	%{nil}
make %{?_smp_mflags}

%install
%cmake_install

%post -n libvidstab%{soname} -p /sbin/ldconfig
%postun -n libvidstab%{soname} -p /sbin/ldconfig

%files -n libvidstab%{soname}
%defattr(0644, root, root, 0755)
%license LICENSE
%{_libdir}/libvidstab.so.*

%files -n libvidstab-devel
%defattr(0644, root, root, 0755)
%{_libdir}/libvidstab.so
%{_includedir}/vid.stab/
%{_libdir}/pkgconfig/vidstab.pc

%changelog
