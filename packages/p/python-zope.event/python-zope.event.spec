#
# spec file for package python-zope.event
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


%global modname zope.event
%{?sle15_python_module_pythons}
Name:           python-zope.event
Version:        5.0
Release:        0
Summary:        Very basic event publishing system
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/%{modname}
Source:         https://files.pythonhosted.org/packages/source/z/zope.event/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Documentation requirements:
BuildRequires:  python3-Sphinx
BuildArch:      noarch
%python_subpackages

%description
An event publishing system and a very simple event-dispatching system on
which more sophisticated event dispatching systems can be built. For
example, a type-based event dispatching system that builds on zope.event
can be found in zope.component.

%package -n %{name}-doc
Summary:        Very basic event publishing system

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build
# cannot give build/lib here, as pkg_resources.py needs the egg info and
# raises DistributionNotFound for zope.event, hence build doc directly
# from source in order to avoid the need for an external doc package
export PYTHONPATH=$(pwd)/src
sphinx-build -b html docs build/sphinx/html && rm -r build/sphinx/html/.{buildinfo,doctrees}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd build/lib
%{python_expand \
$python -m unittest -v zope.event.tests
$python -m doctest -v zope/event/classhandler.py
}

%files %{python_files}
%license COPYRIGHT.txt LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%endif
%doc build/sphinx/html/

%changelog
