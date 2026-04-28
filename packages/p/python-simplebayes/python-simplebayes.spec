#
# spec file for package python-simplebayes
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-simplebayes
Version:        3.2.0
Release:        0
Summary:        A memory-based, optional-persistence naïve bayesian text classifier
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hickeroar/simplebayes
Source:         https://files.pythonhosted.org/packages/source/s/simplebayes/simplebayes-%{version}.tar.gz
BuildRequires:  %{python_module fastapi >= 0.116.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module snowballstemmer >= 3.0.1}
BuildRequires:  %{python_module uvicorn >= 0.35.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-fastapi >= 0.116.1
Requires:       python-snowballstemmer >= 3.0.1
Requires:       python-uvicorn >= 0.35.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

%description
A memory-based, optional-persistence naïve bayesian text classifier
heavily inspired by the python "redisbayes" module.

%python_subpackages

%prep
%setup -q -n simplebayes-%{version}

%build
export LANG=C.UTF-8
%pyproject_wheel

%install
export LANG=C.UTF-8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/simplebayes-server

%pre
%python_libalternatives_reset_alternative simplebayes-server

%post
%python_install_alternative simplebayes-server

%postun
%python_uninstall_alternative simplebayes-server

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/simplebayes-server
%{python_sitelib}/simplebayes
%{python_sitelib}/simplebayes-%{version}*-info

%changelog
