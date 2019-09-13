#
# spec file for package jupyter-jupyter-full-width
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


Name:           jupyter-jupyter-full-width
Version:        1.2.0
Release:        0
Summary:        A button to allow Jupyter to use the full browser width
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/JoaoFelipe/JupyterFullWidth
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_full_width/jupyter_full_width-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       jupyter-notebook >= 5.1
Requires(post): jupyter-notebook >= 5.1
Requires(preun): jupyter-notebook >= 5.1
Provides:       python3-jupyter_full_width = %{version}
Obsoletes:      python3-jupyter_full_width <= %{version}
Provides:       python3-jupyter-full-width = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  jupyter-notebook >= 5.1
# /SECTION

%description
This extension adds a button that makes notebooks use the full
browser width.

%prep
%setup -q -n jupyter_full_width-%{version}

%build
%python3_build

%install
%python3_install

%{jupyter_nbextension_install full_width}
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%post
%{jupyter_nbextension_enable full_width}

%preun
%{jupyter_nbextension_disable full_width}

%files
%doc full_width/jupyter/readme.md
%{python3_sitelib}/jupyter_full_width-*-py*.egg-info
%{python3_sitelib}/full_width/
%{_jupyter_nbextension_dir}/full_width/

%changelog
