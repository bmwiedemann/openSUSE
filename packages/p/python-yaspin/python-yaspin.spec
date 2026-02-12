#
# spec file for package python-yaspin
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-yaspin
Version:        3.4.0
Release:        0
Summary:        Yet Another Terminal Spinner
License:        MIT
URL:            https://github.com/pavdmyt/yaspin
Source:         https://files.pythonhosted.org/packages/source/y/yaspin/yaspin-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-termcolor
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module termcolor}
# /SECTION
%python_subpackages

%description
Yet Another Terminal Spinner.

%prep
%setup -q -n yaspin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/yaspin
%{python_sitelib}/yaspin-%{version}*-info

%changelog
