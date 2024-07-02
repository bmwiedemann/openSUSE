#
# spec file for package python-gst
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


%define _name gst-python

%{?sle15_python_module_pythons}
Name:           python-gst
Version:        1.24.5
Release:        0
Summary:        Python Bindings for GStreamer
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://gstreamer.freedesktop.org
Source0:        %{url}/src/gst-python/%{_name}-%{version}.tar.xz

BuildRequires:  %{python_module devel}
BuildRequires:  c++_compiler
BuildRequires:  gobject-introspection
BuildRequires:  meson >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0
Requires:       gstreamer >= %{version}
%{python_subpackages}

%description
This module contains a wrapper that allows GStreamer applications to be
written in Python.

%package -n gstreamer-plugin-python
Summary:        GStreamer 1.0 plugin for python
Group:          System/Libraries

%description -n gstreamer-plugin-python
This module contains a wrapper that allows GStreamer applications to be
written in Python.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%{python_expand py_var=$python
  mkdir ../$py_var
  cp -rp * ../$py_var
  pushd ../$py_var
  %meson \
    -Dpython=$py_var \
    %{nil}
  %meson_build
  popd
}

%install
%{python_expand py_var=$python
  pushd ../$py_var
  %meson_install
  popd
}

%files %{python_files}
%license COPYING
%doc NEWS README.md
%dir %{python_sitearch}/gi
%{python_sitearch}/gi/overrides/

%files -n gstreamer-plugin-python
%{_libdir}/gstreamer-1.0/libgstpython.so

%changelog
