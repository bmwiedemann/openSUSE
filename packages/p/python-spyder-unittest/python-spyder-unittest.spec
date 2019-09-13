#
# spec file for package python-spyder-unittest
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
Name:           python-spyder-unittest
Version:        0.3.1
Release:        0
Summary:        Plugin to run tests from within the Spyder IDE
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/spyder-ide/spyder-unittest
Source:         https://files.pythonhosted.org/packages/source/s/spyder-unittest/spyder_unittest-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates unit test
frameworks. It allows running tests and viewing the results.

%package -n spyder-unittest
Summary:        Plugin to run tests from within the Spyder IDE
Group:          Development/Languages/Python
Requires:       python-lxml
Requires:       spyder >= 3

%description -n spyder-unittest
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates unit test
frameworks. It allows running tests and viewing the results.

%package -n spyder3-unittest
Summary:        Plugin to run tests from within the Spyder3 IDE
Group:          Development/Languages/Python
Requires:       python3-lxml
Requires:       spyder3 >= 3

%description -n spyder3-unittest
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates unit test
frameworks. It allows running tests and viewing the results.

%prep
%setup -q -n spyder_unittest-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files -n spyder-unittest
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python2_sitelib}/*

%files -n spyder3-unittest
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python3_sitelib}/*

%changelog
