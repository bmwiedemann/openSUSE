#
# spec file for package python-pyhibp
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-pyhibp
Version:        4.1.0
Release:        0
Summary:        An interface to Troy Hunt's 'Have I Been Pwned' public API
License:        AGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://gitlab.com/kitsunix/pyHIBP/pyHIBP
Source:         https://files.pythonhosted.org/packages/source/p/pyhibp/pyhibp-%{version}.tar.gz
BuildRequires:  %{python_module requests >= 2.20.0 }
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.20.0
BuildArch:      noarch
%python_subpackages

%description
A Python interface to Troy Hunt's 'Have I Been Pwned?' (HIBP) public API.

%prep
%setup -q -n pyhibp-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

### Tests need network access to https://haveibeenpwned.com
#%%check
#%%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/*

%changelog
