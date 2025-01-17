#
# spec file for package python-pelican
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pelican
Version:        4.11.0
Release:        0
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files
License:        AGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://getpelican.com/
Source:         https://github.com/getpelican/pelican/archive/refs/tags/%{version}.tar.gz#/pelican-%{version}-gh.tar.gz
BuildRequires:  %{python_module Jinja2 >= 3.1.2}
BuildRequires:  %{python_module Pygments >= 2.16.1}
BuildRequires:  %{python_module Unidecode >= 1.3.7}
BuildRequires:  %{python_module base >= 3.8.1}
BuildRequires:  %{python_module blinker >= 1.7.0}
BuildRequires:  %{python_module docutils >= 0.20.1}
BuildRequires:  %{python_module feedgenerator >= 2.1.0}
BuildRequires:  %{python_module ordered-set >= 4.1.0}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pdm}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil >= 2.8.2}
BuildRequires:  %{python_module rich >= 13.6.0}
BuildRequires:  %{python_module watchfiles >= 0.21.0}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  pandoc
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 3.1.2
Requires:       python-Pygments >= 2.16.1
Requires:       python-Unidecode >= 1.3.7
Requires:       python-blinker >= 1.7.0
Requires:       python-docutils >= 0.20.1
Requires:       python-feedgenerator >= 2.1.0
Requires:       python-ordered-set >= 4.1.0
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-rich >= 13.6.0
Requires:       python-watchfiles >= 0.21.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     make
Suggests:       asciidoc
Suggests:       python-Markdown >= 3.5.1
Suggests:       python-typogrify >= 2.1.0
BuildArch:      noarch
ExcludeArch:    %{ix86}
# SECTION test
BuildRequires:  %{python_module Markdown >= 3.5.1}
BuildRequires:  %{python_module Sphinx >= 7.1.2}
BuildRequires:  %{python_module beautifulsoup4 >= 4.12.2}
BuildRequires:  %{python_module invoke >= 2.2.0}
BuildRequires:  %{python_module livereload >= 2.6.3}
BuildRequires:  %{python_module lxml >= 4.9.3}
BuildRequires:  %{python_module psutil >= 5.9.6}
BuildRequires:  %{python_module pytest >= 7.4.3}
BuildRequires:  %{python_module pytest-cov >= 4.1.0}
BuildRequires:  %{python_module pytest-sugar >= 0.9.7}
BuildRequires:  %{python_module pytest-xdist >= 3.4.0}
BuildRequires:  %{python_module tomli >= 2.0.1 if %python_base < 3.11}
BuildRequires:  %{python_module typogrify >= 2.1.0}
# /SECTION
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
chmod -x \
    pelican/tools/pelican_import.py \
    pelican/tools/pelican_themes.py \
    pelican/tools/pelican_quickstart.py \
    pelican/tools/templates/publishconf.py.jinja2

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/pelican-*.dist-info

%changelog
