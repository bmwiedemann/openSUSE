#
# spec file for package python-markdownify
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
Name:           python-markdownify
Version:        1.2.2
Release:        0
Summary:        Convert HTML to markdown
License:        MIT
URL:            http://github.com/matthewwithanm/python-markdownify
Source:         https://files.pythonhosted.org/packages/source/m/markdownify/markdownify-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  alts
BuildRequires:  fdupes
Requires:       alts
Requires:       python-beautifulsoup4 >= 4.9
Requires:       python-six >= 1.15
BuildArch:      noarch
%python_subpackages

%description
Convert HTML to markdown.

%prep
%autosetup -p1 -n markdownify-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/markdownify
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests not in PyPI tarball, setuptools_scm cannot handle github tarballs

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/markdownify
%{python_sitelib}/markdownify
%{python_sitelib}/markdownify-%{version}.dist-info

%changelog
