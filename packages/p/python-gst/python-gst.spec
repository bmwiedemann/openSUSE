#
# spec file for package python-gst
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-gst
Version:        1.16.1
Release:        0
Summary:        Python Bindings for GStreamer
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            http://www.gstreamer.net/
Source:         https://gstreamer.freedesktop.org/src/gst-python/%{_name}-%{version}.tar.xz

BuildRequires:  %{python_module devel}
BuildRequires:  gobject-introspection
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0
Requires:       gstreamer >= %{version}

%description
This module contains a wrapper that allows GStreamer applications to be
written in Python.

%python_subpackages

%package -n gstreamer-plugin-python
Summary:        GStreamer 1.0 plugin for python
Group:          System/Libraries

%description -n gstreamer-plugin-python
This module contains a wrapper that allows GStreamer applications to be
written in Python.

%prep
%setup -q -n %{_name}-%{version}

%build
for py_var in %{pythons}; do
  mkdir ../$py_var
  cp -rp * ../$py_var
  pushd ../$py_var
  # link ../configure, so we can still use the macro
  export PYTHON=$py_var
  %configure \
    --disable-static
  make %{?_smp_mflags}
  popd
done

%install
for py_var in %{pythons}; do
  pushd ../$py_var
  %make_install
  popd
done
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}%{_libdir}/gstreamer-1.0/libgstpython.so

%files %{python_files}
%license COPYING
%doc NEWS TODO
%{python_sitearch}/gi/overrides/

%files -n gstreamer-plugin-python
%{_libdir}/gstreamer-1.0/libgstpython.cpython*.so

%changelog
