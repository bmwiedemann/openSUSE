#
# spec file for package python-pykickstart
#
# Copyright (c) 2025 SUSE LLC
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
%bcond_without libalternatives
# Python 2 isn't supported...
Name:           python-%{mod_name}
Version:        3.54
Release:        0
Summary:        Python module for parsing and writing kickstart files
License:        GPL-2.0-only AND MIT
Group:          Development/Libraries/Python
URL:            https://fedoraproject.org/wiki/pykickstart
Source0:        https://github.com/pykickstart/pykickstart/releases/download/r%{version}/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Pykickstart is a Python library consisting of a data representation
of kickstart files, a parser to read files into that representation,
and a writer to generate kickstart files.

%prep
%autosetup -n %{mod_name}-%{version} -p1

%build
# Build all the translations and such
%make_build PYTHON=python3

%pyproject_wheel

%install
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/ksflatten
%python_clone -a %{buildroot}%{_mandir}/man1/ksflatten.1
%python_clone -a %{buildroot}%{_bindir}/ksshell
%python_clone -a %{buildroot}%{_mandir}/man1/ksshell.1
%python_clone -a %{buildroot}%{_bindir}/ksvalidator
%python_clone -a %{buildroot}%{_mandir}/man1/ksvalidator.1
%python_clone -a %{buildroot}%{_bindir}/ksverdiff
%python_clone -a %{buildroot}%{_mandir}/man1/ksverdiff.1

%check
%python_expand PYTHONPATH=.. $python -m unittest discover -v

%pre
%python_libalternatives_reset_alternative ksflatten
%python_libalternatives_reset_alternative ksshell
%python_libalternatives_reset_alternative ksvalidator
%python_libalternatives_reset_alternative ksverdiff

%files %{python_files}
%license COPYING
%doc README.rst
%doc data/kickstart.vim
%doc docs/2to3
%doc docs/programmers-guide
%doc docs/kickstart-docs.txt
%{python_sitelib}/%{mod_name}/
%{python_sitelib}/%{mod_name}-*
%python_alternative %{_bindir}/ksflatten
%python_alternative %{_mandir}/man1/ksflatten.1%{?ext_man}
%python_alternative %{_bindir}/ksshell
%python_alternative %{_mandir}/man1/ksshell.1%{?ext_man}
%python_alternative %{_bindir}/ksvalidator
%python_alternative %{_mandir}/man1/ksvalidator.1%{?ext_man}
%python_alternative %{_bindir}/ksverdiff
%python_alternative %{_mandir}/man1/ksverdiff.1%{?ext_man}

%changelog
