#
# spec file for package python-thLib
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
Name:           python-thLib
Version:        0.12.2
Release:        0
Summary:        Collection of Python utilities for signal analysis
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://work.thaslwanter.at
Source:         https://files.pythonhosted.org/packages/source/t/thLib/thLib-%{version}.tar.gz
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module statsmodels}
BuildRequires:  %{python_module sympy}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-scikit-image
Requires:       python-scipy
Requires:       python-statsmodels
Requires:       python-sympy
BuildArch:      noarch
%python_subpackages

%description
The thLib package contains functions for working with sound, and for
fitting circles, lines, sine-waves, and exponential decays. For
signal processing, a Savitzky-Golay filter is included, as well as a
demonstration of the calculation of a power spectrum. UI utilities,
and a few useful vector functions (e.g. an implementation of the\
Savitzky-Golay algorithm) round off thLib.

Note: All functions for working with 3D kinematics have been moved into
the new package "scikit-kinematics"!

%prep
%setup -q -n thLib-%{version}
# hidden-file-or-dir
rm docs/_build/html/.buildinfo
# wrong-file-end-of-line-encoding
sed -i 's/\r$//' *.txt
sed -i 's/\r$//' docs/_build/html/_sources/*.txt
sed -i 's/\r$//' docs/_build/html/_static/pygments.css

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{python_expand mkdir -p %{buildroot}%{_docdir}/%{$python_prefix}-thLib
cp -r docs/_build/html %{buildroot}%{_docdir}/%{$python_prefix}-thLib/
cp -r docs/_build/doctrees %{buildroot}%{_docdir}/%{$python_prefix}-thLib/
%fdupes %{buildroot}%{_docdir}/%{$python_prefix}-thLib/
}

%check
# no testsuite found

%files %{python_files}
%doc CHANGES.txt README.txt
%{_docdir}/%{python_prefix}-thLib/html/
%{_docdir}/%{python_prefix}-thLib/doctrees/
%{python_sitelib}/*

%changelog
