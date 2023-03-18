#
# spec file for package python-mkdocs
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


Name:           python-mkdocs
Version:        1.4.2
Release:        0
Summary:        Project documentation with Markdown
License:        BSD-2-Clause
URL:            https://www.mkdocs.org
Source:         https://github.com/mkdocs/mkdocs/archive/%{version}.tar.gz#/mkdocs-%{version}.tar.gz
BuildRequires:  %{python_module Babel >= 2.9.0}
BuildRequires:  %{python_module Jinja2 >= 2.11.1}
BuildRequires:  %{python_module Markdown >= 3.2.1}
# https://github.com/mkdocs/mkdocs/blob/master/pyproject.toml#L38
#BuildRequires:  %{python_module Markdown <3.4}
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module ghp-import  >= 1.0}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module importlib_metadata if python-base < 3.10}
BuildRequires:  %{python_module mergedeep >= 1.3.4}
BuildRequires:  %{python_module packaging >= 20.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyyaml_env_tag >= 0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module watchdog >= 2.0}
BuildRequires:  fdupes
BuildRequires:  fontawesome-fonts
BuildRequires:  fontawesome-fonts-web
BuildRequires:  python-rpm-macros
Requires:       fontawesome-fonts
Requires:       fontawesome-fonts-web
Requires:       python-Jinja2
Requires:       python-Markdown
Requires:       python-MarkupSafe
Requires:       python-PyYAML
Requires:       python-click
Requires:       python-ghp-import
Requires:       python-importlib_metadata
Requires:       python-mergedeep
Requires:       python-packaging
Requires:       python-pyyaml_env_tag
Requires:       python-watchdog
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       python-babel
BuildArch:      noarch
%python_subpackages

%description
MkDocs is a static site generator for building project documentation.
Documentation source files are written in Markdown, and configured
with a single YAML configuration file.

%prep
%autosetup -n mkdocs-%{version}

# Get rid of shebangs.
find . -type f -name "*.py" -exec sed -i '/#!\/usr\/bin\/env/d' {} +
find . -type f -name "*.svg" -exec chmod -x {} +

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mkdocs

# unbundle fontawesome where possible
if [ -f %{buildroot}%{python_sitelib}/mkdocs/themes/mkdocs/css/font-awesome.min.css ]; then
  if [ -f %{_datadir}/fontawesome-web/css/fontawesome.min.css ]; then
    rm %{buildroot}%{python_sitelib}/mkdocs/themes/mkdocs/css/font-awesome.min.css
    ln -sf %{_datadir}/fontawesome-web/css/fontawesome.min.css %{buildroot}%{python_sitelib}/mkdocs/themes/mkdocs/css/font-awesome.min.css
  fi
fi
for filetype in eot svg ttf woff woff2; do
  for theme in mkdocs readthedocs; do
    [ -f %{_datadir}/fontawesome-web/webfonts/fa-regular-400.$filetype ] || continue
    [ -f %{buildroot}%{python_sitelib}/mkdocs/themes/$theme/fonts/fontawesome-webfont.$filetype ] || continue
    rm %{buildroot}%{python_sitelib}/mkdocs/themes/$theme/fonts/fontawesome-webfont.$filetype
    ln -sf %{_datadir}/fontawesome-web/webfonts/fa-regular-400.$filetype %{buildroot}%{python_sitelib}/mkdocs/themes/$theme/fonts/fontawesome-webfont.$filetype
  done
done

# inconsistent permissions prohibited fdupes from being effective
find %{buildroot} -type f "(" -name "*.eot" -o -name "*.ttf" -o \
	-name "*.woff" ")" -exec chmod a-x {} +

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -vf mkdocs/tests/gh_deploy_tests.py
rm -vf mkdocs/tests/config/config_tests.py
rm -vf mkdocs/tests/cli_tests.py
rm -vf mkdocs/tests/config/base_tests.py
%pyunittest discover -p '*tests.py' -v mkdocs --top-level-directory .

%post
%python_install_alternative mkdocs

%postun
%python_uninstall_alternative mkdocs

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/mkdocs
%{python_sitelib}/mkdocs
%{python_sitelib}/mkdocs-%{version}*-info

%changelog
