#
# spec file for package python-python-cjson
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
Name:           python-python-cjson
Version:        1.2.2
Release:        0
Summary:        C-accelerated JSON encoder/decoder for Python
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/AGProjects/python-cjson
Source:         https://files.pythonhosted.org/packages/source/p/python-cjson/python-cjson-%{version}.tar.gz
# https://github.com/AGProjects/python-cjson/issues/6
Patch0:         py3.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
JSON (JavaScript Object Notation) is a text-based data exchange
format.

The module is written in C and it is up to 250 times faster when compared to
the other Python JSON implementations which are written directly in Python.
This speed gain varies with the complexity of the data and the operation and is
the the range of 10-200 times for encoding operations and in the range of
100-250 times for decoding operations.

%prep
%setup -q -n python-cjson-%{version}
cp jsontest.py jsontest2.py
%if %{with python2}
cp cjson.c cjson2.c
%endif
%patch0 -p1
cp cjson.c cjson3.c

cp jsontest.py jsontest3.py
# Workaround dict order differences on Python 3.4
if [ %{python3_bin_suffix} = '3.4' ]; then
  sed -i 's/\(testWriteComplexArray\|testWriteSmallObject\)/_\1/' jsontest3.py
fi

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%{python_expand #
rm cjson.c
if [ "$python" == "python2" ]; then
  ln -s cjson2.c cjson.c
else
  ln -s cjson3.c cjson.c
fi
%{$python_build}
}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand # run test
if [ "$python" == "python2" ]; then
  python_major_ver=2
else
  python_major_ver=3
fi
PYTHONPATH=%{buildroot}%{$python_sitearch} $python jsontest${python_major_ver}.py -v
}

%files %{python_files}
%doc ChangeLog README
%license LICENSE
%{python_sitearch}/*

%changelog
