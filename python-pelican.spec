#
# spec file for package python-pelican
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


%define skip_python2 1
Name:           python-pelican
Version:        4.8.0
Release:        0
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files
License:        AGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://getpelican.com/
# Use the source instead of the pypi release for the tests
# Source:         https://github.com/getpelican/pelican/archive/%%{version}.tar.gz
Source:         pelican-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-311.patch gh#getpelican/pelican#3055
Patch0:         python-311.patch
BuildRequires:  %{python_module Jinja2 >= 2.11}
BuildRequires:  %{python_module Markdown >= 3.1.1}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module Unidecode}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module blinker >= 1.4}
BuildRequires:  %{python_module docutils >= 0.16}
BuildRequires:  %{python_module feedgenerator >= 1.9}
BuildRequires:  %{python_module flake8-import-order}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module invoke}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module livereload}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz >= 0a}
BuildRequires:  %{python_module rich >= 10.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  %{python_module typogrify}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  pandoc
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.11
Requires:       python-Pygments
Requires:       python-Unidecode
Requires:       python-blinker
Requires:       python-docutils >= 0.15
Requires:       python-feedgenerator >= 1.9
Requires:       python-python-dateutil
Requires:       python-pytz >= 0a
Requires:       python-rich >= 10.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       asciidoc
Suggests:       python-Markdown >= 3.1.1
Suggests:       python-typogrify
BuildArch:      noarch
ExcludeArch:    %{ix86}
%python_subpackages

%description
Pelican is a static site generator, written in Python.

* Write your weblog entries directly with your editor of choice in reStructuredText, Markdown or AsciiDoc
* Includes a simple CLI tool to (re)generate the weblog
* Easy to interface with DVCSes and web hooks
* Completely static output is easy to host anywhere

Pelican currently supports:

* Blog articles and pages
* Comments, via an external service
* Theming support (themes are created using Jinja2 templates)
* PDF generation of the articles/pages (optional)
* Publication of articles in multiple languages
* Atom/RSS feeds
* Code syntax highlighting
* Asset management with webassets (optional)
* Import from WordPress, Dotclear, or RSS feeds
* Integration with external tools: Twitter, Google Analytics, etc. (optional)

%prep
%autosetup -p1 -n pelican-%{version}

# remove useless shebang
sed -i '1d' \
    pelican/tools/pelican_import.py \
    pelican/tools/pelican_themes.py \
    pelican/tools/pelican_quickstart.py
# remove executable bit, this is not a script
chmod -x pelican/tools/templates/publishconf.py.jinja2

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

for p in pelican pelican-import pelican-plugins pelican-quickstart pelican-themes; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%check
export LC_ALL=C.utf8
export PYTHONPATH=.
# gh#getpelican/pelican#2846
%pytest -k 'not (test_basic_generation_works or test_custom_generation_works or test_custom_locale_generation_works)'

%post
%python_install_alternative pelican pelican-import pelican-plugins pelican-quickstart pelican-themes

%postun
%python_uninstall_alternative pelican

%files %{python_files}
%license LICENSE
%doc CONTRIBUTING.rst README.rst THANKS docs/*
%python_alternative %{_bindir}/pelican
%python_alternative %{_bindir}/pelican-import
%python_alternative %{_bindir}/pelican-plugins
%python_alternative %{_bindir}/pelican-quickstart
%python_alternative %{_bindir}/pelican-themes
%{python_sitelib}/pelican
%{python_sitelib}/pelican-*.egg-info

%changelog
