#
# spec file for package python-virtkey
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-virtkey
Version:        0.63.0
%define major   0.63
Release:        0
Summary:        Python extension to emulate keypresses
License:        LGPL-3.0+
Group:          Development/Languages/Python
Url:            https://launchpad.net/virtkey
Source:         https://launchpad.net/virtkey/%{major}/%{version}/+download/virtkey-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xtst)
%python_subpackages

%description
python-virtkey is a python extension for emulating keypresses and
getting the keyboard geometry from the xserver.

%prep
%setup -q -n virtkey-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LESSER NEWS README
%{python_sitearch}/virtkey*.so
%{python_sitearch}/virtkey-%{version}-py*.egg-info

%changelog
