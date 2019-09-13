#
# spec file for package jupyter-rise
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


Name:           jupyter-rise
Version:        5.5.1
Release:        0
Summary:        Jupyter Slideshow Extension
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            http://github.com/damianavila/RISE
Source:         https://files.pythonhosted.org/packages/source/r/rise/rise-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook >= 5.5.0
BuildRequires:  python-rpm-macros
BuildRequires:  python3-certifi
BuildRequires:  python3-setuptools
Provides:       python3-jupyter_rise = %{version}
Obsoletes:      python3-jupyter_rise < %{version}
Provides:       python3-rise = %{version}
BuildArch:      noarch

%description
RISE produces live HTML-based slideshows.

A notebook can be rendered as a Reveal.js-based slideshow,
where you can execute code or show to the audience whatever you can
show/do inside the notebook itself (but in a "slidy" way).

%prep
%setup -q -n rise-%{version}

%build
%python3_build

%install
%python3_install
rm %{buildroot}%{python3_sitelib}/rise/static/reveal.js/.travis.yml
rm %{buildroot}%{python3_sitelib}/rise/static/reveal.js/.npmignore

%{jupyter_move_config}
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%files
%doc README.md
%license LICENSE.md
%license %{python3_sitelib}/rise/static/reveal.js/LICENSE
%doc %{python3_sitelib}/rise/static/README.md
%doc %{python3_sitelib}/rise/static/reveal.js/README.md
%doc %{python3_sitelib}/rise/static/reveal.js-chalkboard/README.md
%{python3_sitelib}/rise/
%{python3_sitelib}/rise-%{version}-py*.egg-info
%{_jupyter_nbextension_dir}/rise/
%config %{_jupyter_nb_notebook_confdir}/rise.json

%changelog
