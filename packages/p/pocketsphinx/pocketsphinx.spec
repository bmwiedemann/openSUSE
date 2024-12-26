#
# spec file for package pocketsphinx
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


%define flavor @BUILD_FLAVOR@%nil

%if "%flavor" == "python"
%define name_suffix -%{flavor}
%else
%define name_suffix %{nil}
%endif

%define sover 5
%define versuffix 5.0.3+git20241211.69167fb
Name:           pocketsphinx%{name_suffix}
Version:        5.0.3+git20241211.69167fb
Release:        0
Summary:        Speech recognizer library written in C
License:        BSD-2-Clause
Group:          Productivity/Office/Other
URL:            http://cmusphinx.sourceforge.net/wiki/download/
Source:         pocketsphinx-%{version}.tar.xz
Patch1:         fix-python-installation.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
%if "%flavor" == "python"
BuildRequires:  pocketsphinx-devel
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-scikit-build-core
%endif
Obsoletes:      pocketsphinx5 <= 5
Provides:       pocketsphinx5 = %{version}

%description
Pocketsphinx is a version of the open-source CMU Sphinx II speech
recognition system which is able to recognize speech in real-time.

%package -n libpocketsphinx%{sover}
Summary:        Speech recognizer library
Group:          System/Libraries
Requires:       pocketsphinx

%description -n libpocketsphinx%{sover}
CMU Sphinx toolkit has a number of packages for different tasks and
applications. Pocketsphinx is a version of the open-source CMU Sphinx
II speech recognition system which is able to recognize speech in
real-time.

%package devel
Summary:        Development files for pocketsphinx, a speech recognizer library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Obsoletes:      pocketsphinx5-devel <= 5
Provides:       pocketsphinx5-devel = %{version}

%description devel
CMU Sphinx toolkit has a number of packages for different tasks and
applications. Pocketsphinx is a version of the open-source CMU Sphinx
II speech recognition system which is able to recognize speech in
real-time.

This is the development package for pocketsphinx.

%package -n python3-pocketsphinx
Summary:        Python bindings for pocketsphinx
Group:          Development/Languages/Python
Requires:       pocketsphinx = %{version}
Obsoletes:      python3-pocketsphinx5-python <= 5
Provides:       python3-pocketsphinx5 = %{version}

%description -n python3-pocketsphinx
Pocketsphinx is a version of the open-source CMU Sphinx II speech
recognition system which is able to recognize speech in real-time.

This package provides python bindings for pocketsphinx.

%package -n gstreamer-plugin-pocketsphinx
Summary:        GStreamer Plugin for pocketsphinx
Requires:       %{name} = %{version}

%description -n gstreamer-plugin-pocketsphinx
Pocketsphinx is a version of the open-source CMU Sphinx II speech
recognition system which is able to recognize speech in real-time.

This package provides the GStreamer plugin for pocketsphinx.

%prep
%setup -q -n pocketsphinx-%{version}
%autopatch -p1

%build
%cmake \
%if "%flavor" == "python"
    -DSKBUILD=1 \
    -DUSE_INSTALLED_POCKETSPHINX=1 \
%else
    -DBUILD_GSTREAMER=1 \
%endif
    %{nil}
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}

%ldconfig_scriptlets -n libpocketsphinx%{sover}

%if "%flavor" != "python"
%files
%doc AUTHORS README.md NEWS
%license LICENSE
%{_bindir}/pocketsphinx_batch
%{_bindir}/pocketsphinx
%{_bindir}/pocketsphinx_jsgf2fsg
%{_bindir}/pocketsphinx_lm_convert
%{_bindir}/pocketsphinx_lm_eval
%{_bindir}/pocketsphinx_mdef_convert
%{_bindir}/pocketsphinx_pitch
%dir %{_datadir}/pocketsphinx/
%dir %{_datadir}/pocketsphinx/model
%{_datadir}/pocketsphinx/model/en-us
%{_mandir}/man1/pocketsphinx*%{ext_man}
%{_mandir}/man1/sphinx*%{ext_man}

%files -n libpocketsphinx%{sover}
%{_libdir}/libpocketsphinx.so.%{sover}*

%files devel
%{_includedir}/pocketsphinx
%{_includedir}/pocketsphinx.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/pocketsphinx.pc

%files -n gstreamer-plugin-pocketsphinx
%{_libdir}/gstreamer-1.0/libgstpocketsphinx.so

%else

%files -n python3-pocketsphinx
%{python3_sitearch}/pocketsphinx

%endif

%changelog
