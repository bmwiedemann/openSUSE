#
# spec file for package jupyter-widgetsnbextension
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


Name:           jupyter-widgetsnbextension
Version:        3.5.1
Release:        0
Summary:        IPython HTML widgets for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/ipywidgets/tree/master/widgetsnbextension
Source:         https://files.pythonhosted.org/packages/source/w/widgetsnbextension/widgetsnbextension-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook >= 4.4.1
BuildRequires:  python-rpm-macros
BuildRequires:  python3-certifi
BuildRequires:  python3-setuptools
Requires:       jupyter-notebook >= 4.4.1
Requires:       python3-certifi
Provides:       python3-jupyter_widgetsnbextension = %{version}
Obsoletes:      python3-jupyter_widgetsnbextension < %{version}
BuildArch:      noarch

%description
Interactive HTML widgets for Jupyter notebooks.

Requires the corresponding package for your kernel. i.e. Python users
would also install `ipywidgets`. Refer to that package's
documentation for usage instructions.

%prep
%setup -q -n widgetsnbextension-%{version}

%build
%python3_build

%install
%python3_install
%{jupyter_move_config}
%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_jupyter_nbextension_dir}
%fdupes %{buildroot}%{_jupyter_nb_notebook_confdir}

%files
%license LICENSE
%{python3_sitelib}/widgetsnbextension/
%{python3_sitelib}/widgetsnbextension-%{version}-py*.egg-info
%{_jupyter_nbextension_dir}/jupyter-js-widgets/
%config %{_jupyter_nb_notebook_confdir}/widgetsnbextension.json

%changelog
