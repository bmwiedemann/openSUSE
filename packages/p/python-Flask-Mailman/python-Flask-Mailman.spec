#
# spec file for package python-Flask-Mailman
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Mailman
Version:        0.3.0
Release:        0
Summary:        Flask extension providing simple email sending capabilities
License:        BSD-3-Clause
URL:            https://github.com/waynerv/flask-mailman
Source:         https://github.com/waynerv/flask-mailman/archive/refs/tags/v%{version}.tar.gz#/Flask-Mailman-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 1.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Flask-Mailman is a Flask extension providing simple email sending capabilities.

It was meant to replace unmaintained Flask-Mail with a better warranty and
more features.

%prep
%autosetup -p1 -n flask-mailman-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/flask_mailman
%{python_sitelib}/flask_mailman-%{version}.*info

%changelog
