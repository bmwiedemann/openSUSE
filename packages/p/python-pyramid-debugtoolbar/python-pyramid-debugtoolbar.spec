#
# spec file for package python-pyramid-debugtoolbar
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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


# nothing provides python2-pyramid needed by python2-pyramid-mako
%define skip_python2 1
Name:           python-pyramid-debugtoolbar
Version:        4.10
Release:        0
Summary:        An interactive HTML debugger for Pyramid application development
License:        BSD-4-Clause AND ZPL-2.1 AND MIT
URL:            https://docs.pylonsproject.org
Source:         https://files.pythonhosted.org/packages/source/p/pyramid_debugtoolbar/pyramid_debugtoolbar-%{version}.tar.gz
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyramid >= 1.4}
BuildRequires:  %{python_module pyramid-mako >= 0.3.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlalchemy}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Requires:       python-pyramid >= 1.4
Requires:       python-pyramid-mako >= 0.3.1
BuildArch:      noarch
%python_subpackages

%description
A package which provides an interactive HTML debugger for Pyramid application
development.

Note that pyramid-debugtoolbar is a blatant rip-off of Michael van Tellingen's
flask-debugtoolbar (which itself was derived from Rob Hudson's
django-debugtoolbar). It also includes a lightly sanded down version of the
Werkzeug debugger code by Armin Ronacher and team.

%package -n %{name}-doc
Summary:        Documentation files for %{name}

%description -n %{name}-doc
Documentation and examples for %{name}.

%prep
%setup -q -n pyramid_debugtoolbar-%{version}
rm -r demo/.gitignore demo/debugtoolbar_demo.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
#Fix spurious executable bit on js/css files
%python_expand find %{buildroot}%{$python_sitelib} -type f -exec chmod 0644 {} \;

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/pyramid_debugtoolbar/
%{python_sitelib}/pyramid_debugtoolbar-%{version}-py%{python_version}.egg-info

%files -n %{name}-doc
%doc CHANGES.txt CONTRIBUTORS.txt README.rst TODO.txt docs/*.rst docs/*.png demo

%changelog
