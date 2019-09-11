#
# spec file for package python-rencode
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
Name:           python-rencode
Version:        1.0.6
Release:        0
Summary:        Web safe object pickling/unpickling
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/aresch/rencode
Source0:        https://github.com/aresch/rencode/archive/v%{version}.tar.gz
Source1:        %{name}.changes
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings. Python2 version of package

%prep
%setup -q -n rencode-%{version}
# to "avoid python-bytecode-inconsistent-mtime" warnings
FAKE_TIMESTAMP=$(LC_ALL=C date -u -r %{SOURCE1} +%%y%%m%%d%%H%%M)
find . -name '*.py' -exec touch -mat $FAKE_TIMESTAMP {} \;
# do not use O3
sed -i -e '/extra_compile_args/d' setup.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}/rencode

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python tests/test_rencode.py

%files %{python_files}
%license COPYING
%{python_sitearch}/rencode
%{python_sitearch}/rencode-%{version}-py%{python_version}.egg-info

%changelog
