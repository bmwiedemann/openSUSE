#
# spec file for package python-pytest-check-links
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


# Tests natually require internet
%bcond_with test
%{?sle15_python_module_pythons}
Name:           python-pytest-check-links
Version:        0.10.1
Release:        0
Summary:        Pytest plugin for checking links in files
License:        BSD-3-Clause
URL:            https://github.com/minrk/pytest-check-links
Source:         https://files.pythonhosted.org/packages/source/p/pytest_check_links/pytest_check_links-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils
Requires:       python-html5lib
Requires:       python-pytest >= 2.8
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-jupyter_nbconvert
Recommends:     python-jupyter_nbformat
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module jupyter_nbconvert}
BuildRequires:  %{python_module jupyter_nbformat}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module requests}
%endif
%python_subpackages

%description
A pytest plugin that checks URLs for HTML-containing files.

%prep
%setup -q -n pytest_check_links-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pytest-check-links
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest --check-links test/linkcheck.ipynb
%endif

%post
%python_install_alternative pytest-check-links

%postun
%python_uninstall_alternative pytest-check-links

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/pytest-check-links
%{python_sitelib}/pytest_check_links
%{python_sitelib}/pytest_check_links-%{version}.dist-info

%changelog
