#
# spec file for package python-spyder-notebook
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
Name:           python-spyder-notebook
Version:        0.1.4
Release:        0
Summary:        Jupyter notebook integration with Spyder
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/spyder-ide/spyder-notebook
Source:         https://files.pythonhosted.org/packages/source/s/spyder-notebook/spyder-notebook-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to control
breakpoints.

%package    -n spyder-notebook
Summary:        Jupyter Notebook plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       python-QtPy
Requires:       python-nbformat
Requires:       python-notebook >= 4.3
Requires:       python-psutil
Requires:       python-requests
Requires:       spyder >= 3.2.0

%description -n spyder-notebook
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to control
breakpoints.

%package    -n spyder3-notebook
Summary:        Jupyter Notebook plugin for the Spyder3 IDE
Group:          Development/Languages/Python
Requires:       python3-QtPy
Requires:       python3-nbformat
Requires:       python3-notebook >= 4.3
Requires:       python3-psutil
Requires:       python3-requests
Requires:       spyder3 >= 3.2.0

%description -n spyder3-notebook
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to control
breakpoints.

%prep
%setup -q -n spyder-notebook-%{version}
sed -i 's/\r$//' CHANGELOG.md README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files -n spyder-notebook
%doc CHANGELOG.md README.md
%license LICENSE
%{python2_sitelib}/*

%files -n spyder3-notebook
%doc CHANGELOG.md README.md
%license LICENSE
%{python3_sitelib}/*

%changelog
