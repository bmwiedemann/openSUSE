#
# spec file for package python-click-help-colors
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
Name:           python-click-help-colors
Version:        0.6
Release:        0
Summary:        Colorization of help messages in Click
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/r-m-n/click-help-colors
Source:         https://files.pythonhosted.org/packages/source/c/click-help-colors/click-help-colors-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 7.0}
# /SECTION
%python_subpackages

%description
Colorization of help messages in Click

%prep
%setup -q -n click-help-colors-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
