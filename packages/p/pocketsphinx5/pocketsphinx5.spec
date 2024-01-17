#
# spec file for package pocketsphinx5
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 3
%define versuffix 5prealpha
Name:           pocketsphinx5
Version:        5~git20200227.e40da77
Release:        0
Summary:        Speech recognizer library written in C
License:        BSD-2-Clause
Group:          Productivity/Office/Other
URL:            http://cmusphinx.sourceforge.net/wiki/download/
Source:         pocketsphinx-%{version}.tar.xz
# PATCH-FIX-UPSTREAM pocketsphinx-doxygen.patch -- Obtained from fedora package (http://pkgs.fedoraproject.org/cgit/rpms/pocketsphinx.git/tree/)
Patch0:         pocketsphinx-doxygen.patch
# PATCH-FIX-OPENSUSE use-python3.patch -- Use python3 to generate python bindings
Patch1:         use-python3.patch
# PATCH-FIX-OPENSUSE fix-reproducible-builds.patch -- Do not use __DATE__ or __TIME__
Patch2:         fix-reproducible-builds.patch
# PATCH-FIX-OPENSUSE python-distutils-deprecated.patch -- ignore distutils deprecation warning
Patch3:         python-distutils-deprecated.patch
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  sphinxbase5-devel
BuildRequires:  swig
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description
Pocketsphinx is a version of the open-source CMU Sphinx II speech
recognition system which is able to recognize speech in real-time.

%package -n libpocketsphinx%{sover}
Summary:        Speech recognizer library
Group:          System/Libraries
Requires:       pocketsphinx5

%description -n libpocketsphinx%{sover}
CMU Sphinx toolkit has a number of packages for different tasks and
applications. Pocketsphinx is a version of the open-source CMU Sphinx
II speech recognition system which is able to recognize speech in
real-time.

%package devel
Summary:        Development files for pocketsphinx, a speech recognizer library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Conflicts:      pocketsphinx-devel

%description devel
CMU Sphinx toolkit has a number of packages for different tasks and
applications. Pocketsphinx is a version of the open-source CMU Sphinx
II speech recognition system which is able to recognize speech in
real-time.

This is the development package for pocketsphinx.

%package -n python3-pocketsphinx5
Summary:        Python bindings for pocketsphinx
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python3-sphinxbase5
Conflicts:      python3-pocketsphinx
Obsoletes:      python3-pocketsphinx-python <= 0.1.3
Provides:       python3-pocketsphinx-python = 0.1.3.0.1

%description -n python3-pocketsphinx5
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
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -ie "1s,^#!/usr/bin/env python$,#!/usr/bin/python3," doc/doxy2swig.py

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}
find %{buildroot} -type f -name "*.la" -delete -print

# Prepare for alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for binary in pocketsphinx_batch pocketsphinx_continuous pocketsphinx_mdef_convert ; do
    mv %{buildroot}%{_bindir}/$binary %{buildroot}%{_bindir}/$binary-%{versuffix}
    ln -s %{_sysconfdir}/alternatives/$binary %{buildroot}%{_bindir}/$binary
    mv %{buildroot}%{_mandir}/man1/$binary.1 %{buildroot}%{_mandir}/man1/$binary-%{versuffix}.1
    ln -s %{_sysconfdir}/alternatives/$binary.1%{ext_man} %{buildroot}%{_mandir}/man1/$binary.1%{ext_man}
done

%check
make check

%post
update-alternatives --install %{_bindir}/pocketsphinx_batch pocketsphinx_batch %{_bindir}/pocketsphinx_batch-%{versuffix} 20 \
  --slave %{_bindir}/pocketsphinx_continuous pocketsphinx_continuous %{_bindir}/pocketsphinx_continuous-%{versuffix} \
  --slave %{_bindir}/pocketsphinx_mdef_convert pocketsphinx_mdef_convert %{_bindir}/pocketsphinx_mdef_convert-%{versuffix} \
  --slave %{_mandir}/man1/pocketsphinx_batch.1%{ext_man} pocketsphinx_batch.1%{ext_man} %{_mandir}/man1/pocketsphinx_batch-%{versuffix}.1%{ext_man} \
  --slave %{_mandir}/man1/pocketsphinx_continuous.1%{ext_man} pocketsphinx_continuous.1%{ext_man} %{_mandir}/man1/pocketsphinx_continuous-%{versuffix}.1%{ext_man} \
  --slave %{_mandir}/man1/pocketsphinx_mdef_convert.1%{ext_man} pocketsphinx_mdef_convert.1%{ext_man} %{_mandir}/man1/pocketsphinx_mdef_convert-%{versuffix}.1%{ext_man}

%postun
if [ ! -f %{_bindir}/pocketsphinx_batch ]; then
    update-alternatives --remove pocketsphinx_batch %{_bindir}/pocketsphinx_batch-%{versuffix}
fi

%post   -n libpocketsphinx%{sover} -p /sbin/ldconfig
%postun -n libpocketsphinx%{sover} -p /sbin/ldconfig

%files
%doc AUTHORS README NEWS
%license LICENSE
%ghost %{_sysconfdir}/alternatives/pocketsphinx_batch
%ghost %{_sysconfdir}/alternatives/pocketsphinx_continuous
%ghost %{_sysconfdir}/alternatives/pocketsphinx_mdef_convert
%ghost %{_sysconfdir}/alternatives/pocketsphinx_batch.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/pocketsphinx_continuous.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/pocketsphinx_mdef_convert.1%{ext_man}
%{_bindir}/pocketsphinx_batch*
%{_bindir}/pocketsphinx_continuous*
%{_bindir}/pocketsphinx_mdef_convert*
%dir %{_datadir}/pocketsphinx/
%dir %{_datadir}/pocketsphinx/model
%{_datadir}/pocketsphinx/model/en-us
%{_datadir}/pocketsphinx/swig
%{_mandir}/man1/*%{ext_man}

%files -n libpocketsphinx%{sover}
%{_libdir}/*.so.%{sover}*

%files devel
%{_includedir}/pocketsphinx
%{_libdir}/*.so
%{_libdir}/pkgconfig/pocketsphinx.pc

%files -n python3-pocketsphinx5
%{python3_sitearch}/pocketsphinx

%files -n gstreamer-plugin-pocketsphinx
%{_libdir}/gstreamer-1.0/libgstpocketsphinx.so

%changelog
