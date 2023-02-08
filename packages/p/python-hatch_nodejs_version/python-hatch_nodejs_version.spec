#
# spec file for package python-hatch_nodejs_version
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-hatch_nodejs_version
Version:        0.3.1
Release:        0
Summary:        This package provides two Hatch plugins for nodejs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/agoose77/hatch-nodejs-version
Source:         https://files.pythonhosted.org/packages/source/h/hatch_nodejs_version/hatch_nodejs_version-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hatchling >= 0.21.0
Provides:       python-hatch-nodejs-version = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Hatch plugin to read pyproject.toml metadata from package.json

This package provides two Hatch plugins:

* version source plugin that reads/writes the package version
  from the version field of the Node.js package.json file.
* metadata hook plugin that reads PEP 621 metadata from the
  Node.js package.json file.

%prep
%setup -q -n hatch_nodejs_version-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%{python_sitelib}/hatch_nodejs_version
%{python_sitelib}/hatch_nodejs_version-%{version}.dist-info

%changelog
