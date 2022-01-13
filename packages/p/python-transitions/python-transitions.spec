#
# spec file for package python-transitions
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019-2021, Martin Hauke <mardnh@gmx.de>
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
%bcond_without python2
Name:           python-transitions
Version:        0.8.10
Release:        0
Summary:        A lightweight, object-oriented Python state machine implementation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytransitions/transitions
Source:         https://files.pythonhosted.org/packages/source/t/transitions/transitions-%{version}.tar.gz
# PATCH-FIX-UPSTREAM transitions-fixpy310.patch -- gh#pytransitions/transitions#559
Patch0:         transitions-fixpy310.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Suggests:       python-pygraphviz
Suggests:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dill}
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pygraphviz}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%if %{with python2}
BuildRequires:  python2-mock
%endif
# png support for graphviz
BuildRequires:  graphviz-gnome
BuildRequires:  noto-sans-fonts
# /SECTION
%python_subpackages

%description
The transitions package makes it convenient and relatively easy to define and
implement FSMs (finite state machines) in python.

%prep
%autosetup -p 1 -n transitions-%{version}
find . -type f -exec chmod -x {} \;
sed -i 's/\r$//' LICENSE Changelog.md README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not TestCodeFormat"

%files %{python_files}
%license LICENSE
%doc Changelog.md README.md
%{python_sitelib}/transitions
%{python_sitelib}/transitions-%{version}*-info

%changelog
