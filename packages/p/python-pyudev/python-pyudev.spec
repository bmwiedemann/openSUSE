#
# spec file for package python-pyudev
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyudev
Version:        0.22.0
Release:        0
Summary:        Udev bindings for Python
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            http://pyudev.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pyudev/pyudev-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pytest_register_mark.patch gh#pyudev/pyudev#404 mcepl@suse.com
# Add missing mark registration and register and use another mark
Patch0:         pytest_register_mark.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
Requires:       libudev1
Requires:       python-six
BuildArch:      noarch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module yapf}
%ifpython2
# pyudev was last used in KDE:Unstable:Playground (pyudev-0.8)
Provides:       pyudev = %{version}
Obsoletes:      pyudev < %{version}
%endif
%python_subpackages

%description
A Python binding to libudev, the hardware management library and service found
in modern linux systems.

%prep
%autosetup -p1 -n pyudev-%{version}

# Disable intersphinx and issuetracker, we don't want to access the web during doc build:
sed -i -e "s|'sphinx.ext.intersphinx',\\?||" -e "s|'sphinxcontrib.issuetracker',\\?||" doc/conf.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# We don't have real /dev in osc build chroot gh#pyudev/pyudev#404
%pytest -k 'not real_udev'

%files %{python_files}
%license COPYING
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
