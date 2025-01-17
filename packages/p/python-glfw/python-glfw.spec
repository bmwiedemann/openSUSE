#
# spec file for package python-glfw
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


%{?sle15_python_module_pythons}
Name:           python-glfw
Version:        2.8.0
Release:        0
Summary:        A ctypes-based wrapper for GLFW3
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/FlorianRhiem/pyGLFW
Source:         https://files.pythonhosted.org/packages/source/g/glfw/glfw-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libglfw3
BuildRequires:  python-rpm-macros
Requires:       libglfw3
BuildArch:      noarch
%python_subpackages

%description
This module provides Python bindings for GLFW . It is a
ctypes wrapper which keeps very close to the original GLFW API,
except for:

-  function names use the pythonic ``words_with_underscores`` notation
   instead of ``camelCase``
-  ``GLFW_`` and ``glfw`` prefixes have been removed, as their function
   is replaced by the module namespace
-  structs have been replaced with Python sequences
-  functions like ``glfwGetMonitors`` return a list instead of a pointer
   and an object count
-  Gamma ramps use floats between 0.0 and 1.0 instead of unsigned shorts
-  GLFW errors are reported as ``glfw.GLFWError`` exceptions if no error
   callback is set (use ``glfw.ERROR_REPORTING=False`` to disable this)

%prep
%setup -q -n glfw-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/glfw
%{python_sitelib}/glfw-*.dist-info

%changelog
