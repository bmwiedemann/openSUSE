#
# spec file for package python-podcastparser
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-podcastparser
Version:        0.6.11
Release:        0
Summary:        A podcast parser
License:        ISC
URL:            https://github.com/gpodder/podcastparser
Source:         https://files.pythonhosted.org/packages/source/p/podcastparser/podcastparser-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-xml
BuildArch:      noarch
%python_subpackages

%description
The podcast parser project is a library from the gPodder project to provide a
way of parsing RSS- and Atom-based podcast feeds in Python.

%prep
%setup -q -n podcastparser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/podcastparser.py
%{python_sitelib}/podcastparser*-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/podcastparser*

%changelog
