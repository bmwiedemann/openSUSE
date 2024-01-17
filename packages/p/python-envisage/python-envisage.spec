#
# spec file for package python-envisage
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


%define         skip_python2 1
%define         X_display         ":98"
%bcond_without     test
Name:           python-envisage
Version:        6.1.1
Release:        0
Summary:        Extensible application framework for Python
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
License:        BSD-3-Clause AND Python-2.0 AND LGPL-3.0-only AND CC-BY-SA-1.0 AND CC-BY-SA-2.0 AND CC-BY-SA-2.5 AND CC-BY-SA-3.0 AND SUSE-Public-Domain
URL:            https://github.com/enthought/envisage
Source:         https://files.pythonhosted.org/packages/source/e/envisage/envisage-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traits >= 6.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-traits >= 6.2
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module apptools}
# Only test optional ipykernel where we still have an old version -- gh#enthought/envisage#423
BuildRequires:  %{python_module ipykernel < 6 if %python-base < 3.7}
BuildRequires:  %{python_module traitsui}
BuildRequires:  xorg-x11-server
%endif
%python_subpackages

%description
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application. When building an
application using Envisage, the entire application consists primarily
of plug-ins. In this respect, it is similar to the Eclipse and
Netbeans frameworks for Java applications.

Part of the Enthought Tool Suite (ETS).

%prep
%setup -q -n envisage-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%pyunittest -v
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt image_LICENSE.txt image_LICENSE_CP.txt
%{python_sitelib}/envisage/
%{python_sitelib}/envisage-%{version}-py*.egg-info

%changelog
