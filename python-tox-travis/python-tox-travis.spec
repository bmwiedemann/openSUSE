#
# spec file for package python-tox-travis
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
Name:           python-tox-travis
Version:        0.12
Release:        0
Summary:        Seamless integration of Tox into Travis CI
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/tox-dev/tox-travis
Source:         https://files.pythonhosted.org/packages/source/t/tox-travis/tox-travis-%{version}.tar.gz
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module tox >= 2.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-tox >= 2.0
BuildArch:      noarch

%python_subpackages

%description
Seamless integration of Tox into Travis CI.

%prep
%setup -q -n tox-travis-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Without isolating the python and tox binaries, py37 would polute the py27
# site-packages, probably related to how tox loads all available pythons.
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m pytest

%files %{python_files}
%doc README.rst docs/*.rst
%license LICENSE
%{python_sitelib}/*

%changelog
