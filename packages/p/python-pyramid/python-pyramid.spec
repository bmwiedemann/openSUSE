#
# spec file for package python-pyramid
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2014-2017 LISA GmbH, Bingen, Germany.
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


Name:           python-pyramid
Version:        2.0.1
Release:        0
Summary:        The Pyramid web application development framework
License:        BSD-4-Clause AND ZPL-2.1 AND MIT
URL:            https://pylonsproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/pyramid/pyramid-%{version}.tar.gz
BuildRequires:  %{python_module PasteDeploy >= 1.5.0}
BuildRequires:  %{python_module WebOb >= 1.8.3}
BuildRequires:  %{python_module WebTest >= 1.3.1}
BuildRequires:  %{python_module hupper >= 1.5}
BuildRequires:  %{python_module plaster-pastedeploy}
BuildRequires:  %{python_module plaster}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module translationstring >= 0.4}
BuildRequires:  %{python_module venusian >= 1.0}
BuildRequires:  %{python_module zope.component >= 4.0}
BuildRequires:  %{python_module zope.deprecation >= 3.5.0}
BuildRequires:  %{python_module zope.interface >= 3.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PasteDeploy >= 1.5.0
Requires:       python-WebOb >= 1.8.3
Requires:       python-hupper >= 1.5
Requires:       python-plaster
Requires:       python-plaster-pastedeploy
Requires:       python-setuptools
Requires:       python-translationstring >= 0.4
Requires:       python-venusian >= 1.0
Requires:       python-zope.deprecation >= 3.5.0
Requires:       python-zope.interface >= 3.8.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-repoze.lru >= 0.4
%endif
%ifpython2
Requires:       python-repoze.lru >= 0.4
%endif
%python_subpackages

%description
Pyramid is a Python web application development framework
produced by the Pylons Project (http://pylonsproject.org).
It was previously known as repoze.bfg (http://bfg.repoze.org).



# NOTE: The documentation in the docs/ directory is under a
# non-free license (CC-BY-NC-SA-3.0). Do not package it.

%prep
%setup -q -n pyramid-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

for p in pdistreport prequest proutes pserve pshell ptweens pviews; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%check
export LANG=en_US.UTF-8
%pytest tests/

%post
%python_install_alternative pdistreport prequest proutes pserve pshell ptweens pviews

%postun
%python_uninstall_alternative pdistreport

%files %{python_files}
%license LICENSE.txt
%doc *.rst
%python_alternative %{_bindir}/pdistreport
%python_alternative %{_bindir}/prequest
%python_alternative %{_bindir}/proutes
%python_alternative %{_bindir}/pserve
%python_alternative %{_bindir}/pshell
%python_alternative %{_bindir}/ptweens
%python_alternative %{_bindir}/pviews
%{python_sitelib}/*

%changelog
