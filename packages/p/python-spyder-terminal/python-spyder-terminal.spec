#
# spec file for package python-spyder-terminal
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
Name:           python-spyder-terminal
Version:        0.2.4
Release:        0
Summary:        Operating system virtual terminal plugin for the Spyder IDE
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/spyder-ide/spyder-terminal
Source:         https://files.pythonhosted.org/packages/source/s/spyder-terminal/spyder-terminal-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Spyder is a scientific python development environment and an
alternative to IDLE.

This package contains the plugin for displaying a virtual terminal
(OS independent) inside the main Spyder window.

%package -n spyder-terminal
Summary:        Operating system virtual terminal plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       python-coloredlogs
Requires:       python-pexpect
Requires:       python-requests
Requires:       python-tornado
Requires:       spyder >= 3.2.0

%description -n spyder-terminal
Spyder is a scientific python development environment and an
alternative to IDLE.

This package contains the plugin for displaying a virtual terminal
(OS independent) inside the main Spyder window.

%package -n spyder3-terminal
Summary:        Operating system virtual terminal plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       python3-coloredlogs
Requires:       python3-pexpect
Requires:       python3-requests
Requires:       python3-tornado
Requires:       spyder3 >= 3.2.0

%description -n spyder3-terminal
Spyder is a scientific python development environment and an
alternative to IDLE.

This package contains the plugin for displaying a virtual terminal
(OS independent) inside the main Spyder window.

%prep
%setup -q -n spyder-terminal-%{version}

# fix rpmlint non-executable-script
sed -i -e '/^#!\//, 1d' spyder_terminal/server/main.py
sed -i -e '/^#!\//, 1d' spyder_terminal/server/tests/print_size.py

rm -r spyder_terminal/server/static/components/xterm.js/.vscode
rm spyder_terminal/server/static/components/jquery/src/.eslintrc.json
find . -name ".bower.json" -exec rm -f {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files -n spyder-terminal
%defattr(-,root,root,-)
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%{python2_sitelib}/*

%files -n spyder3-terminal
%defattr(-,root,root,-)
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%{python3_sitelib}/*

%changelog
