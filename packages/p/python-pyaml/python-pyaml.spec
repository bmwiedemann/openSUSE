#
# spec file for package python-pyaml
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyaml
Version:        25.1.0
Release:        0
Summary:        Python module to produce formatted YAML-serialized data
License:        WTFPL
Group:          Development/Languages/Python
URL:            https://github.com/mk-fg/pretty-yaml
Source:         https://files.pythonhosted.org/packages/source/p/pyaml/pyaml-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Unidecode}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Recommends:     python-Unidecode
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
PyYAML-based python module to produce formatted YAML-serialized data.

%prep
%setup -q -n pyaml-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}/%{_bindir}/pyaml
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pyaml

%postun
%python_uninstall_alternative pyaml

%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/pyaml
%{python_sitelib}/pyaml
%{python_sitelib}/pyaml-%{version}*-info

%changelog
