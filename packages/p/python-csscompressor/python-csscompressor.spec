#
# spec file for package python-csscompressor
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
Name:           python-csscompressor
Version:        0.9.5
Release:        0
Summary:        A python port of YUI CSS Compressor
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/sprymix/csscompressor
Source:         https://files.pythonhosted.org/packages/source/c/csscompressor/csscompressor-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Almost exact python port of YUI CSS Compressor.

%prep
%setup -q -n csscompressor-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{$python_sitelib} py.test-%{$python_bin_suffix} -v csscompressor/tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
