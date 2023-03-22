#
# spec file for package OpenCSD
#
# Copyright (c) 2023 SUSE LLC
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


# Disable doc as graphviz does not include PNG support
%bcond_with build_html_doc

%define libnum  1
Name:           OpenCSD
Version:        1.4.0
Release:        0
Summary:        CoreSight Trace Decode library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/Linaro/OpenCSD
Source0:        https://github.com/Linaro/OpenCSD/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
%if %{with build_html_doc}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif

%description
OpenCSD is an Arm CoreSight Trace Decode library.

%package -n libopencsd%{libnum}
Summary:        C++ API for the CoreSight Trace Decode library
Group:          System/Libraries

%description -n libopencsd%{libnum}
C++ API for the OpenCSD library.

%package -n libopencsd_c_api%{libnum}
Summary:        C API for the CoreSight Trace Decode library
Group:          System/Libraries

%description -n libopencsd_c_api%{libnum}
C API for the OpenCSD library.

%package devel
Summary:        Headers for OpenCSD, a CoreSight Trace Decode library
Group:          Development/Libraries/C and C++
Requires:       libopencsd%{libnum} = %{version}
Requires:       libopencsd_c_api%{libnum} = %{version}

%description devel
Header files and libraries for C and C++ development with OpenCSD.

%package doc
Summary:        Documentation for the OpenCSD API
Group:          Documentation/Other
BuildArch:      noarch

%description doc
OpenCSD is an Arm CoreSight Trace Decode library.

%prep
%autosetup

%build
%make_build -C decoder/build/linux DISABLE_STATIC=1 \
%if %{with build_html_doc}
docs
%endif

%install
%make_install -C decoder/build/linux DISABLE_STATIC=1 LIB_PATH=%{_lib}
# Install man page
mkdir -p %{buildroot}/usr/share/man/man1/
%make_install -C decoder/build/linux DISABLE_STATIC=1 LIB_PATH=%{_lib} install_man

%post	-n libopencsd%{libnum} -p /sbin/ldconfig

%postun	-n libopencsd%{libnum} -p /sbin/ldconfig

%post	-n libopencsd_c_api%{libnum} -p /sbin/ldconfig

%postun	-n libopencsd_c_api%{libnum} -p /sbin/ldconfig

%files
%{_bindir}/trc_pkt_lister

%files -n libopencsd%{libnum}
%license LICENSE
%{_libdir}/libopencsd.so.%{version}
%{_libdir}/libopencsd.so.%{libnum}

%files -n libopencsd_c_api%{libnum}
%{_libdir}/libopencsd_c_api.so.%{version}
%{_libdir}/libopencsd_c_api.so.%{libnum}

%files devel
%{_libdir}/libopencsd.so
%{_libdir}/libopencsd_c_api.so
%{_includedir}/opencsd

%files doc
%doc HOWTO.md README.md TODO
%if %{with build_html_doc}
%doc decoder/docs/html/*.html
%endif
%doc decoder/docs/*.md
%_mandir/*/*

%changelog
