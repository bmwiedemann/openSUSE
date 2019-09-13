#
# spec file for package graphite2
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define libname libgraphite2-3
Name:           graphite2
Version:        1.3.12
Release:        0
Summary:        Font rendering capabilities for complex non-Roman writing systems
License:        LGPL-2.1-or-later OR MPL-2.0+
Group:          Productivity/Publishing/Word
Url:            http://graphite.sil.org/
Source0:        https://github.com/silnrsi/graphite/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         graphite2-1.2.0-cmakepath.patch
Patch2:         link-gcc-shared.diff
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base

%description
Graphite2 is a project within SIL's Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

%package -n %{libname}
Summary:        Text categorization library
Group:          System/Libraries

%description -n %{libname}
Graphite2 is a project within SIL's Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

%package devel
Summary:        Files for Developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel

%description devel
Graphite2 is a project within SIL's Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

This package contains the %{name} development files.

%prep
%setup -q -n graphite-%{version}
%patch0 -p1
%patch2 -p1

# Make sure to use python3 everywhere
find tests -type f -exec sed -i "s|python|python3|g" {} +
find . -name *.cmake -exec sed -i "s|python|python3|g" {} +

%build
%cmake \
	-DGRAPHITE2_COMPARE_RENDERER=OFF \
	-DGRAPHITE2_NTRACING=ON \
	-DCMAKE_SKIP_RPATH=OFF
# Do not use O3, from debian
find . -type f \
	-exec sed -i -e 's/\-O3//g' {} \;

make %{?_smp_mflags}

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
# exclude tests based on fonttool
cd build
ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags} \
    -E "padaukcmp1|chariscmp1|chariscmp2|annacmp1|schercmp1|awamicmp1|awamicmp2|awamicmp3"

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc LICENSE COPYING
%{_bindir}/gr2fonttest

%files -n %{libname}
%{_libdir}/*.so.3*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_includedir}/%{name}*
%{_libdir}/%{name}*

%changelog
