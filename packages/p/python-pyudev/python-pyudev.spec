#
# spec file for package python-pyudev
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pyudev
Version:        0.24.3
Release:        0
Summary:        Udev bindings for Python
License:        LGPL-2.1-or-later
URL:            https://pyudev.readthedocs.io/
Source0:        https://github.com/pyudev/pyudev/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM pytest_register_mark.patch gh#pyudev/pyudev#404 mcepl@suse.com
# Add missing mark registration and register and use another mark
Patch0:         pytest_register_mark.patch
# PATCH-FIX-OPENSUSE hypothesis_settings.patch mcepl@suse.com
# tests timeout on OBS
Patch2:         hypothesis_settings.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module yapf}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
Requires:       libudev1
BuildArch:      noarch
%if 0%{?suse_version} < 1550
BuildRequires:  python-mock
%endif
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# We don't have real /dev in osc build chroot gh#pyudev/pyudev#404
# %%pytest

%files %{python_files}
%license COPYING
%doc CHANGES.rst README.rst
%{python_sitelib}/pyudev
%{python_sitelib}/pyudev-%{version}*-info

%changelog
