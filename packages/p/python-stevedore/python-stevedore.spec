#
# spec file for package python-stevedore
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


Name:           python-stevedore
Version:        5.4.0
Release:        0
Summary:        Manage dynamic plugins for Python applications
License:        Apache-2.0
URL:            https://docs.openstack.org/stevedore/latest/
Source:         https://files.pythonhosted.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
BuildRequires:  %{python_module pbr >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testtools}
# /SECTION
BuildRequires:  fdupes
Requires:       python-importlib-metadata
Requires:       python-pbr
%if "%{?python_provides}" == "python3"
Provides:       python3-stevedore = %{version}
Obsoletes:      python3-stevedore <= %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
(plugins) at runtime. Many applications implement their own
library for doing this, using ``__import__`` or ``importlib``.
stevedore avoids creating yet another extension
mechanism by building on top of setuptools entry points. The code
for managing entry points tends to be repetitive, though, so stevedore
provides manager classes for implementing common patterns for using
dynamically loaded extensions.

%prep
%autosetup -p1 -n stevedore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitelib}/stevedore
%{python_sitelib}/stevedore-%{version}.dist-info

%changelog
