#
# spec file for package python-PyPDF2
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


%{?sle15_python_module_pythons}
Name:           python-PyPDF2
Version:        2.11.1
Release:        0
Summary:        PDF toolkit
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/py-pdf/PyPDF2
Source:         https://github.com/py-pdf/PyPDF2/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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
%setup -q -n PyPDF2-%{version}
#remove unwanted shebang
sed -i '/^#!/ d' PyPDF2/pagerange.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
chmod a-x CHANGELOG.md LICENSE README.md

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/PyPDF2
%{python_sitelib}/[Pp]y[Pp][Dd][Ff]2-%{version}*-info

%changelog
