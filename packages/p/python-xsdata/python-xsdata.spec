#
# spec file for package python-xsdata
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-xsdata
Version:        25.7
Release:        0
Summary:        Python XML Binding
License:        MIT
URL:            https://github.com/tefra/xsdata
Source:         https://files.pythonhosted.org/packages/source/x/xsdata/xsdata-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module click >= 5.0}
BuildRequires:  %{python_module click-default-group >= 1.2}
BuildRequires:  %{python_module docformatter}
BuildRequires:  %{python_module lxml >= 4.5}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module ruff}
BuildRequires:  %{python_module toposort >= 1.5}
BuildRequires:  %{python_module typing-extensions >= 4.7.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing-extensions >= 4.7.0
Suggests:       python-click >= 5.0
Suggests:       python-click-default-group >= 1.2
Suggests:       python-Jinja2 >= 2.10
Suggests:       python-toposort >= 1.5
Suggests:       python-lxml >= 4.5.0
Suggests:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python XML Binding

%prep
%autosetup -p1 -n xsdata-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/xsdata
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative xsdata

%postun
%python_uninstall_alternative xsdata

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%python_alternative %{_bindir}/xsdata
%{python_sitelib}/xsdata
%{python_sitelib}/xsdata-%{version}.dist-info

%changelog
