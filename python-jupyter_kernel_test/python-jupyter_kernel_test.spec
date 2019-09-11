#
# spec file for package python-jupyter_kernel_test
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
%define skip_python2 1
%bcond_with     test
Name:           python-jupyter_kernel_test
Version:        0.3
Release:        0
Summary:        Machinery for testing Jupyter kernels via the messaging protocol
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/Calysto/octave_kernel
Source0:        https://files.pythonhosted.org/packages/py3/j/jupyter_kernel_test/jupyter_kernel_test-%{version}-py3-none-any.whl
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module traitlets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jupyter_client >= 4.3.0
Requires:       python-nose
Requires:       python-traitlets
BuildArch:      noarch
%ifpython3
Provides:       jupyter-jupyter_kernel_test = %{version}
%endif
%python_subpackages

%description
jupyter_kernel_test is a tool for testing Jupyter kernels.
It tests kernels for successful code execution and
conformance with the Jupyter Messaging Protocol
(currently 5.0).

%prep
%setup -q -T -c

%build
# Not needed

%install
%python_expand pip%{$python_bin_suffix} install \
    --root %{buildroot} \
    --prefix %{_prefix} \
    --compile \
    %{SOURCE0}

%python_expand cp %{buildroot}%{$python_sitelib}/jupyter_kernel_test-%{version}.dist-info/COPYING.md .

%if %{with test}
%check
%python_exec test_octave_kernel.py
%endif

%files %{python_files}
%license COPYING.md
%{python_sitelib}/jupyter_kernel_test/
%{python_sitelib}/jupyter_kernel_test-%{version}.dist-info

%changelog
