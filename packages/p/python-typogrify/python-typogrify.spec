#
# spec file for package python-typogrify
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
Name:           python-typogrify
Version:        2.1.0
Release:        0
Summary:        Typography related template filters for Django & Jinja2 applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mintchaos/typogrify
Source:         https://files.pythonhosted.org/packages/source/t/typogrify/typogrify-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module smartypants >= 1.8.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-smartypants >= 1.8.3
BuildArch:      noarch
%python_subpackages

%description
This application provides a set of custom filters for the Django template system
which automatically apply various transformations to plain text in order to yield
typographically-improved HTML.

%prep
%setup -q -n typogrify-%{version}
# remove useless shebang and executable bit
sed -i '1d' \
	typogrify/packages/titlecase/__init__.py \
	typogrify/packages/titlecase/tests.py
chmod -x typogrify/packages/titlecase/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{_prefix}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib} PYTHONDONTWRITEBYTECODE=1
$python -mdoctest -v typogrify/filters.py
}

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/typogrify-%{version}.dist-info
%{python_sitelib}/typogrify

%changelog
