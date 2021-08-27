#
# spec file for package python-mkdocs
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
Name:           python-mkdocs
Version:        1.1.2
Release:        0
Summary:        Project documentation with Markdown
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://www.mkdocs.org
Source:         https://github.com/mkdocs/mkdocs/archive/%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tox}
BuildRequires:  fdupes
BuildRequires:  fontawesome-fonts
BuildRequires:  fontawesome-fonts-web
BuildRequires:  python-rpm-macros
Requires:       fontawesome-fonts
Requires:       fontawesome-fonts-web
Requires:       python-Jinja2
Requires:       python-Markdown
Requires:       python-PyYAML
Requires:       python-click
Requires:       python-ghp-import
Requires:       python-livereload
Requires:       python-tornado
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mkdocs

# unbundle where possible
%if 0%{?suse_version} <= 1500
rm %{buildroot}%{python_sitelib}/mkdocs/themes/mkdocs/fonts/fontawesome-webfont.woff
ln -sf %{_datadir}/fonts/truetype/fontawesome-webfont.woff %{buildroot}%{python_sitelib}/mkdocs/themes/mkdocs/fonts/fontawesome-webfont.woff
rm %{buildroot}%{python_sitelib}/mkdocs/themes/mkdocs/fonts/fontawesome-webfont.svg
ln -sf %{_datadir}/font-awesome-web/fontawesome-webfont.svg %{buildroot}%{python_sitelib}/mkdocs/themes/mkdocs/fonts/fontawesome-webfont.svg
rm %{buildroot}%{python_sitelib}/mkdocs/themes/readthedocs/fonts/fontawesome-webfont.svg
ln -sf %{_datadir}/font-awesome-web/fontawesome-webfont.svg %{buildroot}%{python_sitelib}/mkdocs/themes/readthedocs/fonts/fontawesome-webfont.svg
rm %{buildroot}%{python_sitelib}/mkdocs/themes/readthedocs/fonts/fontawesome-webfont.ttf
ln -sf %{_datadir}/fonts/truetype/fontawesome-webfont.ttf %{buildroot}%{python_sitelib}/mkdocs/themes/readthedocs/fonts/fontawesome-webfont.ttf
%endif

# inconsistent permissions prohibited fdupes from being effective
find "%{buildroot}" -type f "(" -name "*.eot" -o -name "*.ttf" -o \
	-name "*.woff" ")" -exec chmod a-x {} +

%python_expand %fdupes -s %{buildroot}/%{$python_sitelib}

%check
# tries to download stuff at runtime
#tox

%post
%python_install_alternative mkdocs

%postun
%python_uninstall_alternative mkdocs

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/mkdocs
%{python_sitelib}/mkdocs/
%{python_sitelib}/mkdocs-%{version}-py%{python_version}.egg-info

%changelog
