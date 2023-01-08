#
# spec file for package python-widgetsnbextension
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


%define jupver 8.0.5
Name:           python-widgetsnbextension
Version:        4.0.5
Release:        0
Summary:        Jupyter interactive widgets for Jupyter Notebook
License:        BSD-3-Clause AND MIT
URL:            https://github.com/jupyter-widgets/ipywidgets/tree/master/python/widgetsnbextension
Source:         https://files.pythonhosted.org/packages/source/w/widgetsnbextension/widgetsnbextension-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module jupyter-packaging}
BuildRequires:  %{python_module notebook >= 4.4.1}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-widgetsnbextension = %{version}
Requires:       python-notebook >= 4.4.1
Provides:       python-jupyter_widgetsnbextension = %{version}-%{release}
Obsoletes:      python-jupyter_widgetsnbextension < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
This package makes Jupyter widgets available in the classic Jupyter Notebook.
This package provides the necessary JavaScript controls in the Jupyter
Notebook that communicate with the widget objects in the kernel.

Install the corresponding Jupyter widgets package into your kernel, i.e.,
IPython users would install ipywidgets into their kernel.

%package -n jupyter-widgetsnbextension
Summary:        Jupyter interactive widgets for Jupyter Notebook - Jupyter Files
Requires:       python3-widgetsnbextension = %{version}
Provides:       jupyter-jupyter-js-widgets = %{jupver}
Provides:       jupyter-jupyter-jupyter-widgets-notebook-manager = %{jupver}

%description  -n jupyter-widgetsnbextension
This package makes Jupyter widgets available in the classic Jupyter Notebook.
It provides the Jupyter configuration files.

%prep
%setup -q -n widgetsnbextension-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
export JUPYTER_CONFIG_DIR=%{buildroot}%{_jupyter_confdir}
%{python_expand # no $python tests available
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import widgetsnbextension'
jupyter-%{$python_bin_suffix} nbextension list 2>&1 | grep 'jupyter-js-widgets.*enabled'
}
rm -f %{buildroot}%{_jupyter_confdir}migrated

%files %{python_files}
%license LICENSE
%{python_sitelib}/widgetsnbextension
%{python_sitelib}/widgetsnbextension-%{version}*-info

%files -n jupyter-widgetsnbextension
%license LICENSE
%{_jupyter_config} %{_jupyter_nb_notebook_confdir}/widgetsnbextension.json
%dir %{_jupyter_nbextension_dir}/jupyter-js-widgets
%{_jupyter_nbextension_dir}/jupyter-js-widgets/extension.js
%{_jupyter_nbextension_dir}/jupyter-js-widgets/extension.js.LICENSE.txt
%{_jupyter_nbextension_dir}/jupyter-js-widgets/extension.js.map

%changelog
