#
# spec file for package python-click-log
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
Name:           python-click-log
Version:        0.3.2
Release:        0
Summary:        Logging integration for Click
License:        MIT
URL:            https://github.com/click-contrib/click-log
Source:         https://files.pythonhosted.org/packages/source/c/click-log/click-log-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
BuildArch:      noarch
%python_subpackages

%description
Integrates logging with click.
*This is rather experimental.  See tests for usage for now.*

%prep
%setup -q -n click-log-%{version}
rm -rf click_log.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
