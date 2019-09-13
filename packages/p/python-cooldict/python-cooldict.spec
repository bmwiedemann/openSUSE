#
# spec file for package python-cooldict
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
Name:           python-cooldict
Version:        1.04
Release:        0
Summary:        dict-like structures for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/zardus/cooldict
Source:         https://files.pythonhosted.org/packages/source/c/cooldict/cooldict-%{version}.tar.gz
BuildRequires:  %{python_module ana >= 0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ana >= 0.1
BuildArch:      noarch

%python_subpackages

%description
cooldict provides some dict-like structures for Python, such as
* a write-through cache around another dict
* a finalizable dict
* a branching dict
* a copy-on-write dict (with and without sinkholing capability)

%prep
%setup -q -n cooldict-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Well there is a test, but it does not work even on the git, so skip for now
#%%python_exec cooldict.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
