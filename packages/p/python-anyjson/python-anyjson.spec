#
# spec file for package python-anyjson
#
# Copyright (c) 2022 SUSE LLC
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
%define maj_version 0.3
Name:           python-anyjson
Version:        0.3.3+git.1298315003.7bb1d18
Release:        0
Summary:        Provide the best available JSON implementation available
License:        BSD-3-Clause
URL:            https://bitbucket.org/runeh/anyjson
# Currently the official upstream is dead, trying to send patches to
# https://github.com/kennethreitz-archive/anyjson
Source:         anyjson-%{version}.tar.gz
# PATCH-FIX-UPSTREAM port_to_py3k.patch gh#kennethreitz-archive/anyjson#2 mcepl@suse.com
# port to py3k and avoid nose (replace with pytest)
Patch0:         port_to_py3k.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Anyjson loads whichever is the fastest JSON module installed and provides
a uniform API regardless of which JSON implementation is used.

Originally part of carrot (https://github.com/ask/carrot/)

%prep
%setup -q -n anyjson-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG README
%{python_sitelib}/anyjson/
%{python_sitelib}/anyjson-%{maj_version}-py*.egg-info

%changelog
