#
# spec file for package python-ligotimegps
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-ligotimegps
Version:        2.0.1
Release:        0
License:        GPL-3.0
Summary:        A pure-python version of lalLIGOTimeGPS
Url:            https://github.com/gwpy/ligotimegps
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/l/ligotimegps/ligotimegps-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module pytest-runner}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
This module provides a pure-python version of the `LIGOTimeGPS` class,
used to represent GPS times (number of seconds elapsed since GPS
epoch) with nanoseconds precision.

This module is primarily for use as a drop-in replacement for the
'official' `lal.LIGOTimeGPS` class (provided by the SWIG-python
bindings of [LAL](//wiki.ligo.org/DASWG/LALSuite)) for use on those
environments where LAL is not available, or building LAL is
unnecessary for the application (e.g. testing).

The code provided here is much slower than the C-implementation
provided by LAL, so if you really care about performance, don't use
this module.

%prep
%setup -q -n ligotimegps-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
