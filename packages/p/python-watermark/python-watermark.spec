#
# spec file for package python-watermark
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
Name:           python-watermark
Version:        2.0.2
Release:        0
Summary:        IPython magic function to psystem information
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rasbt/watermark
Source:         https://files.pythonhosted.org/packages/source/w/watermark/watermark-%{version}.tar.gz
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ipython
Provides:       python-jupyter_watermark = %{version}
Obsoletes:      python-jupyter_watermark < %{version}
BuildArch:      noarch
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-watermark = %{version}
%endif
%python_subpackages

%description
An Jupyter magic extension for printing date and time stamps, version numbers,
and hardware information.

%prep
%setup -q -n watermark-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -c "import watermark; print('watermark %s' % watermark.__version__)";
%python_expand ipython-%{$python_bin_suffix} -c "%load_ext watermark";

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/watermark-%{version}-py*.egg-info
%{python_sitelib}/watermark/

%changelog
