#
# spec file for package python-mailman3-fedmsg-plugin
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


%{?sle15_python_module_pythons}
Name:           python-mailman3-fedmsg-plugin
Version:        0.5
Release:        0
Summary:        Emit fedmsg messages from mailman3
License:        LGPL-2.0-only
URL:            https://github.com/fedora-infra/mailman3-fedmsg-plugin
Source:         https://files.pythonhosted.org/packages/source/m/mailman3-fedmsg-plugin/mailman3-fedmsg-plugin-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Emit fedmsg messages from mailman3.

%prep
%setup -q -n mailman3-fedmsg-plugin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream testsuite

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/mailman3_fedmsg_plugin.py
%pycache_only %{python_sitelib}/__pycache__/mailman3_fedmsg_plugin*.pyc
%{python_sitelib}/mailman3_fedmsg_plugin-%{version}.dist-info

%changelog
