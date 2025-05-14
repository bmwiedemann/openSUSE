#
# spec file for package python-Flask-Compress
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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
Name:           python-Flask-Compress
Version:        1.14
Release:        0
Summary:        Compress responses in Flask apps with gzip
License:        MIT
URL:            https://github.com/colour-science/flask-compress
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Compress/Flask-Compress-%{version}.tar.gz
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli
Requires:       python-Flask
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
# /SECTION
%python_subpackages

%description
Flask-Compress allows compressing a Flask application's
responses with gzip.

The preferred solution is to have a server (like Nginx) automatically
compress the static files. If that option is not available,
Flask-Compress can solve the problem.

%prep
%setup -q -n Flask-Compress-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/flask_compress
%{python_sitelib}/[Ff]lask[_-][Cc]ompress-%{version}.dist-info
%pycache_only %{python_sitelib}/flask_compress/__pycache__

%changelog
