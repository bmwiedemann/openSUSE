#
# spec file for package python-scripttest
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
Name:           python-scripttest
Version:        2.0
Release:        0
Summary:        Helper to test command-line scripts
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pypa/scripttest
Source:         https://files.pythonhosted.org/packages/source/s/scripttest/scripttest-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
scripttest is a library to help you test your interactive command-line
applications.

With it you can easily run the command (in a subprocess) and see the
output (stdout, stderr) and any file modifications.

%prep
%setup -q -n scripttest-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/scripttest.py
%{python_sitelib}/scripttest-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__/scripttest*

%changelog
