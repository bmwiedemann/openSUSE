#
# spec file for package python-frozendict
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
Name:           python-frozendict
Version:        1.2
Release:        0
Summary:        An immutable dictionary
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/slezica/python-frozendict
Source:         https://files.pythonhosted.org/packages/source/f/frozendict/frozendict-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
frozendict is an immutable wrapper around dictionaries that implements the
complete mapping interface. It can be used as a drop-in replacement for
dictionaries where immutability is desired.

%prep
%setup -q -n frozendict-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/frozendict-%{version}-py*.egg-info/
%{python_sitelib}/frozendict

%changelog
