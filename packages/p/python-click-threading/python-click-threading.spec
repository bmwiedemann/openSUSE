#
# spec file for package python-click-threading
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
Name:           python-click-threading
Version:        0.4.4
Release:        0
Summary:        Multithreaded Click apps made easy
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/click-contrib/click-threading
Source:         https://files.pythonhosted.org/packages/source/c/click-threading/click-threading-%{version}.tar.gz
BuildRequires:  %{python_module click >= 5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-futures
BuildRequires:  python-rpm-macros
Requires:       python-click >= 5.0
%ifpython2
Requires:       python-futures
%endif
BuildArch:      noarch
%python_subpackages

%description
Utilities for multithreading in click <http://click.pocoo.org/>.
*This is rather experimental.  See tests for usage for now.*

%prep
%setup -q -n click-threading-%{version}
rm -rf click_threading.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
