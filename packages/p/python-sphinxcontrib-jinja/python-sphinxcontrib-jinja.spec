#
# spec file for package python-sphinxcontrib-jinja
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


%{?sle15_python_module_pythons}
Name:           python-sphinxcontrib-jinja
Version:        1.2.1
Release:        0
Summary:        Designing beautiful, view size responsive web components
License:        MIT
URL:            https://github.com/tardyp/sphinx-jinja
Source:         https://github.com/tardyp/sphinx-jinja/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-Sphinx >= 1.8
Requires:       python-docutils
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 1.8}
# /SECTION
%python_subpackages

%description
A sphinx extension for designing beautiful, view size responsive web components.

%prep
%setup -q -n sphinx-jinja-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand ln -s sphinxcontrib %{buildroot}%{$python_sitelib}/sphinx_jinja

%check

%files %{python_files}
%doc README.rst ChangeLog
%license LICENSE
%{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinx_jinja
%{python_sitelib}/sphinx_jinja-%{version}.dist-info

%changelog
