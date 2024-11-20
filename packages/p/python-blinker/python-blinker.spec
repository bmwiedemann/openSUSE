#
# spec file for package python-blinker
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


%{?sle15_python_module_pythons}
Name:           python-blinker
Version:        1.9.0
Release:        0
Summary:        Object-to-object and broadcast signaling in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pallets-eco/blinker/
Source:         https://files.pythonhosted.org/packages/source/b/blinker/blinker-%{version}.tar.gz
Patch1:         remove-sphinxextensions.patch
BuildRequires:  %{python_module Pallets-Sphinx-Themes}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinx-issues}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Blinker provides a dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%if 0%{?suse_version} > 1500
%package -n python-blinker-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildRequires:  %{python_module Pallets-Sphinx-Themes}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module sphinxcontrib-htmlhelp}
BuildRequires:  %{python_module sphinxcontrib-jsmath}
BuildRequires:  %{python_module sphinxcontrib-serializinghtml}
Provides:       %{python_module blinker-doc = %{version}}

%description -n python-blinker-doc
Blinker provides a dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

This sub-package contains the HTML documentation.
%endif

%prep
%autosetup -p1 -n blinker-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%{python_expand pushd docs
export PYTHONPATH=%{buildroot}%{$python_sitelib}
# Do not call "make html" directly because it'll use python3 by
# default and that could produce .pyc files from different python
# versions in the package bsc#1213698
$python -m sphinx -M html . _build
popd

%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.md
%{python_sitelib}/blinker-%{version}*-info
%{python_sitelib}/blinker

%if 0%{?suse_version} > 1500
%files -n python-blinker-doc
%endif
%doc docs/_build/html

%changelog
