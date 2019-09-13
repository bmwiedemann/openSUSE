#
# spec file for package python-ujson
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
Name:           python-ujson
Version:        1.35
Release:        0
Summary:        JSON encoder and decoder for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/esnme/ultrajson
Source:         https://files.pythonhosted.org/packages/source/u/ujson/ujson-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- do_not_remove_build_directory_manually.patch -- https://github.com/esnme/ultrajson/issues/179
Patch0:         do_not_remove_build_directory_manually.patch
Patch1:         no-unittest2.patch
Patch2:         ujson-1.35-fix-for-overflowing-long.patch
Patch3:         ujson-1.35-fix-ordering-of-orderdict.patch
Patch4:         ujson-1.35-sort_keys-segfault.patch
Patch5:         ujson-1.35-standard-handling-of-none.patch
Patch6:         ujson-1.35-test-depricationwarning.patch
Patch7:         ujson-1.35-use-static-where-possible.patch
BuildRequires:  %{python_module blist}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
UltraJSON is a JSON encoder and decoder written in pure C with
bindings for Python 2.5+ and 3. For a different C/C++ JSON
decoder experience please checkout ujson4c_, based on UltraJSON.

%prep
%setup -q -n ujson-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd tests
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python tests.py
}

%files %{python_files}
%doc README.rst
%{python_sitearch}/ujson.*
%{python_sitearch}/ujson-%{version}-py*.egg-info

%changelog
