#
# spec file for package python-pelican
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pelican
Version:        4.1.2
Release:        0
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files
License:        AGPL-3.0-only
Group:          Development/Languages/Python
Url:            http://getpelican.com/
Source:         https://files.pythonhosted.org/packages/source/p/pelican/pelican-%{version}.tar.gz
Patch0:         fix-python3-incompatibility.patch
BuildRequires:  %{python_module Jinja2 >= 2.7}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module Unidecode}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module feedgenerator >= 1.9}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.7
Requires:       python-Pygments
Requires:       python-Unidecode
Requires:       python-blinker
Requires:       python-docutils
Requires:       python-feedgenerator >= 1.9
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-six >= 1.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       asciidoc
Suggests:       python-Markdown
Suggests:       python-typogrify
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

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
%setup -q -n pelican-%{version}
%autopatch -p1

# remove useless shebang
sed -i '1d' \
    pelican/tools/templates/publishconf.py.jinja2 \
    pelican/tools/templates/pelicanconf.py.jinja2 \
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

for p in pelican pelican-import pelican-quickstart pelican-themes ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%post
%python_install_alternative pelican pelican-import pelican-quickstart pelican-themes

%postun
%python_uninstall_alternative pelican

%files %python_files
%defattr(-,root,root,-)
%doc CONTRIBUTING.rst LICENSE README.rst THANKS docs/*
%python_alternative %{_bindir}/pelican
%python_alternative %{_bindir}/pelican-import
%python_alternative %{_bindir}/pelican-quickstart
%python_alternative %{_bindir}/pelican-themes
%{python_sitelib}/pelican
%{python_sitelib}/pelican-%{version}-py%{python_version}.egg-info

%changelog
