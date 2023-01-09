#
# spec file for package python-pivy
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


%define skip_python2 1
#%%define skip_python39 1
#%%define skip_python310 1

Name:           python-pivy
Version:        0.6.8
Release:        0
Summary:        Coin Binding for Python
# GPL only applies to some examples
License:        GPL-2.0-only AND ISC
Group:          Development/Libraries/Python
URL:            https://github.com/coin3d/pivy
Source0:        https://github.com/coin3d/pivy/archive/%{version}.tar.gz#/pivy-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  cmake(soqt)
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
%if 0%{suse_version} < 1550
sed -i -e '/find_package/ s/SWIG 4.0.0/SWIG/' CMakeLists.txt
%endif

%build
%{python_expand #
%define __builddir build_%{$python_bin_suffix}
pushd .
%cmake \
  -DPython_EXECUTABLE:FILEPATH=%{_bindir}/python%{$python_bin_suffix}
  %{nil}
popd
}

%{python_expand #
%define __builddir build_%{$python_bin_suffix}
pushd %{__builddir}
%cmake_build
popd
}

%install
%{python_expand #
%define __builddir build_%{$python_bin_suffix}
%cmake_install
$python ./setup.py install_egg_info --install-dir %{buildroot}%{$python_sitearch}
find %{buildroot}%{$python_sitearch} -iname \*sogui.py -exec sed -i -e '1 s@env python@python%{$python_bin_suffix}@' '{}' \; -exec chmod +x '{}' \;
%fdupes %{buildroot}%{$python_sitearch}/pivy/
}

%files %{python_files}
%license LICENSE
%doc AUTHORS HACKING NEWS README.md THANKS
%{python_sitearch}/pivy/
%{python_sitearch}/Pivy-%{version}-py%{python_version}.egg-info

%changelog
