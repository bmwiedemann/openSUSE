#
# spec file for package jupyter-hide_code
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


Name:           jupyter-hide_code
Version:        0.5.2
Release:        0
Summary:        Jupyter notebook extension to hide code, prompts and outputs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kirbs-/hide_code
Source:         https://files.pythonhosted.org/packages/source/h/hide_code/hide_code-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       jupyter-nbconvert >= 5.0
Requires:       jupyter-notebook >= 5.1
Requires:       python3-pdfkit
Requires(post): jupyter-nbconvert >= 5.0
Requires(post): jupyter-notebook >= 5.1
Requires(post): python3-pdfkit
Requires(preun): jupyter-nbconvert >= 5.0
Requires(preun): jupyter-notebook >= 5.1
Requires(preun): python3-pdfkit
Provides:       python-jupyter_hide_code = %{version}
Obsoletes:      python-jupyter_hide_code <= %{version}
Provides:       python3-hide_code = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  jupyter-nbconvert >= 5.0
BuildRequires:  jupyter-notebook >= 5.1
BuildRequires:  python3-pdfkit
# /SECTION

%description
Hide_code is an extension for Jupyter/IPython notebooks to
selectively hide code, prompts and output. Make a notebook a code
free document for exporting or presenting.

%prep
%setup -q -n hide_code-%{version}
rm hide_code.egg-info/.DS_Store

%build
%python3_build

%install
%python3_install

%{jupyter_nbextension_install hide_code}
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%post
%{jupyter_serverextension_enable hide_code}
%{jupyter_nbextension_enable hide_code}

%preun
%{jupyter_serverextension_disable hide_code}
%{jupyter_nbextension_disable hide_code}

%files
%doc README.rst
%license hide_code/LICENSE.txt
%{python3_sitelib}/hide_code-*-py*.egg-info
%{python3_sitelib}/hide_code/
%{_jupyter_nbextension_dir}/hide_code/

%changelog
