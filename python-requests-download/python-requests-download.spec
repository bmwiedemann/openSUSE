#
# spec file for package python-requests-download
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
Name:           python-requests-download
Version:        0.1.2
Release:        0
Summary:        Download files using requests and save them to a target path
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.github.com/takluyver/requests_download
Source:         https://files.pythonhosted.org/packages/source/r/requests_download/requests_download-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/takluyver/requests_download/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-progressbar
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Download files using requests and save them to a target path.

%prep
%setup -q -n requests_download-%{version}
cp %{SOURCE1} .

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
