#
# spec file for package python-orange-canvas-core
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-orange-canvas-core
Version:        0.1.9
Release:        0
License:        GPL-3.0
Summary:        Core component of Orange Canvas
Url:            http://orange.biolab.si/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/o/orange-canvas-core/orange-canvas-core-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-AnyQt
Requires:       python-CacheControl
Requires:       python-commonmark
Requires:       python-docutils
Requires:       python-qt5
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module AnyQt}
BuildRequires:  %{python_module CacheControl}
BuildRequires:  %{python_module commonmark}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module qt5}
BuildRequires:  xorg-x11-server
# /SECTION

%python_subpackages

%description
Core component of Orange Canvas

%prep
%setup -q -n orange-canvas-core-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export QT_QPA_PLATFORM="offscreen"
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
