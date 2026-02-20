#
# spec file for package python-pypdf
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-pypdf
Version:        6.7.1
Release:        0
Summary:        PDF toolkit
License:        BSD-3-Clause
URL:            https://github.com/py-pdf/pypdf
Source0:        https://github.com/py-pdf/pypdf/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Provides:       python3-PyPDF2 = %version-%release
Obsoletes:      python3-PyPDF2 < %version-%release
BuildArch:      noarch

%python_subpackages

%description
A Pure-Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encrypting and decrypting PDF files.

By being Pure-Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.

%prep
%autosetup -n pypdf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no checks possible as large pdf downloaded from the internet are necessary
%check
exit 0

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md
%{python_sitelib}/pypdf
%{python_sitelib}/pypdf-%{version}.dist-info

%changelog
