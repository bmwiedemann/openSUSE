#
# spec file for package ctl
#
# Copyright (c) 2025 SUSE LLC
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


%define so_ver 1_5_3

Name:           ctl
Version:        1.5.3
Release:        0
Summary:        Programming language for digital color management
License:        AMPAS
URL:            https://github.com/ampas/CTL
Source:         https://github.com/ampas/CTL/archive/refs/tags/ctl-%{version}.tar.gz
Source2:        ctl-rpmlintrc
# PATCH-FIX-UPSTREAM https://github.com/ampas/CTL/pull/153
Patch0:         fix-IlmCtl-sover.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel
BuildRequires:  openexr-devel >= 3

%description
The Color Transformation Language (CTL) is a programming language for digital
color management systems (CMS). Color transforms are to be expressed as
programs (rather than declarations), and a CTL interpreter is used to execute
such programs and perform transformations.

Color transforms can be shared by distributing CTL programs. Two
parties with the same CTL program can apply the same transform to an
image.

%package data
Summary:        Contains various CTL files
BuildArch:      noarch

%description data
This package contains various CTL files.

%package devel
Summary:        Development package for CTL
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libIlmCtl%{so_ver} = %{version}
Requires:       libIlmCtlMath%{so_ver} = %{version}
Requires:       libIlmCtlSimd%{so_ver} = %{version}
Requires:       openexr-devel >= 3

%description devel
This package contain the devel files for CTL.

%package doc
Summary:        Documentation files for CTL
BuildArch:      noarch

%description doc
This package provides documentation for CTL.

%package -n libIlmImfCtl%{so_ver}
Summary:        OpenEXR interface to CTL
Group:          System/Libraries
Requires:       %{name}-data

%description -n libIlmImfCtl%{so_ver}
	IlmImfCtl provides a simplified OpenEXR interface to the Color Transformation Language.

%package -n libIlmCtl%{so_ver}
Summary:        Interpreter for the Color Transformation Language
Group:          System/Libraries
Requires:       %{name}-data

%description -n libIlmCtl%{so_ver}
The IlmCtl library provides the CTL interpreter.

%package -n libIlmCtlMath%{so_ver}
Summary:        Math functions for the Color Transformation Language
Group:          System/Libraries
Requires:       %{name}-data

%description -n libIlmCtlMath%{so_ver}
The IlmCtlMath library contains fixed colorspace transforms
(RGB/XYZ/Luv/Lab), LUTs, matrix computation and interpolation code.

%package -n libIlmCtlSimd%{so_ver}
Summary:        SIMD execution for the the Color Transformation Language
Group:          System/Libraries
Requires:       %{name}-data

%description -n libIlmCtlSimd%{so_ver}
The IlmCtlSimd library contains functions to use SIMD from the
CTL interpreter.

%prep
%autosetup -p1 -n CTL-%{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libIlmCtl%{so_ver}
%ldconfig_scriptlets -n libIlmCtlMath%{so_ver}
%ldconfig_scriptlets -n libIlmCtlSimd%{so_ver}
%ldconfig_scriptlets -n libIlmImfCtl%{so_ver}

%files
%license LICENSE
%doc CHANGELOG README.md
%{_bindir}/ctlrender
%{_bindir}/exr_ctl_exr
%{_bindir}/exrdpx

%files data
%{_datadir}/CTL/change_saturation.ctl
%{_datadir}/CTL/transform_DPX_EXR.ctl
%{_datadir}/CTL/transform_EXR_DPX.ctl
%{_datadir}/CTL/utilities.ctl

%files devel
%dir %{_includedir}/CTL
%dir %{_datadir}/CTL
%dir %{_includedir}/OpenEXR
%{_libdir}/libIlmCtl.so
%{_libdir}/libIlmCtlMath.so
%{_libdir}/libIlmCtlSimd.so
%{_libdir}/libIlmImfCtl.so
%{_includedir}/CTL/CtlAddr.h
%{_includedir}/CTL/CtlAlign.h
%{_includedir}/CTL/CtlColorSpace.h
%{_includedir}/CTL/CtlErrors.h
%{_includedir}/CTL/CtlExc.h
%{_includedir}/CTL/CtlFunctionCall.h
%{_includedir}/CTL/CtlInterpreter.h
%{_includedir}/CTL/CtlLContext.h
%{_includedir}/CTL/CtlLookupTable.h
%{_includedir}/CTL/CtlMessage.h
%{_includedir}/CTL/CtlModule.h
%{_includedir}/CTL/CtlRbfInterpolator.h
%{_includedir}/CTL/CtlRcPtr.h
%{_includedir}/CTL/CtlReadWriteAccess.h
%{_includedir}/CTL/CtlSimdInterpreter.h
%{_includedir}/CTL/CtlSparseMatrix.h
%{_includedir}/CTL/CtlStdType.h
%{_includedir}/CTL/CtlSymbolTable.h
%{_includedir}/CTL/CtlSyntaxTree.h
%{_includedir}/CTL/CtlTokens.h
%{_includedir}/CTL/CtlType.h
%{_includedir}/CTL/CtlTypeStorage.h
%{_includedir}/CTL/CtlVersion.h
%{_includedir}/OpenEXR/ImfCtlApplyTransforms.h

%files -n libIlmImfCtl%{so_ver}
%{_libdir}/libIlmImfCtl.so.%{version}

%files -n libIlmCtl%{so_ver}
%{_libdir}/libIlmCtl.so.%{version}

%files -n libIlmCtlMath%{so_ver}
%{_libdir}/libIlmCtlMath.so.%{version}

%files -n libIlmCtlSimd%{so_ver}
%{_libdir}/libIlmCtlSimd.so.%{version}

%files doc
%if 0%{?sle_version} >= 150600 || %{?suse_version} >= 1600
%dir %{_docdir}/ctl
%dir %{_docdir}/ctl/CTL
%{_docdir}/ctl/CTL/CtlManual.*
%else
%dir %{_datadir}/doc
%dir %{_datadir}/doc/CTL
%dir %{_datadir}/doc/CTL/CTL
%{_datadir}/doc/CTL/CTL/CtlManual.*
%endif

%changelog
