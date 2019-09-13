#
# spec file for package python-delegator
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
Name:           python-delegator
Version:        0.0.3
Release:        0
Summary:        Python implementation of Ruby's delegate.rb
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hugobast/delegator
Source:         https://files.pythonhosted.org/packages/source/d/delegator/delegator-%{version}.tar.gz
Patch0:         split-readme.patch
Patch1:         remove-exceptions-import.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Conflicts:      python-delegator.py
%python_subpackages

%description
Python implementation of Ruby's delegate.rb.

%prep
%setup -q -n delegator-%{version}
%patch0 -p1
%patch1 -p1
touch test/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}:${PWD} $python setup.py test

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
