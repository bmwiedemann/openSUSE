#
# spec file for package python-commented-configparser
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Shawn W Dunn <sfalken@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


%global rname commented_configparser

Name:           python-commented-configparser
Version:        3.0.0
Release:        0
Summary:        A custom ConfigParser class that preserves comments
License:        MIT
URL:            https://github.com/Preocts/commented-configparser
Source:         https://files.pythonhosted.org/packages/source/c/%{rname}/%{rname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-flake8
Suggests:       python-flake8-builtins
Suggests:       python-flake8-pep585
Suggests:       python-black
Suggests:       python-isort
Suggests:       python-mypy
BuildArch:      noarch
%python_subpackages

%description
A custom ConfigParser class that preserves comments and most formatting when writing loaded config out.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/commentedconfigparser
%{python_sitelib}/%{rname}-%{version}.dist-info

%changelog
