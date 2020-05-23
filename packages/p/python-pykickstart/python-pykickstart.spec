#
# spec file for package python-pykickstart
#
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


%global mod_name pykickstart

# Python 2 isn't supported...
%global skip_python2 1


Name:           python-%{mod_name}
Version:        3.25
Release:        0
Summary:        Python module for parsing and writing kickstart files
Group:          Development/Libraries/Python
License:        GPL-2.0 AND MIT
URL:            http://fedoraproject.org/wiki/pykickstart
Source0:        https://github.com/pykickstart/pykickstart/releases/download/r%{version}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module ordered-set}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}

Requires:       python-ordered-set
Requires:       python-requests
Requires:       python-six

%python_subpackages

%description
Pykickstart is a Python library consisting of a data representation
of kickstart files, a parser to read files into that representation,
and a writer to generate kickstart files.

%prep
%autosetup -n %{mod_name}-%{version} -p1


%build
# Build all the translations and such
%make_build PYTHON=%{__python3}

%python_build


%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}


%check
%python_expand PYTHONPATH=.. $python -m unittest discover -v


%files %{python_files}
%license COPYING
%doc README.rst
%doc data/kickstart.vim
%doc docs/2to3
%doc docs/programmers-guide
%doc docs/kickstart-docs.txt
%{python_sitelib}/%{mod_name}/
%{python_sitelib}/%{mod_name}-*
%python3_only %{_bindir}/*
%python3_only %{_mandir}/man1/*

%changelog
