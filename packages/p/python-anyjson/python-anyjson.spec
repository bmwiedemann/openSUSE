#
# spec file for package python-anyjson
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
Name:           python-anyjson
Version:        0.3.3
Release:        0
Summary:        Wrapper for the best available JSON implementation available in a common interface
License:        BSD-3-Clause
URL:            https://bitbucket.org/runeh/anyjson
Source:         https://files.pythonhosted.org/packages/source/a/anyjson/anyjson-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Anyjson loads whichever is the fastest JSON module installed and provides
a uniform API regardless of which JSON implementation is used.

Originally part of carrot (http://github.com/ask/carrot/)

%prep
%setup -q -n anyjson-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%doc CHANGELOG README
%{python_sitelib}/anyjson/
%{python_sitelib}/anyjson-%{version}-py*.egg-info

%changelog
