#
# spec file for package python-pyfiglet
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
Name:           python-pyfiglet
Version:        0.8.post1
Release:        0
Summary:        Pure Python FIGlet implementation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pwaller/pyfiglet
Source:         https://files.pythonhosted.org/packages/source/p/pyfiglet/pyfiglet-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  figlet
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
PyFIGlet is a full port of FIGlet (http://www.figlet.org/) into pure
Python. It takes ASCII text and renders it in ASCII art fonts.

%prep
%setup -q -n pyfiglet-%{version}
sed -i -e '1{/^#!/d}' pyfiglet/__init__.py
mv pyfiglet/test.py .

%build
%python_build

%install
%python_install

install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 doc/pyfiglet.1 %{buildroot}%{_mandir}/man1/

%python_clone -a %{buildroot}%{_mandir}/man1/pyfiglet.1
%python_clone -a %{buildroot}%{_bindir}/pyfiglet

%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Fix python-bytecode-inconsistent-mtime
%python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pyfiglet/fonts/
%python_expand $python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pyfiglet/fonts/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test.py

%post
%python_install_alternative pyfiglet pyfiglet.1

%postun
%python_uninstall_alternative pyfiglet pyfiglet.1

%files %{python_files}
%doc README doc/figfont.txt
%license LICENSE
%python_alternative %{_bindir}/pyfiglet
%python_alternative %{_mandir}/man1/pyfiglet.1%{ext_man}
%{python_sitelib}/*

%changelog
