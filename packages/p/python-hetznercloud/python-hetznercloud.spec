#
# spec file for package python-hetznercloud
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-hetznercloud
Version:        1.1.1
Release:        0
Summary:        Hetzner Cloud SDK
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/elsyms/hetznercloud-py
Source:         https://github.com/elsyms/hetznercloud-py/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
#BuildRequires:  %%{python_module nose >= 1.3.7 }
#BuildRequires:  %%{python_module requests >= 2.18.4}
BuildRequires:  fdupes
Requires:       python-requests >= 2.18.4
BuildArch:      noarch
%python_subpackages

%description
A Python 3 SDK for the Hetzner cloud service.

%prep
%setup -q -n hetznercloud-py-%{version}
sed -i 's/\r$//' LICENSE.txt README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disabled since the tests need access to the Hetzner API servers.

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
