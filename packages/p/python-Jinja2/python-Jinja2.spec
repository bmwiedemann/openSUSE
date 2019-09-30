#
# spec file for package python-Jinja2
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
%define oldpython python
Name:           python-Jinja2
Version:        2.10.1
Release:        0
Summary:        A template engine written in pure Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://jinja.pocoo.org/
Source:         https://files.pythonhosted.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
Patch0:         python38.patch
BuildRequires:  %{python_module MarkupSafe >= 0.23}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 0.8
Requires:       python-MarkupSafe >= 0.23
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-jinja2 = %{version}
Obsoletes:      %{oldpython}-jinja2 < %{version}
%endif
%python_subpackages

%description
Jinja2 is a template engine written in pure Python.  It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.  Here a small example of a Jinja template:

    {%% extends 'base.html' %%}
    {%% block title %%}Memberlist{%% endblock %%}
    {%% block content %%}
      <ul>
      {%% for user in users %%}
        <li><a href="{{ user.url }}">{{ user.username }}</a></li>
      {%% endfor %%}
      </ul>
    {%% endblock %%}

%package -n python-Jinja2-vim
Summary:        Jinja2 syntax files for Vim
License:        BSD-3-Clause
Group:          Productivity/Text/Editors
Requires:       %{name} = %{version}
%if 0%{?suse_version} >= 1000 || 0%{?fedora_version} >= 24
Recommends:     vim
%endif

%description -n python-Jinja2-vim
Vim syntax highlighting scheme for Jinja2 templates.

%package -n python-Jinja2-emacs
Summary:        Jinja2 syntax files for Emacs
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
Requires:       %{name} = %{version}
%if 0%{?suse_version} >= 1000 || 0%{?fedora_version} >= 24
Recommends:     emacs
%endif

%description -n python-Jinja2-emacs
Emacs syntax highlighting scheme for Jinja2 templates.

%prep
%setup -q -n Jinja2-%{version}
%patch0 -p1
sed -i 's/\r$//' LICENSE # Fix wrong EOL encoding

%build
%python_build

%install
%python_install
install -Dm644 ext/Vim/jinja.vim %{buildroot}%{_datadir}/vim/site/syntax/jinja.vim # Install VIM syntax file
install -Dm644 ext/jinja.el %{buildroot}%{_datadir}/emacs/site-lisp/jinja.el # Install Emacs syntax file
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst CHANGES.rst artwork examples
%{python_sitelib}/jinja2
%{python_sitelib}/Jinja2-%{version}-py%{python_version}.egg-info

%files -n python-Jinja2-vim
%dir %{_datadir}/vim
%dir %{_datadir}/vim/site
%dir %{_datadir}/vim/site/syntax
%{_datadir}/vim/site/syntax/jinja.vim

%files -n python-Jinja2-emacs
%{_datadir}/emacs/site-lisp/jinja.el

%changelog
