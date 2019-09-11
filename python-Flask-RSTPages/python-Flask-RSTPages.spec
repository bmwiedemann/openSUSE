#
# spec file for package python-Flask-RSTPages
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-Flask-RSTPages
Version:        0.3
Release:        0
Summary:        Support for reStructuredText in Flask applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://flask-rstpages.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-RSTPages/Flask-RSTPages-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-Pygments
Requires:       python-docutils
BuildArch:      noarch
%python_subpackages

%description
Flask-RSTPages adds support for reStructuredText to Flask applications.
See the docs for details: http://flask-rstpages.readthedocs.org/

%prep
%setup -q -n Flask-RSTPages-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/*

%changelog
