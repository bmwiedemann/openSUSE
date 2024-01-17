#
# spec file for package python-pep440
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-pep440
Version:        0.1.2
Release:        0
Summary:        Check whether versions number match PEP 440
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Carreau/pep440
Source:         https://files.pythonhosted.org/packages/source/p/pep440/pep440-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core >= 3.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A simple package with utils to check whether versions number match Pep 440.

%prep
%setup -q -n pep440-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pep440
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%post
%python_install_alternative pep440

%postun
%python_uninstall_alternative pep440

%files %{python_files}
%doc readme.md
%license LICENSE
%python_alternative %{_bindir}/pep440
%{python_sitelib}/pep440
%{python_sitelib}/pep440-%{version}*-info

%changelog
