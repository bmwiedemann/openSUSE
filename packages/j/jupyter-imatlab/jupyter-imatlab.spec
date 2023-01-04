#
# spec file for package jupyter-imatlab
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


%define pythons python3
# We can only test if the commercial MATLAB Engine API for Python is installed
%bcond_with  test
Name:           jupyter-imatlab
Version:        0.4
Release:        0
Summary:        Jupyter kernel for MATLAB
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/imatlab/imatlab
Source0:        https://files.pythonhosted.org/packages/py3/i/imatlab/imatlab-%{version}-py3-none-any.whl
Source1:        https://raw.githubusercontent.com/imatlab/imatlab/master/test_imatlab.py
BuildRequires:  fdupes
BuildRequires:  jupyter-ipykernel >= 4.1
BuildRequires:  jupyter-ipython >= 6
BuildRequires:  jupyter-widgetsnbextension >= 1.0
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-plotly
BuildRequires:  unzip
%if %{with test}
BuildRequires:  python3-curses
BuildRequires:  python3-jupyter-kernel-test
%endif
Requires:       jupyter-ipykernel >= 4.1
Requires:       jupyter-ipython >= 6
Requires:       jupyter-widgetsnbextension >= 1.0
Requires:       python3-plotly
Provides:       python3-jupyter_imatlab_kernel = %{version}
Obsoletes:      python3-jupyter_imatlab_kernel < %{version}
Provides:       python3-imatlab = %{version}
BuildArch:      noarch

%description
A Jupyter kernel for MATLAB.

This kernel requires Jupyter with Python 3.5+,
and the MATLAB engine for Python (this release
provides a much better completion API), which
needs to be installed first.

%prep
%setup -q -T -c
cp %{SOURCE1} .

%build
# Make mock MATLAB engine to allow kernel installation.
# See https://github.com/imatlab/imatlab/issues/31
mkdir matlab
echo 'EngineError = MatlabExecutionError = Exception' > matlab/engine.py

%install
%pyproject_install %{SOURCE0}
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m imatlab install --prefix %{buildroot}%{_prefix}
cp %{buildroot}%{python3_sitelib}/imatlab-%{version}.dist-info/LICENSE.txt .
# not available during install, not a proper PEP440 version information -- gh#imatlab/imatlab#65
sed -i '/Requires-Dist: matlabengineforpython.*R/d' \
   %{buildroot}%{python3_sitelib}/imatlab-%{version}.dist-info/METADATA
%fdupes %{buildroot}%{python3_sitelib}

%check
%if %{with test}
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
%pyunittest -v test_imatlab.py
%endif

%files
%license LICENSE.txt
%{python3_sitelib}/imatlab-%{version}.dist-info
%{python3_sitelib}/imatlab/
%{_jupyter_kernel_dir}/imatlab/

%changelog
