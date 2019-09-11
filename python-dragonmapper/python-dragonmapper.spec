#
# spec file for package python-dragonmapper
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dragonmapper
Version:        0.2.6
Release:        0
License:        MIT
Summary:        Identification and conversion functions for Chinese text processing
Url:            https://github.com/tsroten/dragonmapper
Group:          Development/Languages/Python
Source:         https://github.com/tsroten/dragonmapper/archive/v%{version}.tar.gz#/dragonmapper-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module hanzidentifier >= 1.0.2}
BuildRequires:  %{python_module zhon >= 1.1.3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-hanzidentifier >= 1.0.2
Requires:       python-zhon >= 1.1.3
BuildArch:      noarch

%python_subpackages

%description
Identification and conversion functions for Chinese text processing.

%prep
%setup -q -n dragonmapper-%{version}
mv dragonmapper/tests/test-hanzi.py dragonmapper/tests/test_hanzi.py
mv dragonmapper/tests/test-transcriptions.py dragonmapper/tests/test_transcriptions.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest dragonmapper/tests/

%files %{python_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
