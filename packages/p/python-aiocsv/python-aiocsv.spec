#
# spec file for package python-aiocsv
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-aiocsv
Version:        1.4.0
Release:        0
Summary:        Asynchronous CSV reading/writing in Python
License:        MIT
URL:            https://github.com/MKuranowski/aiocsv
Source:         https://github.com/MKuranowski/aiocsv/archive/refs/tags/v%{version}.tar.gz#/aiocsv-%{version}.tar.gz
BuildRequires:  %{python_module aiofiles}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions
%python_subpackages

%description
Asynchronous CSV reading and writing

AsyncReader & AsyncDictReader accept any object that has a read(size: int) coroutine,
which should return a string.

AsyncWriter & AsyncDictWriter accept any object that has a write(b: str) coroutine.

Reading is implemented using a custom CSV parser, which should behave exactly like
the CPython parser.

Writing is implemented using the synchronous csv.writer and csv.DictWriter objects -
the serializers write data to a StringIO, and that buffer is then rewritten to the
underlying asynchronous file.

%prep
%autosetup -p1 -n aiocsv-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
rm %{buildroot}%{$python_sitearch}/aiocsv/_parser.c
sed -i '/_parser.c/d' %{buildroot}%{$python_sitearch}/aiocsv-%{version}.dist-info/RECORD
%fdupes %{buildroot}%{$python_sitearch}
}

%check
# https://github.com/MKuranowski/aiocsv/issues/33
%pytest_arch -k 'not test_parsing_weird_quotes_nonnumeric'

%files %{python_files}
%doc readme.md
%license LICENSE
%{python_sitearch}/aiocsv
%{python_sitearch}/aiocsv-%{version}.dist-info

%changelog
