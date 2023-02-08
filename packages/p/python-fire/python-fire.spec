#
# spec file for package python-fire
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


%define skip_python2 1
Name:           python-fire
Version:        0.5.0
Release:        0
Summary:        A library for automatically generating command line interfaces
License:        Apache-2.0
URL:            https://github.com/google/python-fire
Source:         https://files.pythonhosted.org/packages/source/f/fire/fire-%{version}.tar.gz
# Based on https://github.com/google/python-fire/pull/265/files
Patch0:         python-fire-no-mock.patch
Patch1:         support-python-311.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       python-termcolor
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Levenshtein}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module termcolor}
# /SECTION
%python_subpackages

%description
Python Fire is a library for automatically generating command line
interfaces (CLIs) from a Python object.

%prep
%autosetup -p1 -n fire-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
