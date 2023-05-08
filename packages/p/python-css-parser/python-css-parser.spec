#
# spec file for package python-css-parser
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-css-parser
Version:        1.0.9
Release:        0
Summary:        CSS related utilities (parsing, serialization, etc) for python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ebook-utils/css-parser
Source:         https://github.com/ebook-utils/css-parser/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module setuptools}
Requires:       python-chardet
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
CSS related utilities (parsing, serialization, etc) for python

A fork of the cssutils project based on version 1.0.2. This fork
includes general bug fixes and extensions specific to editing and
working with ebooks.

The main python source code has been modified so that it will run
without further conversion on both Python >= 2.7 and Python 3.X without
any further modules required. All required modifications are handled
local to each file

%prep
%autosetup -p1 -n css-parser-%{version}

sed -i "1d" src/css_parser/{parse,codec,sac,serialize,scripts/csscapture,_codec2,errorhandler,scripts/cssparse,_codec3,scripts/csscombine,tokenize2,version,encutils/__init__,__init__}.py # Fix non-executable scripts

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%license COPYING COPYING.LESSER
%doc README.md
%{python_sitelib}/css_parser
%{python_sitelib}/css_parser-%{version}*-info/

%changelog
