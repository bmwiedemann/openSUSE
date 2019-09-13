#
# spec file for package python-cyordereddict
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
Name:           python-cyordereddict
Version:        1.0.0
Release:        0
Summary:        Faster Cython implementation of Python's OrderedDict
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/shoyer/cyordereddict
Source:         https://files.pythonhosted.org/packages/source/c/cyordereddict/cyordereddict-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The Python standard library's OrderedDict ported to Cython. A drop-in
replacement that is 2-6x faster.

%prep
%setup -q -n cyordereddict-%{version}
cp -r python2 python_%{python2_bin_suffix}
cp -r python3 python_%{python3_bin_suffix}

# always regenerate cython files
sed -i -e "s:use_cython = is_dev or '--cython' in sys.argv or '--with-cython' in sys.argv:use_cython = True:g" setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec -m nose

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitearch}/*

%changelog
