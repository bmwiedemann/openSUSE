#
# spec file for package python-hide-code
#
# Copyright (c) 2020 SUSE LLC.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-hide-code
Version:        0.5.5
Release:        0
License:        MIT
Summary:        A Jupyter notebook extension to hide code, prompts and outputs
Url:            https://github.com/kirbs-/hide_code
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/h/hide-code/hide_code-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module nbconvert >= 5.0}
BuildRequires:  %{python_module notebook >= 5.1}
BuildRequires:  %{python_module pdfkit}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
Requires:       python-nbconvert >= 5.0
Requires:       python-notebook >= 5.1
Requires:       python-pdfkit
Recommends:     jupyter-hide-code = %{version}
Requires:       wkhtmltopdf
BuildArch:      noarch

%python_subpackages

%description
Hide-code is an extension for Jupyter/IPython notebooks to
selectively hide code, prompts and output. Make a notebook a code
free document for exporting or presenting.

This package provides the python module.

%package     -n jupyter-hide-code
Summary:        A Jupyter notebook extension to hide code, prompts and outputs
Requires:       python3-hide-code = %{version}
Requires:       jupyter-nbconvert >= 5.0
Requires:       jupyter-notebook >= 5.1
Obsoletes:      jupyter-hide_code < %{version}
Provides:       jupyter-hide_code = %{version}
Provides:       python-jupyter_hide_code = %{version}
Obsoletes:      python-jupyter_hide_code < %{version}

%description -n jupyter-hide-code
Hide-code is an extension for Jupyter/IPython notebooks to
selectively hide code, prompts and output. Make a notebook a code
free document for exporting or presenting.

This package provides the jupyter notebook extension.

%prep
%autosetup -p1 -n hide_code-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{jupyter_nbextension_install hide_code}

PYTHONPATH=%{buildroot}%{python3_sitelib} jupyter nbextension install hide_code --user --py
PYTHONPATH=%{buildroot}%{python3_sitelib} jupyter nbextension enable hide_code --user --py
PYTHONPATH=%{buildroot}%{python3_sitelib} jupyter serverextension enable hide_code --user --py

for f in ~/.jupyter/*.json ; do
    tdir=$( basename -s .json ${f} )
    install -Dm 644 ${f} %{buildroot}%{_jupyter_confdir}/${tdir}.d/hide_code-serverextension.json
done
for f in ~/.jupyter/nbconfig/*.json ; do
    tdir=$( basename -s .json ${f} )
    install -Dm 644 ${f} %{buildroot}%{_jupyter_nb_confdir}/${tdir}.d/hide_code.json
done

%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{_jupyter_confdir}}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%files -n jupyter-hide-code
%license %{_jupyter_nbextension_dir}/hide_code/LICENSE
%{_jupyter_nbextension_dir}/hide_code/
%config %{_jupyter_nb_notebook_confdir}/hide_code.json
%config %{_jupyter_servextension_confdir}/hide_code-serverextension.json

%changelog
