#
# spec file for package python-mdurl
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


%{?sle15_python_module_pythons}
Name:           python-mdurl
Version:        0.1.2
Release:        0
Summary:        Markdown URL utilities
License:        MIT
URL:            https://github.com/executablebooks/mdurl
Source:         https://github.com/executablebooks/mdurl/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source:         https://files.pythonhosted.org/packages/source/m/mdurl/mdurl-%%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A Python port of the JavaScript mdurl package. Formats and parses URLs in Markdown-Format.

%prep
%setup -q -n mdurl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/mdurl/
%{python_sitelib}/mdurl-%{version}*-info
%doc README.md
%license LICENSE

%changelog
