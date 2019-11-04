#
# spec file for package python-stevedore
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


Name:           python-stevedore
Version:        1.31.0
Release:        0
Summary:        Manage dynamic plugins for Python applications
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/stevedore/
Source0:        https://files.pythonhosted.org/packages/source/s/stevedore/stevedore-1.31.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-docutils
BuildRequires:  python2-mock
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-pytest
BuildRequires:  python2-setuptools
BuildRequires:  python2-testtools
BuildRequires:  python3-docutils
BuildRequires:  python3-mock
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-testtools
Requires:       python-pbr >= 2.0.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
(plugins) at runtime. Many applications implement their own
library for doing this, using ``__import__`` or ``importlib``.
stevedore avoids creating yet another extension
mechanism by building on top of setuptools entry points. The code
for managing entry points tends to be repetitive, though, so stevedore
provides manager classes for implementing common patterns for using
dynamically loaded extensions.

%package -n python-stevedore-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildRequires:  python2-Sphinx
BuildRequires:  python3-Sphinx
Provides:       %{python_module stevedore-doc = %{version}}

%description -n python-stevedore-doc
Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
(plugins) at runtime. Many applications implement their own
library for doing this, using ``__import__`` or ``importlib``.
stevedore avoids creating yet another extension
mechanism by building on top of setuptools entry points. The code
for managing entry points tends to be repetitive, though, so stevedore
provides manager classes for implementing common patterns for using
dynamically loaded extensions.

This package contains documentation in HTML format.

%prep
%autosetup -p1 -n stevedore-%{version}
%py_req_cleanup

%build
%python_build

# generate html docs
PBR_VERSION=1.31.0 PYTHONPATH=. %sphinx_build -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install

%check
# use pytest instead of stestr to break a build cycle between python-cliff, python-stestr and python-stevedore
%python_exec -m pytest stevedore/tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/stevedore
%{python_sitelib}/stevedore-*.egg-info

%files -n python-stevedore-doc
%license LICENSE
%doc doc/build/html

%changelog
