#
# spec file for package python-blue
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-blue
Version:        0.9.1
Release:        0
Summary:        A code formatter written in, and written for Python
License:        MIT
URL:            https://github.com/grantjenks/blue
Source:         https://github.com/grantjenks/blue/archive/v%{version}.tar.gz#/blue-%{version}.tar.gz
# PATCH-FIX-OPENSUSE unpin-tomli.patch -- gh#grantjenks/blue#66
Patch1:         unpin-tomli.patch
# PATCH-FIX-UPSTREAM flake8-v5-compatibility.patch -- gh#grantjenks/blue#78
Patch2:         flake8-v5-compatibility.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module black >= 21.7}
BuildRequires:  %{python_module flake8 >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION doc and test requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-black >= 21.7
Requires:       python-flake8 > 3.8
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Black is a code formatter written in Python, and reformats Python 2.x
and 3.x code.

Black reformats entire files in place. It is not configurable. It
does not take previous formatting into account. The coding style
enforced is a PEP-8 subset, adheres to PEP-257, and otherwise passes
the rules of the "pycodestyle" checker. Black skips over blocks that
start and end with "# fmt: off" and "# fmt: on", respectively. It
also recognizes YAPF's block comments to the same effect.

%package -n python-blue-doc
Summary:        Documentation files for %name
Provides:       %{python_module foo-doc = %{version}}

%description -n python-blue-doc
HTML Documentation and examples for %name.

%prep
%autosetup -p1 -n blue-%{version}

# avoid pytest addopts for coverage checks
sed -i '/--cov/d' tox.ini

%build
%python_build
( cd docs ; PYTHONPATH=../build/lib make html )

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/blue

%check
# gh#grantjenks/blue#72
%pytest -k 'not (test_good_dirs or test_bad_dirs)'

%post
%python_install_alternative blue

%postun
%python_uninstall_alternative blue

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/blue
%{python_sitelib}/blue
%{python_sitelib}/blue-%{version}*-info

%files -n python-blue-doc
%doc docs/_build/html

%changelog
