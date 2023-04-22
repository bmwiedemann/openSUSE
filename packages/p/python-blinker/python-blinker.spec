#
# spec file for package python-blinker
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?sle15_python_module_pythons}
Name:           python-blinker
Version:        1.5
Release:        0
Summary:        Object-to-object and broadcast signaling in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://pythonhosted.org/blinker/
Source:         https://files.pythonhosted.org/packages/source/b/blinker/blinker-%{version}.tar.gz
BuildRequires:  %{python_module Pallets-Sphinx-Themes}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Blinker provides a dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%package -n python-blinker-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Provides:       %{python_module blinker-doc = %{version}}

%description -n python-blinker-doc
Blinker provides a dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

This sub-package contains the HTML documentation.

%prep
%setup -q -n blinker-%{version}

%build
%python_build

%install
%python_install

%{python_expand pushd docs
export PYTHONPATH=%{buildroot}%{$python_sitelib}
make html
popd

%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/blinker-%{version}-py%{python_version}.egg-info
%{python_sitelib}/blinker

%files -n python-blinker-doc
%doc docs/_build/html

%changelog
