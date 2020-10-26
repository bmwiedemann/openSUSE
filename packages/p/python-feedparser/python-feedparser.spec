#
# spec file for package python-feedparser
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
Name:           python-feedparser
Version:        6.0.2
Release:        0
Summary:        Universal Feed Parser Module for Python
License:        BSD-2-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/kurtmckee/feedparser
Source:         https://files.pythonhosted.org/packages/source/f/feedparser/feedparser-%{version}.tar.gz
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sgmllib3k}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-xml
Recommends:     python-chardet
Requires:       python-sgmllib3k
BuildArch:      noarch
%python_subpackages

%description
A universal feed parser module for Python that handles RSS 0.9x, RSS 1.0, RSS
2.0, CDF, Atom 0.3, Atom 1.0 feeds.

%prep
%setup -q -n feedparser-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}:${PWD}
$python tests/runtests.py
}

%files %{python_files}
%license LICENSE
%doc NEWS README.rst
%{python_sitelib}/feedparser/
%{python_sitelib}/feedparser-%{version}-py%{python_version}.egg-info

%changelog
