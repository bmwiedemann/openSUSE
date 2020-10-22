#
# spec file for package python-debtcollector
#
# Copyright (c) 2020 SUSE LLC
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


Name:           python-debtcollector
Version:        2.2.0
Release:        0
Summary:        A collection of Python deprecation patterns and strategies
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/debtcollector/
Source0:        https://files.pythonhosted.org/packages/source/d/debtcollector/debtcollector-2.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-fixtures
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-stestr
BuildRequires:  python3-wrapt >= 1.7.0
BuildArch:      noarch

%description
A collection of Python deprecation patterns and strategies that help
you collect your technical debt in a non-destructive manner. The goal
of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand
into a larger set of patterns as time goes on. The desired output of
these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about
future deprecations.

%package -n python3-debtcollector
Summary:        A collection of Python deprecation patterns and strategies
Group:          Development/Languages/Python
Requires:       python3-pbr >= 2.0.0
Requires:       python3-six >= 1.10.0
Requires:       python3-wrapt >= 1.7.0

%description -n python3-debtcollector
A collection of Python deprecation patterns and strategies that help
you collect your technical debt in a non-destructive manner. The goal
of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand
into a larger set of patterns as time goes on. The desired output of
these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about
future deprecations.

This package contains the Python 3.x module.

%package -n python-debtcollector-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-debtcollector-doc
A collection of Python deprecation patterns and strategies that help
you collect your technical debt in a non-destructive manner. The goal
of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand
into a larger set of patterns as time goes on. The desired output of
these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about
future deprecations.

This package contains documentation in HTML format.

%prep
%autosetup -p1 -n debtcollector-2.2.0
%py_req_cleanup

%build
%py3_build

# generate html doc
PBR_VERSION=2.2.0 %sphinx_build -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
python3 -m stestr.cli run

%install
%py3_install

%files -n python3-debtcollector
%license LICENSE
%doc README.rst
%{python3_sitelib}/debtcollector
%{python3_sitelib}/debtcollector-*.egg-info

%files -n python-debtcollector-doc
%license LICENSE
%doc doc/build/html

%changelog
