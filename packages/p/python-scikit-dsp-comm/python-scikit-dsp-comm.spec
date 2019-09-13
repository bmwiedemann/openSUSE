#
# spec file for package python-scikit-dsp-comm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-scikit-dsp-comm
Version:        0.0.5
Release:        0
Summary:        DSP and Comm package for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/mwickert/scikit-dsp-comm
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-dsp-comm/scikit-dsp-comm-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/mwickert/scikit-dsp-comm/v%{version}/LICENSE.md
Source100:      python-scikit-dsp-comm-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module tox}
# /SECTION
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-scipy
Recommends:     python-PyAudio
Recommends:     python-pyrtlsdr
BuildArch:      noarch

%python_subpackages

%description
This package is a collection of functions and classes to support
signal processing and communications theory teaching and research.
The foundation for this package is scipy.signal.

%prep
%setup -q -n scikit-dsp-comm-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/sk_dsp_comm/*.txt

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/*

%changelog
