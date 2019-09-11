#
# spec file for package python-rfc6266
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


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rfc6266
Version:        0.0.4
Release:        0
Summary:        Parser-generator for Content-Disposition headers
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/g2p/rfc6266
Source:         https://files.pythonhosted.org/packages/source/r/rfc6266/rfc6266-%{version}.tar.gz
Source1:        COPYING.LESSER
# PATCH-FIX-UPSTREAM 0000-NullHandler.patch -- https://github.com/g2p/rfc6266/issues/12
Patch0:         0000-NullHandler.patch
BuildRequires:  %{python_module LEPL}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-LEPL
BuildArch:      noarch
%python_subpackages

%description
This module parses and generates HTTP Content-Disposition headers.
These headers are used when getting resources for download;
they provide a hint of whether the file should be downloaded,
and of what filename to use when saving.

%prep
%setup -q -n rfc6266-%{version}
cp %{SOURCE1} .
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README
%license COPYING.LESSER
%{python_sitelib}/*

%changelog
