#
# spec file for package python-nbsmoke
#
# Copyright (c) 2022 SUSE LLC
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
%define         skip_python2 1
Name:           python-nbsmoke
Version:        0.6.0
Release:        0
Summary:        Basic notebook checks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyviz-dev/nbsmoke
Source:         https://files.pythonhosted.org/packages/source/n/nbsmoke/nbsmoke-%{version}.tar.gz
# PATCH-FIX-UPSTREAM nbsmoke-pr63-remove-id.patch gh#pyviz-dev/nbsmoke#63
Patch0:         nbsmoke-pr63-remove-id.patch
# PATCH-FIX-OPENSUSE nbsmoke-obs-nounraisableexception.patch, don't error on warnings about obs not closing sockets in time, code@bnavigator.de
Patch1:         nbsmoke-obs-nounraisableexception.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ipykernel
Requires:       python-jupyter-client
Requires:       python-nbconvert
Requires:       python-nbformat
Requires:       python-param
Requires:       python-pyflakes
Requires:       python-pytest >= 3.1.1
Recommends:     python-beautifulsoup4
Recommends:     python-requests
Provides:       python-jupyter_nbsmoke = %{version}
Obsoletes:      python-jupyter_nbsmoke < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter-client}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module param}
BuildRequires:  %{python_module pyflakes}
BuildRequires:  %{python_module pytest >= 3.1.1}
BuildRequires:  %{python_module requests}
# /SECTION
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-nbsmoke = %{version}
%endif
%python_subpackages

%description
Basic notebook smoke tests for checking whether the notebooks run,
and whether they contain lint.

%prep
%autosetup -p1 -n nbsmoke-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# needs to import from sourcedir
export PYTHONPATH=":x"
%pytest -p pytester

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/nbsmoke-%{version}*-info
%{python_sitelib}/nbsmoke/

%changelog
