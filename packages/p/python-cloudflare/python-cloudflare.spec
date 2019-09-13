#
# spec file for package python-cloudflare
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
Name:           python-cloudflare
Version:        2.3.0
Release:        0
Summary:        Python wrapper for the Cloudflare v4 API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cloudflare/python-cloudflare
Source:         https://files.pythonhosted.org/packages/source/c/cloudflare/cloudflare-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module jsonlines}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-future
Requires:       python-jsonlines
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Python wrapper for the Cloudflare Client API v4.

%prep
%setup -q -n cloudflare-%{version}

%build
%python_build

%install
%python_install
# remove examples from sitelib
%python_expand rm -rf %{buildroot}%{$python_sitelib}/examples
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/cli4
%{python_sitelib}/*

%changelog
