#
# spec file for package python-kid
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define skip_python3 1
%define modname kid
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-%{modname}
Version:        0.9.6
Release:        0
Summary:        XML template language
# The site below is mentioned in the tarball itself, but it is now used
# by some other organization.
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.kid-templating.org/
Source:         https://files.pythonhosted.org/packages/source/k/%{modname}/%{modname}-%{version}.tar.gz
Patch0:         %{modname}-setuptools.patch
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A simple and pythonic XML template language.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1

# Fix wrong-script-interpreter
sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python|" bin/kid
sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python|" bin/kidc
sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python|" examples/cgi/kid_handler.cgi

# remove shebang from non-executable scripts
sed -i -e '/\/usr\/bin\/env\s\+python/d' kid/{compile,release,run}.py

%build
%python_build

%install
%python_install
# Install /usr/bin scripts by hand because setuptools support was patched away a while ago
# We can't just revert that because rpm can't update files to dirs and vice versa
install -d %{buildroot}%{_bindir}
install -m0755 bin/kid{,c} %{buildroot}%{_bindir}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -rf {dist,build}
%python_exec run_tests.py

%files %{python_files}
%license COPYING
%doc ChangeLog README
%{_bindir}/%{modname}*
%{python_sitelib}/%{modname}*

%files doc
%doc doc/html/
%doc examples/

%changelog
