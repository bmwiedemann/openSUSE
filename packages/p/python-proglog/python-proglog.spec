#
# spec file for package python-proglog
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


Name:           python-proglog
Version:        0.1.12
Release:        0
Summary:        Log and progress bar manager for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Edinburgh-Genome-Foundry/Proglog
Source:         https://files.pythonhosted.org/packages/source/p/proglog/proglog-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tqdm
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module tqdm}
# /SECTION
%python_subpackages

%description
Proglog is a progress logging system for Python. It allows developers
to build libraries while giving the user control on the management of
logs, callbacks and progress bars.

%prep
%setup -q -n proglog-%{version}
chmod a-x LICENSE README.rst

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/proglog
%{python_sitelib}/proglog-%{version}*-info

%changelog
