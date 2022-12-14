#
# spec file for package python-CherryPy
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-CherryPy
Version:        18.8.0
Release:        0
Summary:        Object-Oriented HTTP framework
License:        BSD-3-Clause
URL:            https://www.cherrypy.dev
Source:         https://files.pythonhosted.org/packages/source/C/CherryPy/CherryPy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-cheroot >= 8.2.1
Requires:       python-jaraco.collections
Requires:       python-more-itertools
Requires:       python-portend >= 2.1.1
Requires:       python-zc.lockfile
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Recommends:     python-Routes >= 2.3.1
Recommends:     python-flup
Recommends:     python-pyOpenSSL
Recommends:     python-python-memcached >= 1.58
Recommends:     python-simplejson
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cheroot >= 8.2.1}
BuildRequires:  %{python_module jaraco.collections}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module path.py}
BuildRequires:  %{python_module portend >= 2.1.1}
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module pytest-services}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module zc.lockfile}
# /SECTION
%python_subpackages

%description
CherryPy is a pythonic, object-oriented HTTP framework.

CherryPy allows developers to build web applications in much the same way they
would build any other object-oriented Python program. This usually results in
smaller source code developed in less time.

CherryPy is now more than three years old and it is has proven very fast and
stable. It is being used in production by many sites, from the simplest ones
to the most demanding ones.

Oh, and most importantly: CherryPy is fun to work with :-)

%prep
%setup -q -n CherryPy-%{version}
# do not require cov/xdist/etc
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/cherryd

%check
# skip all travis known fails as they would most likely fail in obs too
export TRAVIS="true"
# testCombinedTools fails with trace in cheroot tests
%pytest -k 'not testCombinedTools'

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative cherryd

%post
%python_install_alternative cherryd

%postun
%python_uninstall_alternative cherryd

%files %{python_files}
%license LICENSE.md
%doc README.rst CHANGES.rst
%python_alternative %{_bindir}/cherryd
%{python_sitelib}/cherrypy/
%{python_sitelib}/CherryPy-%{version}-py%{python_version}.egg-info

%changelog
