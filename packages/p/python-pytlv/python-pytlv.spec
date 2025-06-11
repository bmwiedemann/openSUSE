#
# spec file for package python-pytlv
#
# Copyright (c) 2025 SUSE LLC
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


%define skip_python2 1
Name:           python-pytlv
Version:        0.71
Release:        0
Summary:        TLV(tag length value) data parser
License:        LGPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/timgabets/pytlv
Source:         https://files.pythonhosted.org/packages/source/p/pytlv/pytlv-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover pytlv/ -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytlv
%{python_sitelib}/pytlv-%{version}.dist-info

%changelog
