#
# spec file for package python-pelican-myst-reader
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-pelican-myst-reader
Version:        1.4.0
Release:        0
Summary:        Pelican plugin for converting MyST's Markdown variant to HTML
License:        AGPL-3.0-only
URL:            https://github.com/ashwinvis/myst-reader
Source:         https://files.pythonhosted.org/packages/source/p/pelican_myst_reader/pelican_myst_reader-%{version}.tar.gz
# PATCH-FIX-OPENSUSE no-bibtex.patch mcepl@suse.com
# Temporarily remove need for sphinxcontrib-bibtex, until we have it packaged
Patch0:         no-bibtex.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Yes, really, Markdown module is required for metadata parsing and
# other stuff
Requires:       python-Markdown
Requires:       python-PyYAML >= 6.0
Requires:       python-beautifulsoup4 >= 4.9.3
Requires:       python-docutils >= 0.19
Requires:       python-markdown-word-count >= 0.1.0
Requires:       python-myst-parser >= 4.0.0
Requires:       python-pelican >= 4.5
# Requires:       python-sphinxcontrib-bibtex >= 2.6.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module beautifulsoup4 >= 4.9.3}
BuildRequires:  %{python_module docutils >= 0.19}
BuildRequires:  %{python_module markdown-word-count >= 0.1.0}
BuildRequires:  %{python_module myst-parser >= 4.0.0}
BuildRequires:  %{python_module pelican >= 4.5}
# FIXME Not available yet
# BuildRequires:  %%{python_module sphinxcontrib-bibtex >= 2.6.3}
# /SECTION
%python_subpackages

%description
MyST Reader is a Pelican plugin that converts documents written in
MyST’s variant of Markdown into HTML.

MyST syntax is a superset of [CommonMark][]. So if you feed your Pelican
site with non-MyST Markdown files or other variants, most of them will
probably renders as they were with this plugin.

%prep
%autosetup -p1 -n pelican_myst_reader-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pelican/plugins/myst_reader/
%{python_sitelib}/pelican_myst_reader-%{version}.dist-info

%changelog
