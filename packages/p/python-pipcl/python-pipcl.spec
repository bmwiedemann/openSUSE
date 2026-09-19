#
# spec file for package python-pipcl
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-pipcl
Version:        13
Release:        0
Summary:        Python packaging operations, including PEP-517 support, for use by a setup.py script
License:        GPL-3.0
URL:            https://github.com/ArtifexSoftware/pipcl
Source:         https://github.com/ArtifexSoftware/pipcl/archive/refs/tags/v%{version}.tar.gz#/pipcl-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module pip}
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging
Requires:       python-pip
BuildArch:      noarch
%python_subpackages

%description
The ``pipcl`` package provides Python `build backend
<https://packaging.python.org/en/latest/guides/tool-recommendations/#build-backends>`_
operations (including PEP 517 support), for use by a ``setup.py`` script.

* Designed to help build complex Python extension packages.
* Can also be used to build simple pure-python packages.
* Works on Linux, Windows, MacOS and OpenBSD.
* Is a python module, not a framework, so does not impose any restrictions on usage.
* Can be used with any external build system by running commands,
  for example with ``subprocess.run()`` or enhanced wrapper ``pipcl.run()``.

The intention is to allow a ``setup.py`` script to use the full power of Python
to do everything that is specific to the package, without having to worry about
generic Python packaging issues such wheel formats etc (see https://packaging.python.org/en/latest/specifications/).

%prep
%autosetup -p1 -n pipcl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# most of the tests needs internet

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/pipcl
%{python_sitelib}/pipcl-%{version}.dist-info

%changelog
