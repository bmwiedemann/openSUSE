#
# spec file for package python-uproot
#
# Copyright (c) 2022 SUSE LLC
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


# No numpy for py3.6
%define skip_python36 1
%global modname uproot
Name:           python-uproot
Version:        4.3.4
Release:        0
Summary:        ROOT I/O in pure Python and Numpy
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scikit-hep/uproot4
Source0:        https://files.pythonhosted.org/packages/source/u/uproot/uproot-%{version}.tar.gz
Source1:        tests.tar.xz
# PATCH-FEATURE-OPENSUSE uproot-use-packaging-module.patch badshah400@gmail.com -- Use packaging module directly instead of calling it via setup.extern; the latter does not work on openSUSE directly
Patch0:         uproot-use-packaging-module.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.13.1
Requires:       python-packaging
Recommends:     python-awkward
Suggests:       python-lz4
Suggests:       python-zstandard
Suggests:       python-xrootd
Suggests:       python-pandas
Suggests:       python-cupy
Suggests:       python-boost-histogram
Suggests:       python-hist
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module awkward}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module numpy >= 1.13.1}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-hep-testdata}
BuildRequires:  %{python_module xxhash}
BuildRequires:  %{python_module boost-histogram >= 0.13 if (%python-base without python2-base)}
# /SECTION
%python_subpackages

%description
Uproot is a reader and a writer of the ROOT file format using only Python and
Numpy. Unlike the standard C++ ROOT implementation, Uproot is only an I/O
library, primarily intended to stream data into machine learning libraries in
Python. It uses Numpy to cast blocks of data from the ROOT file as Numpy
arrays.

%prep
%autosetup -p1 -n %{modname}-%{version}
%setup -q -D -T -a 1 -n %{modname}-%{version}
# gh#scikit-hep/uproot4#396
sed -i '/def test/ i @pytest.mark.network' tests/test_0220-contiguous-byte-ranges-in-http.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
if [ $(getconf LONG_BIT) -eq 32 ]; then
# pandas tests assume 64bit types
skiptests32=("-k" "not (test_jagged_pandas or test_pandas_vector_TLorentzVector or test_iterate_pandas_2 or test_function_iterate_pandas_2 or test_0430)")
fi
%pytest -rfEs -m "not network" "${skiptests32[@]}"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
