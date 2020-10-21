#
# spec file for package python-nocasedict
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
Name:           python-nocasedict
Version:        1.0.1
Release:        0
Summary:        A case-insensitive ordered dictionary for Python
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/pywbem/nocasedict
Source:         https://files.pythonhosted.org/packages/source/n/nocasedict/nocasedict-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Class `NocaseDict`_ is a case-insensitive ordered dictionary that preserves
the original lexical case of its keys.

%prep
%setup -q -n nocasedict-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/nocasedict
%{python_sitelib}/nocasedict-%{version}*info

%changelog
