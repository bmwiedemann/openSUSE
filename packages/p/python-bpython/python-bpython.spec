#
# spec file for package python-bpython
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_with     test
Name:           python-bpython
Version:        0.20
Release:        0
Summary:        Fancy Interface to the Python Interpreter
License:        MIT
URL:            https://www.bpython-interpreter.org/
Source:         https://files.pythonhosted.org/packages/source/b/bpython/bpython-%{version}.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       %{name}-common = %{version}
Requires:       python-curtsies >= 0.1.18
Requires:       python-greenlet
Requires:       python-pygments
Requires:       python-requests
Requires:       python-six >= 1.5
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-jedi
Recommends:     python-ndg-httpsclient
Recommends:     python-pyOpenSSL
Recommends:     python-pyasn1
Recommends:     python-urwid
Recommends:     python-watchdog
Recommends:     python-wcwidth
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module curtsies >= 0.1.18}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six >= 1.5}
BuildRequires:  %{python_module wcwidth}
BuildRequires:  python-mock
%endif
%ifpython2
Provides:       bpython = %{version}
Obsoletes:      bpython <= %{version}
%endif
%python_subpackages

%description
Bpython is an enhanced Python interactive interpreter that uses curses
and provides the following main features: in-line syntax highlighting;
readline-like autocompletion with suggestions displayed as you type; expected
argument specification for functions; a handy pastebin function to quickly
submit your code and return a URL. Its goal is to bring together a few handy
ideas to enhance the standard interpreter without getting carried away.

%package        -n %{name}-common
Summary:        Fancy Interface to the Python Interpreter - common files
Provides:       %{python_module bpython-common = %{version}}

%description    -n %{name}-common
This package contains files shared between the various versions of
Bpython. You don't need to install this directly, packages that
require it will pull it in automatically.

%package        -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module bpython-doc = %{version}}

%description    -n %{name}-doc
Documentation and help files for %{name}.

%prep
%setup -q -n bpython-%{version}

%build
%python_build
%python_exec setup.py build_sphinx && rm build/sphinx/html/.buildinfo # HTML documentation

%install
%python_install

install -m 644 build/man/bpython.1 %{buildroot}%{_mandir}/man1/bpython.1
install -m 644 build/man/bpython-config.5 %{buildroot}%{_mandir}/man5/bpython-config.5

%python_clone -a %{buildroot}%{_bindir}/bpython
%python_clone -a %{buildroot}%{_bindir}/bpython-curses
%python_clone -a %{buildroot}%{_bindir}/bpython-urwid
%python_clone -a %{buildroot}%{_bindir}/bpdb
%python_clone -a %{buildroot}%{_mandir}/man1/bpython.1
%python_clone -a %{buildroot}%{_mandir}/man5/bpython-config.5

install -d %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_mandir}/man5/

%{python_expand %fdupes %{buildroot}%{$python_sitelib}

cp %{buildroot}%{_datadir}/appinfo/org.bpython-interpreter.bpython.appdata.xml %{buildroot}%{_datadir}/appinfo/org.bpython-interpreter.bpython-%{$python_bin_suffix}.appdata.xml
cp %{buildroot}%{_datadir}/applications/org.bpython-interpreter.bpython.desktop %{buildroot}%{_datadir}/applications/org.bpython-interpreter.bpython-%{$python_bin_suffix}.desktop

sed -i 's|bpython.desktop|bpython-%{$python_bin_suffix}.desktop|' %{buildroot}%{_datadir}/appinfo/org.bpython-interpreter.bpython-%{$python_bin_suffix}.appdata.xml
sed -i 's|bpython interpreter|bpython %{$python_prefix} interpreter|' %{buildroot}%{_datadir}/appinfo/org.bpython-interpreter.bpython-%{$python_bin_suffix}.appdata.xml
sed -i 's|Python interpreter|A %{$python_prefix} interpreter|' %{buildroot}%{_datadir}/appinfo/org.bpython-interpreter.bpython-%{$python_bin_suffix}.appdata.xml
desktop-file-edit --set-name=bpython-%{$python_bin_suffix} \
                  --copy-name-to-generic-name \
                  --remove-key=Categories \
                  --add-category=System --add-category=TerminalEmulator \
                  --set-comment="A fancy interface to the %{$python_prefix} interpreter" \
                  --set-key=Exec --set-value="%{_bindir}/bpython-%{$python_bin_suffix}" \
                  %{buildroot}%{_datadir}/applications/org.bpython-interpreter.bpython-%{$python_bin_suffix}.desktop
}

rm %{buildroot}%{_datadir}/appinfo/org.bpython-interpreter.bpython.appdata.xml
rm %{buildroot}%{_datadir}/applications/org.bpython-interpreter.bpython.desktop

%if %{with test}
%check
%python_exec setup.py test
%endif

%post
%{python_install_alternative bpython bpython-curses bpython-urwid bpdb bpython.1%{ext_man} bpython-config.5%{ext_man}}

%postun
%python_uninstall_alternative bpython

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGELOG README.rst
%dir %{python_sitelib}/bpython
%{python_sitelib}/bpython/*
%dir %{python_sitelib}/bpdb
%{python_sitelib}/bpdb/*
%dir %{python_sitelib}/bpython-%{version}-py*.egg-info
%{python_sitelib}/bpython-%{version}-py*.egg-info/*
%python_alternative %{_bindir}/bpython
%python_alternative %{_bindir}/bpython-curses
%python_alternative %{_bindir}/bpython-urwid
%python_alternative %{_bindir}/bpdb
%python_alternative %{_mandir}/man1/bpython.1%{ext_man}
%python_alternative %{_mandir}/man5/bpython-config.5%{ext_man}
%dir %{_datadir}/appinfo/
%{_datadir}/appinfo/org.bpython-interpreter.bpython-%{python_bin_suffix}.appdata.xml
%{_datadir}/applications/org.bpython-interpreter.bpython-%{python_bin_suffix}.desktop

%files -n %{name}-common
%license LICENSE
%{_datadir}/pixmaps/bpython.png

%files -n %{name}-doc
%doc build/sphinx/html

%changelog
