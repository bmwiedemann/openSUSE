#
# spec file for package python-jupyter-ydoc
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


Name:           python-jupyter-ydoc
Version:        0.2.3
Release:        0
Summary:        Document structures for collaborative editing using Ypy
License:        BSD-3-Clause
URL:            https://github.com/jupyter-server/jupyter_ydoc
# Versioned sdist
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter-ydoc/jupyter_ydoc-%{version}.tar.gz
# unversioned, but tests
Source1:        https://github.com/jupyter-server/jupyter_ydoc/archive/refs/tags/v%{version}.tar.gz#/jupyter_ydoc-%{version}-gh.tar.gz
Source2:        node_modules.tar.xz
# Execute this on every package update. See comments in the script.
Source3:        create_node_modules.sh
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatch_nodejs_version}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-importlib-metadata >= 3.6 if python-base < 3.10)
Requires:       (python-y-py >= 0.5.3 with python-y-py < 0.6.0)
Provides:       python-jupyter_ydoc = %{version}-%{release}
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module importlib-metadata >= 3.6 if %python-base < 3.10}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module websockets >= 10.0}
BuildRequires:  %{python_module y-py >= 0.5.3 with %python-y-py < 0.6.0}
BuildRequires:  %{python_module ypy-websocket >= 0.3.1}
BuildRequires:  nodejs
# /SECTION
%python_subpackages

%description
Ypy-based data structures for various documents used in the Jupyter ecosystem.
Built-in documents include:
  - `YBlob`: a generic immutable binary document.
  - `YUnicode`: a generic UTF8-encoded text document (`YFile` is an alias to `YUnicode`).
  - `YNotebook`: a Jupyter notebook document.

%prep
%setup -q -n jupyter_ydoc-%{version} -b1 -a2

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/jupyter_ydoc
%{python_sitelib}/jupyter_ydoc-%{version}.dist-info

%changelog
