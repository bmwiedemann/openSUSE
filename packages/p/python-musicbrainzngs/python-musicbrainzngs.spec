#
# spec file for package python-musicbrainzngs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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
# Tests require network connection
%bcond_with    test
Name:           python-musicbrainzngs
Version:        0.6
Release:        0
Summary:        Python bindings for musicbrainz NGS webservice
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://python-musicbrainzngs.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/m/musicbrainzngs/musicbrainzngs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library implements webservice bindings for the Musicbrainz NGS site, also
known as /ws/2.

%prep
%setup -q -n musicbrainzngs-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license COPYING
%doc CHANGES README.rst
%{python_sitelib}/musicbrainzngs/
%{python_sitelib}/musicbrainzngs-%{version}-py*.egg-info

%changelog
