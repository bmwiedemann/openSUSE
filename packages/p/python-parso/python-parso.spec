#
# spec file for package python-parso
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-parso
Version:        0.5.1
Release:        0
Summary:        An autocompletion tool for Python
License:        MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/davidhalter/parso
Source0:        https://files.pythonhosted.org/packages/source/p/parso/parso-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python
versions). Parso is also able to list multiple syntax errors in your
python file.

Parso has been battle-tested by jedi. It was pulled out of jedi to be
useful for other projects as well.

Parso consists of a small API to parse Python and analyse the syntax
tree.

%prep
%setup -q -n parso-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt CHANGELOG.rst README.rst
%{python_sitelib}/parso-%{version}-py*.egg-info
%{python_sitelib}/parso/

%changelog
