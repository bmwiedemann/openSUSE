#
# spec file for package python-Flask-Compress
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Compress
Version:        1.4.0
Release:        0
Summary:        Compress responses in Flask apps with gzip
License:        MIT
Group:          Development/Languages/Python
Url:            https://libwilliam.github.io/flask-compress/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Compress/Flask-Compress-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Flask}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Flask
BuildArch:      noarch

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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
