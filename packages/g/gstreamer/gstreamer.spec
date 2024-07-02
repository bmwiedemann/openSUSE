#
# spec file for package gstreamer
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


%define gst_branch 1.0

Name:           gstreamer
Version:        1.24.5
Release:        0
Summary:        Streaming-Media Framework Runtime
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source0:        %{url}/src/%{name}/%{name}-%{version}.tar.xz
Source1:        gstreamer.macros
Source2:        gstreamer.prov
Source99:       baselibs.conf

# PATCH-FEATURE-UPSTREAM gstreamer-rpm-prov.patch bgo#588784 dimstar@opensuse.org -- Add --rpm parameter to allow creation of rpm provides, patch from fedora
Patch1:         gstreamer-rpm-prov.patch
# PATCH-FIX-OPENSUSE gstreamer-pie.patch mgorse@suse.com -- create position-independent executables.
Patch2:         gstreamer-pie.patch

BuildRequires:  bison >= 2.4
BuildRequires:  check-devel
BuildRequires:  flex >= 2.5.31
BuildRequires:  gobject-introspection-devel >= 1.31.1
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  meson >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  rust >= 1.48
BuildRequires:  pkgconfig(bash-completion) >= 2.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdw)
# Ensure that the documentation corresponds with the installed version:
Requires:       libgstreamer-1_0-0 = %{version}
# Core modules may depend on new enough libraries:
Requires:       libgstreamer-1_0-0 >= %{version}
Requires(pre):  permissions
# Generic name, never used in SuSE:
Provides:       gstreamer-doc = %{version}
%define libunwind_archs %{ix86} ia64 x86_64 %{arm} ppc ppc64 ppc64le aarch64 riscv64
%ifarch %{libunwind_archs}
BuildRequires:  pkgconfig(libunwind)
%endif

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

%package -n libgstreamer-1_0-0
Summary:        Streaming-Media Framework Runtime
# We want to have core modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstreamer-1_0-0
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

%package -n typelib-1_0-Gst-1_0
Summary:        Streaming-Media Framework Runtime -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Gst-1_0
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer.

%package utils
Summary:        Streaming-Media Framework Runtime
# Generic name, never used in SuSE:
Group:          Productivity/Multimedia/Other
Provides:       gstreamer:%{_bindir}/gst-launch-%{gst_branch} = %{version}
# Symbol for unversioned wrappers:
Provides:       gstreamer-utils_versioned = %{version}

%description utils
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
# gstreamer-utils is required for the gstreamer-provides rpm magic.
Requires:       gstreamer-utils = %{version}
Requires:       libgstreamer-1_0-0 = %{version}
Requires:       typelib-1_0-Gst-1_0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%autosetup -p1
sed -i -e '1{s,^#!/usr/bin/env python3,#!%{_bindir}/python3,}' docs/gst-plugins-doc-cache-generator.py

%build
export PYTHON=%{_bindir}/python3
sed -i "s/'gst-plugin-scanner': /'gst-plugin-scanner-%{_target_cpu}': /" libs/gst/helpers/meson.build
grep "'gst-plugin-scanner-%{_target_cpu}': " libs/gst/helpers/meson.build || (echo "Couldn't set executable suffix in libs/gst/helpers/meson.build" ; exit 1)
sed -i "s/'gst-plugin-scanner'/'gst-plugin-scanner-%{_target_cpu}'/" meson.build
grep "'gst-plugin-scanner-%{_target_cpu}'" meson.build || (echo "Couldn't set executable suffix in meson.build" ; exit 1)
sed -i 's/"gst-plugin-scanner"/"gst-plugin-scanner-%{_target_cpu}"/' gst/gstpluginloader.c
grep '"gst-plugin-scanner-%{_target_cpu}"' gst/gstpluginloader.c || (echo "Couldn't set executable suffix in gst/gstpluginloader.c" ; exit 1)
# TODO: enable dbghelp
%meson \
	-Dptp-helper-permissions=capabilities \
	-Dpackage-name='openSUSE GStreamer package' \
	-Dpackage-origin='http://download.opensuse.org' \
	-Dintrospection=enabled \
	-Dbenchmarks=disabled \
	-Ddoc=disabled \
	-Dexamples=disabled \
	-Ddbghelp=disabled \
