#
# spec file for package python-feedparser-sgmllib
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-feedparser-sgmllib
Version:        2.1.0
Release:        0
Summary:        This is sgmllib from Python 2.7. For feedparser use only
License:        Python-2.0
URL:            https://github.com/python-syndication/feedparser-sgmllib
Source:         https://files.pythonhosted.org/packages/source/f/feedparser-sgmllib/feedparser_sgmllib-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 2.0.0}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
This is sgmllib from Python 2.7. For feedparser use only.

%prep
%autosetup -p1 -n feedparser_sgmllib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/feedparser_sgmllib
%{python_sitelib}/feedparser_sgmllib-%{version}.dist-info
%pycache_only %{python_sitelib}/feedparser_sgmllib/__pycache__/*.pyc

%changelog
