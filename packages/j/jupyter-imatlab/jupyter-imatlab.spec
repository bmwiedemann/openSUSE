#
# spec file for package jupyter-imatlab
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


%bcond_without  test
Name:           jupyter-imatlab
Version:        0.4
Release:        0
Summary:        Jupyter kernel for MATLAB
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/imatlab/imatlab
Source0:        https://files.pythonhosted.org/packages/py3/i/imatlab/imatlab-%{version}-py3-none-any.whl
BuildRequires:  fdupes
BuildRequires:  jupyter-ipykernel >= 4.1
BuildRequires:  jupyter-ipython >= 6
BuildRequires:  jupyter-widgetsnbextension >= 1.0
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-plotly
BuildRequires:  unzip
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

%build
# Make mock MATLAB engine to allow kernel installation.
# See https://github.com/imatlab/imatlab/issues/31
mkdir matlab
echo 'EngineError = MatlabExecutionError = Exception' > matlab/engine.py

%install
# use --no-deps because it looks for MATLAB itself
pip%{python3_bin_suffix} install --root %{buildroot} --prefix %{_prefix} --no-compile --no-deps %{SOURCE0}

PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m imatlab install --prefix %{buildroot}%{_prefix}

%files
%{python3_sitelib}/imatlab-%{version}.dist-info
%license %{python3_sitelib}/imatlab-%{version}.dist-info/LICENSE.txt
%{python3_sitelib}/imatlab/
%{_jupyter_kernel_dir}/imatlab/

%changelog
