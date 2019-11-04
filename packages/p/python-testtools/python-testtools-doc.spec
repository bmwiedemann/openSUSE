#
# spec file for package python-testtools-doc
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-testtools-doc
Version:        2.3.0
Release:        0
Summary:        Documentation for python-testtools
License:        MIT
Group:          Documentation/HTML
URL:            https://launchpad.net/testtools
Source:         https://files.pythonhosted.org/packages/source/t/testtools/testtools-%{version}.tar.gz
Patch0:         testtools-py37.patch
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools = %{version}}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Provides:       python2-testtools-doc = %{version}
Provides:       python3-testtools-doc = %{version}
BuildArch:      noarch

%description
Documentation and help files for python-testtools.

%prep
%setup -q -n testtools-%{version}
%patch0 -p1

%build
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
mkdir -p %{buildroot}%{_docdir}/python-testtools/
cp -r build/sphinx/html %{buildroot}%{_docdir}/python-testtools/
%fdupes %{buildroot}%{_docdir}

%check
%python_exec -m testtools.run testtools.tests.test_suite

%files
%license LICENSE
%{_docdir}/python-testtools/

%changelog
