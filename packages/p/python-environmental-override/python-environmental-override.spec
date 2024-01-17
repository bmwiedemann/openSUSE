#
# spec file for package python-environmental-override
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
Name:           python-environmental-override
Version:        0.1.2
Release:        0
Summary:        Module to configure apps using environment variables
# gh#coddingtonbear/environmental-override#1
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/coddingtonbear/environmental-override
Source:         https://files.pythonhosted.org/packages/source/e/environmental-override/environmental-override-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Environmental Override offers setting configuration values from
environment variables.

%prep
%setup -q -n environmental-override-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*

%changelog
