#
# spec file for package python-css-parser
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
Name:           python-css-parser
Version:        1.0.4
Release:        0
Summary:        CSS related utilities (parsing, serialization, etc) for python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ebook-utils/css-parser
Source:         https://github.com/ebook-utils/css-parser/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         disable-online-tests.patch
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module setuptools}
Requires:       python-chardet
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
CSS related utilities (parsing, serialization, etc) for python

A fork of the cssutils project based on version 1.0.2. This fork includes general bug fixes and extensions specific to editing and working with ebooks.

The main python source code has been modified so that it will run without further conversion on both Python >= 2.7 and Python 3.X without any further modules required. All required modifications are handled local to each file

%prep
%setup -q -n css-parser-%{version}
sed -i "1d" src/css_parser/{parse,codec,sac,serialize,scripts/csscapture,_codec2,errorhandler,scripts/cssparse,_codec3,scripts/csscombine,tokenize2,version,encutils/__init__,__init__}.py # Fix non-executable scripts
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license COPYING COPYING.LESSER
%doc README.md
%{python_sitelib}/css_parser/
%{python_sitelib}/css_parser-%{version}-py*.egg-info/
%pycache_only %{python_sitelib}/css_parser/__pycache__/version.*

%changelog
