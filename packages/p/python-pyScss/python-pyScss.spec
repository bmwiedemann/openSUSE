#
# spec file for package python-pyScss
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 LISA GmbH, Bingen, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyScss
Version:        1.3.5
Release:        0
Summary:        pyScss, a Scss compiler for Python
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/Kronuz/pyScss
Source:         https://files.pythonhosted.org/packages/source/p/pyScss/pyScss-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  pcre-devel
BuildRequires:  python-rpm-macros
%ifpython2
Requires:       python-enum34
%endif
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
pyScss is a compiler for SCSS flavor of the Sass language, a superset of CSS3
that adds programming capabilities and some other syntactic sugar.

95% of Sass 3.2 is supported.  If it's not supported, it's a bug!  Please file
a ticket.

Most of Compass 0.11 is also built in.

Documentation:
http://pyscss.readthedocs.org/en/latest/

The canonical syntax reference is part of the Ruby Sass documentation:
http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html

%prep
%setup -q -n pyScss-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyscss
%python_clone -a %{buildroot}%{_bindir}/less2scss

%post
%python_install_alternative pyscss
%python_install_alternative less2scss

%postun
%python_uninstall_alternative pyscss
%python_uninstall_alternative less2scss

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst
%{python_sitearch}/*
%python_alternative %{_bindir}/pyscss
%python_alternative %{_bindir}/less2scss

%changelog
