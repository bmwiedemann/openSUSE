#
# spec file for package python-easywatch
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


Name:           python-easywatch
Version:        0.0.5
Release:        0
Summary:        Directory monitoring package for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Ceasar/easywatch
Source:         https://files.pythonhosted.org/packages/source/e/easywatch/easywatch-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-watchdog
BuildArch:      noarch
%python_subpackages

%description
Easywatch exports one function, `watch` which watches a directory for
changes and notifies a handler the type of event and the name of the
file that triggered it.

There are four types of events that the handler can be notified about:

  * created: a file was created
  * deleted: a file was deleted
  * modified: a file was modified
  * moved: a file was moved

%prep
%setup -q -n easywatch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/easywatch
%{python_sitelib}/easywatch-%{version}*-info

%changelog
