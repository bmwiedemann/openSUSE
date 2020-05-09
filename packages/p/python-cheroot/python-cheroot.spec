#
# spec file for package python-cheroot
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define pypi_name cheroot
%bcond_without python2
Name:           python-%{pypi_name}
Version:        8.3.0
Release:        0
Summary:        Pure-python HTTP server
License:        BSD-3-Clause
URL:            https://github.com/cherrypy/cheroot
Source:         https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# PATCH-FIX_UPSTREAM //github.com/cherrypy/cheroot/pull/282
Patch1:         0001-Avoid-race-condition-on-persistent-HTTP-connections.patch

BuildRequires:  %{python_module jaraco.functools}
BuildRequires:  %{python_module jaraco.text >= 3.1}
BuildRequires:  %{python_module more-itertools >= 2.6}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-mock >= 1.11.0}
BuildRequires:  %{python_module requests-unixsocket}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools >= 34.4}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools_scm_git_archive >= 1.0}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  %{python_module trustme}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.functools
Requires:       python-more-itertools >= 2.6
Requires:       python-six >= 1.11.0
# the package and distribution name is lowercase-cheroot,
# but PyPI claims the name is capital-Cheroot
# *smacks head against desk*
Provides:       python-Cheroot = %{version}
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-backports.functools_lru_cache
%endif
%ifpython2
Requires:       python-backports.functools_lru_cache
%endif
%ifpython2
Requires:       python-backports.functools_lru_cache
%endif
%python_subpackages

%description
Cheroot is the pure-Python HTTP server used by CherryPy.

%prep
%autosetup -n cheroot-%{version} -p1
# do not require cov/xdist/etc
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Exclusions because of gh#cherrypy/cheroot#200
%pytest -k 'not test_tls_client_auth'

%files %{python_files}
%license LICENSE.md
%doc README.rst CHANGES.rst
%python3_only %{_bindir}/cheroot
%{python_sitelib}/*

%changelog
