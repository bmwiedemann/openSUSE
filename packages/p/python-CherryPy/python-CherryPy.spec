#
# spec file for package python-CherryPy
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-CherryPy
Version:        18.1.2
Release:        0
Summary:        Object-Oriented HTTP framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://www.cherrypy.org
Source:         https://files.pythonhosted.org/packages/source/C/CherryPy/CherryPy-%{version}.tar.gz
Patch0:         pytest5.patch
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cheroot >= 6.2.4
Requires:       python-more-itertools
Requires:       python-portend >= 2.1.1
Requires:       python-zc.lockfile
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Routes >= 2.3.1
Recommends:     python-flup
Recommends:     python-memcached >= 1.58
Recommends:     python-pyOpenSSL
Recommends:     python-simplejson
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cheroot >= 6.2.4}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module path.py}
BuildRequires:  %{python_module portend >= 2.1.1}
BuildRequires:  %{python_module pytest-services}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-toolbelt}
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
%patch0 -p1
# do not require cov/xdist/etc
sed -i -e '/addopts/d' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/cherryd

%check
# gh#cherrypy/cherrypy#1781
%pytest -k 'not (test_wait_publishes_periodically or test_null_bytes)'

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
