#
# spec file for package python-rise
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-rise
Version:        5.7.1
Release:        0
Summary:        Jupyter/IPython Slideshow Extension
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/damianavila/RISE
Source:         https://files.pythonhosted.org/packages/source/r/rise/rise-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-rise = %{version}
Requires:       python-certifi
Requires:       python-notebook >= 5.5.0
Provides:       python-jupyter_rise = %{version}-%{release}
Obsoletes:      python-jupyter_rise < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
RISE produces live HTML-based slideshows.

A notebook can be rendered as a Reveal.js-based slideshow,
where you can execute code or show to the audience whatever you can
show/do inside the notebook itself (but in a "slidy" way).

This package provides the python module.

%package     -n jupyter-rise
Summary:        Jupyter/IPython Slideshow Extension
Group:          Development/Languages/Python
Requires:       jupyter-notebook >= 5.5.0
Requires:       python3-hide-code >= 0.5.5

%description -n jupyter-rise
RISE produces live HTML-based slideshows.

A notebook can be rendered as a Reveal.js-based slideshow,
where you can execute code or show to the audience whatever you can
show/do inside the notebook itself (but in a "slidy" way).

This package provides the jupyter notebook extension.

%prep
%setup -q -n rise-%{version}
find . -type f -exec chmod a-X {} \;
find . -name '.travis.yml' -delete

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%jupyter_move_config

%files %{python_files}
%doc README.md
%license LICENSE.md
%license %{python_sitelib}/rise/static/reveal.js/LICENSE
%doc %{python_sitelib}/rise/static/README.md
%doc %{python_sitelib}/rise/static/reveal.js/README.md
%doc %{python_sitelib}/rise/static/reveal.js-chalkboard/README.md
%{python_sitelib}/rise/
%{python_sitelib}/rise-%{version}-py*.egg-info

%files -n jupyter-rise
%license LICENSE.md
%{_jupyter_nbextension_dir}/rise/
%config %{_jupyter_nb_notebook_confdir}/rise.json

%changelog
