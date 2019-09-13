#
# spec file for package python-pyacoustid
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
Name:           python-pyacoustid
Version:        1.1.7
Release:        0
Summary:        Bindings for Chromaprint acoustic fingerprinting and the Acoustid API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sampsyo/pyacoustid
Source:         https://files.pythonhosted.org/packages/source/p/pyacoustid/pyacoustid-%{version}.tar.gz
BuildRequires:  %{python_module audioread}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-audioread
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Chromaprint and Acoustid for Python

Chromaprint and its associated Acoustid Web service make up a
high-quality, open-source acoustic fingerprinting system. This package provides
Python bindings for both the fingerprinting algorithm library, which is written
in C but portable, and the Web service, which provides fingerprint lookups.

%prep
%setup -q -n pyacoustid-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
