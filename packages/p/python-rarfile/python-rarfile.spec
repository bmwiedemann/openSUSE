#
# spec file for package python-rarfile
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-rarfile
Version:        4.2
Release:        0
Summary:        RAR Archive Reader for Python
License:        ISC
URL:            https://rarfile.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/r/rarfile/rarfile-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  7zip
BuildRequires:  bsdtar
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx >= 1.3
BuildRequires:  unar
Requires:       bsdtar
Recommends:     unar
BuildArch:      noarch
%python_subpackages

%description
This is a Python module for RAR archive reading. It supports both RAR
2.x and 3.x archives, multi volume archives, Unicode filenames,
password-protected archives, archive and file comments. The archive
parsing and non-compressed files are handled in pure Python code, for
compressed files, the "unrar" utility is run.

%package doc
Summary:        RAR Archive Reader for Python (Documentation)
BuildArch:      noarch

%description doc
Python module for RAR archive reading.

This package contains technical documentation.

%prep
%autosetup -p1 -n rarfile-%{version}

%build
%python_build
%make_build -C doc html
rm doc/_build/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not (test_unrar_tool or test_reading or test_rar3_header_encryption)"

%files %{python_files}
%license LICENSE
%pycache_only %{python_sitelib}/__pycache__/rarfile.*.py*
%{python_sitelib}/rarfile.py*
%{python_sitelib}/rarfile-%{version}-py%{python_version}.egg-info

%files %{python_files doc}
%license LICENSE
%doc doc/_build/html/

%changelog
