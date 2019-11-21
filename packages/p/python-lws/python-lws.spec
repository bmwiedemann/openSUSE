#
# spec file for package python-lws
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
Name:           python-lws
Version:        1.2.6
Release:        0
Summary:        Spectrogram phase reconstruction package
License:        Apache-2.0
URL:            https://github.com/Jonathan-LeRoux/lws
Source:         https://files.pythonhosted.org/packages/source/l/lws/lws-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
%python_subpackages

%description
Spectrogram phase reconstruction using Local Weighted Sums.

%prep
%setup -q -n lws-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.md
%{python_sitearch}/*

%changelog
