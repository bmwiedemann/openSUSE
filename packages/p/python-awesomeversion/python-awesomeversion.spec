#
# spec file for package python-awesomeversion
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-awesomeversion
Version:        25.8.0
Release:        0
Summary:        One version package to rule them all
License:        MIT
URL:            https://github.com/ludeeus/awesomeversion
Source:         https://files.pythonhosted.org/packages/source/a/awesomeversion/awesomeversion-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-codspeed}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-snapshot}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
One version package to rule them all, One version package to find them, One version package to bring them all, and in the darkness bind them.

Make anything a version object, and compare against a vast section of other version formats.

%prep
%autosetup -p1 -n awesomeversion-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENCE.md
%{python_sitelib}/awesomeversion
%{python_sitelib}/awesomeversion-%{version}.dist-info

%changelog
