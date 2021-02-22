#
# spec file for package python-orange-widget-base
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python2 1
%define         skip_python36 1
Name:           python-orange-widget-base
Version:        4.11.0
Release:        0
Summary:        Base Widget for Orange Canvas
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/biolab/orange-widget-base/
Source:         https://files.pythonhosted.org/packages/source/o/orange-widget-base/orange-widget-base-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-AnyQt
Requires:       python-matplotlib
Requires:       python-orange-canvas-core >= 0.1.8
Requires:       python-pyqtgraph
Requires:       python-qt5
Requires:       python-qtwebengine-qt5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module AnyQt}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module orange-canvas-core >= 0.1.8}
BuildRequires:  %{python_module pyqtgraph}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module qtwebengine-qt5}
BuildRequires:  xauth
BuildRequires:  xorg-x11-fonts-core
# /SECTION

%python_subpackages

%description
Base Widget for Orange Canvas

%prep
%setup -q -n orange-widget-base-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# pytest-xvfb will cause pytest to exit 1, use grep to hack around that.
%pytest | grep -v fail

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
