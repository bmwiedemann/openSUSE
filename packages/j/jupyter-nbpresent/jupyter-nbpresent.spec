#
# spec file for package jupyter-nbpresent
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


Name:           jupyter-nbpresent
Version:        3.0.0
Release:        0
Summary:        Slide generator for Jupyter Notebooks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Anaconda-Platform/nbpresent
Source:         https://files.pythonhosted.org/packages/source/n/nbpresent/nbpresent-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       jupyter-notebook
Requires(post): jupyter-notebook
Requires(preun): jupyter-notebook
Recommends:     jupyter-nbbrowserpdf
Provides:       python3-jupyter_nbpresent = %{version}
Obsoletes:      python3-jupyter_nbpresent <= %{version}
Provides:       python3-nbpresent = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-coverage
BuildRequires:  python3-nose
BuildRequires:  python3-requests
# /SECTION

%description
This module remixes Jupyter Notebooks into interactive slideshows.

%prep
%setup -q -n nbpresent-%{version}

%build
%python3_build

%install
%python3_install
chmod a-x %{buildroot}%{python3_sitelib}/nbpresent/tasks/*.py

%{jupyter_nbextension_install nbpresent}
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%post
%{jupyter_nbextension_enable nbpresent}

%preun
%{jupyter_nbextension_disable nbpresent}

%files
%doc README.md README.rst
%license LICENSE
%{python3_sitelib}/nbpresent-*-py*.egg-info
%{python3_sitelib}/nbpresent/
%{_bindir}/nbpresent
%{_jupyter_nbextension_dir}/nbpresent/

%changelog
