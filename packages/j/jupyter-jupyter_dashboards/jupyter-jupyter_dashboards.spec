#
# spec file for package jupyter-jupyter_dashboards
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


%bcond_without  test
Name:           jupyter-jupyter_dashboards
Version:        0.7.0
Release:        0
Summary:        Extension for using Jupyter Notebooks as dynamic dashboards
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/dashboards
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_dashboards/jupyter_dashboards-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook >= 4.0
BuildRequires:  python-rpm-macros
BuildRequires:  python3-certifi
BuildRequires:  python3-setuptools
Requires:       jupyter-notebook >= 4.0
Requires:       python3-certifi
Requires(post): jupyter-notebook >= 4.0
Requires(preun): jupyter-notebook >= 4.0
Provides:       python3-jupyter_dashboards = %{version}
Obsoletes:      python3-jupyter_dashboards <= %{version}
BuildArch:      noarch

%description
This package adds the following features to Jupyter Notebook:

* Dashboard layout mode for arranging notebook cell outputs in a grid-like fashion
* Dashboard view mode for interacting with an assembled dashboard within the Jupyter Notebook
* Ability to share notebooks with dashboard layout metadata in them with other Jupyter Notebook users

%prep
%setup -q -n jupyter_dashboards-%{version}
for f in .editorconfig .gitattributes .github .gitignore .travis.yml ; do
rm -rf jupyter_dashboards/nbextension/notebook/bower_components/*/$f
rm -rf jupyter_dashboards/nbextension/notebook/bower_components/*/*/$f
done

# rpmlint: wrong-script-end-of-line-encoding
sed -i 's/\r$//' jupyter_dashboards/nbextension/notebook/bower_components/gridstack/Gruntfile.js

# rpmlint: script-without-shebang
chmod a-x jupyter_dashboards/nbextension/notebook/bower_components/gridstack/Gruntfile.js
chmod a-x jupyter_dashboards/nbextension/notebook/bower_components/gridstack/dist/gridstack.js
chmod a-x jupyter_dashboards/nbextension/notebook/bower_components/gridstack/package.json
chmod a-x jupyter_dashboards/nbextension/notebook/bower_components/jquery-ui/ui/.jshintrc

# rpmlint: non-executable-script
sed -i -e '/^#!\//, 1d' jupyter_dashboards/nbextension/notebook/bower_components/lodash/test/remove.js
sed -i -e '/^#!\//, 1d' jupyter_dashboards/nbextension/notebook/bower_components/lodash/test/saucelabs.js

# rpmlint: python-bytecode-wrong-magic-value
rm -rf jupyter_dashboards/__pycache__/

%build
%python3_build

%install
%python3_install

%{jupyter_nbextension_install jupyter_dashboards}
%{fdupes %{buildroot}%{python3_sitelib} %{buildroot}%{_jupyter_nbextension_dir}}

%post
%{jupyter_nbextension_enable jupyter_dashboards}

%preun
%{jupyter_nbextension_disable jupyter_dashboards}

%if %{with test}
%check
python3 setup.py test
%endif

%files
%license LICENSE.md
%{_bindir}/jupyter-dashboards
%{python3_sitelib}/jupyter_dashboards/
%{python3_sitelib}/jupyter_dashboards-%{version}-py*.egg-info
%{_jupyter_nbextension_dir}/jupyter_dashboards/

%changelog
