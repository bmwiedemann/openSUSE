#
# spec file for package python-pyocr
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


%define sha f4b068cdf359186bfbed36959c53e9e52e2eda84
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyocr
Version:        0.7.2
Release:        0
Summary:        Python wrapper for OCR engines
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://gitlab.gnome.org/World/OpenPaperwork/pyocr
Source:         https://gitlab.gnome.org/World/OpenPaperwork/pyocr/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools_scm_git_archive}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Recommends:     cuneiform
Recommends:     tesseract-ocr
BuildArch:      noarch
%python_subpackages

%description
PyOCR is an optical character recognition (OCR) tool wrapper for python.
That is, it helps using various OCR tools from a Python program.

%prep
%setup -q -n pyocr-%{version}-%{sha}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc AUTHORS ChangeLog README.md
%{python_sitelib}/*

%changelog
