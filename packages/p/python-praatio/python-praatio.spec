#
# spec file for package python-praatio
#
# Copyright (c) 2020 SUSE LLC
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
%define         skip_python2 1
Name:           python-praatio
Version:        4.1.0
Release:        0
Summary:        A library for working with praat
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/timmahrt/praatIO
Source0:        https://github.com/timmahrt/praatIO/archive/v%{version}.tar.gz#/praatIO-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     praat
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch
%python_subpackages

%package -n %{name}-doc
Summary:        Documentation files for praatio
Group:          Documentation/HTML
Provides:       %{python_module praatio-doc = %{version}}

%description -n %{name}-doc
HTML Documentation and examples for praatio.

%description
A library for working with praat, time aligned audio transcripts, and
audio files.

Praat uses a file format called textgrids, which are time aligned
speech transcripts. This library also provides utilities are to work
with  transcripts and associated audio file and some other tools for
use with praat.

%prep
%setup -q -n praatIO-%{version}
sed -i 's/\r$//' examples/files/mary.TextGrid

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest examples/test/*.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%files -n %{name}-doc
%license LICENSE
%doc README.md docs/* examples tutorials

%changelog
