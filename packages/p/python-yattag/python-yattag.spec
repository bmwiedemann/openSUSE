#
# spec file for package python-yattag
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


%define skip_python2 1
Name:           python-yattag
Version:        1.16.1
Release:        0
Summary:        Generate HTML or XML in a pythonic way
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://www.yattag.org
Source:         https://files.pythonhosted.org/packages/source/y/yattag/yattag-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Generate HTML or XML in a pythonic way.
Pure python alternative to web template engines.
Can fill HTML forms with default values and error messages.

%prep
%setup -q -n yattag-%{version}
sed -i 's/distutils.core/setuptools/' setup.py
sed -i '/typing/d' setup.py
touch test/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test/*.py

%files %{python_files}
%doc README.rst
%license license/lgpl-2.1.txt
%{python_sitelib}/yattag
%{python_sitelib}/yattag*.egg-info

%changelog
