#
# spec file for package python-pivy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pivy
Version:        0.6.4
Release:        0
Summary:        Coin Binding for Python
License:        ISC AND GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/FreeCAD/pivy
Source0:        https://github.com/FreeCAD/pivy/archive/%{version}.tar.gz#/Pivy-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://github.com/FreeCAD/pivy/issues/39
Patch0:         Fix-issue-39-PyUnicode_AsUTF8-returns-const-char.patch
# PATCH-FIX-OPENSUSE 0001-Allow-using-SoQt-snapshots-with-stable-Coin-version.patch -- Use CMake to find Coin and SoQt
Patch1:         0001-Allow-using-SoQt-snapshots-with-stable-Coin-version.patch
# PATCH-FIX-OPENSUSE 0002-Fix-the-qmake-executable-name.patch -- Fix the qmake executable name
Patch2:         0002-Fix-the-qmake-executable-name.patch
BuildRequires:  %{python_module devel}
BuildRequires:  Coin-devel
BuildRequires:  SoQt-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
BuildRequires:  swig
%python_subpackages

%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics library
with a C++ Application Programming Interface. Coin uses scene-graph data
structures to render real-time graphics suitable for mostly all kinds of
scientific and engineering visualization applications.

Pivy allows:

- Development of Coin applications and extensions in Python
- Interactive modification of Coin programs from within the Python interpreter
  at runtime
- Incorporation of Scripting Nodes into the scene graph which are capable of
  executing Python code and callbacks

%prep
%autosetup -p1 -n pivy-%{version}

%build
export CFLAGS="%{optflags}"
%{python_build ; rm pivy/coin_wrap.cpp pivy/gui/soqt_wrap.cpp }

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}/pivy/

%files %{python_files}
%license LICENSE
%doc AUTHORS HACKING NEWS README.md THANKS
%{python_sitelib}/pivy/
%{python_sitelib}/Pivy-%{version}-py%{py_ver}.egg-info

%changelog
