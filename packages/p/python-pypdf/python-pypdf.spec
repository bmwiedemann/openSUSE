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
Version:        6.19.0
Release:        0
Summary:        PDF toolkit
License:        BSD-3-Clause
URL:            https://github.com/py-pdf/pypdf
Source0:        https://github.com/py-pdf/pypdf/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python3-PyPDF2 = %version-%release
Obsoletes:      python3-PyPDF2 < %version-%release
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module fonttools}
BuildRequires:  %{python_module pytest-socket}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /SECTION
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
%autosetup -p1 -n pypdf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="testeverythingexcept"
%if 0%{?suse_version} < 1699
# test_font_old_fonttools_substitution: workaround to test wannabe SLFO fonttools on Factory fonttools, fails in Leap because upstream does not like conditional skips
# https://github.com/py-pdf/pypdf/pull/4050
donttest+=" or test_font_old_fonttools_substitution"
%endif
# flaky tests
donttest+=" or test_flatedecode__decode_png_prediction__speed"
donttest+=" or test_decompress__fallback__speed"

# Skip network tests, or tests that require large sample files
%pytest -m "not (enable_socket or samples)" -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md
%{python_sitelib}/pypdf
%{python_sitelib}/pypdf-%{version}.dist-info

%changelog
