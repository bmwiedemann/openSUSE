#
# spec file for package python-wmctrl
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-wmctrl
Version:        0.5
Release:        0
Summary:        Python programmatic control of X windows
# Project is in the process of transitioning from Bitbucket to GitHub
License:        MIT
URL:            https://github.com/antocuni/wmctrl
Source:         https://files.pythonhosted.org/packages/source/w/wmctrl/wmctrl-%{version}.tar.gz
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  openbox
BuildRequires:  python-rpm-macros
BuildRequires:  wmctrl
BuildRequires:  xclock
BuildRequires:  xfontsel
BuildRequires:  xorg-x11-server
BuildRequires:  xvfb-run
Requires:       python-attrs
Requires:       wmctrl
Requires:       xorg-x11-server
BuildArch:      noarch
%python_subpackages

%description
Python tool to programmatically control windows inside X.

%prep
%setup -q -n wmctrl-%{version}

sed -i 's/\(py$\|py\.test\)/pytest/g' test/test_wmctrl.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand #
cat > /tmp/test_script.sh <<EOF
#!/bin/sh
openbox &
sleep 10
wmctrl -l -G -p -x
$python -m pytest -rs -k 'not (test_activate or test_properties or test_Desktop_active)' test/test_wmctrl.py
EOF
chmod +x /tmp/test_script.sh
xvfb-run /tmp/test_script.sh
}

%files %{python_files}
%license LICENSE
%{python_sitelib}/wmctrl.py
%pycache_only %{python_sitelib}/__pycache__/wmctrl*pyc
%{python_sitelib}/wmctrl-%{version}.dist-info

%changelog