%ifnarch %{libunwind_archs}
	-Dlibunwind=disabled \
%endif
	%{nil}
%meson_build

# meson 0.61.4 in SLE 15 SP5 doesn't generate all variables needed in the pc files
# As a result the pkgconfig(...) provides are not generated in the rpm file so
# we have to add the variables to the pc files if they're missing
for pc in *-suse-linux/meson-private/*.pc ; do
   grep -q ^datarootdir= $pc || sed -ie "/^pluginsdir=.*/a datarootdir=\${prefix}\/share" $pc ;
   grep -q ^datadir= $pc || sed -ie "/^datarootdir=.*/a datadir=\${datarootdir}" $pc ;
   grep -q ^libexecdir= $pc || sed -ie "/^datadir=.*/a libexecdir=\${prefix}\/libexec" $pc ;
done

%install
%meson_install
%find_lang %{name}-%{gst_branch}
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_datadir}/gstreamer-%{gst_branch}/presets
# Install the rpm macros
install -m644 -D %{SOURCE1} %{buildroot}%{_fileattrsdir}/gstreamer.attr
install -m755 -D %{SOURCE2} %{buildroot}%{_rpmconfigdir}/gstreamer-provides

%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{_libexecdir}/gstreamer-*/*
%endif

%verifyscript
%verify_permissions -e %{_libexecdir}/gstreamer-%{gst_branch}/gst-ptp-helper

%post
%set_permissions %{_libexecdir}/gstreamer-%{gst_branch}/gst-ptp-helper

%ldconfig_scriptlets -n libgstreamer-1_0-0

%files
%license COPYING
%dir %{_datadir}/gstreamer-%{gst_branch}
%dir %{_datadir}/gstreamer-%{gst_branch}/presets
%dir %{_libdir}/gstreamer-%{gst_branch}
%{_libdir}/gstreamer-%{gst_branch}/libgstcoreelements.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcoretracers.so
%dir %{_libexecdir}/gstreamer-%{gst_branch}
%{_libexecdir}/gstreamer-%{gst_branch}/gst-completion-helper
%{_libexecdir}/gstreamer-%{gst_branch}/gst-plugin-scanner-%{_target_cpu}
%{_libexecdir}/gstreamer-%{gst_branch}/gst-hotdoc-plugins-scanner
%verify(not mode caps) %{_libexecdir}/gstreamer-%{gst_branch}/gst-ptp-helper
%{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/helpers/

%files -n libgstreamer-1_0-0
%{_libdir}/*.so.*

%files -n typelib-1_0-Gst-1_0
%{_libdir}/girepository-1.0/Gst-1.0.typelib
%{_libdir}/girepository-1.0/GstBase-1.0.typelib
%{_libdir}/girepository-1.0/GstCheck-1.0.typelib
%{_libdir}/girepository-1.0/GstController-1.0.typelib
%{_libdir}/girepository-1.0/GstNet-1.0.typelib

%files utils
%{_bindir}/*-%{gst_branch}
%{_mandir}/man?/*-%{gst_branch}*%{ext_man}

%files devel
%doc AUTHORS ChangeLog NEWS README.md RELEASE
%{_datadir}/aclocal/*.m4
# Own these directories to avoid build requirement on gdb
# only for directories ownership
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load%{_libdir}
%{_datadir}/gdb/auto-load%{_libdir}/lib%{name}*.py
%dir %{_datadir}/gstreamer-%{gst_branch}/gdb
%{_datadir}/gstreamer-%{gst_branch}/gdb/glib_gobject_helper.py
%{_datadir}/gstreamer-%{gst_branch}/gdb/gst_gdb.py
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libexecdir}/gstreamer-%{gst_branch}/gst-plugins-doc-cache-generator
%{_rpmconfigdir}/gstreamer-provides
%{_fileattrsdir}/gstreamer.attr
%{_datadir}/gir-1.0/*.gir

%files lang -f %{name}-%{gst_branch}.lang

%changelog
