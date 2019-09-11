#
# spec file for package python-pytlv
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

%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytlv
Version:        0.71
Release:        0
Summary:        TLV(tag length value) data parser
License:        LGPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/timgabets/pytlv
Source:         https://files.pythonhosted.org/packages/source/p/pytlv/pytlv-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
TLV (tag length value) data parser, especially useful for EMV tag parsing.

%prep
%setup -q -n pytlv-%{version}
sed -i -e '/^#!\//, 1d' pytlv/{TLV.py,tests.py}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover pytlv/ -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
